# Your First 48-Hour AI Governance Plan

**A Step-by-Step Playbook for Immediate Action**

---

## Introduction

This playbook provides a clear, actionable plan to establish basic AI governance in your organization within 48 hours. While comprehensive AI governance is an ongoing process, this plan will help you take immediate steps to understand your current state and establish foundational controls.

**Who This Is For:**
- Organizations just starting their AI governance journey
- Teams that need to quickly assess AI usage risks
- IT and security teams responding to an AI governance initiative

**What You'll Accomplish:**
- ✅ Discover what AI tools are currently in use
- ✅ Identify immediate risks and exposure points
- ✅ Establish basic policies and controls
- ✅ Create a foundation for ongoing governance

---

## Pre-Flight Checklist

Before starting, ensure you have:
- [ ] Access to your organization's GitHub, Atlassian, and/or Microsoft 365 accounts
- [ ] Appropriate API tokens or credentials (see scripts for requirements)
- [ ] Access to your organization's policy/template repository
- [ ] 2-4 hours of dedicated time
- [ ] Support from IT, Security, or Compliance teams (if needed)

---

## Day 1: Discovery & Assessment (Hours 0-24)

### Hour 1: Set Up Your Environment

**Objective:** Prepare your tools and access credentials

**Tasks:**
1. **Download the audit scripts**
   ```bash
   # Navigate to the products/scripts directory
   cd AI\ Governance/products/scripts
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

2. **Gather credentials**
   - [ ] GitHub Personal Access Token (PAT) with `repo` and `read:org` permissions
   - [ ] Atlassian API token (if using Atlassian)
   - [ ] Microsoft 365 credentials (if using M365)
   - [ ] Store credentials securely (use environment variables or secure vault)

3. **Set up output directory**
   ```bash
   mkdir -p audit_results
   ```

**Time:** 30 minutes  
**Outcome:** Ready to run audit scripts

---

### Hour 2-3: Run Discovery Scripts

**Objective:** Identify current AI tool usage across your organization

**Task 1: GitHub Copilot Audit**

```bash
# Run GitHub Copilot Auditor
python github_copilot_auditor.py \
  --token YOUR_GITHUB_TOKEN \
  --org YOUR_ORG_NAME \
  --output audit_results/github_copilot_audit.csv
```

**Review the results:**
- [ ] Count repositories with Copilot enabled
- [ ] Identify HIGH and CRITICAL risk repositories
- [ ] Document findings in a summary document

**Task 2: Atlassian AI Scanner (if applicable)**

```bash
# Run Atlassian AI Scanner
python atlassian_ai_scanner.py \
  --domain yourcompany.atlassian.net \
  --email your.email@company.com \
  --api_token YOUR_API_TOKEN \
  --output audit_results/atlassian_ai_scan.csv
```

**Review the results:**
- [ ] List AI add-ons installed
- [ ] Check for Atlassian Intelligence usage
- [ ] Document findings

**Task 3: Microsoft 365 Copilot Check (if applicable)**

```bash
# Run M365 Copilot Checker
python m365_copilot_checker.py \
  --tenant-id YOUR_TENANT_ID \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET \
  --output audit_results/m365_copilot_check.csv
