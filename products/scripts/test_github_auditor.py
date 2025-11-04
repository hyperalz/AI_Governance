#!/usr/bin/env python3
"""
Quick Test Script for GitHub Copilot Auditor
==============================================

This is a simplified version for quick testing. It uses the same logic
but with a simpler interface for demonstration purposes.

Usage:
    export GITHUB_TOKEN=your_token
    python test_github_auditor.py your-org-name
"""

import requests
import csv
import os
import sys

# Configuration - User must set this
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORG_NAME = sys.argv[1] if len(sys.argv) > 1 else None

# Validate configuration
if not GITHUB_TOKEN:
    print("ERROR: Please set the GITHUB_TOKEN environment variable.")
    print("Example: export GITHUB_TOKEN=your_token_here")
    sys.exit(1)

if not ORG_NAME:
    print("ERROR: Please provide organization name as argument.")
    print("Usage: python test_github_auditor.py your-org-name")
    sys.exit(1)

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repos(org):
    """Fetch all repositories for the organization."""
    repos = []
    page = 1
    
    print(f"🔍 Fetching repositories for organization: {org}")
    
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?type=all&page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            sys.exit(1)
            
        page_repos = response.json()
        if not page_repos:
            break
            
        repos.extend(page_repos)
        print(f"   Found {len(page_repos)} repositories (page {page})...")
        page += 1
        
    return repos

def check_copilot_access(repo_full_name):
    """Check if Copilot is enabled for a specific repository."""
    url = f"https://api.github.com/repos/{repo_full_name}/copilot"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('enabled_for_org', False) or data.get('enabled_for_repo', False)
    elif response.status_code == 404:
        # Copilot endpoint not available, likely not enabled
        return False
    else:
        print(f"   ⚠️  Warning: Could not check Copilot for {repo_full_name}. Status: {response.status_code}")
        return "Error"

def determine_risk_level(is_private, copilot_enabled):
    """Determine risk level based on repository privacy and Copilot status."""
    if not copilot_enabled or copilot_enabled == "Error":
        return "LOW"
    elif copilot_enabled and not is_private:
        return "CRITICAL"
    elif copilot_enabled and is_private:
        return "HIGH"
    return "LOW"

def main():
    print("=" * 60)
    print("GitHub Copilot Auditor - Quick Test")
    print("=" * 60)
    print()
    
    print(f"Auditing GitHub organization: {ORG_NAME}")
    repos = get_repos(ORG_NAME)
    print(f"✅ Found {len(repos)} repositories to audit...")
    
    report_data = []
    for i, repo in enumerate(repos, 1):
        repo_name = repo['full_name']
        is_private = repo['private']
        
        print(f"   [{i}/{len(repos)}] Checking {repo_name}...", end=" ")
        copilot_enabled = check_copilot_access(repo_name)
        risk_level = determine_risk_level(is_private, copilot_enabled)
        
        report_data.append({
            'repo_name': repo_name,
            'is_private': 'Yes' if is_private else 'No',
            'copilot_enabled': 'Yes' if copilot_enabled else 'No' if copilot_enabled is False else 'Error',
            'risk_level': risk_level,
            'url': repo.get('html_url', '')
        })
        
        print(f"Risk: {risk_level}")
    
    # Write CSV report
    filename = f"github_ai_audit_{ORG_NAME}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['repo_name', 'is_private', 'copilot_enabled', 'risk_level', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in report_data:
            writer.writerow(row)
    
    print(f"\n✅ Audit complete! Report saved to: {filename}")
    
    # Summary statistics
    critical_count = sum(1 for row in report_data if row['risk_level'] == 'CRITICAL')
    high_count = sum(1 for row in report_data if row['risk_level'] == 'HIGH')
    low_count = sum(1 for row in report_data if row['risk_level'] == 'LOW')
    
    print(f"\n📊 SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total Repositories: {len(repos)}")
    print(f"CRITICAL Risk: {critical_count} (Copilot on PUBLIC repos)")
    print(f"HIGH Risk: {high_count} (Copilot on PRIVATE repos)")
    print(f"LOW Risk: {low_count} (Copilot disabled or unknown)")
    
    if critical_count > 0 or high_count > 0:
        print(f"\n⚠️  ACTION REQUIRED:")
        if critical_count > 0:
            print(f"   Review {critical_count} CRITICAL risk repositories immediately.")
            print(f"   Consider disabling Copilot on public repos or moving sensitive code.")
        if high_count > 0:
            print(f"   Review {high_count} HIGH risk repositories for potential IP leakage.")
    else:
        print(f"\n✅ No high-risk repositories found.")

if __name__ == "__main__":
    main()

