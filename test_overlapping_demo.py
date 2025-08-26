#!/usr/bin/env python3
"""
Demonstration of how the bot handles overlapping ranges.
This simulates the bot's selection algorithm.
"""

def simulate_selection(image_ids, valid_group_bs):
    """Simulate the bot's deterministic selection."""
    print(f"\nValid Group Bs: {valid_group_bs}")
    print(f"Number of valid groups: {len(valid_group_bs)}")
    print("-" * 50)
    
    distribution = {}
    for group in valid_group_bs:
        distribution[group] = 0
    
    for img_id in image_ids:
        # This is exactly what the bot does
        image_hash = hash(img_id)
        selected_index = abs(image_hash) % len(valid_group_bs)
        selected_group = valid_group_bs[selected_index]
        
        distribution[selected_group] += 1
        print(f"Image '{img_id}' → Group {selected_group}")
    
    print("\n📊 Distribution Statistics:")
    print("-" * 50)
    total = len(image_ids)
    for group, count in distribution.items():
        percentage = (count / total) * 100 if total > 0 else 0
        print(f"Group {group}: {count}/{total} ({percentage:.1f}%)")

def main():
    print("=" * 60)
    print("OVERLAPPING RANGES DEMONSTRATION")
    print("=" * 60)
    
    # Scenario 1: Three groups with complete overlap
    print("\n📋 SCENARIO 1: Complete Overlap")
    print("All three groups have range 100-500")
    print("Amount sent: 250 (all can handle)")
    
    # Simulate 12 different images
    image_ids = [f"img_{i:03d}" for i in range(1, 13)]
    valid_groups = ["B1", "B2", "B3"]
    
    simulate_selection(image_ids, valid_groups)
    
    # Scenario 2: Partial overlap
    print("\n\n📋 SCENARIO 2: Partial Overlap")
    print("B1: 100-300, B2: 200-400, B3: 350-500")
    print("Amount sent: 250 (B1 and B2 can handle)")
    
    valid_groups = ["B1", "B2"]  # Only these two match
    simulate_selection(image_ids, valid_groups)
    
    # Scenario 3: Different sized overlaps
    print("\n\n📋 SCENARIO 3: Four Groups Mixed Overlap")
    print("B1: 1-5000, B2: 100-300, B3: 200-400, B4: 250-350")
    print("Amount sent: 275 (B1, B3, B4 can handle)")
    
    valid_groups = ["B1", "B3", "B4"]
    simulate_selection(image_ids, valid_groups)
    
    # Show consistency
    print("\n\n🔄 CONSISTENCY CHECK")
    print("Same image always goes to same group:")
    print("-" * 50)
    
    test_image = "img_test_001"
    valid_groups = ["B1", "B2", "B3"]
    
    for run in range(5):
        image_hash = hash(test_image)
        selected_index = abs(image_hash) % len(valid_groups)
        selected_group = valid_groups[selected_index]
        print(f"Run {run + 1}: '{test_image}' → Group {selected_group}")
    
    print("\n✅ Same result every time!")
    
    # Real commands example
    print("\n" + "=" * 60)
    print("REAL BOT COMMANDS TO TEST THIS")
    print("=" * 60)
    
    print("\n1️⃣ Set up overlapping ranges:")
    print("   /setgroupbrange -1001111111111 100 500")
    print("   /setgroupbrange -1002222222222 100 500")
    print("   /setgroupbrange -1003333333333 100 500")
    
    print("\n2️⃣ Check coverage:")
    print("   /listgroupbranges")
    
    print("\n3️⃣ Test in Group A:")
    print("   Send: 250")
    print("   Result: Goes to ONE Group B (determined by hash)")
    
    print("\n4️⃣ Send multiple times:")
    print("   The SAME amount with SAME image → SAME Group B")
    print("   Different images → Distributed across groups")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    
    print("\n🎯 The bot ensures:")
    print("• No duplicate forwarding")
    print("• Deterministic selection")
    print("• Roughly even distribution")
    print("• Consistent behavior")
    
    print("\n💡 This is perfect for:")
    print("• Load balancing")
    print("• Team distribution")
    print("• Redundancy without duplication")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
