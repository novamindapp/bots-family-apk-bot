# All Apk Downloader — @BotsFamilyApkBot (v1)

Bot for the channel **Our Bots Family | Наша семья ботов**
— https://t.me/BotsFamilyOfficial

## What it does (v1 ONLY)

1. User sends an app name (e.g. `WhatsApp`, `Facebook Lite`).
2. Bot searches **APKPure** (`https://apkpure.com/search?q=...`, verified
   live 2026-11-19) and shows the top 5 results with name + package.
3. User picks one, taps 'Download APK', and the bot downloads the APK and sends the FILE in the chat (up to 48 MB; bigger APKs get the download link instead) + the APKPure page.
4. **Before any download works, the user MUST join @BotsFamilyOfficial.**
   Checked on `/start`, on every search and on every pick. If not joined,
   the bot shows a Join button + an "I joined, check again" button, and
   keeps the pending search/pick so the download continues after joining.

No YouTube downloads, no YouTube search, no AI chat in v1 — those are later.

The APK comes from APKPure, not from the Play Store: the Play Store
does not hand out APK files directly.

## Files

| File | What it is |
|---|---|
| `bot.py` | The bot: forced-join check, search, pick, download link |
| `apkpure.py` | APKPure search + app-page parsing (no token, testable offline) |
| `test_apkpure.py` | Offline parser tests (fixture HTML, no network) |
| `requirements.txt` | python-telegram-bot 21.4, requests, beautifulsoup4, python-dotenv |
| `.env.example` | Copy to `.env`, fill in `BOT_TOKEN` |
| `.gitignore` | Keeps `.env` out of git |

## ⚠️ The bot MUST be an Admin of the channel

Add **@BotsFamilyApkBot as an Admin** of @BotsFamilyOfficial first.
Otherwise Telegram will not reliably tell the bot who joined, and the
membership check fails open (the bot lets the download through).
This is the same rule as the old TikTok/Instagram bot.

## Deploy on FadeHost (Free 256 MB) — steps the owner does himself

The owner holds the token. **Never paste the token in a chat.**

1. In Telegram, open @BotFather → `/newbot` is already done:
   bot is **@BotsFamilyApkBot**, name "All Apk Downloader".
   Copy the token BotFather gave you (keep it secret).
2. In Telegram, open the channel **@BotsFamilyOfficial** → Admins →
   add **@BotsFamilyApkBot** as Admin.
3. On FadeHost, create a new app / service from this folder
   (upload the files, or push them to GitHub first and connect the repo).
4. Install command: `pip install -r requirements.txt`
5. Start command: `python bot.py`
6. Set the environment variable in FadeHost (NOT in a file):
   - `BOT_TOKEN` = the token from BotFather
   - `FORCE_CHANNEL` = `@BotsFamilyOfficial`
7. Start / redeploy the service. You should see
   `✅ Bot is running...` in the logs.
8. Test from **another account that has NOT joined the channel**:
   send `/start` to @BotsFamilyApkBot → it must ask you to join first.
   Then join the channel, tap "I joined, check again", send `Facebook Lite`
   → pick the app → tap "Download APK".

## Test locally (no token needed for the parser test)

```bash
pip install -r requirements.txt
python -m py_compile bot.py apkpure.py   # syntax check
python test_apkpure.py                   # offline parser tests
```

To run the real bot locally:

```bash
cp .env.example .env   # then put your BOT_TOKEN in .env
python bot.py
```

## Known limits (v1)

- The bot sends a **download link** (APKPure download page), not the APK
  file itself. Many APKs are over Telegram's 50 MB bot file limit, and
  APKPure's file download can be blocked from some hosts. Sending the
  file directly is a possible v1.1 step, after testing the download
  from the FadeHost server.
- APKPure has no public search API; the bot parses the public search
  page. If APKPure changes its page layout, search returns no results
  and the bot says so instead of crashing.
- The download URL pattern is `https://apkpure.com/<slug>/<package>/download`
  (the standard "Download APK" button on the app page). It was not
  live-tested end-to-end from FadeHost yet — see "Untested" below.

## شرح بالدارجة — شنو خاصك دير نتا

1. التوكن عندك من BotFather — **ما تصيفطوش في الشات**، حطو في FadeHost
   في Environment Variables.
2. زيد البوت **أدمن** في قناة @BotsFamilyOfficial، بلا هادشي التحقق
   من الاشتراك ما غاديش يخدم مزيان.
3. في FadeHost: ثبت المكتبات (`pip install -r requirements.txt`)،
   وشغل البوت (`python bot.py`)، وزيد `BOT_TOKEN` و `FORCE_CHANNEL`.
4. جرب من حساب آخر ما مشتركش في القناة: البوت خاصو يطلب منك
   تشترك أولا، ومن بعد يعطيك التحميل.
