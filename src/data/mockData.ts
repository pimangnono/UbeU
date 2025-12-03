export const sectors = [
    {
        id: 'accountancy',
        label: 'Accountancy',
        tracks: [
            {
                id: 'assurance',
                label: 'Assurance',
                roles: [
                    { id: 'audit-manager', label: 'Audit Manager' },
                    { id: 'senior-associate', label: 'Senior Associate' },
                    { id: 'junior-auditor', label: 'Junior Auditor' },
                ],
            },
            {
                id: 'tax',
                label: 'Tax',
                roles: [
                    { id: 'tax-consultant', label: 'Tax Consultant' },
                    { id: 'tax-manager', label: 'Tax Manager' },
                ],
            },
            {
                id: 'advisory',
                label: 'Advisory',
                roles: [
                    { id: 'risk-consultant', label: 'Risk Consultant' },
                    { id: 'strategy-associate', label: 'Strategy Associate' },
                ],
            },
        ],
    },
    {
        id: 'technology',
        label: 'Technology',
        tracks: [
            {
                id: 'software-engineering',
                label: 'Software Engineering',
                roles: [
                    { id: 'frontend-dev', label: 'Frontend Developer' },
                    { id: 'backend-dev', label: 'Backend Developer' },
                    { id: 'fullstack-dev', label: 'Fullstack Developer' },
                ],
            },
            {
                id: 'data',
                label: 'Data Science',
                roles: [
                    { id: 'data-analyst', label: 'Data Analyst' },
                    { id: 'ml-engineer', label: 'Machine Learning Engineer' },
                ],
            },
        ],
    },
    {
        id: 'marketing',
        label: 'Marketing',
        tracks: [
            {
                id: 'digital',
                label: 'Digital Marketing',
                roles: [
                    { id: 'seo-specialist', label: 'SEO Specialist' },
                    { id: 'content-strategist', label: 'Content Strategist' },
                ],
            },
        ],
    },
];

export const difficultyLevels = [
    { id: 'intern', label: 'Intern', description: 'Basic concepts and behavioral fit' },
    { id: 'fresh-grad', label: 'Fresh Graduate', description: 'Foundational knowledge and problem solving' },
    { id: 'junior', label: '1-3 Years Exp', description: 'Applied skills and scenario handling' },
    { id: 'senior', label: '3-5 Years Exp', description: 'Advanced technical and leadership scenarios' },
    { id: 'expert', label: '5+ Years Exp', description: 'Strategic thinking and complex crisis management' },
];

export const personas = [
    { id: 'strict', label: 'Strict Technical Interviewer', description: 'Focuses on deep technical details and edge cases. Minimal small talk.' },
    { id: 'friendly', label: 'Friendly HR Manager', description: 'Focuses on culture fit, soft skills, and behavioral questions. Encouraging tone.' },
    { id: 'pragmatic', label: 'Pragmatic Team Lead', description: 'Balanced approach. Interested in practical problem solving and collaboration.' },
    { id: 'stress', label: 'Stress Tester', description: 'Intentionally challenges the candidate to see how they handle pressure.' },
];

export const timeDurations = [
    { id: '20', label: '20 min' },
    { id: '45', label: '45 min' },
    { id: '60', label: '60 min' },
];

export const interviewTypes = [
    { id: '1-to-1', label: '1-to-1 Interview', description: 'Standard individual interview format.' },
    { id: 'group-case', label: 'Group Case Study', description: 'Candidates work together to solve a business case.' },
    { id: 'group-discussion', label: 'Group Discussion', description: 'Candidates discuss a specific topic or issue.' },
    { id: 'role-play', label: 'Role-Play Simulation', description: 'Simulated scenario to test specific skills.' },
];

export const assessmentCategories = [
    {
        id: 'problem-solving',
        label: 'Problem-Solving / Analytical',
        templates: [
            { id: 'guesstimation', label: 'Guesstimation', description: 'Estimate an unknown quantity using structured assumptions and logical reasoning.' },
            { id: 'market-sizing', label: 'Market Sizing', description: 'Calculate the size of a market or demand using data-driven assumptions.' },
            { id: 'data-interpretation', label: 'Data Interpretation', description: 'Analyze charts, tables, or short datasets to extract insights and make decisions.' },
            { id: 'analytical-reasoning', label: 'Analytical Reasoning', description: 'Solve structured logical problems that require identifying patterns or cause–effect.' },
            { id: 'logical-case', label: 'Logical Case Analysis', description: 'Break down a small case scenario into components, identify issues, and propose solutions.' },
        ]
    },
    {
        id: 'case-based',
        label: 'Case-Based',
        templates: [
            { id: 'business-case', label: 'Business Case Study', description: 'Evaluate a business scenario, diagnose challenges, and recommend strategic actions.' },
            { id: 'operational', label: 'Operational / Process Improvement', description: 'Identify inefficiencies in a workflow or system and propose improvements.' },
            { id: 'product-thinking', label: 'Product Thinking Case', description: 'Analyze user needs and propose product features, improvements, or trade-offs.' },
            { id: 'customer-experience', label: 'Customer Experience Case', description: 'Evaluate customer pain points and design solutions to improve end-to-end experience.' },
            { id: 'public-policy', label: 'Public Policy Case', description: 'Analyze a societal or public-sector problem and propose policy interventions.' },
            { id: 'strategy', label: 'Strategy Case', description: 'Assess competitive dynamics and recommend high-level strategic directions.' },
            { id: 'financial', label: 'Financial Case Analysis', description: 'Interpret financial statements or metrics to propose financially sound decisions.' },
        ]
    },
    {
        id: 'behavioral',
        label: 'Behavioural / Soft-Skill',
        templates: [
            { id: 'collaboration', label: 'Collaboration Scenario', description: 'Work with multiple teammates to jointly solve a problem or produce an outcome.' },
            { id: 'conflict-management', label: 'Conflict Management', description: 'Handle disagreement, misalignment, or interpersonal friction constructively.' },
            { id: 'influencing', label: 'Influencing & Stakeholder Mgmt', description: 'Persuade or align different stakeholders with conflicting agendas or priorities.' },
            { id: 'leadership', label: 'Leadership Simulation', description: 'Demonstrate decision-making, team guidance, and prioritization under pressure.' },
            { id: 'inclusivity', label: 'Inclusivity & Team Dynamics', description: 'Ensure equitable participation, respect diverse viewpoints, and foster a safe environment.' },
            { id: 'change-adaptability', label: 'Change & Adaptability', description: 'Respond to unexpected changes in scope, data, or requirements quickly and calmly.' },
        ]
    },
    {
        id: 'communication',
        label: 'Communication',
        templates: [
            { id: 'presentation', label: 'Structured Presentation / Pitch', description: 'Deliver a clear, logical presentation summarizing insights and recommendations.' },
            { id: 'summarization', label: 'Summarization Challenge', description: 'Distill a complex problem or dataset into a concise, high-level summary.' },
            { id: 'debate', label: 'Debate or Discussion Prompt', description: 'Present and defend a viewpoint while engaging respectfully with opposing arguments.' },
        ]
    },
    {
        id: 'creative',
        label: 'Creative / Innovation',
        templates: [
            { id: 'brainstorming', label: 'Brainstorming Challenge', description: 'Generate a wide range of ideas under time pressure.' },
            { id: 'innovation', label: 'Innovation Ideation', description: 'Propose novel solutions using creative and lateral thinking methods.' },
            { id: 'product-redesign', label: 'Product Redesign Case', description: 'Redesign an existing product or service to better meet user needs or improve performance.' },
        ]
    },
];
