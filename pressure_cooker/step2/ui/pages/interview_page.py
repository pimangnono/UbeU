"""
Page 3: Live Interview — Meeting Room Layout

Semicircle meeting room with 4 avatars:
  Facilitator (top), Jordan (left), Sam (right), You (bottom)
Speech bubbles appear near the active speaker.
Only the latest exchange is visible; old messages vanish.
AI turns revealed sequentially with typing-dots animation.
"""

import re
import time

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"

# Speaker config: color, initial, CSS position
SPEAKERS = {
    "Facilitator": {"color": "#6b7280", "initial": "F", "pos": "top"},
    "Jordan":      {"color": "#dc2626", "initial": "J", "pos": "left"},
    "Sam":         {"color": "#16a34a", "initial": "S", "pos": "right"},
}

TTS_VOICE_SETTINGS = {
    "Jordan":      {"pitch": 0.9, "rate": 1.0},
    "Sam":         {"pitch": 1.1, "rate": 1.0},
    "Facilitator": {"pitch": 1.0, "rate": 0.9},
}


def _display_duration(content: str, is_typing: bool = False, tts_enabled: bool = False) -> float:
    """Calculate how long to display a message based on reading speed."""
    if is_typing:
        return min(2.5, 0.8 + len(content) * 0.003)
    word_count = len(content.split())
    if tts_enabled:
        return max(3.0, word_count * 0.35)  # ~150 WPM speech
    return max(3.0, word_count * 0.3)  # ~200 WPM reading


def _render_data_panel(placeholder) -> None:
    """Render the facilitator data panel into the given st.empty() placeholder."""
    import html as _html_mod

    fac_history = st.session_state.get("facilitator_history", [])

    if not fac_history:
        placeholder.html(
            '<div style="border:1px solid #e2e8f0;border-radius:12px;padding:16px;'
            'height:300px;display:flex;align-items:center;justify-content:center;'
            'color:#94a3b8;font-size:14px;">'
            "No data shared yet.<br>Ask the Facilitator for data to see it here.</div>"
        )
        return

    cards = ""
    for i, fmsg in enumerate(fac_history):
        escaped = _html_mod.escape(fmsg).replace("\n", "<br>")
        cards += (
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;'
            f'border-radius:8px;padding:10px 12px;margin-bottom:8px;">'
            f'<div style="font-weight:600;font-size:11px;color:#6b7280;'
            f'text-transform:uppercase;letter-spacing:0.5px;margin-bottom:4px;">'
            f"Data #{i + 1}</div>"
            f'<div style="font-size:13px;color:#1e293b;line-height:1.5;">'
            f"{escaped}</div></div>"
        )

    placeholder.html(
        '<div style="border:1px solid #e2e8f0;border-radius:12px;overflow:hidden;">'
        '<div style="background:#f1f5f9;padding:10px 14px;'
        'font-weight:700;font-size:13px;color:#475569;'
        'text-transform:uppercase;letter-spacing:0.5px;'
        'border-bottom:1px solid #e2e8f0;">Data Panel</div>'
        '<div style="padding:10px;max-height:350px;overflow-y:auto;">'
        f"{cards}</div></div>"
    )


