"""
4 Consulting Case Study Scenarios for Pressure Cooker Step 2.

Each case has a clear company + problem + 5-6 hidden data categories
that are revealed only when the candidate asks about them.
"""

from step2.case_data import CaseStudy, CaseDataItem


# --- Case 1: TechFlow (SaaS, profitability) ---

TECHFLOW = CaseStudy(
    id="techflow",
    company_name="TechFlow",
    industry="B2B SaaS",
    problem_statement=(
        "We're a B2B SaaS company with $12M ARR but margins are declining. "
        "How can we improve profitability by 5 percentage points?"
    ),
    data_items=[
        CaseDataItem(
            category="customer_segments",
            label="Customer Segments",
            detail=(
                "Three segments:\n"
                "- Enterprise (50 accounts, $150K avg ACV, 95% retention) — 62% of revenue\n"
                "- Mid-market (200 accounts, $25K avg ACV, 85% retention) — 42% of revenue\n"
                "- SMB (800 accounts, $3K avg ACV, 65% retention) — 20% of revenue\n"
                "Note: SMB accounts consume 45% of support tickets but contribute only 20% of revenue."
            ),
            keywords=["customer", "segment", "who are the customers", "client", "account", "user base"],
        ),
        CaseDataItem(
            category="revenue",
            label="Revenue Breakdown",
            detail=(
                "Total ARR: $12M\n"
                "- Subscription revenue: $10.2M (85%)\n"
                "- Professional services: $1.2M (10%)\n"
                "- Usage-based overages: $0.6M (5%)\n"
                "ARPU trend: Enterprise +8% YoY, Mid-market flat, SMB -12% YoY\n"
                "Net revenue retention: 108% (Enterprise), 95% (Mid-market), 72% (SMB)"
            ),
            keywords=["revenue", "ARR", "ARPU", "how much", "income", "sales", "money", "pricing"],
        ),
        CaseDataItem(
            category="costs",
            label="Cost Structure",
            detail=(
                "Total operating costs: $11.4M (95% of revenue)\n"
                "- Engineering & Product: $4.2M (37%)\n"
                "- Sales & Marketing: $3.6M (32%) — CAC: $45K Enterprise, $8K Mid-market, $2K SMB\n"
                "- Customer Success & Support: $2.1M (18%) — 60% of support costs from SMB\n"
                "- G&A: $1.5M (13%)\n"
                "Gross margin: 72% (down from 78% two years ago)"
            ),
            keywords=["cost", "expense", "spending", "margin", "CAC", "burn", "overhead", "budget"],
        ),
        CaseDataItem(
            category="competitors",
            label="Competitive Landscape",
            detail=(
                "Key competitors:\n"
                "1. **StreamLine** — $45M ARR, 30% market share. Premium pricing ($200K+ Enterprise). "
                "Known for enterprise features and compliance. Weakness: slow innovation cycle.\n"
                "2. **QuickOps** — $18M ARR, 15% market share. Low-cost leader ($1.5K SMB plans). "
                "Aggressive growth strategy, burning cash. Strength: self-serve onboarding.\n"
                "3. **DataBridge** — $8M ARR, 8% market share. Niche focus on healthcare vertical. "
                "Higher margins (82% gross). Strength: deep domain expertise.\n"
                "TechFlow market share: ~10%"
            ),
            keywords=["competitor", "competition", "market share", "rival", "alternative", "landscape", "benchmark"],
        ),
        CaseDataItem(
            category="operations",
            label="Operations & Product",
            detail=(
                "Product:\n"
                "- Core platform with 3 pricing tiers (Starter, Growth, Enterprise)\n"
                "- 18-month old technical debt in SMB onboarding flow\n"
                "- Enterprise feature requests backlog: 6 months\n"
                "- Platform uptime: 99.7% (below industry standard 99.9%)\n\n"
                "Team: 85 employees\n"
                "- Engineering: 35, Sales: 20, CS/Support: 15, Marketing: 8, G&A: 7\n"
                "- Support team handles avg 1,200 tickets/month (SMB: 540, Mid: 420, Ent: 240)"
            ),
            keywords=["operation", "product", "team", "employee", "platform", "technical", "infrastructure", "headcount"],
        ),
    ],
)


# --- Case 2: GreenLeaf (organic food, market entry) ---

