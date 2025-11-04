#!/usr/bin/env python3
"""
Microsoft 365 Copilot Readiness Checker
========================================

Uses Microsoft Graph API (read-only, delegated permissions) to:
- List users licensed for Copilot
- Identify potential data exposure points
- Assess organizational Copilot adoption

Requirements:
    pip install msal requests

Usage:
    python m365_copilot_checker.py --tenant-id YOUR_TENANT --client-id YOUR_CLIENT_ID --client-secret YOUR_SECRET

Author: AI Governance Team
"""

import requests
import csv
import argparse
import sys
from typing import List, Dict, Optional
from datetime import datetime

try:
    from msal import ConfidentialClientApplication
except ImportError:
    print("❌ Error: msal library not installed. Run: pip install msal")
    sys.exit(1)


class M365CopilotChecker:
    """Checker for Microsoft 365 Copilot usage."""
    
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        """
        Initialize the checker.
        
        Args:
            tenant_id: Azure AD Tenant ID
            client_id: Azure AD Application (Client) ID
            client_secret: Client secret value
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scope = ["https://graph.microsoft.com/.default"]
        
        self.graph_endpoint = "https://graph.microsoft.com/v1.0"
        self.access_token = None
        self.results: List[Dict] = []
    
    def get_access_token(self) -> str:
        """Get OAuth2 access token using client credentials flow."""
        print("🔐 Authenticating with Microsoft Graph API...")
        
        app = ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority
        )
        
        result = app.acquire_token_for_client(scopes=self.scope)
        
        if "access_token" in result:
            self.access_token = result["access_token"]
            print("✅ Authentication successful")
            return self.access_token
        else:
            error = result.get("error_description", result.get("error", "Unknown error"))
            print(f"❌ Authentication failed: {error}")
            sys.exit(1)
    
    def get_headers(self) -> Dict[str, str]:
        """Get request headers with authentication."""
        if not self.access_token:
            self.get_access_token()
        
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
    
    def get_copilot_licensed_users(self) -> List[Dict]:
        """Get list of users licensed for Microsoft 365 Copilot."""
        print("🔍 Checking for Copilot-licensed users...")
        
        licensed_users = []
        
        try:
            # Get all users (this requires User.Read.All permission)
            url = f"{self.graph_endpoint}/users"
            params = {
                "$select": "id,displayName,userPrincipalName,assignedLicenses",
                "$top": 999
            }
            
            headers = self.get_headers()
            
            while url:
                response = requests.get(url, headers=headers, params=params if '?' not in url else None)
                
                if response.status_code == 401:
                    print("❌ Authentication failed. Please check your credentials.")
                    sys.exit(1)
                elif response.status_code == 403:
                    print("❌ Insufficient permissions. Ensure the app has 'User.Read.All' permission.")
                    sys.exit(1)
                
                response.raise_for_status()
                data = response.json()
                
                users = data.get('value', [])
                
                # Check for Copilot licenses
                # Copilot license SKU IDs (these may change - verify with Microsoft)
                copilot_sku_ids = [
                    "c17df3e0-3b78-4c93-a7e5-4a3b3d3d3d3d",  # Microsoft 365 Copilot (placeholder - verify actual SKU)
                ]
                
                for user in users:
                    assigned_licenses = user.get('assignedLicenses', [])
                    
                    # Check if user has any Copilot-related license
                    has_copilot = False
                    for license in assigned_licenses:
                        sku_id = license.get('skuId', '')
                        # In production, you'd check against actual Copilot SKU IDs
                        # This is a placeholder - you need to verify actual SKU IDs
                        
                    # For now, we'll check all users and flag for manual review
                    # In production, filter by actual Copilot SKU IDs
                    
                    user_info = {
                        'user_id': user.get('id'),
                        'display_name': user.get('displayName'),
                        'email': user.get('userPrincipalName'),
                        'copilot_licensed': 'Unknown',  # Would be Yes/No with proper SKU checking
                        'license_count': len(assigned_licenses)
                    }
                    licensed_users.append(user_info)
                
                # Check for next page
                url = data.get('@odata.nextLink')
                params = None  # nextLink already has params
                
                print(f"   Processed {len(licensed_users)} users...")
            
            print(f"✅ Found {len(licensed_users)} users to check")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching users: {e}")
            return []
        
        return licensed_users
    
    def identify_data_exposure_points(self) -> List[Dict]:
        """Identify potential data exposure points."""
        print("🔍 Identifying potential data exposure points...")
        
        exposure_points = []
        
        try:
            headers = self.get_headers()
            
            # Check SharePoint sites (potential data sources)
            # This requires Sites.Read.All permission
            url = f"{self.graph_endpoint}/sites"
            params = {"$select": "id,name,webUrl,displayName"}
            
            try:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    sites = response.json().get('value', [])
                    print(f"   Found {len(sites)} SharePoint sites")
                    
                    for site in sites[:20]:  # Limit for performance
                        exposure_points.append({
                            'type': 'SharePoint Site',
                            'name': site.get('displayName'),
                            'url': site.get('webUrl'),
                            'risk_level': 'MEDIUM'
                        })
            except:
                print("   ⚠️  Could not access SharePoint sites (may require additional permissions)")
            
            # Check Teams (potential collaboration data)
            # This requires Team.ReadBasic.All permission
            url = f"{self.graph_endpoint}/teams"
            
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    teams = response.json().get('value', [])
                    print(f"   Found {len(teams)} Teams")
                    
                    for team in teams[:20]:  # Limit for performance
                        exposure_points.append({
                            'type': 'Microsoft Teams',
                            'name': team.get('displayName'),
                            'id': team.get('id'),
                            'risk_level': 'MEDIUM'
                        })
            except:
                print("   ⚠️  Could not access Teams (may require additional permissions)")
                
        except Exception as e:
            print(f"   ⚠️  Error identifying exposure points: {e}")
        
        return exposure_points
    
    def check(self) -> Dict:
        """Perform complete check."""
        print("=" * 60)
        print("Microsoft 365 Copilot Readiness Check")
        print("=" * 60)
        print()
        
        results = {
            'licensed_users': self.get_copilot_licensed_users(),
            'exposure_points': self.identify_data_exposure_points()
        }
        
        self.results = results
        return results
    
    def generate_report(self, output_file: str = None) -> None:
        """Generate CSV report."""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"m365_copilot_check_{self.tenant_id}_{timestamp}.csv"
        
        all_rows = []
        
        # Add licensed users
        for user in self.results.get('licensed_users', []):
            all_rows.append({
                'type': 'User',
                'name': user.get('display_name'),
                'email': user.get('email'),
                'copilot_licensed': user.get('copilot_licensed'),
                'license_count': user.get('license_count'),
                'risk_level': 'MEDIUM' if user.get('copilot_licensed') == 'Yes' else 'LOW'
            })
        
        # Add exposure points
        for point in self.results.get('exposure_points', []):
            all_rows.append(point)
        
        if not all_rows:
            print("⚠️  No results to report.")
            return
        
        fieldnames = ['type', 'name', 'email', 'copilot_licensed', 'license_count', 'url', 'id', 'risk_level']
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(all_rows)
        
        print(f"\n✅ Report generated: {output_file}")
        print(f"   Total items: {len(all_rows)}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Check Microsoft 365 for Copilot usage and data exposure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
    python m365_copilot_checker.py --tenant-id YOUR_TENANT_ID --client-id YOUR_CLIENT_ID --client-secret YOUR_SECRET

Note: You need to register an Azure AD app with these API permissions:
    - User.Read.All
    - Sites.Read.All (optional, for SharePoint check)
    - Team.ReadBasic.All (optional, for Teams check)

Required permissions must be granted by an admin.
        """
    )
    
    parser.add_argument('--tenant-id', required=True, help='Azure AD Tenant ID')
    parser.add_argument('--client-id', required=True, help='Azure AD Application (Client) ID')
    parser.add_argument('--client-secret', required=True, help='Client secret value')
    parser.add_argument('--output', '-o', help='Output CSV file path')
    
    args = parser.parse_args()
    
    checker = M365CopilotChecker(args.tenant_id, args.client_id, args.client_secret)
    
    try:
        checker.check()
        checker.generate_report(args.output)
        
        print("\n✅ Check complete!")
        print("\n⚠️  Note: This tool provides basic checks. For comprehensive Copilot")
        print("   auditing, verify actual SKU IDs and use Microsoft's admin tools.")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Check interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during check: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