def _meeting_room_css() -> str:
    """Return the CSS for the meeting room component."""
    return """
<style>
.meeting-room {
    max-width: 720px;
    height: 260px;
    margin: 0 auto;
    position: relative;
    border-radius: 24px;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    border: 1px solid #cbd5e1;
    overflow: hidden;
}

/* Oval table in center */
.meeting-table {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 280px;
    height: 140px;
    background: linear-gradient(145deg, #92400e 0%, #78350f 40%, #92400e 100%);
    border-radius: 50%;
    border: 3px solid #713f12;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15), inset 0 2px 4px rgba(255,255,255,0.1);
}

/* Avatar seats */
.avatar-seat {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 2;
}
.avatar-seat.pos-top    { top: 18px;  left: 50%; transform: translateX(-50%); }
.avatar-seat.pos-left   { top: 50%;   left: 42px; transform: translateY(-50%); }
.avatar-seat.pos-right  { top: 50%;   right: 42px; transform: translateY(-50%); }
.avatar-seat.pos-bottom { bottom: 18px; left: 50%; transform: translateX(-50%); }

.avatar-circle {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 22px;
    color: white;
    transition: opacity 0.3s, box-shadow 0.3s;
    border: 3px solid white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}
.avatar-circle.dimmed {
    opacity: 0.35;
}
.avatar-circle.speaking {
    opacity: 1;
    animation: pulse-ring 1.2s ease-out infinite;
}

@keyframes pulse-ring {
    0%   { box-shadow: 0 0 0 0 rgba(59,130,246,0.5); }
    70%  { box-shadow: 0 0 0 10px rgba(59,130,246,0); }
    100% { box-shadow: 0 0 0 0 rgba(59,130,246,0); }
}

.avatar-name {
    margin-top: 4px;
    font-size: 12px;
    font-weight: 600;
    color: #334155;
    text-align: center;
}

/* Speaker card below the meeting room */
.speaker-card {
    max-width: 720px;
    margin: 0.5rem auto 0 auto;
    padding: 12px 16px;
    background: white;
    border-radius: 14px;
    font-size: 14px;
    line-height: 1.45;
    color: #1e293b;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    border: 1px solid #e2e8f0;
    animation: fade-in 0.3s ease-out;
}
.speaker-card .speaker-label {
    font-weight: 700;
    font-size: 12px;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

@keyframes fade-in {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Typing dots */
.typing-dots {
    display: flex;
    gap: 5px;
    padding: 4px 0;
    width: fit-content;
}
.typing-dots span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #94a3b8;
    animation: dot-bounce 1.4s ease-in-out infinite;
}
.typing-dots span:nth-child(2) { animation-delay: 0.2s; }
.typing-dots span:nth-child(3) { animation-delay: 0.4s; }

@keyframes dot-bounce {
    0%, 60%, 100% { transform: translateY(0); }
    30% { transform: translateY(-6px); }
}
</style>
"""


def _build_meeting_html(
    active_speaker: str | None,
    bubble_speaker: str | None,
    bubble_content: str | None,
    participant_name: str,
    show_typing: bool = False,
    typing_speaker: str | None = None,
    tts_enabled: bool = False,
    tts_settings: dict | None = None,
) -> str:
    """Build the meeting room HTML with avatars and optional speech bubble."""
    import html as html_mod

    # Build avatar seats
    all_seats = {}
    for name, cfg in SPEAKERS.items():
        all_seats[name] = cfg
    # Add participant ("You") seat
    all_seats[participant_name] = {"color": "#2563eb", "initial": "Y", "pos": "bottom"}

    avatars_html = ""
    for name, cfg in all_seats.items():
        state_class = "dimmed"
        if active_speaker and name == active_speaker:
            state_class = "speaking"
        elif active_speaker is None:
            state_class = ""  # no one active = all normal

        display_name = "You" if name == participant_name else name
        avatars_html += f"""
        <div class="avatar-seat pos-{cfg['pos']}">
            <div class="avatar-circle {state_class}" style="background:{cfg['color']};">
                {cfg['initial']}
            </div>
            <div class="avatar-name">{display_name}</div>
        </div>
        """

    # Build speaker card (rendered below the room, not inside it)
    card_html = ""
    if show_typing and typing_speaker:
        tp_cfg = all_seats.get(typing_speaker, all_seats.get(participant_name))
        speaker_label = "You" if typing_speaker == participant_name else typing_speaker
        color = tp_cfg["color"] if tp_cfg else "#2563eb"
        card_html = f"""
        <div class="speaker-card">
            <div class="speaker-label" style="color:{color};">{speaker_label}</div>
            <div class="typing-dots">
                <span style="background:{color};"></span>
                <span style="background:{color};"></span>
                <span style="background:{color};"></span>
            </div>
        </div>
        """
    elif bubble_speaker and bubble_content:
        bp_cfg = all_seats.get(bubble_speaker, all_seats.get(participant_name))
        display = "You" if bubble_speaker == participant_name else bubble_speaker
        color = bp_cfg["color"] if bp_cfg else "#2563eb"
        escaped = html_mod.escape(bubble_content)
        card_html = f"""
        <div class="speaker-card">
            <div class="speaker-label" style="color:{color};">{display}</div>
            {escaped}
        </div>
        """

    # TTS script injection for AI messages (not typing, not user's own)
    tts_html = ""
    if (
        tts_enabled
        and bubble_speaker
        and bubble_content
        and not show_typing
        and bubble_speaker != participant_name
    ):
        settings = (tts_settings or {}).get(bubble_speaker, {})
        pitch = settings.get("pitch", 1.0)
        rate = settings.get("rate", 1.0)
        # Escape content for JS string literal
        js_escaped = (
            bubble_content
            .replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace("\n", "\\n")
            .replace("\r", "")
        )
        tts_html = f"""
        <script>
        (function() {{
            var synth = window.speechSynthesis;
            if (synth) {{
                synth.cancel();
                var msg = new SpeechSynthesisUtterance('{js_escaped}');
                msg.rate = {rate};
                msg.pitch = {pitch};
                synth.speak(msg);
            }}
        }})();
        </script>
        """

    return f"""
    {_meeting_room_css()}
    <div class="meeting-room">
        <div class="meeting-table"></div>
        {avatars_html}
    </div>
    {card_html}
    {tts_html}
    """


