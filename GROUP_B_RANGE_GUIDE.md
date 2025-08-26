# Group B Range-Based Trigger System Guide

## Overview
The bot includes a powerful range-based trigger system that allows you to control which Group B chats receive messages based on the amount specified in Group A messages.

## How It Works
1. **Default Behavior**: Without any range configured, Group B chats receive all messages (amounts between 20-5000)
2. **With Range Set**: Group B only receives messages where the amount falls within its configured min-max range
3. **Multiple Group B**: Different Group B chats can have different ranges, allowing for segmentation

## Commands (Admin Only - Private Chat)

### Setting a Range
```
/setgroupbrange <group_b_id> <min_amount> <max_amount>
```
**Example**: `/setgroupbrange -1002648811668 100 1000`
- This Group B will only receive messages with amounts between 100 and 1000

### Removing a Range
```
/removegroupbrange <group_b_id>
```
**Example**: `/removegroupbrange -1002648811668`
- Removes the range restriction (Group B will receive all amounts again)

### Listing All Ranges
```
/listgroupbranges
```
- Shows all configured Group B ranges

### Listing All Group B IDs
```
/listgroupb
```
- Shows all Group B IDs with their current range settings

## Practical Examples

### Scenario 1: Tiered Processing
- Group B1: `/setgroupbrange -1001234567890 20 500` (handles small amounts)
- Group B2: `/setgroupbrange -1009876543210 501 2000` (handles medium amounts)
- Group B3: `/setgroupbrange -1005555555555 2001 5000` (handles large amounts)

### Scenario 2: Specific Range Only
- Group B: `/setgroupbrange -1001234567890 100 300`
- Only processes amounts between 100-300, ignoring all others

### Scenario 3: VIP Processing
- Regular Group B: `/setgroupbrange -1001111111111 20 999`
- VIP Group B: `/setgroupbrange -1002222222222 1000 5000`

## How Amount Detection Works
When a message is sent in Group A with format like:
- "100" or "+100" → Amount detected as 100
- "金额100" → Amount detected as 100
- The bot extracts the amount and checks which Group B chats can handle it

## Important Notes
1. If NO Group B has a range that includes the amount, the message is NOT forwarded anywhere
2. If multiple Group B chats can handle an amount, the bot uses a deterministic algorithm to select one
3. Ranges are inclusive (min ≤ amount ≤ max)
4. Only global admins can configure ranges via private chat with the bot

## Troubleshooting
- **Message not forwarding?** Check if the amount falls within any Group B's range using `/listgroupbranges`
- **Wrong Group B receiving?** Verify ranges don't overlap using `/listgroupb`
- **Want to disable ranges?** Use `/removegroupbrange` for specific groups or remove all ranges to restore default behavior
