#!/usr/bin/env python3
"""
Script Validation Test
======================

This script validates that all the GitHub Copilot Auditor scripts
are syntactically correct and have the expected structure.
"""

import ast
import sys
import os

def check_script_structure(filepath):
    """Check if a Python script has valid syntax and key components."""
    print(f"\n📝 Checking {os.path.basename(filepath)}...")
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            tree = ast.parse(content)
        
        # Check for key functions/classes
        has_main = False
        has_imports = False
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                has_imports = True
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            if isinstance(node, ast.ClassDef):
                classes.append(node.name)
            if isinstance(node, ast.If):
                if isinstance(node.test, ast.Compare):
                    if isinstance(node.test.left, ast.Name) and node.test.left.id == '__name__':
                        has_main = True
        
        # Check for requests import
        has_requests = 'requests' in content
        
        print(f"   ✅ Valid Python syntax")
        print(f"   📦 Has imports: {has_imports}")
        print(f"   📦 Has requests: {has_requests}")
        print(f"   🔧 Has main guard: {has_main}")
        print(f"   📚 Functions: {len(functions)} found")
        print(f"   🏗️  Classes: {len(classes)} found")
        
        if classes:
            print(f"      Classes: {', '.join(classes)}")
        
        return True
        
    except SyntaxError as e:
        print(f"   ❌ Syntax error: {e}")
        return False
    except Exception as e:
        print(f"   ⚠️  Error: {e}")
        return False

def main():
    print("=" * 60)
    print("GitHub Copilot Auditor - Script Validation")
    print("=" * 60)
    
    scripts = [
        "github_copilot_auditor.py",
        "test_github_auditor.py",
        "demo_mode.py"
    ]
    
    all_valid = True
    for script in scripts:
        if os.path.exists(script):
            if not check_script_structure(script):
                all_valid = False
        else:
            print(f"\n❌ {script} not found")
            all_valid = False
    
    print("\n" + "=" * 60)
    if all_valid:
        print("✅ All scripts are valid!")
        print("\n📋 Next steps for testing:")
        print("   1. Install dependencies: pip install requests")
        print("   2. Get GitHub token: https://github.com/settings/tokens")
        print("   3. Run: python test_github_auditor.py your-org-name")
        print("\n💡 See QUICK_START.md for detailed instructions")
    else:
        print("❌ Some scripts have issues")
        sys.exit(1)

if __name__ == "__main__":
    main()

