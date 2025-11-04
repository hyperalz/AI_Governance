#!/usr/bin/env python3
"""
Mock Demo - Shows Expected Output
==================================

This script demonstrates what the GitHub Copilot Auditor output looks like
without making actual API calls. Useful for understanding the tool before running.
"""

import csv
from datetime import datetime

def simulate_audit():
    """Simulate an audit run with sample data."""
    
    print("=" * 60)
    print("GitHub Copilot Auditor - Mock Demo")
    print("=" * 60)
    print()
    print("🔍 This is a simulation of what the audit output looks like")
    print("   (No actual API calls are made)")
    print()
    
    # Simulate organization
    org_name = "example-org"
    print(f"Auditing GitHub organization: {org_name}")
    print(f"🔍 Fetching repositories for organization: {org_name}")
    print(f"   Found 5 repositories (page 1)...")
    print(f"✅ Total repositories found: 5")
    
    # Sample data
    sample_repos = [
        {
            'repo_name': f'{org_name}/public-api',
            'is_private': 'No',
            'copilot_enabled': 'Yes',
            'risk_level': 'CRITICAL',
            'url': f'https://github.com/{org_name}/public-api'
        },
        {
            'repo_name': f'{org_name}/private-backend',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{org_name}/private-backend'
        },
        {
            'repo_name': f'{org_name}/docs',
            'is_private': 'No',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{org_name}/docs'
        },
        {
            'repo_name': f'{org_name}/internal-tools',
            'is_private': 'Yes',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{org_name}/internal-tools'
        },
        {
            'repo_name': f'{org_name}/legacy-code',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{org_name}/legacy-code'
        }
    ]
    
    print(f"\n🔎 Auditing {len(sample_repos)} repositories for Copilot usage...")
    
    for i, repo in enumerate(sample_repos, 1):
        print(f"   [{i}/{len(sample_repos)}] Checking {repo['repo_name']}... Risk: {repo['risk_level']}")
    
    # Generate CSV
    filename = f"github_ai_audit_{org_name}_demo.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['repo_name', 'is_private', 'copilot_enabled', 'risk_level', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_repos)
    
    print(f"\n✅ Report generated: {filename}")
    print(f"   Total repositories audited: {len(sample_repos)}")
    
    # Summary
    risk_counts = {}
    for repo in sample_repos:
        risk = repo['risk_level']
        risk_counts[risk] = risk_counts.get(risk, 0) + 1
    
    print("\n📊 Risk Summary:")
    for risk in ['CRITICAL', 'HIGH', 'LOW']:
        count = risk_counts.get(risk, 0)
        print(f"   {risk}: {count}")
    
    critical_count = risk_counts.get('CRITICAL', 0)
    high_count = risk_counts.get('HIGH', 0)
    
    if critical_count > 0 or high_count > 0:
        print(f"\n⚠️  IMPORTANT:")
        if critical_count > 0:
            print(f"   {critical_count} CRITICAL risk repositories found (Copilot enabled on PUBLIC repos)")
            print(f"   Consider disabling Copilot on public repos or moving sensitive code to private repos.")
        if high_count > 0:
            print(f"   {high_count} HIGH risk repositories found (Copilot enabled on PRIVATE repos)")
            print(f"   Review these repositories for potential IP/code leakage risks.")
    
    print(f"\n✅ Audit complete!")
    print()
    print("=" * 60)
    print("📋 To run a real audit:")
    print("=" * 60)
    print("1. Get GitHub token: https://github.com/settings/tokens")
    print("2. Set token: export GITHUB_TOKEN=your_token")
    print("3. Run: python test_github_auditor.py your-org-name")
    print("4. See QUICK_START.md for detailed instructions")
    print()

if __name__ == "__main__":
    simulate_audit()