GREENLEAF = CaseStudy(
    id="greenleaf",
    company_name="GreenLeaf",
    industry="Organic Food & Beverage",
    problem_statement=(
        "We're a regional organic food brand with $8M revenue considering national expansion. "
        "Should we enter the retail or D2C channel?"
    ),
    data_items=[
        CaseDataItem(
            category="current_operations",
            label="Current Operations",
            detail=(
                "Regional presence: 3 states in the Pacific Northwest\n"
                "Distribution: 180 independent grocery stores + 12 regional chain locations\n"
                "Product lines: organic snack bars (60% of revenue), granola (25%), trail mix (15%)\n"
                "Manufacturing: single facility, currently at 70% capacity\n"
                "Brand recognition: 42% aided awareness in current region, <5% nationally"
            ),
            keywords=["operation", "current", "today", "existing", "distribution", "product", "manufacturing", "facility"],
        ),
        CaseDataItem(
            category="customer_base",
            label="Customer Demographics",
            detail=(
                "Core customer profile:\n"
                "- Age 28-45, household income $75K+, health-conscious\n"
                "- 70% female, 85% college-educated\n"
                "- Purchase frequency: 2.3x/month (loyal segment), 0.6x/month (casual)\n"
                "- NPS: 72 (excellent for CPG)\n"
                "- Customer acquisition: 55% word-of-mouth, 25% in-store discovery, 20% social media"
            ),
            keywords=["customer", "consumer", "demographic", "who buys", "target", "audience", "buyer", "shopper"],
        ),
        CaseDataItem(
            category="financials",
            label="Financial Details",
            detail=(
                "Revenue: $8M (growing 22% YoY)\n"
                "Gross margin: 45% (retail), estimated 62% (D2C based on industry benchmarks)\n"
                "Net margin: 8%\n"
                "Cash on hand: $2.1M\n"
                "Available credit line: $1.5M\n"
                "Estimated national retail expansion cost: $3-5M (slotting fees, sales team, logistics)\n"
                "Estimated D2C launch cost: $1.5-2.5M (e-commerce, fulfillment, digital marketing)"
            ),
            keywords=["financial", "money", "revenue", "margin", "cost", "profit", "cash", "budget", "investment", "price"],
        ),
        CaseDataItem(
            category="competitors",
            label="Competitive Landscape",
            detail=(
                "Key competitors:\n"
                "1. **NatureValley (General Mills)** — $800M+ revenue. Dominant shelf space. "
                "Mass market positioning, lower price point ($0.15/oz vs GreenLeaf $0.28/oz). "
                "Weakness: perceived as less 'authentic' organic.\n"
                "2. **RXBAR (Kellogg's)** — $200M revenue. Strong D2C + retail hybrid. "
                "Premium pricing ($0.32/oz). Strength: clean label marketing, strong social media.\n"
                "3. **Purely Elizabeth** — $50M revenue. Regional-to-national success story. "
                "Started D2C, expanded to Whole Foods then mainstream retail. 65% retail / 35% D2C mix."
            ),
            keywords=["competitor", "competition", "market", "rival", "brand", "alternative", "landscape", "who else"],
        ),
        CaseDataItem(
            category="supply_chain",
            label="Supply Chain & Logistics",
            detail=(
                "Current supply chain:\n"
                "- 4 organic ingredient suppliers (2 local, 2 national)\n"
                "- Lead time: 3-4 weeks for key ingredients\n"
                "- Shelf life: 9 months (bars), 12 months (granola/trail mix)\n"
                "- Shipping: regional LTL carrier, avg $0.18/unit\n\n"
                "National expansion logistics:\n"
                "- Retail: would need 2-3 regional distribution centers ($200K/year each)\n"
                "- D2C: could use 3PL fulfillment partner, avg $0.85/unit shipped\n"
                "- D2C return rate: industry avg 3-5% for food/beverage"
            ),
            keywords=["supply", "logistics", "shipping", "warehouse", "fulfillment", "distribution", "chain", "delivery"],
        ),
    ],
)


# --- Case 3: MediCore (healthcare, efficiency) ---

