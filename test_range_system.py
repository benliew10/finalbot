#!/usr/bin/env python3
"""
Test Script for Group B Range-Based Trigger System
This script helps verify the range functionality works correctly.
"""

import json
import os

def display_current_config():
    """Display current configuration."""
    print("=" * 60)
    print("CURRENT CONFIGURATION")
    print("=" * 60)
    
    # Check Group A IDs
    if os.path.exists('group_a_ids.json'):
        with open('group_a_ids.json', 'r') as f:
            group_a_ids = json.load(f)
            print(f"\n📱 Group A IDs: {group_a_ids if group_a_ids else 'None configured'}")
    
    # Check Group B IDs
    if os.path.exists('group_b_ids.json'):
        with open('group_b_ids.json', 'r') as f:
            group_b_ids = json.load(f)
            print(f"📱 Group B IDs: {group_b_ids if group_b_ids else 'None configured'}")
    
    # Check Group B ranges
    if os.path.exists('group_b_amounts_ranges.json'):
        with open('group_b_amounts_ranges.json', 'r') as f:
            ranges = json.load(f)
            if ranges:
                print(f"\n📊 Group B Ranges:")
                for group_id, range_config in ranges.items():
                    print(f"   • {group_id}: {range_config['min']}-{range_config['max']}")
            else:
                print(f"\n📊 Group B Ranges: None configured (all accept 20-5000)")
    
    print()

def create_test_config():
    """Create test configuration files."""
    print("=" * 60)
    print("CREATING TEST CONFIGURATION")
    print("=" * 60)
    
    # Example Group IDs (you'll need to replace with real ones)
    test_group_a = [-1001234567890]  # Replace with your Group A ID
    test_group_b = [-1002222222222, -1003333333333]  # Replace with your Group B IDs
    
    print("\n⚠️ NOTE: You need to replace these with your actual Group IDs!")
    print(f"Test Group A: {test_group_a}")
    print(f"Test Group B: {test_group_b}")
    
    # Create test ranges
    test_ranges = {
        str(test_group_b[0]): {"min": 100, "max": 300},  # Group B1: Only 100-300
        str(test_group_b[1]): {"min": 500, "max": 800}   # Group B2: Only 500-800
    }
    
    print("\n📊 Test Ranges Configuration:")
    print(f"   • Group B1 ({test_group_b[0]}): 100-300")
    print(f"   • Group B2 ({test_group_b[1]}): 500-800")
    print("\n🔍 Coverage Gaps (will be silent):")
    print("   • 20-99: Below all ranges")
    print("   • 301-499: Gap between ranges")
    print("   • 801-5000: Above all ranges")
    
    return test_group_a, test_group_b, test_ranges

def generate_test_scenarios():
    """Generate test scenarios."""
    print("\n" + "=" * 60)
    print("TEST SCENARIOS")
    print("=" * 60)
    
    scenarios = [
        {
            "amount": 50,
            "expected": "🤫 SILENT (below all ranges)",
            "reason": "50 < 100 (minimum configured range)"
        },
        {
            "amount": 150,
            "expected": "✅ Forward to Group B1",
            "reason": "150 is within 100-300 range"
        },
        {
            "amount": 250,
            "expected": "✅ Forward to Group B1",
            "reason": "250 is within 100-300 range"
        },
        {
            "amount": 400,
            "expected": "🤫 SILENT (in gap)",
            "reason": "400 is between ranges (301-499)"
        },
        {
            "amount": 600,
            "expected": "✅ Forward to Group B2",
            "reason": "600 is within 500-800 range"
        },
        {
            "amount": 900,
            "expected": "🤫 SILENT (above all ranges)",
            "reason": "900 > 800 (maximum configured range)"
        },
        {
            "amount": 2000,
            "expected": "🤫 SILENT (above all ranges)",
            "reason": "2000 > 800 (maximum configured range)"
        }
    ]
    
    print("\n📝 Test these amounts in Group A:")
    print("-" * 40)
    for i, scenario in enumerate(scenarios, 1):
        print(f"\nTest {i}: Send '{scenario['amount']}' in Group A")
        print(f"   Expected: {scenario['expected']}")
        print(f"   Reason: {scenario['reason']}")
    
    return scenarios

