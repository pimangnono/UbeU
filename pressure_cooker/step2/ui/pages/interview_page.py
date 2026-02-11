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
    "Jordan":      {"color": "#dc2626", "initial": "J", "pos": "left"},
    "Sam":         {"color": "#16a34a", "initial": "S", "pos": "right"},
}

TTS_VOICE_SETTINGS = {
    "Jordan":      {"pitch": 0.9, "rate": 1.0},
    "Sam":         {"pitch": 1.1, "rate": 1.0},
}


def _display_duration(content: str, is_typing: bool = False, tts_enabled: bool = False) -> float:
    """Calculate how long to display a message based on reading speed."""
    if is_typing:
        return min(2.5, 0.8 + len(content) * 0.003)
    word_count = len(content.split())
    if tts_enabled:
        return max(3.0, word_count * 0.35)  # ~150 WPM speech
    return max(3.0, word_count * 0.3)  # ~200 WPM reading


def _parse_data_to_html(detail: str) -> str:
    """Parse case data detail text into formatted HTML with tables and charts."""
    import html as _html_mod
    import re

    lines = detail.strip().split("\n")
    html_parts = []
    current_section = None
    table_rows = []
    bar_data = []  # For percentage-based bar charts

    def flush_table():
        nonlocal table_rows
        if table_rows:
            table_html = (
                '<table style="width:100%;border-collapse:collapse;font-size:12px;margin:8px 0;">'
            )
            for row in table_rows:
                table_html += (
                    f'<tr style="border-bottom:1px solid #e2e8f0;">'
                    f'<td style="padding:6px 8px;color:#374151;font-weight:500;">{row[0]}</td>'
                    f'<td style="padding:6px 8px;color:#1e293b;text-align:right;">{row[1]}</td>'
                    f'</tr>'
                )
            table_html += '</table>'
            html_parts.append(table_html)
            table_rows = []

    def flush_bars():
        nonlocal bar_data
        if bar_data:
            bars_html = '<div style="margin:8px 0;">'
            colors = ['#3b82f6', '#22c55e', '#f59e0b', '#ef4444', '#8b5cf6']
            for i, (label, pct) in enumerate(bar_data):
                color = colors[i % len(colors)]
                bars_html += (
                    f'<div style="margin:4px 0;">'
                    f'<div style="display:flex;justify-content:space-between;font-size:11px;color:#64748b;margin-bottom:2px;">'
                    f'<span>{label}</span><span>{pct}%</span></div>'
                    f'<div style="height:8px;background:#e2e8f0;border-radius:4px;overflow:hidden;">'
                    f'<div style="height:100%;width:{min(pct, 100)}%;background:{color};border-radius:4px;"></div>'
                    f'</div></div>'
                )
            bars_html += '</div>'
            html_parts.append(bars_html)
            bar_data = []

    for line in lines:
        line = line.strip()
        if not line:
            flush_table()
            flush_bars()
            continue

        # Section header (ends with ":")
        if line.endswith(":") and not line.startswith("-"):
            flush_table()
            flush_bars()
            current_section = line[:-1]
            html_parts.append(
                f'<div style="font-weight:600;font-size:11px;color:#6b7280;'
                f'margin-top:10px;margin-bottom:4px;text-transform:uppercase;">'
                f'{_html_mod.escape(current_section)}</div>'
            )
            continue

        # Bullet point with data
        if line.startswith("- "):
            content = line[2:]

            # Try to extract percentage for bar chart
            pct_match = re.search(r'\((\d+(?:\.\d+)?)\s*%\)', content)
            if pct_match:
                pct = float(pct_match.group(1))
                label = re.sub(r'\s*\(\d+(?:\.\d+)?%\).*', '', content).strip()
                if ":" in label:
                    label = label.split(":")[0].strip()
                bar_data.append((label, pct))
                continue

            # Try to parse as table row (label: value or label — value)
            if ": " in content or " — " in content:
                flush_bars()
                sep = " — " if " — " in content else ": "
                parts = content.split(sep, 1)
                if len(parts) == 2:
                    table_rows.append((_html_mod.escape(parts[0]), _html_mod.escape(parts[1])))
                    continue

            # Fallback: add as text
            flush_table()
            flush_bars()
            html_parts.append(
                f'<div style="font-size:12px;color:#374151;padding:2px 0;padding-left:12px;">'
                f'• {_html_mod.escape(content)}</div>'
            )
            continue

        # Numbered item
        if re.match(r'^\d+\.', line):
            flush_table()
            flush_bars()
            html_parts.append(
                f'<div style="font-size:12px;color:#374151;padding:4px 0;'
                f'border-left:3px solid #3b82f6;padding-left:10px;margin:4px 0;">'
                f'{_html_mod.escape(line)}</div>'
            )
            continue

        # Key metric line (contains $, %, or numbers)
        if re.search(r'\$[\d.]+[MKB]?|\d+(?:\.\d+)?%', line):
            flush_table()
            flush_bars()
            html_parts.append(
                f'<div style="font-size:12px;color:#1e293b;padding:4px 8px;'
                f'background:#f0fdf4;border-radius:4px;margin:4px 0;">'
                f'{_html_mod.escape(line)}</div>'
            )
            continue

        # Regular text
        flush_table()
        flush_bars()
        html_parts.append(
            f'<div style="font-size:12px;color:#374151;padding:2px 0;">'
            f'{_html_mod.escape(line)}</div>'
        )

    flush_table()
    flush_bars()
    return "".join(html_parts)


