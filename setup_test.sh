#!/bin/bash

# Setup script for testing range-based triggers

echo "================================================"
echo "🚀 Range-Based Trigger Test Setup"
echo "================================================"

# Check Python
echo -e "\n📌 Checking Python..."
if command -v python3 &> /dev/null; then
    echo "✅ Python3 found: $(python3 --version)"
else
    echo "❌ Python3 not found. Please install Python 3.7+"
    exit 1
fi

# Install dependencies
echo -e "\n📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check for .env file
echo -e "\n🔑 Checking bot token..."
if [ -f .env ]; then
    echo "✅ .env file exists"
    if grep -q "YOUR_BOT_TOKEN_HERE" .env; then
        echo "⚠️  Please update BOT_TOKEN in .env with your actual token from @BotFather"
    else
        echo "✅ Bot token appears to be configured"
    fi
else
    echo "📝 Creating .env file..."
    echo "BOT_TOKEN=YOUR_BOT_TOKEN_HERE" > .env
    echo "⚠️  Please edit .env and add your bot token from @BotFather"
fi

# Run pre-test check
echo -e "\n🔍 Running environment check..."
python3 pre_test_check.py

echo -e "\n================================================"
echo "📋 Next Steps:"
echo "================================================"
echo "1. Edit .env file with your bot token (if not done)"
echo "2. Run: python3 bot.py"
echo "3. Set up test groups in Telegram"
echo "4. Configure ranges as shown in COMPLETE_TEST_GUIDE.md"
echo "5. Test with different amounts!"
echo ""
echo "📖 See COMPLETE_TEST_GUIDE.md for detailed instructions"
echo "================================================"
