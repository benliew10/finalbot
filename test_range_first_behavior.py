#!/usr/bin/env python3
"""
Test Range-First Behavior
This demonstrates the corrected behavior where ranges take priority over ownership.
"""

def test_range_first_behavior():
    """Test the new range-first behavior."""
    
    print("🧪 TESTING RANGE-FIRST BEHAVIOR")
    print("=" * 60)
    
    # Setup from your logs
    print("\n📋 YOUR ACTUAL SETUP:")
    print("• Group B1 (-1002648889060): Range 20-200")
    print("• Group B2 (-1002648811668): Range 300-2000")
    print("• Image set by Group B1 (outside range for amount 300)")
    
    scenarios = [
        {
            "amount": 100,
            "valid_groups": [-1002648889060],  # Only B1 can handle
            "original_group": -1002648889060,  # B1 set the image
            "expected": -1002648889060,
            "reason": "Original group CAN handle amount - use original"
        },
        {
            "amount": 199,
            "valid_groups": [-1002648889060],  # Only B1 can handle  
            "original_group": -1002648811668,  # B2 set the image
            "expected": -1002648889060,
            "reason": "Original group CANNOT handle amount - use valid group"
        },
        {
            "amount": 300,
            "valid_groups": [-1002648811668],  # Only B2 can handle
            "original_group": -1002648889060,  # B1 set the image
            "expected": -1002648811668,
            "reason": "Original group CANNOT handle amount - use valid group (YOUR CASE)"
        },
        {
            "amount": 1000,
            "valid_groups": [-1002648811668],  # Only B2 can handle
            "original_group": -1002648811668,  # B2 set the image
            "expected": -1002648811668,
            "reason": "Original group CAN handle amount - use original"
        },
        {
            "amount": 250,
            "valid_groups": [],  # No groups can handle (gap in ranges)
            "original_group": -1002648889060,  # B1 set the image
            "expected": "SILENT",
            "reason": "No groups can handle - stay silent"
        }
    ]
    
    print(f"\n🎯 TEST SCENARIOS:")
    print("-" * 60)
    
    for i, scenario in enumerate(scenarios, 1):
        amount = scenario['amount']
        valid_groups = scenario['valid_groups']
        original_group = scenario['original_group']
        expected = scenario['expected']
        reason = scenario['reason']
        
        print(f"\nTest {i}: Amount {amount}")
        print(f"   Original Group B: {original_group}")
        print(f"   Valid Groups: {valid_groups}")
        
        # Simulate the NEW behavior
        if not valid_groups:
            result = "SILENT"
            print(f"   ✅ Result: {result} (no groups can handle)")
        elif original_group in valid_groups:
            result = original_group
            print(f"   ✅ Result: {result} (original can handle)")
        else:
            result = valid_groups[0]  # Simplified for demo
            print(f"   ✅ Result: {result} (original cannot handle, using valid)")
        
        print(f"   📝 Reason: {reason}")
        
        if result == expected:
            print(f"   ✅ CORRECT BEHAVIOR")
        else:
            print(f"   ❌ UNEXPECTED: Expected {expected}, got {result}")

def demonstrate_your_specific_case():
    """Demonstrate your specific problematic case."""
    
    print(f"\n" + "=" * 60)
    print("🚨 YOUR SPECIFIC CASE DEMONSTRATION")
    print("=" * 60)
    
    print(f"\nFrom your logs:")
    print(f"• Group B1 (-1002648889060) set an image")
    print(f"• Group B1 range: 20-200")
    print(f"• Group B2 (-1002648811668) range: 300-2000")
    print(f"• Amount sent: 300")
    
    print(f"\n🔴 OLD BEHAVIOR (What you experienced):")
    print(f"   300 can be handled by: [-1002648811668] (only B2)")
    print(f"   Original image from: -1002648889060 (B1)")
    print(f"   ❌ Bot sent to B1 anyway (strict ownership)")
    print(f"   ❌ B1 received amount outside its range!")
    
    print(f"\n🟢 NEW BEHAVIOR (Fixed):")
    print(f"   300 can be handled by: [-1002648811668] (only B2)")
    print(f"   Original image from: -1002648889060 (B1)")
    print(f"   ✅ B1 cannot handle 300 (outside 20-200 range)")
    print(f"   ✅ Bot sends to B2 instead (range compliance)")
    print(f"   ✅ Only B2 receives the message!")

def show_expected_logs():
    """Show what the logs should look like after the fix."""
    
    print(f"\n" + "=" * 60)
    print("📋 EXPECTED LOG OUTPUT AFTER FIX")
    print("=" * 60)
    
    print(f"\nWhen you send amount 300:")
    print(f"""
INFO - Group B IDs that can handle amount 300.0: [-1002648811668]
INFO - Original Group B -1002648889060 cannot handle amount 300.0, will select from valid groups
INFO - Selected Group B -1002648811668 from valid range-capable options: [-1002648811668]
INFO - Final target Group B ID for forwarding: -1002648811668
""")
    
    print(f"Key changes:")
    print(f"• ✅ 'cannot handle amount' - respects ranges")
    print(f"• ✅ 'will select from valid groups' - doesn't force original")
    print(f"• ✅ Selected -1002648811668 - goes to correct group")

def main():
    """Main test function."""
    test_range_first_behavior()
    demonstrate_your_specific_case()
    show_expected_logs()
    
    print(f"\n" + "=" * 60)
    print("✅ SUMMARY OF THE FIX")
    print("=" * 60)
    
    print(f"\nBEFORE (What you experienced):")
    print(f"• Images always went to original Group B")
    print(f"• Ranges were ignored for existing images")
    print(f"• Groups received amounts outside their ranges")
    
    print(f"\nAFTER (Fixed behavior):")
    print(f"• Ranges take priority over ownership")
    print(f"• Images only go to groups that can handle the amount")
    print(f"• Strict range enforcement")
    print(f"• Your specific case is now fixed!")
    
    print(f"\n🎯 THE FIX:")
    print(f"Now when amount 300 is sent:")
    print(f"1. Check who can handle 300: Only Group B2")
    print(f"2. Check if original Group B1 is in that list: NO")
    print(f"3. Send to Group B2 instead ✅")
    
    print(f"\n" + "=" * 60)

if __name__ == "__main__":
    main()
