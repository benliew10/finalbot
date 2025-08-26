#!/usr/bin/env python3
"""
Diagnostic Tool for Image Mapping Issues
This helps identify when images are going to wrong Group B chats.
"""

import sqlite3
import json
import sys
import os

def analyze_image_mappings():
    """Analyze current image mappings and potential issues."""
    
    if not os.path.exists('images.db'):
        print("❌ No images.db found. Run this in the bot directory.")
        return
    
    print("🔍 ANALYZING IMAGE MAPPINGS")
    print("=" * 60)
    
    try:
        conn = sqlite3.connect('images.db')
        cursor = conn.cursor()
        
        # Get all images with metadata
        cursor.execute("SELECT id, number, file_id, status, metadata FROM images")
        images = cursor.fetchall()
        
        if not images:
            print("📋 No images found in database.")
            return
        
        print(f"\n📊 Found {len(images)} images in database\n")
        
        # Analyze each image
        problematic_images = []
        
        for img_id, number, file_id, status, metadata_str in images:
            print(f"🖼️  Image ID: {img_id}")
            print(f"   📝 Number: {number}")
            print(f"   🏷️  Status: {status}")
            
            if metadata_str:
                try:
                    metadata = json.loads(metadata_str)
                    source_group_b = metadata.get('source_group_b_id', 'Unknown')
                    print(f"   🏠 Original Group B: {source_group_b}")
                    
                    # Check for potential issues
                    if source_group_b != 'Unknown':
                        print(f"   ✅ Has original Group B mapping")
                    else:
                        print(f"   ⚠️  No original Group B mapping")
                        problematic_images.append(img_id)
                        
                except json.JSONDecodeError:
                    print(f"   ❌ Invalid metadata format")
                    problematic_images.append(img_id)
            else:
                print(f"   ❌ No metadata found")
                problematic_images.append(img_id)
            
            print()
        
        # Summary
        print("=" * 60)
        print("📋 ANALYSIS SUMMARY")
        print("=" * 60)
        
        if problematic_images:
            print(f"\n⚠️  {len(problematic_images)} images may have mapping issues:")
            for img_id in problematic_images:
                print(f"   • {img_id}")
        else:
            print(f"\n✅ All images have proper Group B mappings")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error analyzing database: {e}")

def simulate_range_conflicts():
    """Simulate potential range conflicts."""
    
    print("\n" + "=" * 60)
    print("🎭 SIMULATING RANGE CONFLICTS")
    print("=" * 60)
    
    # Check if ranges file exists
    if os.path.exists('group_b_amounts_ranges.json'):
        with open('group_b_amounts_ranges.json', 'r') as f:
            ranges = json.load(f)
            
        if not ranges:
            print("\n✅ No ranges configured - no conflicts possible")
            return
            
        print(f"\n📊 Found {len(ranges)} range configurations:")
        
        for group_id, range_config in ranges.items():
            min_amt = range_config.get('min', 20)
            max_amt = range_config.get('max', 5000)
            print(f"   • Group {group_id}: {min_amt}-{max_amt}")
        
        # Simulate conflicts
        print(f"\n🎯 POTENTIAL CONFLICT SCENARIOS:")
        print("-" * 40)
        
        example_amounts = [50, 150, 250, 400, 600, 1000, 2000]
        
        for amount in example_amounts:
            valid_groups = []
            for group_id, range_config in ranges.items():
                min_amt = range_config.get('min', 20)
                max_amt = range_config.get('max', 5000)
                if min_amt <= amount <= max_amt:
                    valid_groups.append(group_id)
            
            if len(valid_groups) > 1:
                print(f"   Amount {amount}: Multiple groups can handle → {valid_groups}")
                print(f"      ⚠️  If image was set by different group, it will be reassigned!")
            elif len(valid_groups) == 0:
                print(f"   Amount {amount}: No groups can handle → Silent")
            else:
                print(f"   Amount {amount}: Only {valid_groups[0]} can handle → OK")
    else:
        print("\n✅ No ranges file found - using default behavior")

def check_current_groups():
    """Check current group configurations."""
    
    print("\n" + "=" * 60)
    print("👥 CURRENT GROUP CONFIGURATION")
    print("=" * 60)
    
    # Check Group A
    if os.path.exists('group_a_ids.json'):
        with open('group_a_ids.json', 'r') as f:
            group_a_ids = json.load(f)
            print(f"\n📱 Group A IDs: {group_a_ids if group_a_ids else 'None'}")
    
    # Check Group B
    if os.path.exists('group_b_ids.json'):
        with open('group_b_ids.json', 'r') as f:
            group_b_ids = json.load(f)
            print(f"📱 Group B IDs: {group_b_ids if group_b_ids else 'None'}")

def main():
    """Main diagnostic function."""
    
    print("🩺 IMAGE MAPPING DIAGNOSTIC TOOL")
    print("=" * 60)
    print("This tool helps identify why images might be going to wrong Group B chats.")
    
    # Run all checks
    analyze_image_mappings()
    simulate_range_conflicts()
    check_current_groups()
    
    print("\n" + "=" * 60)
    print("💡 RECOMMENDATIONS")
    print("=" * 60)
    
    print("\nIf images are going to wrong Group B:")
    print("1. Check if ranges are causing reassignment")
    print("2. Consider using strict ownership mode")
    print("3. Review range configurations for conflicts")
    print("4. Clear image metadata to reset mappings")
    
    print("\n🔧 QUICK FIXES:")
    print("• Remove ranges: Use /removegroupbrange for each group")
    print("• Clear mappings: Delete images.db and re-add images")
    print("• Use strict mode: Modify bot to ignore ranges for existing images")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
