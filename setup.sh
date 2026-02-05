#!/bin/bash
# Setup script for Resume Optimizer

set -e  # Exit on error

echo "🚀 Resume Optimizer Setup"
echo "=========================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.7"

if (( $(echo "$python_version < $required_version" | bc -l) )); then
    echo "❌ Python 3.7+ is required. You have Python $python_version"
    exit 1
fi
echo "✅ Python $python_version detected"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt --quiet
echo "✅ Dependencies installed"
echo ""

# Check for API key
echo "🔑 Checking for API key..."
if [ -z "$ANTHROPIC_API_KEY" ] && [ ! -f .env ]; then
    echo "⚠️  No API key found!"
    echo ""
    echo "You need an Anthropic API key to use this tool."
    echo ""
    read -p "Do you have an Anthropic API key? (y/n): " has_key
    
    if [ "$has_key" = "y" ] || [ "$has_key" = "Y" ]; then
        read -p "Enter your API key: " api_key
        echo "ANTHROPIC_API_KEY=$api_key" > .env
        echo "✅ API key saved to .env file"
    else
        echo ""
        echo "To get an API key:"
        echo "1. Visit: https://console.anthropic.com/"
        echo "2. Sign up or log in"
        echo "3. Create a new API key"
        echo "4. Run this setup again with your key"
        echo ""
        echo "Or set it manually:"
        echo "  export ANTHROPIC_API_KEY='your-key-here'"
        echo ""
        exit 0
    fi
else
    echo "✅ API key found"
fi
echo ""

# Test the installation
echo "🧪 Testing installation..."
if python3 -c "import anthropic; print('✅ Anthropic package works')" 2>/dev/null; then
    echo "✅ All systems go!"
else
    echo "❌ Installation test failed"
    exit 1
fi
echo ""

# Show next steps
echo "✨ Setup complete!"
echo ""
echo "Try these commands to get started:"
echo ""
echo "1. Test with sample files:"
echo "   python3 resume_optimizer.py --resume examples/sample_resume.txt --job-description examples/sample_job_description.txt --score"
echo ""
echo "2. Optimize your own resume:"
echo "   python3 resume_optimizer.py --resume your_resume.txt --job-description job.txt --output optimized.txt"
echo ""
echo "3. Get help:"
echo "   python3 resume_optimizer.py --help"
echo ""
echo "📚 Check QUICKSTART.md for more examples!"
echo ""
