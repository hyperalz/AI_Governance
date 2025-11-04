# AI Governance Toolkit

A comprehensive package of scripts, templates, and guides for establishing AI governance in your organization.

## 📦 Package Contents

### 🔍 Discovery & Audit Scripts

Automated tools to discover AI usage across your organization:

1. **GitHub Copilot Auditor** (`scripts/github_copilot_auditor.py`)
   - Scans GitHub organizations for Copilot usage
   - Identifies risk levels by repository visibility
   - Generates CSV reports with detailed findings

2. **Atlassian AI Feature Scanner** (`scripts/atlassian_ai_scanner.py`)
   - Scans Confluence and Jira Cloud for AI features
   - Identifies AI-related add-ons and integrations
   - Checks for Atlassian Intelligence usage

3. **Microsoft 365 Copilot Readiness Checker** (`scripts/m365_copilot_checker.py`)
   - Lists users licensed for Microsoft 365 Copilot
   - Identifies potential data exposure points
   - Assesses organizational Copilot adoption

### 📋 Policy & Control Templates

Ready-to-customize policy documents:

1. **AI Acceptable Use Policy** (`templates/ai_acceptable_use_policy.md`)
   - Comprehensive policy template
   - Covers data handling, security, ethics
   - Includes prohibited uses and compliance requirements

2. **AI Vendor Assessment Checklist** (`templates/ai_vendor_assessment_checklist.md`)
   - Due diligence checklist for evaluating AI tools
   - Covers security, privacy, compliance, and ethics
   - Includes risk assessment framework

3. **Request an AI Tool Form Template** (`templates/request_ai_tool_form.md`)
   - Complete form template for centralized AI tool requests
   - Works with Google Forms, Microsoft Forms, Typeform
   - Includes approval workflow guidance

### 📚 Action & Implementation Guides

Step-by-step guides for implementation:

1. **48-Hour AI Governance Plan** (`guides/48_hour_ai_governance_plan.md`)
   - Hour-by-hour playbook for immediate action
   - Covers discovery, policy creation, and risk mitigation
   - Includes success metrics and common challenges

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Appropriate API credentials (see individual scripts for requirements)

### Installation

1. **Install Python dependencies:**
   ```bash
   cd scripts
   pip install -r requirements.txt
   ```

2. **Set up credentials:**
   - GitHub: Create Personal Access Token with `repo` and `read:org` permissions
   - Atlassian: Generate API token from account settings
   - Microsoft 365: Register Azure AD app and get client credentials

3. **Run discovery scripts:**
   ```bash
   # GitHub Copilot Audit
   python github_copilot_auditor.py --token YOUR_TOKEN --org YOUR_ORG

   # Atlassian AI Scanner
   python atlassian_ai_scanner.py --domain company.atlassian.net --email user@company.com --api_token YOUR_TOKEN

   # Microsoft 365 Copilot Check
   python m365_copilot_checker.py --tenant-id YOUR_TENANT --client-id YOUR_CLIENT_ID --client-secret YOUR_SECRET
   ```

## 📖 Documentation

### Scripts

Each script includes:
- Detailed help text (`--help` flag)
- Inline code comments
- Error handling and validation
- CSV report generation

### Templates

Each template includes:
- Comprehensive sections covering key areas
- Placeholder fields for customization
- Best practices and guidance
- Industry-standard language

### Guides

The 48-Hour Plan includes:
- Step-by-step instructions
- Time estimates for each task
- Success criteria
- Troubleshooting tips

## 🔒 Security & Privacy

- All scripts use read-only API access where possible
- No sensitive data is stored or transmitted
- Credentials should be managed securely (environment variables, vaults)
- Review and understand data handling before running scripts

## 🛠️ Customization

### Scripts
- Modify risk scoring logic in scripts
- Add additional checks or validations
- Integrate with your ticketing/CRM systems
- Customize CSV output format

### Templates
- Customize policies for your industry
- Add organization-specific requirements
- Adjust form fields for your workflow
- Integrate with your approval processes

## 📊 Usage Examples

### Example 1: Complete Organization Audit

```bash
# 1. Run all discovery scripts
python github_copilot_auditor.py --token $GITHUB_TOKEN --org mycompany
python atlassian_ai_scanner.py --domain mycompany.atlassian.net --email admin@mycompany.com --api_token $ATLASSIAN_TOKEN
python m365_copilot_checker.py --tenant-id $TENANT_ID --client-id $CLIENT_ID --client-secret $CLIENT_SECRET

# 2. Review CSV reports
# 3. Import findings into risk assessment
# 4. Create action plan
```

### Example 2: Quick Policy Implementation

1. Open `templates/ai_acceptable_use_policy.md`
2. Search and replace `[Your Organization Name]` with your org name
3. Customize approved tools list
4. Review with Legal/Compliance
5. Publish to employees

### Example 3: Set Up Tool Request Process

1. Create Google Form using `templates/request_ai_tool_form.md`
2. Set up form notifications
3. Configure approval workflow
4. Announce to employees
5. Monitor and refine

## 🐛 Troubleshooting

### Common Issues

**Authentication Errors:**
- Verify API tokens are valid and not expired
- Check token permissions match requirements
- Ensure tokens have necessary scopes

**Rate Limiting:**
- Scripts include rate limit handling
- Wait for rate limit reset if needed
- Consider using multiple tokens for large organizations

**Missing Dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

**Permission Errors:**
- Ensure you have admin/appropriate access
- Check API permissions in platform settings
- Verify organization-level permissions

## 🤝 Contributing

This toolkit is designed to be customized for your organization. Feel free to:
- Modify scripts for your specific needs
- Add additional checks or validations
- Extend templates with industry-specific requirements
- Share improvements with your team

## 📝 License & Usage

These tools are provided as templates and starting points. Adapt them to your organization's needs and ensure compliance with your internal policies and applicable regulations.

## 📞 Support

For questions or issues:
1. Review script documentation (`--help` flags)
2. Check template guidance sections
3. Refer to the 48-Hour Plan troubleshooting section
4. Consult with your IT, Security, or Compliance teams

## 🔄 Version History

- **v1.0** (Initial Release)
  - GitHub Copilot Auditor
  - Atlassian AI Scanner
  - Microsoft 365 Copilot Checker
  - Policy and template documents
  - 48-Hour Implementation Plan

## 📚 Additional Resources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Atlassian REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/overview)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

**Last Updated:** [Date]  
**Maintained By:** AI Governance Team