def _render_data_panel(placeholder, is_new: bool = False) -> None:
    """Render the case data panel into the given st.empty() placeholder."""
    import html as _html_mod

    case_data = st.session_state.get("case_data_items", [])

    if not case_data:
        placeholder.html(
            '<div style="border:2px dashed #cbd5e1;border-radius:12px;padding:20px;'
            'height:300px;display:flex;flex-direction:column;align-items:center;'
            'justify-content:center;background:linear-gradient(135deg,#f8fafc 0%,#f1f5f9 100%);">'
            '<div style="font-size:32px;margin-bottom:12px;">📊</div>'
            '<div style="color:#64748b;font-size:14px;font-weight:600;text-align:center;">'
            'Case Data Loading...</div>'
            "</div>"
        )
        return

    cards = ""
    for i, item in enumerate(case_data):
        label = _html_mod.escape(item.get("label", f"Data {i+1}"))
        detail = item.get("detail", "")
        formatted_detail = _parse_data_to_html(detail)
        cards += (
            f'<details style="background:#f8fafc;border:1px solid #e2e8f0;'
            f'border-radius:8px;margin-bottom:8px;">'
            f'<summary style="padding:10px 14px;cursor:pointer;font-weight:600;'
            f'font-size:12px;color:#16a34a;text-transform:uppercase;letter-spacing:0.5px;'
            f'list-style:none;display:flex;align-items:center;gap:6px;">'
            f'<span style="transition:transform 0.2s;">▼</span> {label}</summary>'
            f'<div style="padding:0 14px 12px 14px;">'
            f"{formatted_detail}</div></details>"
        )

    placeholder.html(
        f'<style>'
        f'details[open] > summary span {{ transform: rotate(0deg); }}'
        f'details:not([open]) > summary span {{ transform: rotate(-90deg); }}'
        f'details summary::-webkit-details-marker {{ display: none; }}'
        f'</style>'
        f'<div style="border:2px solid #22c55e;border-radius:12px;overflow:hidden;'
        f'background:#fff;box-shadow:0 4px 12px rgba(34,197,94,0.15);">'
        f'<div style="background:linear-gradient(135deg,#22c55e 0%,#16a34a 100%);'
        f'padding:12px 16px;display:flex;align-items:center;gap:8px;">'
        f'<span style="font-size:18px;">📊</span>'
        f'<span style="font-weight:700;font-size:14px;color:white;'
        f'text-transform:uppercase;letter-spacing:1px;">Case Data</span>'
        f'<span style="margin-left:auto;background:rgba(255,255,255,0.25);'
        f'padding:2px 8px;border-radius:10px;font-size:11px;color:white;">'
        f'{len(case_data)} items</span></div>'
        f'<div style="padding:12px;max-height:550px;overflow-y:auto;">'
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

/* Speaker card below the meeting room - more immersive */
.speaker-card {
    max-width: 720px;
    margin: 1rem auto 0 auto;
    padding: 16px 20px;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 16px;
    font-size: 15px;
    line-height: 1.55;
    color: #1e293b;
    box-shadow: 0 4px 20px rgba(0,0,0,0.12), 0 0 0 1px rgba(0,0,0,0.05);
    border-left: 4px solid currentColor;
    animation: message-appear 0.4s ease-out;
    position: relative;
}
.speaker-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 16px;
    pointer-events: none;
    animation: glow-fade 1.5s ease-out;
}
.speaker-card .speaker-label {
    font-weight: 800;
    font-size: 13px;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.speaker-card .speaker-label::before {
    content: '💬';
    font-size: 14px;
}

@keyframes message-appear {
    from {
        opacity: 0;
        transform: translateY(15px) scale(0.98);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes glow-fade {
    0% { box-shadow: 0 0 30px rgba(59,130,246,0.4); }
    100% { box-shadow: 0 0 0px rgba(59,130,246,0); }
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
    fullscreen_mode: bool = False,
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

    base_html = f"""
    {_meeting_room_css()}
    <div class="meeting-room">
        <div class="meeting-table"></div>
        {avatars_html}
    </div>
    {card_html}
    {tts_html}
    """

    if fullscreen_mode:
        return f"""
        <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:#0f172a;z-index:999998;"></div>
        <div style="position:relative;z-index:999999;min-height:100vh;background:#0f172a;
                    display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;">
            {base_html}
        </div>
        """
    return base_html


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

    # --- Loading page + opening reveal (runs once after session creation) ---
    pending = st.session_state.get("pending_opening")
    if pending:
        _show_loading_and_reveal(pending, participant_name)
        return

    # --- Auto-timeout check: end session if 15 minutes have passed ---
    session_state = st.session_state.get("session_state", "active")
    if (
        session_state != "ended"
        and "interview_start" in st.session_state
        and time.time() > st.session_state.interview_start + 2 * 60
    ):
        # Time's up — automatically end the session and go to survey
        try:
            resp = httpx.post(f"{API_BASE}/session/{sid}/end", timeout=60.0)
            resp.raise_for_status()
        except Exception:
            pass
        # Mark as ended and redirect to survey
        st.session_state.session_state = "ended"
        st.session_state.waiting_for_response = False
        st.session_state.queued_message = None
        st.session_state.current_step = "survey"
        st.rerun()

    # --- Timer display (real-time JS) + TTS toggle ---
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled = False

    if "interview_start" in st.session_state:
        import streamlit.components.v1 as stc

        end_time_ms = int((st.session_state.interview_start + 2 * 60) * 1000)
        session_state = st.session_state.get("session_state", "active")

        # Timer display (sound toggle hidden - TTS not implemented)
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
                var ended=false;
                function tick(){{
                    var r=Math.max(0,end-Date.now());
                    var m=Math.floor(r/60000);
                    var s=Math.floor(r%60000/1000);
                    el.textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s+' remaining';
                    el.style.color=r<=60000?'#dc2626':r<=180000?'#ea580c':'#1e293b';
                    if(r>0){{
                        setTimeout(tick,500);
                    }}else if(!ended){{
                        ended=true;
                        el.textContent='00:00 — Time up! Click anywhere to continue to survey.';
                        el.style.color='#dc2626';
                        el.style.cursor='pointer';
                        el.onclick=function(){{
                            // Use streamlit's setComponentValue to trigger rerun
                            window.parent.postMessage({{type:'streamlit:setComponentValue',value:true}},'*');
                        }};
                    }}
                }}
                tick();
            }})();
            </script>
            """, height=35)

    # --- Check if time has expired (show end button) ---
    time_expired = (
        "interview_start" in st.session_state
        and time.time() > st.session_state.interview_start + 2 * 60
    )
    if time_expired and st.session_state.get("session_state") != "ended":
        st.warning("⏰ Time is up! Please end the session to continue to the survey.")
        if st.button("End Session & Continue to Survey", type="primary"):
            try:
                httpx.post(f"{API_BASE}/session/{sid}/end", timeout=60.0)
            except Exception:
                pass
            st.session_state.session_state = "ended"
            st.session_state.waiting_for_response = False
            st.session_state.queued_message = None
            st.session_state.current_step = "survey"
            st.rerun()

    # --- Check state before layout ---
    session_state = st.session_state.get("session_state", "active")
    demo_mode = st.session_state.get("demo_mode", False)
    waiting = st.session_state.get("waiting_for_response", False)

    # --- Anchored Problem Statement Header ---
    problem_statement = st.session_state.get("problem_statement", "")
    company_name = st.session_state.get("company_name", "")
    if problem_statement:
        st.markdown(
            f'<div style="background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%);'
            f'border:2px solid #3b82f6;border-radius:12px;padding:16px 20px;margin-bottom:16px;'
            f'box-shadow:0 4px 12px rgba(59,130,246,0.2);">'
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">'
            f'<span style="font-size:20px;">🎯</span>'
            f'<span style="font-weight:700;font-size:14px;color:#93c5fd;'
            f'text-transform:uppercase;letter-spacing:1px;">Your Task</span>'
            f'{f\'<span style="margin-left:auto;background:#3b82f6;padding:4px 12px;border-radius:16px;font-size:12px;color:white;font-weight:600;">{company_name}</span>\' if company_name else ""}'
            f'</div>'
            f'<div style="font-size:15px;color:#e2e8f0;line-height:1.6;">'
            f'{problem_statement}</div></div>',
            unsafe_allow_html=True,
        )

    # --- Two-column layout: Data Panel (main, left) + Chat Area (right) ---
    data_col, chat_col = st.columns([3, 2])

    with data_col:
        # --- Data Panel (scrollable, main focus) ---
        data_placeholder = st.empty()
        _render_data_panel(data_placeholder)

    with chat_col:
        # --- Last message from bots ---
        latest = st.session_state.get("latest_display", [])
        opening = st.session_state.get("opening_display", [])
        last_msg = None
        if latest:
            last_msg = latest[-1]
        elif opening:
            last_msg = opening[-1]

        if last_msg:
            speaker = last_msg["speaker"]
            content = last_msg["content"]
            speaker_colors = {"Jordan": "#dc2626", "Sam": "#16a34a"}
            color = speaker_colors.get(speaker, "#6b7280")
            st.markdown(
                f'<div style="background:#f8fafc;border-left:4px solid {color};'
                f'border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:12px;">'
                f'<div style="font-weight:600;font-size:13px;color:{color};margin-bottom:6px;">'
                f'{speaker}</div>'
                f'<div style="font-size:14px;color:#1e293b;line-height:1.5;">'
                f'{content}</div></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div style="background:#f1f5f9;border-radius:8px;padding:16px;'
                'text-align:center;color:#64748b;font-size:13px;margin-bottom:12px;">'
                'Discussion will appear here</div>',
                unsafe_allow_html=True,
            )

        # Keep room_placeholder for compatibility (hidden)
        room_placeholder = st.empty()

        # --- Session ended check ---
        if session_state == "ended":
            if st.button("Continue to Survey", type="primary", use_container_width=True):
                st.session_state.current_step = "survey"
                st.rerun()
            return

        # --- Demo Mode check ---
        if demo_mode:
            _run_demo_turn(sid, participant_name, room_placeholder, data_placeholder)
            return

        # --- Chat form inside chat column ---
        target_options = ["Everyone", "Jordan", "Sam"]

        with st.form("chat_form", clear_on_submit=True):
            selected = st.radio(
                "Talk to",
                target_options,
                index=0,
                horizontal=True,
                disabled=waiting,
            )
            user_input = st.text_area(
                "Message",
                placeholder=(
                    "Waiting for response..."
                    if waiting
                    else "Type your message..."
                ),
                label_visibility="collapsed",
                disabled=waiting,
                height=120,
            )
            submitted = st.form_submit_button(
                "Sending..." if waiting else "Send",
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

        # Show user's message in static format
        import html as _html_mod
        speaker_colors = {"Jordan": "#dc2626", "Sam": "#16a34a", participant_name: "#2563eb"}
        room_placeholder.html(
            f'<div style="background:#eff6ff;border-left:4px solid #2563eb;'
            f'border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:8px;">'
            f'<div style="font-weight:600;font-size:13px;color:#2563eb;margin-bottom:6px;">You</div>'
            f'<div style="font-size:14px;color:#1e293b;line-height:1.5;">'
            f'{_html_mod.escape(queued_input)}</div></div>'
            f'<div style="text-align:center;color:#64748b;font-size:12px;padding:8px;">'
            f'Waiting for response...</div>'
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

            # Build static message display for all AI responses
            display_turns = [{"speaker": participant_name, "content": queued_input}]
            all_messages_html = (
                f'<div style="background:#eff6ff;border-left:4px solid #2563eb;'
                f'border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:8px;">'
                f'<div style="font-weight:600;font-size:13px;color:#2563eb;margin-bottom:6px;">You</div>'
                f'<div style="font-size:14px;color:#1e293b;line-height:1.5;">'
                f'{_html_mod.escape(queued_input)}</div></div>'
            )

            for ai_turn in ai_turns:
                speaker = ai_turn["speaker"]
                content = ai_turn["content"]
                messages.append({"speaker": speaker, "content": content})
                display_turns.append({"speaker": speaker, "content": content})

                color = speaker_colors.get(speaker, "#6b7280")
                all_messages_html += (
                    f'<div style="background:#f8fafc;border-left:4px solid {color};'
                    f'border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:8px;">'
                    f'<div style="font-weight:600;font-size:13px;color:{color};margin-bottom:6px;">'
                    f'{speaker}</div>'
                    f'<div style="font-size:14px;color:#1e293b;line-height:1.5;">'
                    f'{_html_mod.escape(content)}</div></div>'
                )

            # Add notification sound using parent window context
            notification_sound = """
            <script>
            (function() {
                try {
                    // Access parent window's AudioContext to bypass iframe restrictions
                    var win = window.parent || window;
                    var AudioContext = win.AudioContext || win.webkitAudioContext;
                    if (AudioContext) {
                        var ctx = new AudioContext();
                        // Resume context if suspended (required for autoplay policies)
                        if (ctx.state === 'suspended') {
                            ctx.resume();
                        }
                        var osc = ctx.createOscillator();
                        var gain = ctx.createGain();
                        osc.connect(gain);
                        gain.connect(ctx.destination);
                        osc.frequency.value = 660;
                        osc.type = 'sine';
                        gain.gain.setValueAtTime(0.15, ctx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.2);
                        osc.start(ctx.currentTime);
                        osc.stop(ctx.currentTime + 0.2);
                        // Play second tone for "ding-dong" effect
                        setTimeout(function() {
                            var osc2 = ctx.createOscillator();
                            var gain2 = ctx.createGain();
                            osc2.connect(gain2);
                            gain2.connect(ctx.destination);
                            osc2.frequency.value = 880;
                            osc2.type = 'sine';
                            gain2.gain.setValueAtTime(0.15, ctx.currentTime);
                            gain2.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
                            osc2.start(ctx.currentTime);
                            osc2.stop(ctx.currentTime + 0.3);
                        }, 150);
                    }
                } catch(e) { console.log('Sound error:', e); }
            })();
            </script>
            """
            room_placeholder.html(all_messages_html + notification_sound)

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

    # Full-screen dark overlay that covers everything including any remnant UI
    st.markdown(
        "<style>"
        "html, body, [data-testid='stAppViewContainer'], section[data-testid='stMain'] {"
        "  overflow: hidden !important;"
        "  height: 100vh !important;"
        "  max-height: 100vh !important;"
        "}"
        "section[data-testid='stMain'] {background:#0f172a !important;}"
        "[data-testid='stMainBlockContainer'] {"
        "  background:#0f172a !important;"
        "  overflow: hidden !important;"
        "  height: 100vh !important;"
        "}"
        "header[data-testid='stHeader'] {background:#0f172a !important; display:none !important;}"
        "[data-testid='stSidebar'] {display:none !important;}"
        ".block-container {padding-top:0 !important; overflow: hidden !important;}"
        "/* Hide all other streamlit elements */"
        "[data-testid='stBottom'], [data-testid='stToolbar'], "
        "[data-testid='stDecoration'], footer {display:none !important;}"
        "</style>"
        "<!-- Full screen overlay to hide any background content -->"
        '<div style="position:fixed;top:0;left:0;right:0;bottom:0;'
        'background:#0f172a;z-index:999998;"></div>',
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
        '<div style="position:relative;z-index:999999;display:flex;flex-direction:column;align-items:center;'
        "justify-content:center;min-height:100vh;color:#e2e8f0;background:#0f172a;"
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
        "Review the <strong>Case Data</strong> panel on the right</div>"
        '<div style="padding:6px 0;font-size:15px;color:#cbd5e1;line-height:1.5;">'
        '<span style="color:#3b82f6;font-weight:700;">&#8594; </span>'
        "Discuss and analyze the problem with Jordan and Sam</div>"
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
    # Demo mode: 5 seconds, Normal mode: 30 seconds
    demo_mode = st.session_state.get("demo_mode", False)
    time.sleep(5 if demo_mode else 30)

    # Transition: replace instruction card with sequential meeting room reveal
    revealed = []
    for msg in pending_messages:
        speaker = msg["speaker"]
        msg_content = msg["content"]

        # Typing dots
        content_area.html(
            _build_meeting_html(
                active_speaker=speaker,
                bubble_speaker=None,
                bubble_content=None,
                participant_name=participant_name,
                show_typing=True,
                typing_speaker=speaker,
                fullscreen_mode=True,
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
                fullscreen_mode=True,
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

            # Populate data panel with all case data at start
            case_data = data.get("case_data", [])
            st.session_state.case_data_items = case_data

            # Store problem statement for anchored header
            st.session_state.problem_statement = data.get("problem_statement", "")
            st.session_state.company_name = data.get("company_name", "")

            st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to start session: {e}. Is the backend running?")


def _run_demo_turn(sid: str, participant_name: str, room_placeholder, data_placeholder):
    """Run a demo turn with AI-generated response."""
    import asyncio

    # Show demo mode indicator
    demo_persona = st.session_state.get("demo_persona", "fluent_expert")
    persona_names = {
        "fluent_expert": "🎓 Fluent Expert",
        "reluctant_expert": "😓 Reluctant Expert",
        "novice_learner": "🌱 Novice Learner",
    }

    st.markdown(
        f'<div style="background:linear-gradient(135deg,#3b82f6,#8b5cf6);'
        f'color:white;padding:8px 16px;border-radius:8px;margin-bottom:10px;'
        f'font-weight:600;text-align:center;">'
        f'🤖 DEMO MODE — {persona_names.get(demo_persona, demo_persona)} is responding...</div>',
        unsafe_allow_html=True,
    )

    # Check turn count to prevent infinite loops
    demo_turns = st.session_state.get("demo_turn_count", 0)
    max_demo_turns = 15

    if demo_turns >= max_demo_turns:
        st.success(f"Demo complete! {demo_turns} turns processed.")
        if st.button("End Demo & Continue to Survey"):
            try:
                httpx.post(f"{API_BASE}/session/{sid}/end", timeout=60.0)
            except Exception:
                pass
            st.session_state.session_state = "ended"
            st.session_state.demo_mode = False
            st.session_state.current_step = "survey"
            st.rerun()
        return

    # Generate AI response
    if st.button(f"▶️ Generate Response (Turn {demo_turns + 1}/{max_demo_turns})", type="primary"):
        st.session_state.demo_generating = True
        st.rerun()

    if st.session_state.get("demo_generating", False):
        with st.spinner("AI candidate is thinking..."):
            try:
                # Get AI response from our test candidate
                response = asyncio.run(_generate_demo_response(
                    demo_persona,
                    st.session_state.get("messages", []),
                    participant_name,
                ))

                # Show candidate's response
                room_placeholder.html(
                    _build_meeting_html(
                        active_speaker=participant_name,
                        bubble_speaker=participant_name,
                        bubble_content=response,
                        participant_name=participant_name,
                    ),
                )
                time.sleep(2)

                # Send to backend
                resp = httpx.post(
                    f"{API_BASE}/session/{sid}/message",
                    json={"content": response, "target_speaker": None},
                    timeout=180.0,
                )
                resp.raise_for_status()
                data = resp.json()

                # Process AI turns
                messages = st.session_state.get("messages", [])
                messages.append({"speaker": participant_name, "content": response})
                display_turns = [{"speaker": participant_name, "content": response}]

                for ai_turn in data.get("ai_turns", []):
                    speaker = ai_turn["speaker"]
                    content = ai_turn["content"]
                    messages.append({"speaker": speaker, "content": content})

                    # Show typing then message
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

                    room_placeholder.html(
                        _build_meeting_html(
                            active_speaker=speaker,
                            bubble_speaker=speaker,
                            bubble_content=content,
                            participant_name=participant_name,
                        ),
                    )
                    display_turns.append({"speaker": speaker, "content": content})
                    time.sleep(_display_duration(content))

                st.session_state.messages = messages
                st.session_state.latest_display = display_turns
                st.session_state.session_state = data.get("session_state", "active")
                st.session_state.demo_turn_count = demo_turns + 1
                st.session_state.demo_generating = False

                if data.get("session_state") == "ended":
                    st.session_state.demo_mode = False

                st.rerun()

            except Exception as e:
                st.error(f"Error generating response: {e}")
                st.session_state.demo_generating = False

    # Show stop button
    if st.button("⏹️ Stop Demo"):
        try:
            httpx.post(f"{API_BASE}/session/{sid}/end", timeout=60.0)
        except Exception:
            pass
        st.session_state.session_state = "ended"
        st.session_state.demo_mode = False
        st.rerun()


async def _generate_demo_response(persona_id: str, messages: list, participant_name: str) -> str:
    """Generate a response using the AI test candidate."""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

    from agents.test_candidate_agent import AITestCandidate
    from clients.llm_client import LLMClient
    from config.test_personas import get_test_persona
    from config.scenarios import SCENARIOS

    persona = get_test_persona(persona_id)
    scenario = list(SCENARIOS.values())[0]

    client = LLMClient()
    candidate = AITestCandidate(
        client=client,
        scenario=scenario,
        persona=persona,
        case_study=None,
    )

    # Build context from recent messages
    context_parts = []
    for msg in messages[-8:]:
        context_parts.append(f"[{msg['speaker']}]: {msg['content']}")

    context = "\n".join(context_parts)
    if context:
        context = f"Recent conversation:\n{context}"

    response = await candidate.generate_response(context)
    return response