def render():
    pid = st.session_state.get("participant_id")
    if not pid:
        st.warning("Please complete the consent form first.")
        st.session_state.current_step = "consent"
        st.rerun()
        return

    # CSS is now included in each _build_meeting_html() call

    # --- Session initialization ---
    if "session_id" not in st.session_state or st.session_state.session_id is None:
        _initialize_session(pid)
        return

    sid = st.session_state.session_id
    participant_name = st.session_state.get("participant_name", "You")

    # Initialize facilitator history
    if "facilitator_history" not in st.session_state:
        st.session_state.facilitator_history = []

    # --- Loading page + opening reveal (runs once after session creation) ---
    pending = st.session_state.get("pending_opening")
    if pending:
        _show_loading_and_reveal(pending, participant_name)
        return

    # --- Timer display (real-time JS) + TTS toggle ---
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled = False

    if "interview_start" in st.session_state:
        import streamlit.components.v1 as stc

        end_time_ms = int((st.session_state.interview_start + 15 * 60) * 1000)
        session_state = st.session_state.get("session_state", "active")

        timer_col, sound_col = st.columns([3, 1])
        with timer_col:
            is_waiting = st.session_state.get("waiting_for_response", False)
            if session_state == "ended":
                st.markdown("**00:00** — Discussion ended")
            elif is_waiting:
                # Timer paused while waiting for AI — show frozen time
                stc.html(f"""
                <div id="timer" style="font-weight:700; font-size:18px;
                     font-family:ui-monospace,SFMono-Regular,monospace;
                     padding:2px 0; line-height:1.4;"></div>
                <script>
                (function(){{
                    var end={end_time_ms};
                    var el=document.getElementById('timer');
                    var r=Math.max(0,end-Date.now());
                    var m=Math.floor(r/60000);
                    var s=Math.floor(r%60000/1000);
                    el.textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s+' remaining  ⏸ paused';
                    el.style.color='#6b7280';
                }})();
                </script>
                """, height=35)
            else:
                stc.html(f"""
                <div id="timer" style="font-weight:700; font-size:18px;
                     font-family:ui-monospace,SFMono-Regular,monospace;
                     padding:2px 0; line-height:1.4;"></div>
                <script>
                (function(){{
                    var end={end_time_ms};
                    var el=document.getElementById('timer');
                    function tick(){{
                        var r=Math.max(0,end-Date.now());
                        var m=Math.floor(r/60000);
                        var s=Math.floor(r%60000/1000);
                        el.textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s+' remaining';
                        el.style.color=r<=60000?'#dc2626':r<=180000?'#ea580c':'#1e293b';
                        if(r>0)setTimeout(tick,500);
                    }}
                    tick();
                }})();
                </script>
                """, height=35)
        with sound_col:
            st.session_state.tts_enabled = st.toggle(
                "Sound", value=st.session_state.tts_enabled
            )

    # --- Two-column layout: Meeting Room (left) + Data Panel (right) ---
    main_col, data_col = st.columns([3, 2])

    with main_col:
        # --- Meeting room display ---
        room_placeholder = st.empty()

        latest = st.session_state.get("latest_display", [])
        opening = st.session_state.get("opening_display", [])

        if latest:
            last_msg = latest[-1]
            room_placeholder.html(
                _build_meeting_html(
                    active_speaker=last_msg["speaker"],
                    bubble_speaker=last_msg["speaker"],
                    bubble_content=last_msg["content"],
                    participant_name=participant_name,
                ),
            )
        elif opening:
            last_msg = opening[-1]
            room_placeholder.html(
                _build_meeting_html(
                    active_speaker=last_msg["speaker"],
                    bubble_speaker=last_msg["speaker"],
                    bubble_content=last_msg["content"],
                    participant_name=participant_name,
                ),
            )
        else:
            room_placeholder.html(
                _build_meeting_html(
                    active_speaker=None,
                    bubble_speaker=None,
                    bubble_content=None,
                    participant_name=participant_name,
                ),
            )

    with data_col:
        # --- Data Panel (scrollable, fixed height, updated in real-time) ---
        data_placeholder = st.empty()
        _render_data_panel(data_placeholder)

    # --- Check if session ended ---
    session_state = st.session_state.get("session_state", "active")
    if session_state == "ended":
        st.markdown("---")
        if st.button("Continue to Survey", type="primary"):
            st.session_state.current_step = "survey"
            st.rerun()
        return

    # --- Chat form (two-phase: save → rerun disabled → process → rerun enabled) ---
    waiting = st.session_state.get("waiting_for_response", False)
    target_options = ["Everyone", "Jordan", "Sam", "Facilitator"]

    with st.form("chat_form", clear_on_submit=True):
        selected = st.radio(
            "Talk to",
            target_options,
            index=0,
            horizontal=True,
            disabled=waiting,
        )
        input_col, btn_col = st.columns([6, 1])
        with input_col:
            user_input = st.text_input(
                "Message",
                placeholder=(
                    "Waiting for response..."
                    if waiting
                    else "Type your response... (or @Jordan to target someone)"
                ),
                label_visibility="collapsed",
                disabled=waiting,
            )
        with btn_col:
            submitted = st.form_submit_button(
                "..." if waiting else "Send",
                use_container_width=True,
                disabled=waiting,
            )

    # --- Phase 1: On new submit, save message and rerun to show disabled form ---
    if submitted and user_input and not waiting:
        # Determine target from radio selection
        api_target = None if selected == "Everyone" else selected

        # @mention parsing (overrides radio selection)
        mention_match = re.match(
            r"^@(jordan|sam|facilitator|everyone)\b\s*",
            user_input,
            re.IGNORECASE,
        )
        if mention_match:
            mentioned = mention_match.group(1).capitalize()
            user_input = user_input[mention_match.end():]
            api_target = None if mentioned == "Everyone" else mentioned

        # Save to session state for Phase 2
        st.session_state.queued_message = user_input
        st.session_state.queued_target = api_target
        st.session_state.waiting_for_response = True
        st.rerun()

    # --- Phase 2: Process queued message (form is now rendered as disabled) ---
    if waiting and st.session_state.get("queued_message"):
        queued_input = st.session_state.queued_message
        api_target = st.session_state.queued_target

        messages = st.session_state.get("messages", [])
        messages.append({"speaker": participant_name, "content": queued_input})
        st.session_state.messages = messages

        # Show user's bubble immediately
        room_placeholder.html(
            _build_meeting_html(
                active_speaker=participant_name,
                bubble_speaker=participant_name,
                bubble_content=queued_input,
                participant_name=participant_name,
            ),
        )

        # Send to backend and get AI responses
        api_start = time.time()
        try:
            resp = httpx.post(
                f"{API_BASE}/session/{sid}/message",
                json={"content": queued_input, "target_speaker": api_target},
                timeout=180.0,
            )
            resp.raise_for_status()
            data = resp.json()

            # Compensate timer: don't count LLM wait time against the participant
            api_wait = time.time() - api_start
            st.session_state.interview_start += api_wait

            ai_turns = data["ai_turns"]

            # Sequential reveal: show each AI turn one at a time
            display_turns = [{"speaker": participant_name, "content": queued_input}]
            for ai_turn in ai_turns:
                speaker = ai_turn["speaker"]
                content = ai_turn["content"]
                messages.append({"speaker": speaker, "content": content})

                # Append to facilitator data history and update panel immediately
                if speaker == "Facilitator":
                    hist = st.session_state.get("facilitator_history", [])
                    hist.append(content)
                    st.session_state.facilitator_history = hist
                    _render_data_panel(data_placeholder)

                # 1. Show typing dots
                room_placeholder.html(
                    _build_meeting_html(
                        active_speaker=speaker,
                        bubble_speaker=None,
                        bubble_content=None,
                        participant_name=participant_name,
                        show_typing=True,
                        typing_speaker=speaker,
                    ),
                )
                time.sleep(_display_duration(content, is_typing=True))

                # 2. Show the actual message (with TTS if enabled)
                tts_on = st.session_state.get("tts_enabled", False)
                room_placeholder.html(
                    _build_meeting_html(
                        active_speaker=speaker,
                        bubble_speaker=speaker,
                        bubble_content=content,
                        participant_name=participant_name,
                        tts_enabled=tts_on,
                        tts_settings=TTS_VOICE_SETTINGS,
                    ),
                )
                display_turns.append({"speaker": speaker, "content": content})
                time.sleep(_display_duration(content, tts_enabled=tts_on))

            # Save display state — only latest exchange visible
            st.session_state.messages = messages
            st.session_state.latest_display = display_turns
            st.session_state.session_state = data["session_state"]

        except (httpx.HTTPError, httpx.TimeoutException, Exception) as e:
            # Compensate timer even on error — LLM delay isn't the participant's fault
            api_wait = time.time() - api_start
            st.session_state.interview_start += api_wait
            # Try to extract friendly error from response body
            error_msg = str(e)
            if hasattr(e, "response") and e.response is not None:
                try:
                    detail = e.response.json().get("detail", "")
                    if detail:
                        error_msg = detail
                except Exception:
                    pass
            st.error(f"{error_msg} Please try sending your message again.")

        # Clear queued message and re-enable form
        st.session_state.queued_message = None
        st.session_state.queued_target = None
        st.session_state.waiting_for_response = False
        st.rerun()


