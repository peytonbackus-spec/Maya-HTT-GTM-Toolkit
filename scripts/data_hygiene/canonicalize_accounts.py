import difflib

def find_canonical_account(incoming_domain, existing_accounts):
    """
    Fuzzy-matches incoming lead domains against canonical CRM Account records.
    Prevents duplicate account creation during signal-based Clay enrichment.
    """
    domains = [acc['domain'] for acc in existing_accounts]
    matches = difflib.get_close_matches(incoming_domain, domains, n=1, cutoff=0.85)
    
    if matches:
        matched_domain = matches[0]
        for acc in existing_accounts:
            if acc['domain'] == matched_domain:
                return {
                    "status": "MATCH_FOUND",
                    "account_id": acc['id'],
                    "matched_domain": matched_domain,
                    "action": "LINK_TO_EXISTING"
                }
    
    return {
        "status": "NO_MATCH",
        "account_id": None,
        "matched_domain": None,
        "action": "CREATE_NEW_ACCOUNT"
    }

if __name__ == "__main__":
    crm_db = [
        {"id": "acc_001", "domain": "mayahtt.com"},
        {"id": "acc_002", "domain": "planful.com"}
    ]
    # Test fuzzy domain match
    print(find_canonical_account("maya-htt.com", crm_db))
