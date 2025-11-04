# Quick Start Guide - Test the GitHub Copilot Auditor

This guide will help you quickly test the GitHub Copilot Auditor script.

## Prerequisites

1. **Python 3.8+** installed
2. **GitHub Personal Access Token (PAT)** with the following permissions:
   - `repo` (read access to repositories)
   - `read:org` (read organization data)

## Step 1: Get Your GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "AI Governance Auditor"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

## Step 2: Install Dependencies

```bash
cd products/scripts
pip install requests
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

## Step 3: Run the Test Script

### Option A: Using the Quick Test Script (Simplest)

```bash
# Set your token as an environment variable
export GITHUB_TOKEN=your_token_here

# Run the test script
python test_github_auditor.py your-org-name
```

### Option B: Using the Full Script

```bash
# Set your token
export GITHUB_TOKEN=your_token_here

# Run with command-line arguments
python github_copilot_auditor.py --org your-org-name

# Or pass token directly
python github_copilot_auditor.py --token your_token_here --org your-org-name
```

## Step 4: Review the Results

The script will:
1. ✅ Fetch all repositories from your organization
2. ✅ Check each repository for Copilot access
3. ✅ Generate a CSV report with risk levels
4. ✅ Display a summary with counts by risk level

### Understanding Risk Levels

- **CRITICAL**: Copilot enabled on PUBLIC repositories
  - ⚠️ Highest risk - code could be exposed
  - Action: Review and consider disabling Copilot on public repos
  
- **HIGH**: Copilot enabled on PRIVATE repositories
  - ⚠️ Medium risk - potential IP leakage
  - Action: Review for sensitive code
  
- **LOW**: Copilot disabled or status unknown
  - ✅ Lowest risk - no immediate action needed

## Example Output

```
============================================================
GitHub Copilot Auditor - Quick Test
============================================================

Auditing GitHub organization: my-company
🔍 Fetching repositories for organization: my-company
   Found 15 repositories (page 1)...
✅ Found 15 repositories to audit...

   [1/15] Checking my-company/api-server... Risk: HIGH
   [2/15] Checking my-company/frontend... Risk: CRITICAL
   [3/15] Checking my-company/docs... Risk: LOW
   ...

✅ Audit complete! Report saved to: github_ai_audit_my-company.csv

📊 SUMMARY
============================================================
Total Repositories: 15
CRITICAL Risk: 2 (Copilot on PUBLIC repos)
HIGH Risk: 5 (Copilot on PRIVATE repos)
LOW Risk: 8 (Copilot disabled or unknown)

⚠️  ACTION REQUIRED:
   Review 2 CRITICAL risk repositories immediately.
   Consider disabling Copilot on public repos or moving sensitive code.
   Review 5 HIGH risk repositories for potential IP leakage.
```

## Troubleshooting

### "Authentication failed"
- Check that your token is correct
- Verify token hasn't expired
- Ensure token has required permissions

### "Organization not found"
- Check organization name spelling
- Verify you have access to the organization
- Ensure token has `read:org` permission

### "Rate limit exceeded"
- Wait a few minutes and try again
- GitHub API allows 5,000 requests/hour for authenticated users
- The script includes rate limit handling

### "Permission denied"
- Your token may not have sufficient permissions
- Organization may require admin access
- Check token scopes in GitHub settings

## Security Notes

⚠️ **Important Security Practices:**

1. **Never commit tokens to version control**
   - Use environment variables
   - Add `.env` files to `.gitignore`
   - Use secret management tools in production

2. **Use least-privilege tokens**
   - Only grant minimum required permissions
   - Create tokens for specific purposes
   - Rotate tokens regularly

3. **Protect token files**
   - Don't share tokens publicly
   - Use secure storage for tokens
   - Revoke tokens if compromised

## Next Steps

After testing:
1. Review the CSV report for detailed findings
2. Address CRITICAL and HIGH risk repositories
3. Consider implementing the full AI Governance framework
4. Set up regular audits (monthly/quarterly)

## Need Help?

- Check the main README.md for detailed documentation
- Review the 48-Hour AI Governance Plan for implementation guidance
- Contact the AI Governance team for support

