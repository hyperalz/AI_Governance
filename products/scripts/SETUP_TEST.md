# Setting Up for Real Test

## Step 1: Get Your GitHub Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it: "AI Governance Auditor Test"
4. Select these permissions:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

## Step 2: Set Up Environment

### Option A: Using Virtual Environment (Recommended)

```bash
cd products/scripts

# Create virtual environment (if not already created)
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install dependencies
pip install requests
```

### Option B: Install Globally (if you have permission)

```bash
pip install requests
# OR
pip install --user requests
```

## Step 3: Run the Test

```bash
# Set your token (replace with your actual token)
export GITHUB_TOKEN=ghp_your_token_here

# Run the test script
python test_github_auditor.py your-org-name

# OR use the full script
python github_copilot_auditor.py --org your-org-name
```

## Example

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
python test_github_auditor.py my-company
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
- Make sure you activated the virtual environment
- Or install requests: `pip install requests`

### "Authentication failed"
- Check your token is correct
- Verify token hasn't expired
- Ensure token has `repo` and `read:org` permissions

### "Organization not found"
- Check organization name spelling
- Verify you have access to the organization
- Try with a different organization name

