# 🧪 Complete Testing Guide for Range-Based Triggers

## 📋 Test Preparation Checklist

### ✅ Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### ✅ Step 2: Set Up Bot Token
```bash
# Create .env file with your bot token from @BotFather
echo 'BOT_TOKEN=YOUR_ACTUAL_TOKEN_HERE' > .env
```

### ✅ Step 3: Run Pre-Test Check
```bash
python3 pre_test_check.py
```

## 🚀 Running the Test

### 1️⃣ Start the Bot
```bash
python3 bot.py
```
**Expected Output:**
```
2024-XX-XX INFO: Bot started successfully
2024-XX-XX INFO: Current state: Groups A: 0, Groups B: 0
```

### 2️⃣ Set Up Test Groups

#### Create Test Groups in Telegram:
1. Create **Group A** (for sending amounts)
2. Create **Group B1** (will handle 100-300)
3. Create **Group B2** (will handle 500-800)
4. Add your bot to all groups as admin

#### Configure Groups:
- **In Group A:** Send `设置群聊A`
  - Bot responds: "✅ 群组已设置为群聊A"
- **In Group B1:** Send `设置群聊B`
  - Bot responds: "✅ 群组已设置为群聊B"
- **In Group B2:** Send `设置群聊B`
  - Bot responds: "✅ 群组已设置为群聊B"

### 3️⃣ Configure Ranges (Private Chat with Bot)

First, get the Group IDs:
```
/listgroupb
```

Then set ranges:
```
/setgroupbrange [GROUP_B1_ID] 100 300
/setgroupbrange [GROUP_B2_ID] 500 800
```

Verify configuration:
```
/listgroupbranges
```

**Expected Visual Output:**
```
🎯 GROUP B RANGE COVERAGE MAP
━━━━━━━━━━━━━━━━━━━━━━━━━
AMOUNT SPECTRUM (20-5000)
20 ──────────────────────── 5000
   ████                          (100-300)
            ████                 (500-800)

⚠️ UNCOVERED GAPS:
• 20 - 99 (no Group B will receive)
• 301 - 499 (no Group B will receive)
• 801 - 5000 (no Group B will receive)
```

## 🎯 Test Execution

### Test Cases in Group A

Send these messages one by one in Group A and observe:

| Test | Send | Expected Result | Bot Log Message |
|------|------|----------------|-----------------|
| 1 | `50` | 🤫 **SILENT** - No forward | "No Group B chats can handle amount 50. Remaining completely silent." |
| 2 | `150` | ✅ Forward to Group B1 | "Forwarding to Group B - amount: 150" |
| 3 | `250` | ✅ Forward to Group B1 | "Forwarding to Group B - amount: 250" |
| 4 | `400` | 🤫 **SILENT** - No forward | "No Group B chats can handle amount 400. Remaining completely silent." |
| 5 | `600` | ✅ Forward to Group B2 | "Forwarding to Group B - amount: 600" |
| 6 | `900` | 🤫 **SILENT** - No forward | "No Group B chats can handle amount 900. Remaining completely silent." |

## 📊 Verification Points

### For SILENT Cases (50, 400, 900):
- [ ] No message appears in ANY Group B
- [ ] No error message in Group A
- [ ] Bot console shows "Remaining completely silent"
- [ ] Image returns to queue (check logs)

### For FORWARDED Cases (150, 250, 600):
- [ ] Message appears in correct Group B
- [ ] Amount 150, 250 → Group B1
- [ ] Amount 600 → Group B2
- [ ] Bot console shows "Forwarding to Group B"

## 🔍 What the Console Logs Show

### Successful Forward (In Range):
```
2024-XX-XX INFO: Group B IDs that can handle amount 150: [-1002222222222]
2024-XX-XX INFO: Selected Group B -1002222222222 from valid options
2024-XX-XX INFO: Forwarding to Group B - img_id: XXX, amount: 150, number: XXX
2024-XX-XX INFO: Message forwarded to Group B with message_id: XXX
```

### Silent Behavior (Out of Range):
```
2024-XX-XX INFO: Group B IDs that can handle amount 400: []
2024-XX-XX INFO: No Group B chats can handle amount 400. Remaining completely silent.
2024-XX-XX INFO: Image XXX status set to: open
```

## 🎭 Live Test Demo

### Terminal Window 1 (Bot):
```bash
$ python3 bot.py
2024-XX-XX INFO: Bot started successfully
2024-XX-XX INFO: Loaded 1 Group A IDs from file
2024-XX-XX INFO: Loaded 2 Group B IDs from file
2024-XX-XX INFO: Loaded Group B amount ranges from file: {-1002222222222: {'min': 100, 'max': 300}, -1003333333333: {'min': 500, 'max': 800}}
```

### Telegram Group A:
```
You: 50
[No response - SILENT ✅]

You: 150
[Bot forwards to Group B1 ✅]

You: 400
[No response - SILENT ✅]

You: 600
[Bot forwards to Group B2 ✅]
```

### Telegram Group B1:
```
[Receives message when amount is 150, 250]
Bot: 💰 金额：150
     🔢 群：XXX
```

### Telegram Group B2:
```
[Receives message when amount is 600]
Bot: 💰 金额：600
     🔢 群：XXX
```

## ✨ Test Success Criteria

### ✅ PASS Conditions:
1. **Silent for out-of-range**: No forwarding for 50, 400, 900
2. **Correct routing**: 150→B1, 600→B2
3. **No user errors**: No error messages in Group A
4. **Proper logging**: Console shows correct behavior

### ❌ FAIL Conditions:
1. Out-of-range amounts get forwarded
2. Error messages appear in Group A
3. Wrong Group B receives message
4. Bot crashes or becomes unresponsive

## 🔧 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| Bot not starting | Check BOT_TOKEN in .env |
| Groups not recognized | Re-run setup commands |
| All amounts forwarded | Check ranges with `/listgroupbranges` |
| Nothing forwarded | Verify Group B IDs are correct |

## 📝 Test Report Template

```
TEST REPORT - Range-Based Triggers
Date: _____________
Tester: ___________

Setup:
[ ] Bot started successfully
[ ] Groups configured (A, B1, B2)
[ ] Ranges set (B1: 100-300, B2: 500-800)

Test Results:
[ ] Amount 50: SILENT ✅/❌
[ ] Amount 150: → Group B1 ✅/❌
[ ] Amount 250: → Group B1 ✅/❌
[ ] Amount 400: SILENT ✅/❌
[ ] Amount 600: → Group B2 ✅/❌
[ ] Amount 900: SILENT ✅/❌

Overall: PASS / FAIL

Notes: ___________________
```

## 🎉 Conclusion

If all tests pass, your range-based trigger system is working perfectly! The bot:
- ✅ Forwards messages only when amounts are within configured ranges
- ✅ Stays completely silent for out-of-range amounts
- ✅ Routes to correct Group B based on ranges
- ✅ Provides no error feedback to users (professional silent operation)
