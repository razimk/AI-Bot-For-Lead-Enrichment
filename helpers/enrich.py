def enrich_company(company_name):
    return {
        "company_name": company_name,
        "website": f"https://www.{company_name.lower()}.com",
        "industry": "Software",
        "company_size": "201-500",
        "hq_location": "San Francisco, USA"
    }