def _show_loading_and_reveal(pending_messages: list, participant_name: str):
    """Show instruction page, then transition to opening message reveal."""
    import streamlit.components.v1 as stc

    # Dark background + hide sidebar (applies to whole page)
    st.markdown(
        "<style>"
        "section[data-testid='stMain'] {background:#0f172a !important;}"
        "[data-testid='stMainBlockContainer'] {background:#0f172a !important;}"
        "header[data-testid='stHeader'] {background:#0f172a !important;}"
        "[data-testid='stSidebar'] {display:none !important;}"
        ".block-container {padding-top:1rem !important;}"
        "</style>",
        unsafe_allow_html=True,
    )

    # Scroll to top (in iframe, but fires before visual content)
    stc.html(
        "<script>"
        "var els=window.parent.document.querySelectorAll("
        "'section.main,[data-testid=\"stMain\"],[data-testid=\"stAppViewContainer\"]');"
        "els.forEach(function(e){e.scrollTop=0;});"
        "window.parent.scrollTo(0,0);"
        "</script>",
        height=0,
    )

    # Single placeholder — first shows instructions, then replaced by meeting room
    content_area = st.empty()

    # Show instruction card
    content_area.markdown(
        "<style>"
        "@keyframes pulse-glow {"
        "  0%,100%{box-shadow:0 0 20px rgba(59,130,246,0.3);}"
        "  50%{box-shadow:0 0 40px rgba(59,130,246,0.6);}"
        "}"
        "@keyframes spin-ring {to{transform:rotate(360deg);}}"
        "@keyframes fade-up {"
        "  from{opacity:0;transform:translateY(20px);}"
        "  to{opacity:1;transform:translateY(0);}"
        "}"
        "</style>"
        '<div style="display:flex;flex-direction:column;align-items:center;'
        "justify-content:center;min-height:85vh;color:#e2e8f0;"
        "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
        'animation:fade-up 0.6s ease-out;">'
        '<div style="width:80px;height:80px;border-radius:50%;'
        "background:linear-gradient(135deg,#3b82f6,#8b5cf6);"
        "display:flex;align-items:center;justify-content:center;"
        "font-size:36px;margin-bottom:24px;"
        'animation:pulse-glow 2s ease-in-out infinite;">&#128188;</div>'
        '<div style="font-size:24px;font-weight:700;color:#f1f5f9;margin-bottom:8px;">'
        "Entering the Discussion Room</div>"
        '<div style="font-size:15px;color:#94a3b8;margin-bottom:32px;">'
        "Setting up your consulting case study...</div>"
        '<div style="max-width:520px;width:90%;background:rgba(255,255,255,0.05);'
        "border:1px solid rgba(255,255,255,0.1);border-radius:16px;"
        'padding:24px 28px;text-align:left;">'
        '<div style="font-size:14px;font-weight:600;color:#94a3b8;'
        'text-transform:uppercase;letter-spacing:1px;margin-bottom:16px;">'
        "How it works</div>"
        '<div style="padding:6px 0;font-size:15px;color:#cbd5e1;line-height:1.5;">'
        '<span style="color:#3b82f6;font-weight:700;">&#8594; </span>'
        "The <strong>Facilitator</strong> will present a business case</div>"
        '<div style="padding:6px 0;font-size:15px;color:#cbd5e1;line-height:1.5;">'
        '<span style="color:#3b82f6;font-weight:700;">&#8594; </span>'
        "Ask the Facilitator for specific data when you need it "
        "(costs, revenue, customers, etc.)</div>"
        '<div style="padding:6px 0;font-size:15px;color:#cbd5e1;line-height:1.5;">'
        '<span style="color:#3b82f6;font-weight:700;">&#8594; </span>'
        "You have <strong>15 minutes</strong> for the discussion</div>"
        '<div style="font-size:13px;color:#64748b;font-style:italic;'
        "border-top:1px solid rgba(255,255,255,0.08);"
        'padding-top:12px;margin-top:12px;">'
        "Tip: Use the speaker buttons below the meeting room to direct your "
        "message to a specific person, or type @Jordan to target someone.</div>"
        "</div>"
        '<div style="margin-top:28px;width:32px;height:32px;'
        "border:3px solid rgba(255,255,255,0.1);border-top-color:#3b82f6;"
        'border-radius:50%;animation:spin-ring 0.8s linear infinite;"></div>'
        "</div>",
        unsafe_allow_html=True,
    )

    # Let user read the instructions
    time.sleep(4)

    # Transition: replace instruction card with sequential meeting room reveal
    revealed = []
    for msg in pending_messages:
        speaker = msg["speaker"]
        msg_content = msg["content"]

        if speaker == "Facilitator":
            hist = st.session_state.get("facilitator_history", [])
            hist.append(msg_content)
            st.session_state.facilitator_history = hist

        # Typing dots
        content_area.html(
            _build_meeting_html(
                active_speaker=speaker,
                bubble_speaker=None,
                bubble_content=None,
                participant_name=participant_name,
                show_typing=True,
                typing_speaker=speaker,
            ),
        )
        time.sleep(_display_duration(msg_content, is_typing=True))

        # Show message (with TTS if enabled)
        tts_on = st.session_state.get("tts_enabled", False)
        content_area.html(
            _build_meeting_html(
                active_speaker=speaker,
                bubble_speaker=speaker,
                bubble_content=msg_content,
                participant_name=participant_name,
                tts_enabled=tts_on,
                tts_settings=TTS_VOICE_SETTINGS,
            ),
        )
        revealed.append(msg)
        time.sleep(_display_duration(msg_content, tts_enabled=tts_on))

    st.session_state.opening_display = revealed
    st.session_state.opening_revealed = True
    st.session_state.pending_opening = None
    st.session_state.latest_display = []
    st.rerun()


def _initialize_session(pid: str):
    """Create session via backend. Shows a spinner, stores data, then reruns."""
    with st.spinner("Connecting to discussion room..."):
        try:
            resp = httpx.post(
                f"{API_BASE}/session/create",
                json={"participant_id": pid},
                timeout=60.0,
            )
            resp.raise_for_status()
            data = resp.json()

            st.session_state.session_id = data["session_id"]
            st.session_state.interview_start = time.time()

            opening_messages = [
                {"speaker": m["speaker"], "content": m["content"]}
                for m in data["opening_messages"]
            ]
            st.session_state.messages = list(opening_messages)
            st.session_state.session_state = "active"
            st.session_state.opening_revealed = False
            st.session_state.opening_display = []
            st.session_state.latest_display = []
            st.session_state.pending_opening = opening_messages

            st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to start session: {e}. Is the backend running?")
