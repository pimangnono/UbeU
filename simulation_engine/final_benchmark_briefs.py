"""Final benchmark briefs: 20 real-world historical scenarios.

Each brief is a tuple of (brief_id, brief_text, simulation_mode).
- GUIDED (10): outcome-anchored scenarios with known historical outcomes
- EXPLORATORY (10): open-ended scenarios with divergent possible trajectories

All scenarios based on documented real-world events for later comparison
of simulation outcomes against what actually happened.
"""

from __future__ import annotations

from typing import NamedTuple


class BenchmarkBrief(NamedTuple):
    brief_id: str
    brief_text: str
    simulation_mode: str  # "guided" or "exploratory"
    scenario_type: str  # "policy" or "non_policy"


# ── GUIDED TRACK (10 scenarios — outcome-anchored) ──────────────────────────

GUIDED_POLICY_BRIEFS = [
    BenchmarkBrief(
        brief_id="california_ab5_gig_classification",
        brief_text=(
            "California AB5 gig worker classification law (2019-2020). The state legislature "
            "passed AB5 to reclassify gig workers as employees, but Uber and Lyft fought back "
            "with Proposition 22, spending over $200M on the campaign. Stakeholders: a single-mom "
            "DoorDash driver who needs schedule flexibility to manage childcare, a labor union "
            "organizer pushing for full employment benefits and worker protections, a small "
            "restaurant owner dependent on gig delivery platforms for 40% of revenue, and a "
            "disability rights advocate who relies on flexible gig scheduling for mobility-limited "
            "workers who cannot commit to fixed hours."
        ),
        simulation_mode="guided",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="eu_gdpr_implementation",
        brief_text=(
            "EU General Data Protection Regulation rollout (2016-2018). GDPR imposed massive "
            "compliance costs on businesses worldwide, with some US sites blocking EU users "
            "entirely rather than comply. Stakeholders: a bootstrapped SaaS startup founder "
            "facing EUR 20K compliance costs that represent 15% of annual revenue, a national "
            "data protection authority enforcement officer tasked with processing thousands of "
            "complaints, an ad-tech engineer who built the tracking systems now being dismantled "
            "and faces potential job loss, and a medical researcher whose patient data sharing "
            "across hospitals got restricted by consent requirements."
        ),
        simulation_mode="guided",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="japan_intern_training_reform",
        brief_text=(
            "Japan's Technical Intern Training Program reform (2023-2024). The program was "
            "renamed after systemic abuse reports documented wage theft, passport confiscation, "
            "and dangerous working conditions. Stakeholders: a Vietnamese trainee who experienced "
            "wage theft and isolation in a rural factory with no language support, a rural factory "
            "owner whose business depends entirely on the program due to Japan's aging population, "
            "an immigration rights lawyer documenting abuses and pushing for systemic reform, and "
            "a Japanese language school operator who feeds the pipeline and profits from mandatory "
            "pre-arrival training fees."
        ),
        simulation_mode="guided",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="nyc_congestion_pricing",
        brief_text=(
            "NYC congestion pricing (2024). The MTA approved a $15 toll for vehicles entering "
            "Manhattan below 60th Street, then Governor Hochul indefinitely paused it weeks "
            "before launch citing economic concerns. Stakeholders: an outer-borough delivery "
            "driver with no viable transit alternative who would pay $3,900/year in new tolls, "
            "an MTA capital projects manager with $15B in planned subway upgrades dependent on "
            "toll revenue, a small business owner in the congestion zone hoping for fewer cars "
            "but worried about delivery cost increases, and a hospital ambulance services "
            "coordinator worried about toll exemption complexity delaying emergency response."
        ),
        simulation_mode="guided",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="singapore_hdb_waittime_crisis",
        brief_text=(
            "Singapore HDB public housing BTO wait time crisis (2020-2023). Build-To-Order "
            "flat wait times ballooned from 3 to 5+ years due to COVID construction delays and "
            "supply chain disruptions, forcing couples to delay marriage and family planning. "
            "Stakeholders: a young couple in their late 20s who have delayed marriage for 3 years "
            "waiting for their BTO flat, a construction workers' union representative facing "
            "severe labor shortages after migrant worker dormitory lockdowns, an elderly flat "
            "owner who cannot downsize because resale market rules changed and prices surged, "
            "and an urban planner proposing satellite town expansion to increase supply."
        ),
        simulation_mode="guided",
        scenario_type="policy",
    ),
]

