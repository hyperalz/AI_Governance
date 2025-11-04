#!/usr/bin/env python3
"""
GitHub Copilot Auditor - Demo Mode
====================================

This version allows testing with public repositories only,
perfect for demonstrations without requiring authentication.

Usage:
    python demo_mode.py your-org-name
"""

import requests
import csv
import sys

ORG_NAME = sys.argv[1] if len(sys.argv) > 1 else None

if not ORG_NAME:
    print("Usage: python demo_mode.py your-org-name")
    print("Note: This demo mode only checks PUBLIC repositories")
    sys.exit(1)

def get_public_repos(org):
    """Fetch public repositories for the organization (no auth required)."""
    repos = []
    page = 1
    
    print(f"🔍 Fetching PUBLIC repositories for organization: {org}")
    print("   (Demo mode: Only public repos are accessible without authentication)")
    
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?type=public&page={page}&per_page=100"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            if response.status_code == 404:
                print(f"   Organization '{org}' not found or has no public repositories.")
            sys.exit(1)
            
        page_repos = response.json()
        if not page_repos:
            break
            
        repos.extend(page_repos)
        print(f"   Found {len(page_repos)} public repositories (page {page})...")
        page += 1
        
    return repos

def check_copilot_access_demo(repo_full_name):
    """
    Check Copilot status for public repo (limited without auth).
    
    Note: Without authentication, we can only check if the repo exists
    and infer some information. Full Copilot checking requires auth.
    """
    # Without auth, we can't access the /copilot endpoint
    # This is a demo placeholder
    return "Unknown (requires authentication)"

def determine_risk_level_demo(is_private, copilot_status):
    """Determine risk level for demo mode."""
    if is_private:
        return "N/A (private repos require authentication)"
    
    # For public repos without auth, we can't determine Copilot status
    return "Check Required (full audit needs authentication)"

def main():
    print("=" * 60)
    print("GitHub Copilot Auditor - DEMO MODE")
    print("=" * 60)
    print()
    print("⚠️  This is a limited demo mode.")
    print("   - Only checks PUBLIC repositories")
    print("   - Cannot determine Copilot status (requires authentication)")
    print("   - For full audit, use: github_copilot_auditor.py")
    print()
    
    repos = get_public_repos(ORG_NAME)
    
    if not repos:
        print(f"\n❌ No public repositories found for organization: {ORG_NAME}")
        print("   - Organization may have no public repos")
        print("   - Organization name may be incorrect")
        print("   - Try with the full script and authentication for complete audit")
        sys.exit(1)
    
    print(f"\n✅ Found {len(repos)} public repositories")
    print("\n📋 Public Repository List:")
    print("-" * 60)
    
    report_data = []
    for i, repo in enumerate(repos, 1):
        repo_name = repo['full_name']
        is_private = repo['private']
        url = repo.get('html_url', '')
        
        print(f"{i}. {repo_name}")
        print(f"   URL: {url}")
        print(f"   Private: {is_private}")
        print(f"   Status: Full Copilot check requires authentication")
        print()
        
        report_data.append({
            'repo_name': repo_name,
            'is_private': 'No' if not is_private else 'Yes',
            'copilot_enabled': 'Unknown (requires auth)',
            'risk_level': 'Check Required',
            'url': url
        })
    
    # Write CSV report
    filename = f"github_demo_audit_{ORG_NAME}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['repo_name', 'is_private', 'copilot_enabled', 'risk_level', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(report_data)
    
    print(f"\n✅ Demo report saved to: {filename}")
    print(f"\n📊 Summary:")
    print(f"   Total Public Repositories: {len(repos)}")
    print(f"   Private Repositories: Not accessible in demo mode")
    print(f"\n💡 To perform a full audit:")
    print(f"   1. Get a GitHub Personal Access Token")
    print(f"   2. Run: python github_copilot_auditor.py --org {ORG_NAME}")
    print(f"   3. See QUICK_START.md for detailed instructions")

if __name__ == "__main__":
    main()

