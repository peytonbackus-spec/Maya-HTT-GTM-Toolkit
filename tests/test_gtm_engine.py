import pytest
from scripts.data_hygiene.canonicalize_accounts import find_canonical_account
from integrations.gong.gong_trigger_handler import process_gong_call_event

# Mock CRM DB for matching tests
MOCK_CRM = [
    {"id": "acc_100", "domain": "mayahtt.com"},
    {"id": "acc_200", "domain": "planful.com"}
]

def test_canonicalize_accounts_exact_match():
    res = find_canonical_account("mayahtt.com", MOCK_CRM)
    assert res["status"] == "MATCH_FOUND"
    assert res["account_id"] == "acc_100"

def test_canonicalize_accounts_fuzzy_match():
    # Handles dash variation (maya-htt.com -> mayahtt.com)
    res = find_canonical_account("maya-htt.com", MOCK_CRM)
    assert res["status"] == "MATCH_FOUND"
    assert res["account_id"] == "acc_100"

def test_canonicalize_accounts_no_match():
    res = find_canonical_account("unrelatedcompany.io", MOCK_CRM)
    assert res["status"] == "NO_MATCH"
    assert res["account_id"] is None

def test_gong_trigger_handler_risk_detection():
    # Call payload missing competitor discovery
    payload_no_comp = '{"meta": {"id": "c1", "accountId": "acc_100"}, "trackers": []}'
    res = process_gong_call_event(payload_no_comp)
    assert res["action_required"] is True
    assert "NO_COMPETITOR_DISCOVERY" in res["risk_flags"]

    # Call payload with competitor discovery
    payload_with_comp = '{"meta": {"id": "c2", "accountId": "acc_100"}, "trackers": [{"name": "CompetitorA", "category": "Competitors"}]}'
    res_clean = process_gong_call_event(payload_with_comp)
    assert res_clean["action_required"] is False
    assert len(res_clean["risk_flags"]) == 0
