# 08 — RevOps Architecture & Salesforce Data Model

## Custom Object & Schema Design
* **Lead / Contact Routing:** Automated scoring based on Siemens software usage, company headcount, and industrial signal triggers.
* **Opportunity Stages:** Standardized handoffs between BDR, Account Executive, Pre-Sales Application Engineers, and Post-Sales Implementation teams.
* **Siemens Co-Sell Attachment Tracker:** Custom SFDC fields tracking joint Siemens partner rep ID, co-sell deal margin, and product attachment (Simcenter, Teamcenter, EPIQ-M).

## System Integrations
```text
[Marketing Automation / Apollo] ──> [Clay Enrichment Engine] ──> [Salesforce CRM] ──> [Outreach / Email Sequences]
                                                                        │
                                                                        └──> [Services / Delivery Handshake]
