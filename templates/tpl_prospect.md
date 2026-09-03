---
type: prospect_outreach
company: "{{company}}"
contact_name: "{{contact_name}}"
title: "{{title}}"
icp_score: {{icp_score}}
qualified: {{qualified}}
created_date: {{created_date}}
tags:
  - gtm/outbound
  - sequence/draft
---

# Prospect: {{contact_name}} ({{company}})

## Qualification Overview
- **Title:** {{title}}
- **Headcount:** {{headcount}}
- **ICP Fit Score:** `{{icp_score}} / 100`
- **Primary Tech Stack:** {{tech_stack}}

### Fit Triggers
{{fit_reasons}}

---

## Outbound Email Sequence (Step 1)

**Subject:** `{{subject}}`

```text
{{body}}
```

---

## Task Execution
- [ ] Send Step 1 email via Outreach / manual send
- [ ] Connect with {{first_name}} on LinkedIn
- [ ] Log activity in SFDC / CRM
