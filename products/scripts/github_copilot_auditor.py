#!/usr/bin/env python3
"""
GitHub Copilot Auditor
========================

A comprehensive Python script that audits a GitHub organization for AI-related risks.
Specifically checks if GitHub Copilot is enabled on repositories and assesses risk levels.

Requirements:
    pip install requests

Usage:
    python github_copilot_auditor.py --token YOUR_GITHUB_TOKEN --org YOUR_ORG_NAME
    
    Or set environment variable:
    export GITHUB_TOKEN=your_token
    python github_copilot_auditor.py --org YOUR_ORG_NAME

Author: AI Governance Team
"""

import requests
import csv
import argparse
import sys
import os
import time
from typing import List, Dict, Optional
from datetime import datetime


class GitHubCopilotAuditor:
    """Main class for auditing GitHub organizations for Copilot usage."""
    
    def __init__(self, token: str, org_name: str):
        """
        Initialize the auditor.
        
        Args:
            token: GitHub Personal Access Token (PAT)
            org_name: Name of the GitHub organization to audit
        """
        self.token = token
        self.org_name = org_name
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Copilot-Auditor/1.0"
        }
        self.repos: List[Dict] = []
        self.rate_limit_remaining = None
        self.rate_limit_reset = None
    
    def check_rate_limit(self) -> None:
        """Check and handle GitHub API rate limits."""
        response = requests.get(f"{self.base_url}/rate_limit", headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            self.rate_limit_remaining = data['resources']['core']['remaining']
            self.rate_limit_reset = data['resources']['core']['reset']
            
            if self.rate_limit_remaining < 10:
                wait_time = self.rate_limit_reset - time.time()
                if wait_time > 0:
                    print(f"⚠️  Rate limit approaching. Waiting {int(wait_time)} seconds...")
                    time.sleep(wait_time + 1)
    
    def get_all_repos(self) -> List[Dict]:
        """
        Fetch all repositories for the organization.
        
        Returns:
            List of repository dictionaries
        """
        repos = []
        page = 1
        per_page = 100
        
        print(f"🔍 Fetching repositories for organization: {self.org_name}")
        
        while True:
            self.check_rate_limit()
            
            url = f"{self.base_url}/orgs/{self.org_name}/repos"
            params = {
                "page": page,
                "per_page": per_page,
                "type": "all"  # Include all repo types
            }
            
            try:
                response = requests.get(url, headers=self.headers, params=params)
                
                if response.status_code == 401:
                    print("❌ Authentication failed. Please check your GitHub token.")
                    sys.exit(1)
                elif response.status_code == 404:
                    print(f"❌ Organization '{self.org_name}' not found.")
                    sys.exit(1)
                elif response.status_code == 403:
                    print("❌ Access forbidden. Check token permissions and rate limits.")
                    sys.exit(1)
                
                response.raise_for_status()
                data = response.json()
                
                if not data:
                    break
                
                repos.extend(data)
                print(f"   Found {len(data)} repositories (page {page})...")
                
                # Check if there are more pages
                if len(data) < per_page:
                    break
                
                page += 1
                
            except requests.exceptions.RequestException as e:
                print(f"❌ Error fetching repositories: {e}")
                sys.exit(1)
        
        print(f"✅ Total repositories found: {len(repos)}")
        return repos
    
    def check_copilot_access(self, repo_full_name: str) -> bool:
        """
        Check if Copilot is enabled for a specific repository.
        
        Args:
            repo_full_name: Full name of the repository (org/repo)
            
        Returns:
            True if Copilot is enabled, False if not, or "Error" if check failed
        """
        self.check_rate_limit()
        
        # Use the Copilot API endpoint
        url = f"{self.base_url}/repos/{repo_full_name}/copilot"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            data = response.json()
            # Check if Copilot is enabled at org or repo level
            return data.get('enabled_for_org', False) or data.get('enabled_for_repo', False)
        elif response.status_code == 404:
            # Copilot endpoint not available, likely not enabled
            return False
        else:
            print(f"   ⚠️  Warning: Could not check Copilot for {repo_full_name}. Status: {response.status_code}")
            return "Error"
    
    def assess_risk_level(self, is_private: bool, copilot_enabled) -> str:
        """
        Assess risk level based on repository visibility and Copilot status.
        
        Args:
            is_private: Whether the repository is private
            copilot_enabled: Whether Copilot is enabled (True/False/"Error")
            
        Returns:
            Risk level string (CRITICAL, HIGH, LOW)
        """
        if not copilot_enabled or copilot_enabled == "Error":
            return "LOW"
        
        if copilot_enabled and not is_private:
            return "CRITICAL"  # Massive IP/compliance risk on public repo
        elif copilot_enabled and is_private:
            return "HIGH"  # Potential IP/code leakage risk
        
        return "LOW"
    
    def audit_organization(self) -> List[Dict]:
        """
        Perform complete audit of the organization.
        
        Returns:
            List of audit results
        """
        repos = self.get_all_repos()
        results = []
        
        print(f"\n🔎 Auditing {len(repos)} repositories for Copilot usage...")
        
        for i, repo in enumerate(repos, 1):
            repo_name = repo['full_name']
            is_private = repo['private']
            
            print(f"   [{i}/{len(repos)}] Checking {repo_name}...", end=" ")
            
            copilot_enabled = self.check_copilot_access(repo_name)
            risk_level = self.assess_risk_level(is_private, copilot_enabled)
            
            result = {
                'repo_name': repo_name,
                'is_private': 'Yes' if is_private else 'No',
                'copilot_enabled': 'Yes' if copilot_enabled else 'No' if copilot_enabled is False else 'Error',
                'risk_level': risk_level,
                'url': repo['html_url'],
                'created_at': repo.get('created_at', ''),
                'updated_at': repo.get('updated_at', '')
            }
            
            results.append(result)
            print(f"Risk: {risk_level}")
            
            # Small delay to be respectful of API rate limits
            time.sleep(0.1)
        
        return results
    
    def generate_report(self, results: List[Dict], output_file: str = None) -> None:
        """
        Generate CSV report from audit results.
        
        Args:
            results: List of audit result dictionaries
            output_file: Optional output file path (default: auto-generated)
        """
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"github_copilot_audit_{self.org_name}_{timestamp}.csv"
        
        fieldnames = ['repo_name', 'is_private', 'copilot_enabled', 'risk_level', 'url', 'created_at', 'updated_at']
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"\n✅ Report generated: {output_file}")
        print(f"   Total repositories audited: {len(results)}")
        
        # Print summary
        risk_counts = {}
        for result in results:
            risk = result['risk_level']
            risk_counts[risk] = risk_counts.get(risk, 0) + 1
        
        print("\n📊 Risk Summary:")
        for risk, count in sorted(risk_counts.items(), key=lambda x: ['CRITICAL', 'HIGH', 'LOW'].index(x[0]) if x[0] in ['CRITICAL', 'HIGH', 'LOW'] else 99):
            print(f"   {risk}: {count}")
        
        # Highlight critical findings
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


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Audit GitHub organization for Copilot usage and assess risks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
    # Using command-line arguments
    python github_copilot_auditor.py --token ghp_xxxxxxxxxxxx --org my-organization
    
    # Using environment variable
    export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
    python github_copilot_auditor.py --org my-organization
    
Note: Your GitHub token needs the following permissions:
    - repo (read access to repositories)
    - read:org (read organization data)
        """
    )
    
    # Try to get token from environment variable first
    default_token = os.getenv('GITHUB_TOKEN')
    
    parser.add_argument(
        '--token',
        default=default_token,
        help='GitHub Personal Access Token (PAT). Can also be set via GITHUB_TOKEN environment variable.'
    )
    
    parser.add_argument(
        '--org',
        '--organization',
        dest='org',
        required=True,
        help='GitHub organization name'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        help='Output CSV file path (default: auto-generated)'
    )
    
    args = parser.parse_args()
    
    # Validate token
    if not args.token:
        print("❌ ERROR: GitHub token is required.")
        print("   Set it via --token argument or GITHUB_TOKEN environment variable.")
        print("   Example: export GITHUB_TOKEN=your_token_here")
        sys.exit(1)
    
    print("=" * 60)
    print("GitHub Copilot Auditor")
    print("=" * 60)
    print()
    
    auditor = GitHubCopilotAuditor(args.token, args.org)
    
    try:
        results = auditor.audit_organization()
        auditor.generate_report(results, args.output)
        
        print("\n✅ Audit complete!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Audit interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during audit: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
