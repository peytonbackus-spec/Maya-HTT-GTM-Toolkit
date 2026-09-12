import json

def process_gong_call_event(event_payload):
    """
    Parses Gong call transcripts for MEDDPICC risk keywords
    and flags low-engagement deals.
    """
    call_data = json.loads(event_payload)
    meta = call_data.get("meta", {})
    trackers = call_data.get("trackers", [])
    
    risk_flags = []
    competitor_mentions = [t["name"] for t in trackers if t.get("category") == "Competitors"]
    
    if not competitor_mentions:
        risk_flags.append("NO_COMPETITOR_DISCOVERY")
        
    return {
        "call_id": meta.get("id"),
        "account_id": meta.get("accountId"),
        "competitor_mentions": competitor_mentions,
        "risk_flags": risk_flags,
        "action_required": len(risk_flags) > 0
    }

if __name__ == "__main__":
    sample_event = '{"meta": {"id": "gong_123", "accountId": "acc_99"}, "trackers": [{"name": "CompetitorX", "category": "Competitors"}]}'
    print(process_gong_call_event(sample_event))
