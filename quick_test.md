# 🧪 Quick Test Guide for Range-Based Triggers

## ⚡ Quick Test Steps

### Step 1: Check Bot Token
```bash
# Create .env file if not exists
echo "BOT_TOKEN=YOUR_BOT_TOKEN_HERE" > .env
```

### Step 2: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 3: Start the Bot
```bash
python3 bot.py
```

### Step 4: Initial Setup (One Time)

#### A. Set Up Groups
1. **Add bot to your test groups** (must be admin)
2. **In Group A:** Send `设置群聊A`
3. **In Group B1:** Send `设置群聊B`
4. **In Group B2:** Send `设置群聊B` (if you have multiple)

#### B. Configure Ranges (Private Chat with Bot)
```
/setgroupbrange [GROUP_B1_ID] 100 300
/setgroupbrange [GROUP_B2_ID] 500 800
```

#### C. Verify Setup
```
/listgroupb         # Shows all Group B with ranges
/listgroupbranges   # Shows visual coverage map
```

## 🎯 Test Scenarios

### Test Matrix
| Amount | Expected Result | Reason |
|--------|----------------|---------|
| **50** | 🤫 SILENT | Below all ranges (< 100) |
| **150** | ✅ Forward to B1 | Within B1 range (100-300) |
| **250** | ✅ Forward to B1 | Within B1 range (100-300) |
| **400** | 🤫 SILENT | In gap (301-499) |
| **600** | ✅ Forward to B2 | Within B2 range (500-800) |
| **900** | 🤫 SILENT | Above all ranges (> 800) |

### How to Test
In **Group A**, send these messages one by one:
```
50
150
250
400
600
900
```

## ✅ What to Look For

### For SILENT Cases (50, 400, 900):
- ❌ No message in any Group B
- ❌ No error message in Group A
- ✅ Bot console shows: "No Group B chats can handle amount X. Remaining silent."

### For FORWARDED Cases (150, 250, 600):
- ✅ Message appears in appropriate Group B
- ✅ Bot console shows: "Forwarding to Group B"

## 📊 Check Bot Logs

Watch the bot console for these key messages:

**Successful forward:**
```
Group B IDs that can handle amount 150: [-1002222222222]
Forwarding to Group B - img_id: XXX, amount: 150
```

**Silent behavior (out of range):**
```
No Group B chats can handle amount 400. Remaining completely silent.
```

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot not responding | Check BOT_TOKEN in .env file |
| Groups not recognized | Run setup commands in each group |
| Ranges not working | Check with `/listgroupbranges` |
| All messages forwarded | Remove ranges: `/removegroupbrange [ID]` |

## 📝 Example Test Run

```bash
# Terminal 1: Start bot
python3 bot.py

# Terminal 2: Watch logs
tail -f bot.log

# In Telegram:
# 1. Private chat: /listgroupbranges
# 2. Group A: Send "150"  → Check Group B1 receives
# 3. Group A: Send "400"  → Check silence (no forward)
# 4. Group A: Send "600"  → Check Group B2 receives
# 5. Group A: Send "1000" → Check silence (no forward)
```

## ✨ Success Indicators

✅ **Test Passed If:**
1. In-range amounts forward correctly
2. Out-of-range amounts stay silent
3. No error messages to users
4. Logs show proper behavior

❌ **Test Failed If:**
1. Out-of-range amounts get forwarded
2. Error messages appear in Group A
3. Wrong Group B receives message
4. Bot crashes or stops responding