MEDICORE = CaseStudy(
    id="medicore",
    company_name="MediCore",
    industry="Healthcare / Hospital Network",
    problem_statement=(
        "Our hospital network is running at 78% bed occupancy but operating costs are "
        "15% above regional average. How do we improve efficiency?"
    ),
    data_items=[
        CaseDataItem(
            category="operations",
            label="Operations Overview",
            detail=(
                "Network: 4 hospitals across 2 metropolitan areas\n"
                "Total beds: 1,200 (300 per hospital)\n"
                "Bed occupancy: 78% average (Hospital A: 88%, B: 82%, C: 72%, D: 68%)\n"
                "Average length of stay: 4.8 days (regional avg: 4.2 days)\n"
                "ED wait time: 3.2 hours average (regional avg: 2.1 hours)\n"
                "Surgical suite utilization: 62% (industry benchmark: 75-80%)"
            ),
            keywords=["operation", "hospital", "bed", "occupancy", "facility", "utilization", "capacity", "how many"],
        ),
        CaseDataItem(
            category="financials",
            label="Financial Performance",
            detail=(
                "Annual revenue: $480M\n"
                "Operating costs: $465M (96.9% of revenue)\n"
                "Operating margin: 3.1% (regional avg: 5.5%)\n"
                "Cost breakdown:\n"
                "- Labor: $280M (60%) — 4,800 FTE, avg cost $58K/employee\n"
                "- Supplies & equipment: $95M (20%)\n"
                "- Facility & maintenance: $48M (10%)\n"
                "- Administrative: $42M (9%)\n"
                "Revenue per adjusted patient day: $2,850 (regional avg: $2,920)"
            ),
            keywords=["financial", "cost", "revenue", "money", "expense", "margin", "budget", "spend", "profit"],
        ),
        CaseDataItem(
            category="staffing",
            label="Staffing & Workforce",
            detail=(
                "Total FTE: 4,800\n"
                "- Nursing: 2,100 (nurse-to-patient ratio 1:5.2, benchmark 1:4.5)\n"
                "- Physicians: 420\n"
                "- Administrative/clerical: 980 (20% of total, benchmark 15%)\n"
                "- Support staff: 1,300\n\n"
                "Overtime costs: $18M/year (6.4% of labor costs)\n"
                "Turnover rate: 22% nursing (industry avg: 18%)\n"
                "Agency/temp staff costs: $12M/year\n"
                "Average tenure: 3.2 years (down from 4.8 years three years ago)"
            ),
            keywords=["staff", "employee", "nurse", "doctor", "workforce", "hiring", "labor", "people", "team", "headcount"],
        ),
        CaseDataItem(
            category="competitors",
            label="Comparable Networks & Benchmarks",
            detail=(
                "Comparable hospital networks:\n"
                "1. **RegionalHealth Partners** — 5 hospitals, 1,500 beds. Operating margin: 6.2%. "
                "Known for lean operations and centralized scheduling. Admin staff: 14% of total. "
                "Average length of stay: 4.0 days.\n"
                "2. **MetroCare Systems** — 3 hospitals, 900 beds. Operating margin: 5.8%. "
                "Invested $15M in EHR optimization, reduced documentation time 30%. "
                "Surgical utilization: 78%.\n"
                "3. **Unity Health** — 4 hospitals, 1,100 beds. Operating margin: 4.9%. "
                "Best-in-class ED throughput (1.8hr wait). Weakness: high supply costs."
            ),
            keywords=["competitor", "benchmark", "compare", "other hospital", "peer", "industry", "standard", "best practice"],
        ),
        CaseDataItem(
            category="patient_flow",
            label="Patient Flow & Quality",
            detail=(
                "Patient flow metrics:\n"
                "- Admissions: 52,000/year\n"
                "- Readmission rate (30-day): 14.2% (benchmark: 11%)\n"
                "- Discharge delays: avg 6.2 hours after medical clearance\n"
                "- Bed turnover time: 4.5 hours (benchmark: 2.5 hours)\n"
                "- Elective surgery cancellation rate: 8% (benchmark: 3%)\n\n"
                "Quality scores:\n"
                "- Patient satisfaction (HCAHPS): 68th percentile\n"
                "- Infection rates: at regional average\n"
                "- Medication error rate: slightly above average (1.2 vs 0.9 per 1000 patient days)"
            ),
            keywords=["patient", "flow", "admission", "discharge", "readmission", "quality", "satisfaction", "wait", "throughput"],
        ),
    ],
)


# --- Case 4: SwiftCart (e-commerce, retention) ---