def create_bot_test_commands():
    """Generate bot commands for testing."""
    print("\n" + "=" * 60)
    print("BOT SETUP COMMANDS")
    print("=" * 60)
    
    print("\n📋 Run these commands in private chat with your bot:")
    print("-" * 40)
    
    print("\n1️⃣ First, set up Groups (run in respective group chats):")
    print("   In Group A chat: Send '设置群聊A'")
    print("   In Group B1 chat: Send '设置群聊B'")
    print("   In Group B2 chat: Send '设置群聊B'")
    
    print("\n2️⃣ Then, configure ranges (run in private chat):")
    print("   /setgroupbrange [GROUP_B1_ID] 100 300")
    print("   /setgroupbrange [GROUP_B2_ID] 500 800")
    
    print("\n3️⃣ Verify configuration:")
    print("   /listgroupb          # Shows all Group B with ranges")
    print("   /listgroupbranges    # Shows visual coverage map")
    
    print("\n4️⃣ Test in Group A:")
    print("   Send various amounts and observe behavior")

def create_verification_checklist():
    """Create verification checklist."""
    print("\n" + "=" * 60)
    print("VERIFICATION CHECKLIST")
    print("=" * 60)
    
    print("\n✅ Check these behaviors:")
    print("-" * 40)
    checklist = [
        "Amount within Group B1 range (100-300) → Forwards to Group B1",
        "Amount within Group B2 range (500-800) → Forwards to Group B2",
        "Amount below all ranges (< 100) → SILENT, no forwarding",
        "Amount in gap (301-499) → SILENT, no forwarding",
        "Amount above all ranges (> 800) → SILENT, no forwarding",
        "No error messages shown in Group A for out-of-range",
        "Bot logs show 'Remaining silent' for out-of-range"
    ]
    
    for i, item in enumerate(checklist, 1):
        print(f"   [{' '}] {i}. {item}")
    
    print("\n📊 Expected Results Summary:")
    print("-" * 40)
    print("   • In-range amounts: Forward to appropriate Group B")
    print("   • Out-of-range amounts: Complete silence")
    print("   • No error messages to users")
    print("   • Activity logged but users not notified")

def main():
    """Main test script."""
    print("\n" + "🚀 GROUP B RANGE TESTING GUIDE 🚀".center(60))
    print("=" * 60)
    
    # Display current configuration
    display_current_config()
    
    # Create test configuration
    test_group_a, test_group_b, test_ranges = create_test_config()
    
    # Generate test scenarios
    scenarios = generate_test_scenarios()
    
    # Create bot commands
    create_bot_test_commands()
    
    # Create verification checklist
    create_verification_checklist()
    
    print("\n" + "=" * 60)
    print("HOW TO RUN THE TEST")
    print("=" * 60)
    
    print("\n1. Start your bot:")
    print("   python bot.py")
    
    print("\n2. Configure groups and ranges using the commands above")
    
    print("\n3. Test each scenario in Group A")
    
    print("\n4. Observe:")
    print("   • Which Group B receives the message (if any)")
    print("   • Whether Group A gets any error message")
    print("   • Check bot console logs for 'Remaining silent' messages")
    
    print("\n5. Compare results with expected behavior")
    
    print("\n" + "=" * 60)
    print("💡 QUICK TEST EXAMPLE")
    print("=" * 60)
    print("\nAfter setup, in Group A send these messages:")
    print("   '150'  → Should forward to Group B1")
    print("   '400'  → Should be SILENT (no forward)")
    print("   '600'  → Should forward to Group B2")
    print("   '1000' → Should be SILENT (no forward)")
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS CRITERIA")
    print("=" * 60)
    print("\nThe test is successful if:")
    print("1. Messages within range are forwarded correctly")
    print("2. Messages outside range are silently ignored")
    print("3. No error messages appear in Group A")
    print("4. Bot logs show proper range checking")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
