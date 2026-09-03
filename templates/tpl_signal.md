---
type: intent_signal
company: "{{company}}"
domain: "{{domain}}"
signal_type: "{{signal_type}}"
source: "{{source}}"
impact_score: {{impact_score}}
headcount: {{headcount}}
funding_stage: "{{funding_stage}}"
created_date: {{created_date}}
tags:
  - gtm/signal
  - intelligence/account
---

# Intent Signal: {{company}} - {{signal_type}}

## Account Intelligence
- **Company:** {{company}} (`{{domain}}`)
- **Headcount:** {{headcount}}
- **Funding Stage:** {{funding_stage}}
- **Tech Stack:** {{tech_stack}}
- **Trigger:** `{{signal_type}}` (Impact: `{{impact_score}}/10`)

## Detected Raw Signal
> {{raw_text}}

---

## Actionable Strategy
{{gtm_angle}}

- [ ] Route signal trigger to account owner
- [ ] Trigger sequence customized to {{tech_stack}}
