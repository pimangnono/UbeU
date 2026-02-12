"""
Case Studies: Business cases with gated data for Mode 1 interviews.

Each case study has:
- Company context (name, industry, problem statement)
- Hidden data categories revealed only when candidate asks

Modeled after McKinsey/BCG case interview format.
"""

from utils.models import CaseStudyData


# =============================================================================
# CASE 1: TECHFLOW PROFITABILITY
# =============================================================================

TECHFLOW_CASE = CaseStudyData(
    id="techflow_profitability",
    company_name="TechFlow Solutions",
    industry="Enterprise SaaS",
    problem_statement="TechFlow's profit margins have declined 15% over the past two years despite revenue growth of 25%. The CEO wants to understand why profitability is declining and what actions to take.",
    data_categories={
        "revenue_breakdown": {
            "keywords": ["revenue", "sales", "income", "top line", "pricing"],
            "data": """Revenue breakdown:
- Enterprise tier: $45M (60% of revenue, -5% YoY)
- Mid-market tier: $20M (27% of revenue, +40% YoY)
- SMB tier: $10M (13% of revenue, +80% YoY)
Average contract value: Enterprise $250K, Mid-market $50K, SMB $5K""",
            "display_name": "revenue breakdown",
            "revealed": False,
        },
        "cost_structure": {
            "keywords": ["cost", "expense", "spending", "margin", "cogs"],
            "data": """Cost structure (% of revenue):
- Sales & Marketing: 45% (up from 35% two years ago)
- R&D: 25% (stable)
- Customer Success: 18% (up from 10%)
- G&A: 12% (stable)
Customer acquisition cost: Enterprise $80K, Mid-market $25K, SMB $3K""",
            "display_name": "cost structure",
            "revealed": False,
        },
        "customer_metrics": {
            "keywords": ["customer", "churn", "retention", "ltv", "lifetime value"],
            "data": """Customer metrics:
- Enterprise churn: 5% annually
- Mid-market churn: 15% annually
- SMB churn: 35% annually
- NPS: Enterprise 65, Mid-market 45, SMB 25
LTV/CAC: Enterprise 8x, Mid-market 3x, SMB 1.2x""",
            "display_name": "customer metrics",
            "revealed": False,
        },
        "market_data": {
            "keywords": ["market", "competitor", "industry", "benchmark", "share"],
            "data": """Market data:
- Total addressable market: $2B
- TechFlow market share: 4%
- Top competitor (CloudPrime) market share: 15%
- Industry average S&M spend: 35% of revenue
- Industry average gross margin: 75%""",
            "display_name": "market and competitive data",
            "revealed": False,
        },
        "product_usage": {
            "keywords": ["usage", "feature", "engagement", "adoption", "product"],
            "data": """Product usage data:
- Feature adoption rate: 40% (only 40% of features used by average customer)
- Support tickets per customer: Enterprise 2/month, Mid-market 8/month, SMB 15/month
- Time to value: Enterprise 45 days, Mid-market 90 days, SMB 120+ days""",
            "display_name": "product usage data",
            "revealed": False,
        },
        "sales_efficiency": {
            "keywords": ["sales", "pipeline", "conversion", "cycle", "rep"],
            "data": """Sales efficiency:
- Sales cycle: Enterprise 6 months, Mid-market 3 months, SMB 2 weeks
- Win rate: Enterprise 35%, Mid-market 25%, SMB 15%
- Quota attainment: 65% of reps hitting quota
- Sales rep productivity: $800K ARR per rep (down from $1.1M two years ago)""",
            "display_name": "sales efficiency metrics",
            "revealed": False,
        },
    },
)


# =============================================================================
# CASE 2: MEDDEVICE MARKET ENTRY
# =============================================================================

