#!/usr/bin/env python3
"""
Test Public Repository Access
=============================

Tests what information we can access about public repositories,
including Copilot status (if available).
"""

import requests
import sys
import os

def check_public_repo(repo_name, token=None):
    """
    Check what information we can access about a public repository.
    
    Args:
        repo_name: Repository in format "owner/repo"
        token: Optional GitHub token (for authenticated requests)
    """
    print(f"🔍 Checking repository: {repo_name}")
    print("=" * 60)
    
    # Set up headers
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
        print("✅ Using authenticated request")
    else:
        print("⚠️  Using unauthenticated request (rate limited)")
    
    # Check basic repo info (public - no auth needed)
    print("\n1. Basic Repository Information:")
    repo_url = f"https://api.github.com/repos/{repo_name}"
    resp = requests.get(repo_url, headers=headers)
    
    if resp.status_code == 200:
        data = resp.json()
        print(f"   ✅ Repository exists")
        print(f"   Name: {data.get('name')}")
        print(f"   Owner: {data.get('owner', {}).get('login')}")
        print(f"   Private: {data.get('private', False)}")
        print(f"   Public: {not data.get('private', False)}")
        print(f"   URL: {data.get('html_url')}")
    elif resp.status_code == 404:
        print(f"   ❌ Repository not found or private")
        return False
    else:
        print(f"   ⚠️  Error: {resp.status_code}")
        return False
    
    # Try Copilot endpoint
    print("\n2. Copilot Status Check:")
    copilot_url = f"https://api.github.com/repos/{repo_name}/copilot"
    copilot_resp = requests.get(copilot_url, headers=headers)
    
    print(f"   Status: {copilot_resp.status_code}")
    
    if copilot_resp.status_code == 200:
        copilot_data = copilot_resp.json()
        print(f"   ✅ Can access Copilot information!")
        print(f"   Enabled for org: {copilot_data.get('enabled_for_org', False)}")
        print(f"   Enabled for repo: {copilot_data.get('enabled_for_repo', False)}")
        return True
    elif copilot_resp.status_code == 403:
        print(f"   ❌ Forbidden - Need owner/admin access")
        print(f"   💡 Copilot status is private - only owners/admins can check")
        return False
    elif copilot_resp.status_code == 404:
        print(f"   ⚠️  Endpoint not found")
        print(f"   Possible reasons:")
        print(f"     - Copilot API endpoint may not be publicly available")
        print(f"     - Repository doesn't have Copilot configured")
        print(f"     - Endpoint requires special permissions")
        return False
    else:
        print(f"   ⚠️  Unexpected status: {copilot_resp.status_code}")
        print(f"   Response: {copilot_resp.text[:200]}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_public_repo.py owner/repo [token]")
        print("\nExample:")
        print("  python test_public_repo.py microsoft/vscode")
        print("  python test_public_repo.py facebook/react github_pat_...")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    token = sys.argv[2] if len(sys.argv) > 2 else os.getenv('GITHUB_TOKEN')
    
    if not token:
        print("⚠️  No token provided - using unauthenticated requests")
        print("   (Rate limited to 60 requests/hour)")
    
    check_public_repo(repo_name, token)
    
    print("\n" + "=" * 60)
    print("📋 Summary:")
    print("=" * 60)
    print("✅ Public repository info: Always accessible")
    print("❌ Copilot status: Typically requires owner/admin access")
    print("\n💡 To check Copilot on repositories:")
    print("   1. You must be the repository owner")
    print("   2. OR be an organization admin")
    print("   3. OR have explicit permissions granted")
    print("\n⚠️  You cannot check Copilot status on random public repos")
    print("   due to privacy/security restrictions.")

if __name__ == "__main__":
    main()