```

**Review the results:**
- [ ] Count users with Copilot licenses
- [ ] Identify data exposure points
- [ ] Document findings

**Time:** 1-2 hours (depending on organization size)  
**Outcome:** CSV reports with current AI usage inventory

---

### Hour 4-5: Manual Discovery

**Objective:** Identify AI tools not covered by automated scripts

**Tasks:**
1. **Survey employees** (quick survey via email/Slack)
   - Create a simple form: "What AI tools are you currently using for work?"
   - Common tools to ask about:
     - ChatGPT, Claude, Perplexity
     - GitHub Copilot, Codeium, Cursor
     - DALL-E, Midjourney, Stable Diffusion
     - Notion AI, Grammarly, Jasper
     - Custom/internal AI tools

2. **Check expense reports**
   - [ ] Review recent software purchases
   - [ ] Look for AI tool subscriptions
   - [ ] Check vendor invoices

3. **Review approved software lists**
   - [ ] Check IT's approved software catalog
   - [ ] Review procurement records
   - [ ] Check app store/admin console for installed apps

4. **Network/Security logs** (if accessible)
   - [ ] Check firewall logs for AI tool domains
   - [ ] Review proxy logs for AI service usage
   - [ ] Check DNS queries for AI service domains

**Time:** 1-2 hours  
**Outcome:** Comprehensive list of AI tools in use

---

### Hour 6-8: Risk Assessment

**Objective:** Prioritize risks and identify immediate actions needed

**Tasks:**
1. **Compile all findings**
   - [ ] Merge all audit results into one master inventory
   - [ ] Create a risk matrix (see template below)

2. **Categorize by risk level**
   - **CRITICAL:** Public repos with Copilot, sensitive data exposure
   - **HIGH:** Private repos with Copilot, unapproved AI tools with data access
   - **MEDIUM:** Approved tools with proper controls
   - **LOW:** Low-risk tools with minimal data exposure

3. **Create risk summary document**
   ```
   Risk Summary Template:
   - Total AI tools identified: [number]
   - Critical risks: [number]
   - High risks: [number]
   - Immediate actions needed: [list]
   ```

**Time:** 2 hours  
**Outcome:** Prioritized risk assessment document

---

## Day 2: Policy & Control Implementation (Hours 24-48)

### Hour 9-10: Create Acceptable Use Policy

**Objective:** Establish basic policy for AI tool usage

**Tasks:**
1. **Customize the AI Acceptable Use Policy template**
   - [ ] Open `products/templates/ai_acceptable_use_policy.md`
   - [ ] Fill in organization-specific details
   - [ ] Customize approved tools list
   - [ ] Adjust based on your industry/regulations

2. **Key sections to focus on:**
   - [ ] Section 5: Approved AI Tools (add your approved list)
   - [ ] Section 6: Prohibited Uses (customize for your needs)
   - [ ] Section 7: Data Handling Requirements

3. **Get initial review**
   - [ ] Share draft with Legal/Compliance (if available)
   - [ ] Get IT Security review
   - [ ] Make revisions based on feedback

**Time:** 1-2 hours  
**Outcome:** Draft AI Acceptable Use Policy

---

### Hour 11-12: Set Up Tool Request Process

**Objective:** Create a centralized process for AI tool approvals

**Tasks:**
1. **Set up the "Request an AI Tool" form**
   - [ ] Choose form platform (Google Forms, Microsoft Forms, Typeform)
   - [ ] Use template from `products/templates/request_ai_tool_form.md`
   - [ ] Customize fields for your organization
   - [ ] Test form submission

2. **Configure notifications**
   - [ ] Set up email notifications to AI Governance team
   - [ ] Create approval workflow (if using automation)
   - [ ] Set up response time SLAs

3. **Communicate the process**
   - [ ] Send announcement email to employees
   - [ ] Post in company Slack/Teams
   - [ ] Add to employee handbook or intranet

**Time:** 1-2 hours  
**Outcome:** Functional tool request form and process

---

### Hour 13-14: Address Critical Risks

**Objective:** Take immediate action on highest-risk items

**Tasks:**
1. **Review critical findings**
   - [ ] Identify top 3-5 critical risks from Day 1
   - [ ] For each risk, determine immediate action

2. **Immediate actions (examples):**
   - **Public repos with Copilot enabled:**
     - [ ] Disable Copilot on public repos (if appropriate)
     - [ ] Or move sensitive code to private repos
     - [ ] Review public repo contents for sensitive data
   
   - **Unapproved tools with sensitive data:**
     - [ ] Assess if tool should be approved
     - [ ] If not approved, communicate to users
     - [ ] Provide approved alternatives
   
   - **Data exposure risks:**
     - [ ] Review data sharing agreements
     - [ ] Check vendor security certifications
     - [ ] Assess need for data processing agreements

3. **Document actions taken**
   - [ ] Create action log
   - [ ] Track remediation status
   - [ ] Set follow-up dates

**Time:** 2 hours  
**Outcome:** Critical risks addressed or remediation plan in place

---

### Hour 15-16: Create Vendor Assessment Process

**Objective:** Establish process for evaluating new AI vendors

**Tasks:**
1. **Review vendor assessment checklist**
   - [ ] Open `products/templates/ai_vendor_assessment_checklist.md`
   - [ ] Customize for your organization
   - [ ] Add industry-specific requirements

2. **Set up review process**
   - [ ] Identify who reviews vendor assessments (Security, Legal, IT)
   - [ ] Define approval workflow
   - [ ] Set review timelines and SLAs

3. **Create vendor assessment template**
   - [ ] Save customized checklist as template
   - [ ] Create folder structure for vendor assessments
   - [ ] Set up tracking spreadsheet/database

**Time:** 1-2 hours  
**Outcome:** Vendor assessment process and template ready

---

### Hour 17-18: Documentation & Communication

**Objective:** Document everything and communicate to stakeholders

**Tasks:**
1. **Create governance documentation**
   - [ ] Document current state (what you found)
   - [ ] Document policies created
   - [ ] Document processes established
   - [ ] Create a governance handbook or wiki page

2. **Prepare stakeholder communication**
   - [ ] Create executive summary (1-2 pages)
   - [ ] Prepare presentation for leadership
   - [ ] Draft email to all employees about new policies

3. **Key messages to communicate:**
   - Why AI governance is important
   - What was discovered
   - New policies and processes
   - How to request AI tools
   - Where to find resources

**Time:** 2 hours  
**Outcome:** Documentation complete and communications ready

---

## Immediate Next Steps (Post-48 Hours)

### Week 1 Follow-Up

1. **Review and refine**
   - [ ] Review policy feedback from stakeholders
   - [ ] Refine processes based on initial usage
   - [ ] Address any issues with tool request process

2. **Training and awareness**
   - [ ] Schedule AI governance training sessions
   - [ ] Create training materials
   - [ ] Record training sessions for onboarding

3. **Ongoing monitoring**
   - [ ] Schedule monthly audits
   - [ ] Review tool requests weekly
   - [ ] Monitor for new AI tools in use

### Month 1 Goals

1. **Complete policy approvals**
   - [ ] Get final approval on AI Acceptable Use Policy
   - [ ] Publish policy to all employees
   - [ ] Require policy acknowledgment

2. **Expand discovery**
   - [ ] Run additional discovery scripts
   - [ ] Complete manual discovery gaps
   - [ ] Identify shadow IT AI tools

3. **Establish governance committee**
   - [ ] Form cross-functional AI governance team
   - [ ] Set meeting cadence
   - [ ] Define roles and responsibilities

---

## Success Metrics

Track these metrics to measure progress:

- **Discovery:**
  - Number of AI tools identified
  - Percentage of tools that are approved
  - Number of critical risks found

- **Process:**
  - Number of tool requests submitted
  - Average approval time
  - Number of tools approved/rejected

- **Awareness:**
  - Employee training completion rate
  - Policy acknowledgment rate
  - Number of questions/support requests

---

## Common Challenges & Solutions

### Challenge 1: "We don't have time for this"
**Solution:** Start with critical risks only. Focus on high-impact, low-effort actions first.

### Challenge 2: "Employees will resist"
**Solution:** Frame as enabling safe AI use, not restricting. Provide approved alternatives.

### Challenge 3: "We don't have the technical skills"
**Solution:** Use the provided scripts. They're designed to be run by non-technical users with minimal setup.

### Challenge 4: "Legal/Compliance needs to review"
**Solution:** Create a "quick start" version of the policy for immediate use, then refine with legal input.

### Challenge 5: "Too many tools to manage"
**Solution:** Start with approved list of top 5-10 tools. Expand gradually based on business needs.

---

## Resources & Templates

All resources are located in the `products/` directory:

- **Scripts:** `products/scripts/`
  - `github_copilot_auditor.py`
  - `atlassian_ai_scanner.py`
  - `m365_copilot_checker.py`

- **Templates:** `products/templates/`
  - `ai_acceptable_use_policy.md`
  - `ai_vendor_assessment_checklist.md`
  - `request_ai_tool_form.md`

- **Guides:** `products/guides/`
  - `48_hour_ai_governance_plan.md` (this document)

---

## Getting Help

If you encounter issues or need assistance:

1. **Script Issues:**
   - Check script documentation and comments
   - Verify API credentials and permissions
   - Review error messages for guidance

2. **Policy Questions:**
   - Review template guidance
   - Consult with Legal/Compliance teams
   - Adapt templates to your industry needs

3. **Process Questions:**
   - Start simple and iterate
   - Focus on high-risk areas first
   - Build processes that work for your organization

---

## Conclusion

Congratulations on completing your first 48 hours of AI governance! You've established:

✅ **Discovery:** Know what AI tools are in use  
✅ **Policy:** Have basic acceptable use policy  
✅ **Process:** Have tool request and approval process  
✅ **Risk Management:** Addressed critical risks  
✅ **Foundation:** Built base for ongoing governance

**Remember:** AI governance is a journey, not a destination. Use this plan as a starting point and continuously improve based on your organization's needs.

---

**Document Version:** 1.0  
**Last Updated:** [Date]  
**Next Review:** [Date]