GUIDED_NON_POLICY_BRIEFS = [
    BenchmarkBrief(
        brief_id="boeing_737max_return",
        brief_text=(
            "Boeing 737 MAX return-to-service decision (2020). After two crashes killing 346 "
            "people and a 20-month grounding, regulators debated conditions for the MAX to fly "
            "again. Stakeholders: a regional airline CEO with 14 grounded MAX aircraft causing "
            "daily route cancellations and $2M/month in losses, a pilots' union safety committee "
            "chair demanding extensive retraining beyond Boeing's proposed iPad course, an "
            "aerospace insurance underwriter repricing risk across the entire MAX fleet, and a "
            "victim family member serving on the FAA advisory panel who lost their daughter in "
            "the Lion Air crash."
        ),
        simulation_mode="guided",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="netflix_password_crackdown",
        brief_text=(
            "Netflix password-sharing crackdown (2023). After years of tolerating account sharing "
            "among 100M+ households, Netflix enforced household-only access. Initial subscriber "
            "backlash with cancellation spikes reversed into the biggest quarterly subscriber "
            "gain in years. Stakeholders: a single parent sharing an account with their ex-spouse "
            "so their children can watch at both homes, a Netflix regional content licensing "
            "negotiator whose deals depend on subscriber count projections, a competing streamer's "
            "retention strategist seeing an influx of angry Netflix defectors, and a VPN service "
            "product manager seeing a demand spike from users trying to circumvent restrictions."
        ),
        simulation_mode="guided",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="starbucks_unionization",
        brief_text=(
            "Starbucks unionization wave (2021-2023). Over 300 stores voted to unionize, starting "
            "from a single Buffalo store, while corporate mounted aggressive counter-campaigns "
            "including store closures and firing organizers. Stakeholders: a barista-organizer "
            "working two jobs to cover rent who was written up for 'tardiness' after organizing "
            "meetings, a store manager caught between corporate directives to discourage unions "
            "and personal loyalty to their staff, a longtime customer and disability advocate "
            "concerned about service changes if experienced baristas leave, and a commercial "
            "real estate analyst tracking store closure patterns that correlate with union votes."
        ),
        simulation_mode="guided",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="microsoft_activision_merger",
        brief_text=(
            "Microsoft-Activision Blizzard $69B acquisition (2022-2023). The FTC sued to block "
            "the largest gaming acquisition in history, but ultimately lost in court. Stakeholders: "
            "a game studio creative director at Activision worried about losing creative autonomy "
            "under Microsoft's corporate structure, an esports league organizer whose entire "
            "business depends on Call of Duty franchise titles that could become Xbox exclusives, "
            "a cloud gaming infrastructure engineer at Microsoft planning technical integration "
            "of Activision's server architecture, and an indie developer worried about marketplace "
            "power consolidation reducing visibility for small studios."
        ),
        simulation_mode="guided",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="zoom_return_to_office",
        brief_text=(
            "Zoom's return-to-office mandate (2023). The company that became synonymous with "
            "remote work told employees living within 50 miles to come to the office at least "
            "twice a week. Stakeholders: a deaf employee who thrives with remote async "
            "communication and whose productivity dropped 40% in open-plan offices, an engineering "
            "manager who believes in-person whiteboard sessions produce better architecture "
            "decisions, Zoom's commercial real estate lease negotiator who secured long-term "
            "office leases pre-pandemic, and a competitor (Microsoft Teams) enterprise sales "
            "director spotting a recruiting opportunity among disgruntled Zoom employees."
        ),
        simulation_mode="guided",
        scenario_type="non_policy",
    ),
]

# ── EXPLORATORY TRACK (10 scenarios — open-ended) ───────────────────────────

