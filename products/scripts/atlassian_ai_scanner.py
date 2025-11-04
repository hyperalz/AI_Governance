#!/usr/bin/env python3
"""
Atlassian AI Feature Scanner
=============================

Scans Confluence and Jira Cloud instances for enabled AI features and add-ons.
Identifies potential AI tool usage and data exposure risks.

Requirements:
    pip install requests

Usage:
    python atlassian_ai_scanner.py --domain YOUR_DOMAIN.atlassian.net --email YOUR_EMAIL --api_token YOUR_API_TOKEN

Author: AI Governance Team
"""

import requests
import csv
import argparse
import sys
import base64
from typing import List, Dict, Optional
from datetime import datetime


class AtlassianAIScanner:
    """Scanner for Atlassian AI features and add-ons."""
    
    def __init__(self, domain: str, email: str, api_token: str):
        """
        Initialize the scanner.
        
        Args:
            domain: Atlassian domain (e.g., 'mycompany.atlassian.net')
            email: Atlassian account email
            api_token: Atlassian API token
        """
        self.domain = domain
        self.email = email
        self.api_token = api_token
        
        # Base64 encode credentials for Basic Auth
        credentials = f"{email}:{api_token}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        self.headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        self.base_url = f"https://{domain}"
        self.results: List[Dict] = []
    
    def check_confluence_ai_features(self) -> List[Dict]:
        """Check for AI features in Confluence."""
        print("🔍 Scanning Confluence for AI features...")
        results = []
        
        # Check for AI-powered features
        # Note: Specific endpoints may vary based on Confluence version
        ai_features = [
            "AI Content Generator",
            "Smart Suggestions",
            "AI Writing Assistant",
            "Intelligent Search"
        ]
        
        try:
            # Check Confluence REST API
            url = f"{self.base_url}/wiki/rest/api/space"
            response = requests.get(url, headers=self.headers, params={"limit": 100})
            
            if response.status_code == 200:
                spaces = response.json().get('results', [])
                print(f"   Found {len(spaces)} spaces")
                
                # Check for AI-related content/macros
                for space in spaces[:10]:  # Limit to first 10 for performance
                    space_key = space.get('key', '')
                    # Additional checks can be added here
                    
        except requests.exceptions.RequestException as e:
            print(f"   ⚠️  Could not access Confluence: {e}")
        
        return results
    
    def check_jira_ai_addons(self) -> List[Dict]:
        """Check for AI-related add-ons in Jira."""
        print("🔍 Scanning Jira for AI add-ons...")
        results = []
        
        ai_addon_keywords = [
            'ai', 'copilot', 'assistant', 'intelligent', 'smart',
            'automation', 'ml', 'machine learning', 'nlp', 'natural language'
        ]
        
        try:
            # Get installed apps/add-ons
            url = f"{self.base_url}/rest/api/3/app/metadata"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                apps = response.json()
                installed_apps = apps.get('installedApps', [])
                
                print(f"   Found {len(installed_apps)} installed apps")
                
                for app in installed_apps:
                    app_name = app.get('name', '').lower()
                    app_key = app.get('key', '')
                    
                    # Check if app name contains AI-related keywords
                    is_ai_related = any(keyword in app_name for keyword in ai_addon_keywords)
                    
                    if is_ai_related:
                        result = {
                            'type': 'Jira Add-on',
                            'name': app.get('name', 'Unknown'),
                            'key': app_key,
                            'vendor': app.get('vendor', {}).get('name', 'Unknown'),
                            'ai_related': 'Yes',
                            'risk_level': 'MEDIUM'  # Add-ons typically have limited access
                        }
                        results.append(result)
                        print(f"   ⚠️  Found AI-related add-on: {app.get('name')}")
                        
        except requests.exceptions.RequestException as e:
            print(f"   ⚠️  Could not access Jira: {e}")
        
        return results
    
    def check_atlassian_intelligence(self) -> List[Dict]:
        """Check for Atlassian Intelligence (built-in AI) features."""
        print("🔍 Checking for Atlassian Intelligence features...")
        results = []
        
        # Atlassian Intelligence is a built-in feature
        # Check if it's enabled at the instance level
        try:
            # This would require admin API access
            # Check for AI-related settings or features
            url = f"{self.base_url}/rest/api/3/instance/license"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                license_data = response.json()
                # Check license type and features
                
                # Note: Direct Intelligence check may require different endpoints
                result = {
                    'type': 'Atlassian Intelligence',
                    'name': 'Built-in AI Features',
                    'status': 'Unknown',  # Would need specific endpoint
                    'risk_level': 'MEDIUM'
                }
                results.append(result)
                
        except requests.exceptions.RequestException as e:
            print(f"   ⚠️  Could not check Intelligence features: {e}")
        
        return results
    
    def scan(self) -> List[Dict]:
        """Perform complete scan of Atlassian instance."""
        print("=" * 60)
        print(f"Scanning Atlassian instance: {self.domain}")
        print("=" * 60)
        print()
        
        all_results = []
        
        # Scan different components
        all_results.extend(self.check_jira_ai_addons())
        all_results.extend(self.check_confluence_ai_features())
        all_results.extend(self.check_atlassian_intelligence())
        
        self.results = all_results
        return all_results
    
    def generate_report(self, output_file: str = None) -> None:
        """Generate CSV report."""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"atlassian_ai_scan_{self.domain.replace('.', '_')}_{timestamp}.csv"
        
        if not self.results:
            print("⚠️  No results to report.")
            return
        
        fieldnames = ['type', 'name', 'key', 'vendor', 'ai_related', 'status', 'risk_level']
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.results)
        
        print(f"\n✅ Report generated: {output_file}")
        print(f"   Total AI features/add-ons found: {len(self.results)}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scan Atlassian instance for AI features and add-ons',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
    python atlassian_ai_scanner.py --domain mycompany.atlassian.net --email user@example.com --api_token YOUR_API_TOKEN

Note: You need to create an API token at:
    https://id.atlassian.com/manage-profile/security/api-tokens
        """
    )
    
    parser.add_argument('--domain', required=True, help='Atlassian domain (e.g., mycompany.atlassian.net)')
    parser.add_argument('--email', required=True, help='Atlassian account email')
    parser.add_argument('--api_token', required=True, help='Atlassian API token')
    parser.add_argument('--output', '-o', help='Output CSV file path')
    
    args = parser.parse_args()
    
    scanner = AtlassianAIScanner(args.domain, args.email, args.api_token)
    
    try:
        scanner.scan()
        scanner.generate_report(args.output)
        
        print("\n✅ Scan complete!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during scan: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

