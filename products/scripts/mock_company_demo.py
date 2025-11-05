#!/usr/bin/env python3
"""
Mock Company Demo - Realistic Output Example
============================================

This script demonstrates what the GitHub Copilot Auditor output would look like
for a fictional company with various Copilot scenarios.

Perfect for demonstrations, documentation, or understanding expected results.
"""

import csv
import sys
from datetime import datetime

def generate_mock_audit():
    """Generate a realistic mock audit report for a fictional company."""
    
    company_name = "TechCorp-Dev"
    
    # Realistic repository scenarios
    mock_repos = [
        # CRITICAL RISK - Public repos with Copilot enabled
        {
            'repo_name': f'{company_name}/public-api',
            'is_private': 'No',
            'copilot_enabled': 'Yes',
            'risk_level': 'CRITICAL',
            'url': f'https://github.com/{company_name}/public-api',
            'description': 'Main public API - sensitive endpoints exposed'
        },
        {
            'repo_name': f'{company_name}/marketing-site',
            'is_private': 'No',
            'copilot_enabled': 'Yes',
            'risk_level': 'CRITICAL',
            'url': f'https://github.com/{company_name}/marketing-site',
            'description': 'Public marketing website with embedded secrets'
        },
        
        # HIGH RISK - Private repos with Copilot enabled
        {
            'repo_name': f'{company_name}/payment-processing',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{company_name}/payment-processing',
            'description': 'Payment gateway integration - sensitive financial code'
        },
        {
            'repo_name': f'{company_name}/user-database',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{company_name}/user-database',
            'description': 'User management system with PII handling'
        },
        {
            'repo_name': f'{company_name}/internal-admin-tools',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{company_name}/internal-admin-tools',
            'description': 'Internal admin dashboard'
        },
        {
            'repo_name': f'{company_name}/legacy-monolith',
            'is_private': 'Yes',
            'copilot_enabled': 'Yes',
            'risk_level': 'HIGH',
            'url': f'https://github.com/{company_name}/legacy-monolith',
            'description': 'Legacy system with outdated dependencies'
        },
        
        # LOW RISK - Copilot disabled or not applicable
        {
            'repo_name': f'{company_name}/documentation',
            'is_private': 'No',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/documentation',
            'description': 'Public documentation site'
        },
        {
            'repo_name': f'{company_name}/test-suite',
            'is_private': 'Yes',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/test-suite',
            'description': 'Automated test suite'
        },
        {
            'repo_name': f'{company_name}/frontend-app',
            'is_private': 'No',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/frontend-app',
            'description': 'React frontend application'
        },
        {
            'repo_name': f'{company_name}/infrastructure',
            'is_private': 'Yes',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/infrastructure',
            'description': 'Terraform infrastructure as code'
        },
        {
            'repo_name': f'{company_name}/design-system',
            'is_private': 'No',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/design-system',
            'description': 'Shared component library'
        },
        {
            'repo_name': f'{company_name}/analytics-dashboard',
            'is_private': 'Yes',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/analytics-dashboard',
            'description': 'Internal analytics and reporting'
        },
        {
            'repo_name': f'{company_name}/mobile-app',
            'is_private': 'No',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/mobile-app',
            'description': 'iOS/Android mobile application'
        },
        {
            'repo_name': f'{company_name}/ci-cd-pipelines',
            'is_private': 'Yes',
            'copilot_enabled': 'No',
            'risk_level': 'LOW',
            'url': f'https://github.com/{company_name}/ci-cd-pipelines',
            'description': 'CI/CD pipeline configurations'
        },
    ]
    
    print("=" * 70)
    print("GitHub Copilot Auditor")
    print("=" * 70)
    print()
    
    print(f"🔍 Fetching repositories for organization: {company_name}")
    print(f"   Found {len(mock_repos)} repositories (page 1)...")
    print(f"✅ Total repositories found: {len(mock_repos)}")
    print()
    
    print(f"🔎 Auditing {len(mock_repos)} repositories for Copilot usage...")
    print()
    
    # Simulate checking each repo
    for i, repo in enumerate(mock_repos, 1):
        risk_emoji = "🔴" if repo['risk_level'] == 'CRITICAL' else "🟡" if repo['risk_level'] == 'HIGH' else "🟢"
        print(f"   [{i:2}/{len(mock_repos)}] {risk_emoji} Checking {repo['repo_name']}... Risk: {repo['risk_level']}")
    
    print()
    
    # Generate CSV report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"github_copilot_audit_{company_name.lower()}_{timestamp}.csv"
    
    fieldnames = ['repo_name', 'is_private', 'copilot_enabled', 'risk_level', 'url']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in mock_repos:
            writer.writerow({k: repo[k] for k in fieldnames})
    
    print(f"✅ Report generated: {filename}")
    print(f"   Total repositories audited: {len(mock_repos)}")
    print()
    
    # Calculate summary statistics
    risk_counts = {}
    for repo in mock_repos:
        risk = repo['risk_level']
        risk_counts[risk] = risk_counts.get(risk, 0) + 1
    
    print("📊 Risk Summary:")
    print("-" * 70)
    for risk in ['CRITICAL', 'HIGH', 'LOW']:
        count = risk_counts.get(risk, 0)
        percentage = (count / len(mock_repos)) * 100
        bar = "█" * int(percentage / 2)
        print(f"   {risk:8} {count:2} repositories ({percentage:5.1f}%) {bar}")
    
    print()
    
    # Detailed breakdown
    critical_count = risk_counts.get('CRITICAL', 0)
    high_count = risk_counts.get('HIGH', 0)
    
    if critical_count > 0 or high_count > 0:
        print("⚠️  IMPORTANT FINDINGS:")
        print("-" * 70)
        
        if critical_count > 0:
            print(f"\n🔴 CRITICAL RISK: {critical_count} repository/repositories")
            print("   Copilot is enabled on PUBLIC repositories.")
            print("   This poses significant IP and compliance risks.")
            print()
            print("   Affected repositories:")
            for repo in mock_repos:
                if repo['risk_level'] == 'CRITICAL':
                    print(f"   • {repo['repo_name']}")
                    print(f"     {repo['description']}")
                    print(f"     URL: {repo['url']}")
                    print()
            print("   💡 RECOMMENDED ACTIONS:")
            print("   1. Immediately review what code is being processed by Copilot")
            print("   2. Consider disabling Copilot on public repositories")
            print("   3. Move sensitive code to private repositories")
            print("   4. Review and remove any secrets or sensitive data")
            print("   5. Implement code scanning for exposed credentials")
            print()
        
        if high_count > 0:
            print(f"🟡 HIGH RISK: {high_count} repositories")
            print("   Copilot is enabled on PRIVATE repositories.")
            print("   Potential IP/code leakage risk with sensitive codebases.")
            print()
            print("   Affected repositories:")
            for repo in mock_repos:
                if repo['risk_level'] == 'HIGH':
                    print(f"   • {repo['repo_name']}")
                    print(f"     {repo['description']}")
                    print()
            print("   💡 RECOMMENDED ACTIONS:")
            print("   1. Review Copilot usage policies for private repos")
            print("   2. Ensure team members understand data handling")
            print("   3. Consider enabling Copilot ignore files (.copilotignore)")
            print("   4. Monitor for any unusual Copilot activity")
            print("   5. Document approved use cases")
            print()
    
    low_count = risk_counts.get('LOW', 0)
    if low_count > 0:
        print(f"🟢 LOW RISK: {low_count} repositories")
        print("   Copilot is disabled or not applicable.")
        print("   No immediate action required.")
        print()
    
    print("=" * 70)
    print("✅ Audit complete!")
    print("=" * 70)
    print()
    print(f"📄 Full report saved to: {filename}")
    print()
    print("📋 Next Steps:")
    print("   1. Review the CSV report for detailed findings")
    print("   2. Prioritize CRITICAL and HIGH risk repositories")
    print("   3. Implement remediation actions")
    print("   4. Establish ongoing monitoring and governance")
    print("   5. Update AI governance policies based on findings")
    print()
    print("💡 This is a mock demonstration. For real audits, run:")
    print("   python test_github_auditor.py your-org-name")
    print()

if __name__ == "__main__":
    generate_mock_audit()

