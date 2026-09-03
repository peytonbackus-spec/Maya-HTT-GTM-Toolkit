---
type: pipeline_hygiene_audit
audit_date: "{{audit_date}}"
total_deals_reviewed: {{total_deals}}
deals_at_risk: {{deals_at_risk}}
tags:
  - gtm/pipeline_audit
  - revops/hygiene
---

# Pipeline Hygiene Audit ({{audit_date}})

## Executive Summary
- **Total Pipeline Reviewed:** {{total_deals}} Deals
- **Deals Flagged At-Risk:** `{{deals_at_risk}}`
- **Hygiene Compliance Rate:** `{{compliance_rate}}%`

---

## Flagged Stage Violations

{{violation_breakdown}}

---

## Required Action Items
{{action_items}}
