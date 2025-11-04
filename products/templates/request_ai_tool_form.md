# Request an AI Tool - Form Template

This document provides a template for creating a "Request an AI Tool" form. You can use this with:
- Google Forms
- Microsoft Forms
- Typeform
- Qualtrics
- Any other form builder

---

## Form Configuration

**Form Title:** Request an AI Tool  
**Description:** Use this form to request approval for new AI tools, services, or features. All requests will be reviewed by the AI Governance team.

---

## Form Fields

### Section 1: Requester Information

**1. Requester Name**
- Type: Short answer text
- Required: Yes
- Validation: Text only

**2. Requester Email**
- Type: Email
- Required: Yes
- Validation: Valid email format

**3. Department/Team**
- Type: Dropdown or short answer
- Required: Yes
- Options (if dropdown):
  - IT
  - Engineering
  - Marketing
  - Sales
  - Operations
  - Legal
  - HR
  - Finance
  - Other (specify)

**4. Job Title**
- Type: Short answer text
- Required: Yes

---

### Section 2: Tool Information

**5. Tool/Vendor Name**
- Type: Short answer text
- Required: Yes
- Help text: "What is the name of the AI tool or vendor you want to use?"

**6. Tool Website/URL**
- Type: URL
- Required: Yes
- Help text: "Link to the tool's website or product page"

**7. Tool Category**
- Type: Multiple choice
- Required: Yes
- Options:
  - Chatbot/Conversational AI (ChatGPT, Claude, etc.)
  - Code Generation (GitHub Copilot, Codeium, etc.)
  - Image/Video Generation (DALL-E, Midjourney, etc.)
  - Content Creation/Writing
  - Data Analysis/Analytics
  - Customer Service/Support
  - Development Tools
  - Productivity Tools
  - Other (specify)

**8. Tool Type**
- Type: Multiple choice
- Required: Yes
- Options:
  - SaaS (Cloud-based)
  - On-premise/Private instance
  - API/Integration
  - Browser Extension
  - Desktop Application
  - Mobile Application
  - Other

---

### Section 3: Business Justification

**9. Primary Use Case**
- Type: Long answer text
- Required: Yes
- Help text: "Describe the primary business problem or use case this tool will address"

**10. Expected Benefits**
- Type: Long answer text
- Required: Yes
- Help text: "What benefits do you expect from using this tool? (e.g., time savings, cost reduction, improved quality)"

**11. Alternative Solutions Considered**
- Type: Long answer text
- Required: Yes
- Help text: "What other solutions (including non-AI alternatives) did you consider? Why was this tool selected?"

**12. Expected ROI or Cost Savings**
- Type: Short answer text
- Required: No
- Help text: "If applicable, provide estimated ROI or cost savings"

---

### Section 3: Technical Details

**13. Data Types to be Processed**
- Type: Checkboxes
- Required: Yes
- Options:
  - Public/non-sensitive data only
  - Customer data
  - Employee data (PII)
  - Financial data
  - Health information (PHI)
  - Intellectual property
  - Trade secrets
  - Code/repositories
  - Other (specify)

**14. Data Volume**
- Type: Multiple choice
- Required: Yes
- Options:
  - Low (< 1,000 records/month)
  - Medium (1,000 - 100,000 records/month)
  - High (100,000+ records/month)
  - Not applicable

**15. Integration Requirements**
- Type: Long answer text
- Required: No
- Help text: "Does this tool need to integrate with existing systems? If yes, describe."

**16. User Population**
- Type: Multiple choice
- Required: Yes
- Options:
  - Individual user
  - Small team (< 10 users)
  - Department (10-50 users)
  - Organization-wide (50+ users)
  - Public-facing

---

### Section 4: Security and Compliance

**17. Data Storage Location**
- Type: Multiple choice
- Required: Yes
- Options:
  - Cloud (US)
  - Cloud (EU)
  - Cloud (Other region - specify)
  - On-premise
  - Hybrid
  - Unknown

**18. Compliance Requirements**
- Type: Checkboxes
- Required: Yes
- Options:
  - GDPR
  - CCPA
  - HIPAA
  - PCI-DSS
  - SOC 2
  - Industry-specific (specify)
  - None
  - Not sure

