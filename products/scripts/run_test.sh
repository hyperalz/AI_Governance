#!/bin/bash
# Helper script to run GitHub Copilot Auditor test

echo "============================================================"
echo "GitHub Copilot Auditor - Test Runner"
echo "============================================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if requests is installed
python3 -c "import requests" 2>/dev/null || {
    echo "📥 Installing requests..."
    pip install requests --quiet
}

# Check for token
if [ -z "$GITHUB_TOKEN" ]; then
    echo ""
    echo "⚠️  GITHUB_TOKEN environment variable is not set"
    echo ""
    echo "To set it, run:"
    echo "  export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "Or provide it when prompted below:"
    echo ""
    read -p "Enter your GitHub token (or press Enter to exit): " token
    if [ -z "$token" ]; then
        echo "❌ No token provided. Exiting."
        exit 1
    fi
    export GITHUB_TOKEN="$token"
fi

# Get organization name
if [ -z "$1" ]; then
    echo ""
    read -p "Enter GitHub organization name: " org_name
    if [ -z "$org_name" ]; then
        echo "❌ Organization name required"
        exit 1
    fi
else
    org_name="$1"
fi

echo ""
echo "🚀 Running audit for organization: $org_name"
echo "============================================================"
echo ""

# Run the test
python3 test_github_auditor.py "$org_name"

echo ""
echo "============================================================"
echo "✅ Test complete!"
echo "============================================================"