EXPLORATORY_POLICY_BRIEFS = [
    BenchmarkBrief(
        brief_id="flint_water_crisis",
        brief_text=(
            "Flint, Michigan water crisis (2014-2016). The city switched water sources to save "
            "$5M, causing lead contamination that affected 100,000 residents. Government response "
            "was catastrophically slow — officials denied the problem for 18 months. Stakeholders: "
            "a pediatrician who first identified blood lead level spikes in children and was "
            "initially dismissed by state health officials, a water treatment plant operator who "
            "raised internal concerns about corrosion control before the switch, a state budget "
            "analyst who approved the cost-saving water source switch based on incomplete risk "
            "data, and a community church pastor organizing bottled water distribution while "
            "parishioners lose trust in all government institutions."
        ),
        simulation_mode="exploratory",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="australia_robodebt",
        brief_text=(
            "Australia's Robodebt automated welfare debt recovery scheme (2016-2020). An algorithm "
            "averaged annual income across fortnights to generate false debts, issuing 500,000+ "
            "notices. A Royal Commission found it unlawful; the scheme caused documented suicides. "
            "Stakeholders: a single parent issued an incorrect $12K debt notice who cannot afford "
            "legal representation, a Centrelink call center worker processing appeals they know "
            "are unjust but face disciplinary action for raising concerns, a government data "
            "scientist who flagged the averaging algorithm flaws internally but was overruled, "
            "and a social worker counseling affected clients through financial and mental health "
            "crises caused by the notices."
        ),
        simulation_mode="exploratory",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="uk_post_office_horizon",
        brief_text=(
            "UK Post Office Horizon IT scandal (2000-2024). Fujitsu's accounting software had "
            "bugs that made it appear sub-postmasters were stealing money. The Post Office "
            "prosecuted 700+ people, some were imprisoned, some committed suicide. It took 24 "
            "years for justice. Stakeholders: a sub-postmaster who was imprisoned for 15 months "
            "for 'theft' caused by system errors and lost their home, a Fujitsu developer aware "
            "of unresolved software bugs who was told not to disclose them in court, a Post "
            "Office internal auditor who saw patterns suggesting systemic software issues but "
            "was pressured to treat each case as individual fraud, and a local community member "
            "who lost their village post office and now travels 8 miles for basic services."
        ),
        simulation_mode="exploratory",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="sf_homelessness_policy",
        brief_text=(
            "San Francisco homelessness policy and Proposition C (2018-2022). A business tax "
            "to fund $300M in homeless services passed narrowly amid deep community divide. "
            "Tent encampments grew despite increased spending. Stakeholders: a small business "
            "owner whose storefront foot traffic dropped 60% due to nearby encampments, a street "
            "outreach worker with years of trust relationships among unhoused clients who fears "
            "forced sweeps will destroy that trust, an ER physician treating 20+ medical "
            "emergencies per week from encampments at enormous public cost, and a formerly "
            "homeless person now in supportive housing navigating reintegration while mentoring "
            "others still on the streets."
        ),
        simulation_mode="exploratory",
        scenario_type="policy",
    ),
    BenchmarkBrief(
        brief_id="fukushima_nuclear_restart",
        brief_text=(
            "Japan's Fukushima-area nuclear reactor restart debate (2012-present). After the "
            "2011 meltdown, all 54 reactors were shut down. Gradual restarts began against "
            "fierce local opposition, while Japan struggled with energy costs and climate goals. "
            "Stakeholders: a fishing cooperative leader whose catch was banned for years and "
            "whose livelihood depends on public perception of local seafood safety, a TEPCO "
            "safety retrofit engineer implementing new post-Fukushima standards who believes "
            "the upgrades are genuinely sufficient, an evacuee still in temporary housing 10+ "
            "years later who cannot return to their contaminated hometown, and a local mayor "
            "facing town depopulation without the nuclear plant jobs and tax revenue that "
            "sustained the community for decades."
        ),
        simulation_mode="exploratory",
        scenario_type="policy",
    ),
]

