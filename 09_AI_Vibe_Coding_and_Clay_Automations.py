"""
Maya HTT GTM Engineering — AI-Enabled Workflow & Enrichment Automation
Simulates automated lead enrichment, account signal detection, and customized outreach generation.
"""

import json

def enrich_account_signal(company_name: str, tech_stack: list) -> dict:
    has_siemens = any(tool in ["Teamcenter", "NX", "Simcenter"] for tool in tech_stack)
    signal_score = 95 if has_siemens else 60
    
    return {
        "company": company_name,
        "siemens_ecosystem_user": has_siemens,
        "fit_score": signal_score,
        "recommended_angle": "Co-Sell AI Integration & Custom IP" if has_siemens else "CAE Software Optimization"
    }

def generate_ai_personalized_copy(account_data: dict) -> str:
    company = account_data["company"]
    angle = account_data["recommended_angle"]
    
    return f"""
    Hi Team,

    Noticed {company} is leveraging core industrial engineering workflows. 
    Maya HTT specializes in {angle}, accelerating simulation solve times and bridging operational data directly into Teamcenter.

    Best,
    Peyton Backus | Maya HTT GTM Team
    """.strip()

if __name__ == "__main__":
    sample_account = enrich_account_signal("Aerospace Dynamics Inc", ["NX", "Teamcenter", "Ansys"])
    copy = generate_ai_personalized_copy(sample_account)
    
    print("\n" + "="*50)
    print(" GTM AI-ENABLED WORKFLOW TEST RUN")
    print("="*50)
    print("ENRICHMENT DATA:\n", json.dumps(sample_account, indent=2))
    print("\nPERSONALIZED OUTREACH COPY:\n", copy)
    print("="*50 + "\n")