SWIFTCART = CaseStudy(
    id="swiftcart",
    company_name="SwiftCart",
    industry="E-commerce",
    problem_statement=(
        "Our e-commerce platform has 2M active users but repeat purchase rate dropped "
        "from 35% to 22%. How do we recover retention?"
    ),
    data_items=[
        CaseDataItem(
            category="user_data",
            label="User & Behavior Data",
            detail=(
                "Active users: 2M monthly (defined as visited in last 30 days)\n"
                "Registered users: 5.2M total\n"
                "User cohort behavior:\n"
                "- Power users (5+ orders/year): 180K users, 52% of revenue, retention 78%\n"
                "- Regular users (2-4 orders/year): 420K users, 31% of revenue, retention 45%\n"
                "- One-time buyers: 1.4M users, 17% of revenue, retention 8%\n\n"
                "Key drop-off points:\n"
                "- 60% of one-time buyers never return after first purchase\n"
                "- Biggest churn spike: days 14-30 after first purchase\n"
                "- App uninstall rate: 35% within 90 days"
            ),
            keywords=["user", "customer", "behavior", "who", "cohort", "active", "demographic", "buyer"],
        ),
        CaseDataItem(
            category="product_mix",
            label="Product & Category Mix",
            detail=(
                "Product categories (by GMV):\n"
                "- Electronics: 35% ($52.5M) — highest AOV ($120), lowest repeat rate (15%)\n"
                "- Fashion: 28% ($42M) — moderate AOV ($55), moderate repeat (32%)\n"
                "- Home & Living: 22% ($33M) — moderate AOV ($65), highest repeat (48%)\n"
                "- Beauty & Personal Care: 15% ($22.5M) — lowest AOV ($35), high repeat (44%)\n\n"
                "Total GMV: $150M\n"
                "Average order value: $62 (down from $68 last year)\n"
                "Items per order: 2.3 (down from 2.8)"
            ),
            keywords=["product", "category", "sell", "item", "catalog", "what do they sell", "SKU", "merchandise", "GMV"],
        ),
        CaseDataItem(
            category="marketing",
            label="Marketing & Acquisition",
            detail=(
                "Monthly marketing spend: $2.8M\n"
                "Channel mix:\n"
                "- Paid social (Meta/TikTok): 40% of spend, CAC $18\n"
                "- Search (Google): 25% of spend, CAC $22\n"
                "- Influencer/affiliate: 15% of spend, CAC $28\n"
                "- Email/push: 10% of spend, CAC $5 (existing users only)\n"
                "- Retargeting: 10% of spend, CAC $12\n\n"
                "Overall blended CAC: $19 (up from $14 last year)\n"
                "LTV:CAC ratio: 2.8 (down from 3.5)\n"
                "Email open rate: 18% (industry avg: 22%)\n"
                "Push notification opt-in: 32% (declining)"
            ),
            keywords=["marketing", "acquisition", "CAC", "advertising", "ad spend", "channel", "campaign", "LTV"],
        ),
        CaseDataItem(
            category="competitors",
            label="Competitive Landscape",
            detail=(
                "Key competitors:\n"
                "1. **ShopEase** — 5M active users, 38% repeat rate. Loyalty program with "
                "tiered rewards (Bronze/Silver/Gold). Free shipping threshold: $40. "
                "Strength: personalized recommendations, 15% of revenue from loyalty program.\n"
                "2. **BuyFast** — 3M active users, 28% repeat rate. Aggressive pricing strategy, "
                "flash sales 2x/week. Subscription box option for consumables. "
                "Strength: fastest delivery (same-day in 12 cities).\n"
                "3. **TrendMart** — 1.5M active users, 42% repeat rate. Niche focus on curated "
                "lifestyle products. Higher prices but strong brand community. "
                "Strength: UGC content, 25% of traffic from community/social."
            ),
            keywords=["competitor", "competition", "rival", "other platform", "benchmark", "market", "landscape", "who else"],
        ),
        CaseDataItem(
            category="customer_support",
            label="Customer Support & Experience",
            detail=(
                "Support metrics:\n"
                "- Monthly tickets: 85,000\n"
                "- Top issues: delivery delays (28%), returns/refunds (24%), product quality (18%), "
                "account issues (15%), other (15%)\n"
                "- Average resolution time: 18 hours (industry benchmark: 12 hours)\n"
                "- CSAT score: 3.6/5 (industry avg: 4.1/5)\n"
                "- Return rate: 12% (up from 8% last year)\n\n"
                "Post-purchase experience:\n"
                "- Avg delivery time: 4.2 days (competitor avg: 2.8 days)\n"
                "- On-time delivery rate: 82% (industry benchmark: 92%)\n"
                "- No post-purchase engagement program currently"
            ),
            keywords=["support", "service", "complaint", "return", "delivery", "experience", "satisfaction", "NPS", "CSAT", "help"],
        ),
    ],
)


# --- Scenario registry ---

CONSULTING_SCENARIOS: dict[str, CaseStudy] = {
    "techflow": TECHFLOW,
    "greenleaf": GREENLEAF,
    "medicore": MEDICORE,
    "swiftcart": SWIFTCART,
}


def get_consulting_scenario(scenario_id: str) -> CaseStudy:
    """Get a consulting case study by ID."""
    if scenario_id not in CONSULTING_SCENARIOS:
        raise ValueError(
            f"Unknown consulting scenario: {scenario_id}. "
            f"Available: {list(CONSULTING_SCENARIOS.keys())}"
        )
    return CONSULTING_SCENARIOS[scenario_id]


def get_all_consulting_scenario_ids() -> list[str]:
    """Get all available consulting scenario IDs."""
    return list(CONSULTING_SCENARIOS.keys())