MEDDEVICE_CASE = CaseStudyData(
    id="meddevice_market_entry",
    company_name="MedTech Innovations",
    industry="Medical Devices",
    problem_statement="MedTech has developed a novel diagnostic device and is considering entering the Southeast Asian market. The board wants a recommendation on whether to enter and how.",
    data_categories={
        "market_size": {
            "keywords": ["market", "size", "tam", "opportunity", "demand"],
            "data": """Southeast Asian diagnostic device market:
- Total market: $3.2B annually
- Growth rate: 12% CAGR
- Target segment (point-of-care diagnostics): $800M
- Hospital segment: 60%, Clinic segment: 30%, Home-use: 10%""",
            "display_name": "market size",
            "revealed": False,
        },
        "competitor_landscape": {
            "keywords": ["competitor", "competition", "players", "rivalry", "share"],
            "data": """Competitive landscape:
- Market leader (Siemens Healthineers): 25% share, strong hospital relationships
- #2 (Abbott): 20% share, broad product portfolio
- Regional players: 35% combined, compete on price
- MedTech's device advantage: 30% faster results, 20% lower cost per test""",
            "display_name": "competitive landscape",
            "revealed": False,
        },
        "regulatory": {
            "keywords": ["regulatory", "approval", "compliance", "fda", "certification"],
            "data": """Regulatory landscape:
- Singapore HSA approval: 6-9 months, $200K cost
- Thailand FDA: 12-18 months, $150K cost
- Indonesia BPOM: 18-24 months, $300K cost
- Regional mutual recognition possible for some approvals
- CE Mark (MedTech has this) recognized in Singapore""",
            "display_name": "regulatory requirements",
            "revealed": False,
        },
        "distribution": {
            "keywords": ["distribution", "channel", "partner", "logistics", "supply"],
            "data": """Distribution options:
- Direct sales: Requires $5M investment, 18-month setup
- Distributor partnership: 25-30% margin to distributor, immediate access
- Potential partners: 3 regional distributors with hospital networks
- Service/maintenance: Critical for hospital adoption, +$2M if direct""",
            "display_name": "distribution channels",
            "revealed": False,
        },
        "financials": {
            "keywords": ["financial", "investment", "cost", "return", "profit", "revenue"],
            "data": """Financial projections (5-year):
- Entry investment: $8-15M depending on approach
- Year 1-2: Likely losses of $3-5M
- Year 3: Break-even possible with 3% market share
- Year 5: $50M revenue at 8% market share (optimistic)
- Required IRR for approval: 15%""",
            "display_name": "financial projections",
            "revealed": False,
        },
        "risks": {
            "keywords": ["risk", "challenge", "barrier", "threat", "concern"],
            "data": """Key risks:
- Currency volatility: SGD/THB fluctuated 15% in past year
- Political: Regulatory changes possible post-election in Thailand
- Competitive response: Siemens has announced new product for 2025
- Talent: Shortage of qualified medical device sales reps in region
- Reimbursement: Hospital budgets under pressure""",
            "display_name": "key risks",
            "revealed": False,
        },
    },
)


# =============================================================================
# CASE 3: RETAILCHAIN PRICING
# =============================================================================

RETAILCHAIN_CASE = CaseStudyData(
    id="retailchain_pricing",
    company_name="ValueMart",
    industry="Grocery Retail",
    problem_statement="ValueMart is losing customers to a new discount competitor. The CEO wants to know whether to match competitor prices or pursue a different strategy.",
    data_categories={
        "customer_data": {
            "keywords": ["customer", "segment", "demographic", "shopper", "behavior"],
            "data": """Customer segments:
- Value seekers (40%): Price-first, will switch for 5% savings
- Convenience (35%): Pay premium for location/speed, 15% higher basket
- Quality (25%): Prefer premium products, 30% higher basket
Customer loss to competitor: Primarily from value seeker segment (60% of losses)""",
            "display_name": "customer segments",
            "revealed": False,
        },
        "pricing_analysis": {
            "keywords": ["price", "pricing", "discount", "premium", "margin"],
            "data": """Pricing comparison:
- ValueMart vs. competitor: 8-12% higher on comparable items
- Competitor's strategy: Loss leaders on 100 key items, standard on others
- ValueMart gross margin: 24%
- Matching all prices would reduce margin to 18%
- Private label penetration: ValueMart 15%, competitor 35%""",
            "display_name": "pricing analysis",
            "revealed": False,
        },
        "store_economics": {
            "keywords": ["store", "location", "foot traffic", "sales per", "square foot"],
            "data": """Store economics:
- Average store size: 45,000 sq ft
- Sales per sq ft: $450 (down from $500)
- Stores within 2 miles of competitor: 60% of locations
- Those stores: -15% traffic decline
- Stores not near competitor: -3% traffic decline (economy)""",
            "display_name": "store economics",
            "revealed": False,
        },
        "operations": {
            "keywords": ["operation", "supply", "inventory", "efficiency", "cost"],
            "data": """Operational data:
- Supply chain cost: 12% of revenue (industry best: 9%)
- Inventory turnover: 10x (competitor: 14x)
- Shrinkage: 2.5% (industry average: 1.5%)
- Labor cost: 11% of revenue
- Potential efficiency savings: $50M annually with investment""",
            "display_name": "operations data",
            "revealed": False,
        },
        "digital": {
            "keywords": ["digital", "online", "ecommerce", "app", "delivery"],
            "data": """Digital performance:
- Online sales: 8% of revenue (competitor: 15%)
- App downloads: 2M (competitor: 8M)
- Click & collect adoption: 12% of online orders
- Delivery cost per order: $8 (losing $3 per delivery order)
- Customer satisfaction with digital: 3.2/5 stars""",
            "display_name": "digital performance",
            "revealed": False,
        },
        "brand_perception": {
            "keywords": ["brand", "perception", "loyalty", "nps", "satisfaction"],
            "data": """Brand metrics:
- Brand awareness: 92% (strong)
- Brand preference: 35% (declining from 45%)
- NPS: +15 (competitor: +25)
- Associate with "value": 40% (competitor: 75%)
- Associate with "quality": 55% (competitor: 30%)""",
            "display_name": "brand perception",
            "revealed": False,
        },
    },
)


