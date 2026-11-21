# EPG – עידן פלוס / Israeli guide

עודכן: 21.11.2026

## מטרה
להוסיף לוח תוכניות אמיתי לערוצים **עכשיו 14**, **ערוץ 16**, **כלכלה 10** ב-SS IPTV, בלי לשנות שידורים, לוגואים או EPG שכבר עובד.

## סטטוס
- מזהי `tvg-id` ו-`tvg-name` הוספו לשלושת הערוצים, אך המשתמש דיווח שב-SS IPTV לא הופיע לוח. **לא פתרון בפני עצמו.**
- סקריפט `scripts/build_epg.py` מחפש תוכניות אמיתיות במקורות XMLTV ציבוריים, ומפרסם `epg/idan-plus.xml` רק אם מתקבלות תוכניות בתוקף.
- קובץ `.github/workflows/build-epg.yml` מוגדר לרוץ כל 6 שעות ולשמור את המדריך ב-GitHub.
- **לא להוסיף `x-tvg-url` לרשימת ה-M3U לפני שקובץ `epg/idan-plus.xml` נוצר, מכיל תוכניות אמיתיות לערוצים הנדרשים, זמין ציבורית, ונבדק ב-SS IPTV.**
- אם למקור אין תוכניות לערוץ 16, הוא יישאר ללא EPG. אין להמציא שמות או שעות.

## בדיקת הקובץ לאחר ריצה
- [הפעלת Workflow במאגר](https://github.com/doronvodka-del/-Israel-Live-TV-/actions/workflows/build-epg.yml)
- [XMLTV (כשהקובץ נוצר)](https://raw.githubusercontent.com/doronvodka-del/-Israel-Live-TV-/main/epg/idan-plus.xml)
- [דוח כיסוי (כשהקובץ נוצר)](https://raw.githubusercontent.com/doronvodka-del/-Israel-Live-TV-/main/epg/status.json)

## בדיקות חובה טרם חיבור
1. נוצר קובץ XMLTV תקין ובו לפחות תוכנית אחת שתאריך ההתחלה והסיום שלה תקף לעכשיו.
2. `programme channel="Now14.il@SD"` ו/או `programme channel="EconomyChannel.il@SD"` קיימים בפועל. נוכחות `<channel>` בלבד לא מספיקה.
3. אין שימוש בנתוני לוח ישנים.
4. בטלוויזיה רענון SS IPTV מראה את התוכניות בשלושת הערוצים, והערוצים הקיימים לא נפגעו.