**19. Security Features**
- Type: Checkboxes
- Required: Yes
- Options:
  - MFA/2FA
  - SSO integration
  - Encryption at rest
  - Encryption in transit
  - Audit logging
  - Role-based access control
  - Data residency controls
  - Unknown

**20. Vendor Security Certifications**
- Type: Checkboxes
- Required: No
- Options:
  - SOC 2 Type II
  - ISO 27001
  - FedRAMP
  - Other (specify)
  - Unknown

---

### Section 5: Timeline and Urgency

**21. Requested Start Date**
- Type: Date
- Required: Yes
- Help text: "When do you need access to this tool?"

**22. Urgency Level**
- Type: Multiple choice
- Required: Yes
- Options:
  - Low (can wait for full review)
  - Medium (needed within 1-2 months)
  - High (needed within 2 weeks)
  - Critical (needed immediately - explain in notes)

**23. Business Impact if Not Approved**
- Type: Long answer text
- Required: No
- Help text: "Describe the impact if this request is not approved or delayed"

---

### Section 6: Budget and Licensing

**24. Estimated Cost**
- Type: Multiple choice
- Required: Yes
- Options:
  - Free/Freemium
  - < $100/month
  - $100 - $500/month
  - $500 - $2,000/month
  - $2,000+/month
  - Per-user pricing (specify)
  - Unknown

**25. Budget Approval**
- Type: Multiple choice
- Required: Yes
- Options:
  - Budget approved
  - Pending budget approval
  - No budget approval needed
  - Seeking budget

**26. License Type**
- Type: Multiple choice
- Required: Yes
- Options:
  - Individual license
  - Team license
  - Organization license
  - Enterprise license
  - Per-user subscription
  - Usage-based pricing
  - Unknown

---

### Section 7: Additional Information

**27. Additional Notes or Context**
- Type: Long answer text
- Required: No
- Help text: "Any additional information that would help in the review process"

**28. Supporting Documents**
- Type: File upload
- Required: No
- Help text: "Upload any relevant documents (vendor information, security reports, etc.)"
- Accepted file types: PDF, DOC, DOCX
- Max file size: 10MB

---

## Form Settings

### Workflow and Notifications

**Notification Settings:**
- Send confirmation email to requester upon submission
- Notify AI Governance team upon new submission
- Send reminder if no action after 5 business days
- Send approval/rejection notification to requester

**Approval Workflow:**
1. Form submission → AI Governance team receives notification
2. Initial review (security, privacy, compliance)
3. If needed, escalate to IT Security, Legal, or Privacy team
4. Decision made and communicated to requester
5. If approved, provisioning and onboarding

**Response Time SLAs:**
- Low urgency: 10 business days
- Medium urgency: 5 business days
- High urgency: 2 business days
- Critical: 1 business day (expedited review)

---

## Integration with Other Systems

### Google Forms Implementation
1. Create new Google Form
2. Add all fields above
3. Set up form responses sheet
4. Configure notification rules (Google Apps Script)
5. Set up automated routing to approval workflow

### Microsoft Forms Implementation
1. Create new Microsoft Form
2. Add all fields above
3. Configure Power Automate flow for:
   - Notification to AI Governance team
   - Create ticket in tracking system
   - Send acknowledgment email

### Typeform Implementation
1. Create new Typeform
2. Use logic jumps for conditional questions
3. Integrate with Zapier/Make for workflow automation
4. Connect to CRM or ticketing system

---

## Customization Notes

- **Industry-Specific Fields**: Add fields relevant to your industry (e.g., healthcare, finance)
- **Risk Scoring**: Automatically calculate risk score based on responses
- **Pre-Approval List**: For low-risk tools, create a pre-approved list
- **Integration**: Connect form to your IT service management (ITSM) tool
- **Reporting**: Set up dashboards to track request volume and approval rates

---

## Form Submission Template (Email/Notification)

**Subject:** New AI Tool Request: [Tool Name] - [Requester Name]

**Body:**
```
A new AI tool request has been submitted:

Requester: [Name] ([Email])
Department: [Department]
Tool: [Tool Name]
URL: [URL]
Use Case: [Use Case]
Urgency: [Urgency Level]
Requested Start: [Date]

View full request: [Link to form response]

Please review and respond within SLA timeframe.
```

---

**Template Version:** 1.0  
**Last Updated:** [Date]  
**Maintained By:** AI Governance Team

