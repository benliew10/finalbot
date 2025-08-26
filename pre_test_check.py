#!/usr/bin/env python3
"""
Pre-test Environment Checker
Run this before testing to ensure everything is ready.
"""

import os
import sys
import json

def check_requirements():
    """Check if required packages are installed."""
    print("🔍 Checking Python packages...")
    
    required_packages = {
        'telegram': 'python-telegram-bot',
        'requests': 'requests',
        'dotenv': 'python-dotenv',
        'schedule': 'schedule'
    }
    
    missing_packages = []
    
    for module, package_name in required_packages.items():
        try:
            if module == 'telegram':
                import telegram
            elif module == 'requests':
                import requests
            elif module == 'dotenv':
                import dotenv
            elif module == 'schedule':
                import schedule
            print(f"   ✅ {package_name} installed")
        except ImportError:
            print(f"   ❌ {package_name} missing")
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n⚠️ Install missing packages with:")
        print(f"   pip3 install {' '.join(missing_packages)}")
        return False
    return True

def check_bot_token():
    """Check if bot token is configured."""
    print("\n🔑 Checking bot token...")
    
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            content = f.read()
            if 'BOT_TOKEN' in content and 'YOUR_BOT_TOKEN_HERE' not in content:
                print("   ✅ Bot token configured in .env")
                return True
            else:
                print("   ⚠️ Bot token not properly set in .env")
                return False
    else:
        print("   ❌ No .env file found")
        print("   Create one with: echo 'BOT_TOKEN=YOUR_BOT_TOKEN_HERE' > .env")
        return False

def check_configuration():
    """Check current bot configuration."""
    print("\n📋 Checking configuration files...")
    
    config_files = {
        'group_a_ids.json': 'Group A IDs',
        'group_b_ids.json': 'Group B IDs',
        'group_b_amounts_ranges.json': 'Group B Ranges'
    }
    
    config_status = {}
    
    for filename, description in config_files.items():
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                if data:
                    print(f"   ✅ {description}: Configured")
                    config_status[filename] = data
                else:
                    print(f"   ⚠️ {description}: Empty (needs setup)")
                    config_status[filename] = None
        else:
            print(f"   ⚠️ {description}: File missing (will be created on bot start)")
            config_status[filename] = None
    
    return config_status

def display_test_readiness(has_packages, has_token, config_status):
    """Display overall test readiness."""
    print("\n" + "=" * 60)
    print("TEST READINESS REPORT")
    print("=" * 60)
    
    ready_to_test = has_packages and has_token
    
    if ready_to_test:
        print("\n✅ Bot is ready to start!")
        print("\nNext steps:")
        print("1. Start the bot: python3 bot.py")
        print("2. Set up groups if not configured:")
        print("   - In Group A: Send '设置群聊A'")
        print("   - In Group B: Send '设置群聊B'")
        print("3. Configure ranges in private chat:")
        print("   - /setgroupbrange [GROUP_B_ID] [MIN] [MAX]")
        print("4. Test with different amounts in Group A")
    else:
        print("\n❌ Not ready to test. Please fix the issues above.")
        
        if not has_packages:
            print("\n1. Install missing packages:")
            print("   pip3 install -r requirements.txt")
        
        if not has_token:
            print("\n2. Set up bot token:")
            print("   - Get token from @BotFather on Telegram")
            print("   - Create .env file: echo 'BOT_TOKEN=YOUR_TOKEN' > .env")

def create_sample_env():
    """Create sample .env file if it doesn't exist."""
    if not os.path.exists('.env'):
        print("\n📝 Creating sample .env file...")
        with open('.env.sample', 'w') as f:
            f.write("# Telegram Bot Token from @BotFather\n")
            f.write("BOT_TOKEN=YOUR_BOT_TOKEN_HERE\n")
        print("   Created .env.sample - copy it to .env and add your token")

def main():
    """Main pre-test check."""
    print("\n" + "🚀 PRE-TEST ENVIRONMENT CHECK 🚀".center(60))
    print("=" * 60)
    
    # Check requirements
    has_packages = check_requirements()
    
    # Check bot token
    has_token = check_bot_token()
    
    # Check configuration
    config_status = check_configuration()
    
    # Display readiness
    display_test_readiness(has_packages, has_token, config_status)
    
    # Create sample .env if needed
    if not has_token:
        create_sample_env()
    
    # Display current ranges if configured
    if config_status.get('group_b_amounts_ranges.json'):
        print("\n📊 Current Range Configuration:")
        print("-" * 40)
        ranges = config_status['group_b_amounts_ranges.json']
        for group_id, range_config in ranges.items():
            print(f"   Group B {group_id}: {range_config['min']}-{range_config['max']}")
    
    print("\n" + "=" * 60)
    
    return has_packages and has_token

if __name__ == "__main__":
    ready = main()
    sys.exit(0 if ready else 1)