EXPLORATORY_NON_POLICY_BRIEFS = [
    BenchmarkBrief(
        brief_id="wework_ipo_collapse",
        brief_text=(
            "WeWork's IPO collapse and SoftBank rescue (2019). The company's valuation crashed "
            "from $47B to $8B after the S-1 filing exposed governance failures. CEO Adam Neumann "
            "was ousted; mass layoffs followed. Stakeholders: an enterprise tenant locked into "
            "a 10-year lease at a WeWork building whose parent company just filed for bankruptcy "
            "protection, a community manager facing imminent layoff who has been the sole point "
            "of contact for 200 members, a SoftBank investment committee member who championed "
            "the $10B investment and now faces career consequences, and a small business owner "
            "subletting desk space from a WeWork member who may lose access entirely."
        ),
        simulation_mode="exploratory",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="ftx_collapse",
        brief_text=(
            "FTX cryptocurrency exchange collapse (November 2022). $8B in customer funds were "
            "missing, secretly funneled to sister company Alameda Research. Founder Sam "
            "Bankman-Fried was convicted of fraud. Stakeholders: a retail crypto trader who "
            "moved their life savings to FTX for the 8% yield program and cannot withdraw, "
            "an Alameda Research quantitative analyst who discovered the balance sheet hole "
            "and faces personal legal exposure, a charitable foundation that received $15M in "
            "FTX donations now subject to bankruptcy clawback proceedings, and a Bahamian "
            "financial regulatory officer whose jurisdiction approved FTX's license."
        ),
        simulation_mode="exploratory",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="svb_bank_run",
        brief_text=(
            "Silicon Valley Bank run (March 2023). The fastest bank failure in US history — $42B "
            "withdrawn in a single day after the bank disclosed $1.8B in bond portfolio losses. "
            "Stakeholders: a startup CEO with two weeks of payroll for 85 employees frozen in "
            "SVB with no backup banking relationship, an SVB commercial banker who had been "
            "flagging concentration risk in tech-sector deposits internally for months, an FDIC "
            "field examiner assessing resolution options under extreme time pressure with "
            "systemic contagion risk, and a VC general partner simultaneously calming 30 "
            "portfolio companies while trying to understand their own fund's exposure."
        ),
        simulation_mode="exploratory",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="peloton_demand_cliff",
        brief_text=(
            "Peloton's post-pandemic demand cliff (2022). The stock crashed over 90% from its "
            "peak, the company laid off thousands, and warehouses filled with unsold bikes that "
            "cost more to store than to manufacture. Stakeholders: a Taiwanese factory line "
            "supervisor still producing bikes with no confirmed destination while workers fear "
            "contract cancellation, a Peloton fitness instructor being reclassified from employee "
            "to independent contractor losing health benefits, an Apple Fitness+ product lead "
            "evaluating whether to aggressively recruit Peloton's instructor talent, and an "
            "activist investor pushing for the company to be sold to a larger fitness or "
            "technology acquirer."
        ),
        simulation_mode="exploratory",
        scenario_type="non_policy",
    ),
    BenchmarkBrief(
        brief_id="theranos_whistleblower",
        brief_text=(
            "Theranos whistleblower aftermath (2015-2016). Lab technicians and employees exposed "
            "the fraudulent blood testing technology, facing legal threats and personal "
            "retaliation. Stakeholders: a lab technician running tests they know produce "
            "unreliable results who fears both patient harm and career destruction if they speak "
            "up, a hospital procurement director who integrated Theranos devices into patient "
            "workflows affecting thousands of diagnostic decisions, a patient who received "
            "incorrect blood test results that led to unnecessary medical procedures, and a "
            "Walgreens corporate partnership manager with $140M committed to the Theranos "
            "in-store testing rollout."
        ),
        simulation_mode="exploratory",
        scenario_type="non_policy",
    ),
]

# ── Combined list ────────────────────────────────────────────────────────────

FINAL_BENCHMARK_BRIEFS: list[BenchmarkBrief] = (
    GUIDED_POLICY_BRIEFS
    + GUIDED_NON_POLICY_BRIEFS
    + EXPLORATORY_POLICY_BRIEFS
    + EXPLORATORY_NON_POLICY_BRIEFS
)

ACTOR_COUNTS = [3, 5, 10]
CONDITIONS = ["engine_structural", "naive"]
REPETITIONS = 4

# Derived totals
TOTAL_SCRIPTS = len(FINAL_BENCHMARK_BRIEFS) * len(ACTOR_COUNTS)  # 60
TOTAL_RUNS = TOTAL_SCRIPTS * len(CONDITIONS) * REPETITIONS  # 480
