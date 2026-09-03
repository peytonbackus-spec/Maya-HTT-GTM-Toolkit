---
type: inbound_lead
company: "{{company}}"
contact_name: "{{contact_name}}"
email: "{{email}}"
lead_score: {{lead_score}}
assigned_rep: "{{assigned_rep}}"
created_date: "{{created_date}}"
tags:
  - gtm/inbound
  - routing/assigned
---

# Inbound Lead: {{contact_name}} ({{company}})

## Routing & Scoring Summary
- **Lead Score:** `{{lead_score}} / 100`
- **Assigned Territory Rep:** `{{assigned_rep}}`
- **Inbound Channel:** {{channel}}

## Qualification Breakdown
- **Company Size:** {{company_size}}
- **Use Case / Notes:** {{use_case}}

---

## Suggested SLA Email Response

**Subject:** `{{subject}}`

```text
{{body}}
```
