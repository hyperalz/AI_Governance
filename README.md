# AI Governance Toolkit

A comprehensive package of scripts, templates, and guides for establishing AI governance in your organization. This toolkit helps you discover AI usage, assess risks, and implement governance frameworks quickly and effectively.

![AI Governance](https://img.shields.io/badge/AI-Governance-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Quick Start

Get started in 3 simple steps:

```bash
# 1. Clone the repository
git clone https://github.com/hyperalz/AI_Governance.git
cd AI_Governance/products/scripts

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the GitHub Copilot Auditor
export GITHUB_TOKEN=your_token_here
python test_github_auditor.py your-org-name
```

See the [Quick Start Guide](products/scripts/QUICK_START.md) for detailed instructions.

## 📦 What's Included

### 🔍 Discovery & Audit Scripts

Automated Python scripts to discover AI usage across your organization:

- **GitHub Copilot Auditor** - Scans GitHub organizations for Copilot usage and assesses risk levels
- **Atlassian AI Feature Scanner** - Scans Confluence and Jira Cloud for AI features and add-ons
- **Microsoft 365 Copilot Readiness Checker** - Lists Copilot-licensed users and identifies data exposure points

### 📋 Policy & Control Templates

Ready-to-customize policy documents:

- **AI Acceptable Use Policy** - Comprehensive policy template covering data handling, security, and ethics
- **AI Vendor Assessment Checklist** - Due diligence checklist for evaluating AI tools
- **Request an AI Tool Form Template** - Form template for centralized AI tool requests

### 📚 Implementation Guides

Step-by-step guides for implementation:

- **48-Hour AI Governance Plan** - Hour-by-hour playbook for immediate action
- **Quick Start Guide** - Fast setup and testing instructions

## 🎯 Key Features

- ✅ **Automated Discovery** - Find AI tools in use across your organization
- ✅ **Risk Assessment** - Automated risk scoring (CRITICAL, HIGH, LOW)
- ✅ **CSV Reports** - Detailed reports with actionable recommendations
- ✅ **Policy Templates** - Ready-to-use policy documents
- ✅ **Quick Implementation** - Get up and running in 48 hours

## 📖 Documentation

- [Quick Start Guide](products/scripts/QUICK_START.md) - Get started in minutes
- [48-Hour Implementation Plan](products/guides/48_hour_ai_governance_plan.md) - Complete implementation guide
- [Product Documentation](products/README.md) - Detailed toolkit documentation

## 🛠️ Requirements

- Python 3.8 or higher
- GitHub Personal Access Token (for GitHub scripts)
- Appropriate API credentials (see individual scripts for requirements)

## 📁 Repository Structure

```
AI_Governance/
├── products/
│   ├── scripts/
│   │   ├── github_copilot_auditor.py      # GitHub Copilot audit script
│   │   ├── atlassian_ai_scanner.py        # Atlassian AI scanner
│   │   ├── m365_copilot_checker.py        # Microsoft 365 checker
│   │   ├── test_github_auditor.py         # Quick test script
│   │   ├── demo_mode.py                   # Demo mode (no auth)
│   │   ├── requirements.txt                # Python dependencies
│   │   └── QUICK_START.md                 # Quick start guide
│   ├── templates/
│   │   ├── ai_acceptable_use_policy.md     # Policy template
│   │   ├── ai_vendor_assessment_checklist.md
│   │   └── request_ai_tool_form.md        # Form template
│   └── guides/
│       └── 48_hour_ai_governance_plan.md  # Implementation guide
├── index.html                              # Website homepage
├── components/                             # Website components
└── README.md                               # This file
```

## 🔐 Security

⚠️ **Important Security Practices:**

- Never commit tokens or credentials to version control
- Use environment variables for sensitive data
- Review the `.gitignore` file to ensure secrets aren't committed
- Use least-privilege tokens with minimal required permissions

## 📊 Example Output

```
============================================================
GitHub Copilot Auditor
============================================================

🔍 Fetching repositories for organization: my-company
   Found 15 repositories (page 1)...
✅ Total repositories found: 15

🔎 Auditing 15 repositories for Copilot usage...
   [1/15] Checking my-company/api-server... Risk: HIGH
   [2/15] Checking my-company/frontend... Risk: CRITICAL
   ...

📊 Risk Summary:
   CRITICAL: 2
   HIGH: 5
   LOW: 8

✅ Report generated: github_copilot_audit_my-company_20241104.csv
```

## 🤝 Contributing

This toolkit is designed to be customized for your organization. Feel free to:
- Fork the repository
- Modify scripts for your specific needs
- Add additional checks or validations
- Extend templates with industry-specific requirements

## 📝 License

This project is provided as-is for use in establishing AI governance. Adapt the tools and templates to your organization's needs and ensure compliance with your internal policies and applicable regulations.

## 🔗 Resources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Atlassian REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/overview)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## 📞 Support

For questions or issues:
1. Review the [Quick Start Guide](products/scripts/QUICK_START.md)
2. Check the [48-Hour Implementation Plan](products/guides/48_hour_ai_governance_plan.md)
3. Open an issue on GitHub

---

**Repository:** [https://github.com/hyperalz/AI_Governance](https://github.com/hyperalz/AI_Governance.git)

**Last Updated:** November 2024