# =============================================================================
# CASE 4: FINTECH GROWTH
# =============================================================================

FINTECH_CASE = CaseStudyData(
    id="fintech_growth",
    company_name="QuickPay",
    industry="Fintech / Payments",
    problem_statement="QuickPay's user growth has stalled after rapid expansion. The board wants to understand the growth barriers and identify the best path to reignite growth.",
    data_categories={
        "user_metrics": {
            "keywords": ["user", "growth", "acquisition", "activation", "sign up"],
            "data": """User metrics:
- Registered users: 5M
- Monthly active users (MAU): 1.2M (24% activation)
- New user growth: 50K/month (down from 200K/month last year)
- User acquisition cost: $15/user (up from $5)
- Activation rate (first transaction): 35%""",
            "display_name": "user metrics",
            "revealed": False,
        },
        "transaction_data": {
            "keywords": ["transaction", "payment", "volume", "frequency", "amount"],
            "data": """Transaction data:
- Monthly transaction volume: $200M
- Average transaction: $45
- Transactions per active user: 4/month
- Peak times: Weekends, evening hours
- Top use cases: P2P transfers (60%), bill pay (25%), merchant (15%)""",
            "display_name": "transaction data",
            "revealed": False,
        },
        "monetization": {
            "keywords": ["revenue", "monetization", "profit", "income", "margin"],
            "data": """Monetization:
- Revenue: $30M annually
- Revenue per active user: $25/year
- Primary revenue: Merchant fees (1.5% of merchant volume)
- Secondary: Premium features (2% of users, $5/month)
- Current gross margin: 45%
- Path to profitability: Need 3x current revenue""",
            "display_name": "monetization data",
            "revealed": False,
        },
        "competitive": {
            "keywords": ["competitor", "market", "alternative", "comparison", "benchmark"],
            "data": """Competitive landscape:
- Main competitors: Traditional banks (60% share), PayNow (government, 25%)
- QuickPay share: 8%
- Competitor advantages: Trust (banks), free (PayNow)
- QuickPay advantages: Better UX, faster, social features
- New entrant threat: GrabPay expanding from ride-hailing""",
            "display_name": "competitive landscape",
            "revealed": False,
        },
        "churn_analysis": {
            "keywords": ["churn", "retention", "drop off", "leave", "abandon"],
            "data": """Churn analysis:
- Monthly churn: 8% of MAU
- Primary churn reasons: "Don't need it" (40%), "Friends don't use it" (30%), "Fees" (20%)
- Churn timing: 60% churn within first 3 months
- Power users (10+ txn/month): 5% churn
- Casual users (<3 txn/month): 15% churn""",
            "display_name": "churn analysis",
            "revealed": False,
        },
        "product_roadmap": {
            "keywords": ["product", "feature", "roadmap", "development", "investment"],
            "data": """Product options under consideration:
- Crypto/investing feature: $3M to build, uncertain regulatory
- Credit/BNPL: $5M, requires banking license
- Business accounts: $2M, targets merchant segment
- Social features (group pay): $1M, drives engagement
- Loyalty program: $1.5M, improves retention
Available development budget: $4M this year""",
            "display_name": "product roadmap options",
            "revealed": False,
        },
    },
)


# =============================================================================
# ALL CASE STUDIES
# =============================================================================

CASE_STUDIES = {
    "techflow_profitability": TECHFLOW_CASE,
    "meddevice_market_entry": MEDDEVICE_CASE,
    "retailchain_pricing": RETAILCHAIN_CASE,
    "fintech_growth": FINTECH_CASE,
}


def create_case_study(case_id: str) -> CaseStudyData:
    """Get a case study by ID. Returns a fresh copy to avoid state pollution."""
    if case_id not in CASE_STUDIES:
        raise ValueError(f"Unknown case study: {case_id}. Available: {list(CASE_STUDIES.keys())}")

    # Return a deep copy to avoid shared state
    original = CASE_STUDIES[case_id]
    return CaseStudyData(
        id=original.id,
        company_name=original.company_name,
        industry=original.industry,
        problem_statement=original.problem_statement,
        data_categories={
            k: {**v, "revealed": False}
            for k, v in original.data_categories.items()
        },
    )


def get_all_case_ids() -> list[str]:
    """Get list of all available case study IDs."""
    return list(CASE_STUDIES.keys())
