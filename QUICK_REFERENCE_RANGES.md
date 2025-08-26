# 🚀 QUICK REFERENCE: Group B Range Triggers

## ✅ The Feature Already Exists!
Your bot **already has** the range-based trigger system implemented. You just need to configure it.

## 🎯 What It Does
- **Controls which Group B receives messages based on amount**
- **Only forwards to Group B if amount is within configured range**
- **Supports multiple Group B with different or overlapping ranges**

## ⚡ Quick Setup (Admin Private Chat Only)

### 1️⃣ Check Current Groups
```
/listgroupb
```
Shows all Group B IDs and their current ranges

### 2️⃣ Set a Range
```
/setgroupbrange -1002648811668 100 500
```
This Group B will ONLY receive amounts between 100-500

### 3️⃣ View Coverage
```
/listgroupbranges
```
Shows visual map of all ranges and gaps

### 4️⃣ Remove a Range
```
/removegroupbrange -1002648811668
```
Group B will receive ALL amounts again

## 📊 Common Scenarios

### Scenario A: Split by Amount Size
```
Group B1: /setgroupbrange [ID1] 20 500      # Small
Group B2: /setgroupbrange [ID2] 501 2000    # Medium
Group B3: /setgroupbrange [ID3] 2001 5000   # Large
```

### Scenario B: Filter Specific Amounts
```
Group B: /setgroupbrange [ID] 100 300       # Only 100-300
```
⚠️ Amounts outside range won't be forwarded anywhere!

### Scenario C: Multiple Groups Same Range
```
Group B1: /setgroupbrange [ID1] 100 1000
Group B2: /setgroupbrange [ID2] 100 1000
```
Bot will distribute between them

## ❓ How It Works

1. **Message in Group A** → Bot extracts amount (e.g., "250")
2. **Bot checks** → Which Group B ranges include 250?
3. **If match found** → Forward to that Group B
4. **If no match** → Message not forwarded (silent)
5. **If multiple matches** → Bot selects one deterministically

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Message not forwarding | Check if amount is in any range: `/listgroupbranges` |
| Wrong Group B receiving | Check for overlapping ranges: `/listgroupbranges` |
| Want to disable ranges | Use `/removegroupbrange [ID]` for each group |
| Can't run commands | Must be global admin in private chat with bot |

## 💡 Pro Tips

1. **No range = Accept all** (default behavior)
2. **Ranges are inclusive** (min ≤ amount ≤ max)
3. **Changes apply instantly** (no restart needed)
4. **Visual coverage map** helps identify gaps
5. **Test with different amounts** to verify setup

## 📝 Example Commands Flow
```bash
# 1. Check what you have
/listgroupb

# 2. Set up ranges
/setgroupbrange -1001234567890 20 999
/setgroupbrange -1009876543210 1000 5000

# 3. Verify coverage
/listgroupbranges

# 4. Test in Group A
Send: "500"    → Goes to first Group B
Send: "1500"   → Goes to second Group B
Send: "10000"  → Not forwarded (out of range)
```

---
✨ **That's it! The feature is ready to use. Just configure your ranges!**
