import difflib

def find_canonical_account(incoming_domain, existing_accounts):
    """
    Fuzzy-matches incoming lead domains against canonical CRM Account records.
    """
    domains = [acc['domain'] for acc in existing_accounts]
    matches = difflib.get_close_matches(incoming_domain, domains, n=1, cutoff=0.85)
    
    if matches:
        matched_domain = matches[0]
        for acc in existing_accounts:
            if acc['domain'] == matched_domain:
                return {"status": "MATCH_FOUND", "account_id": acc['id'], "matched_domain": matched_domain}
    
    return {"status": "NO_MATCH", "account_id": None, "matched_domain": None}

if __name__ == "__main__":
    crm_db = [{"id": "acc_001", "domain": "mayahtt.com"}, {"id": "acc_002", "domain": "planful.com"}]
    print(find_canonical_account("maya-htt.com", crm_db))
