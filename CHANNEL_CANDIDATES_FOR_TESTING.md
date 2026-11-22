# היקף מחקר מעודכן – 22.11.2026

**הוראה עדכנית ומחייבת של בעל המאגר:** לחפש ולהוסיף מועמדים **רק מערוצי HOT, STING TV / STING+, FreeTV, yes, NEXT TV, סלקום TV+, Disney+ ישראל ו־HBO Max ישראל**. שפות מותרות: **עברית ואנגלית בלבד**. יש לאמת שהערוץ מופיע באחד משמונת השירותים. ההרחבה הקודמת לשידורים קהילתיים שאינם בחבילות אלה ולשפות אחרות בוטלה בבקשת המשתמש האחרונה.

**מקורות גילוי:** המשתמש אישר במפורש גם קישורים לא רשמיים ופיראטיים שפורסמו בפומבי, ובכלל זה חבילות GitHub. רשימת GitHub היא מקור למציאת כתובת; היא אינה הוכחה לשם הערוץ, לשפה, לניגון או להרשאת הפצה. אין להחליף ערוץ בגרסת FAST אחרת רק מפני שהמותג דומה.

**כללי עבודה שאושרו:** להוסיף מועמדים ל־**חדשים לבדיקה**; רק לאחר אישור ניגון של דורון ב־LG/SS IPTV להעביר לקטגוריית תוכן. להימנע מכפילויות וגרסאות איכות של אותו ערוץ, ולשמר ערוצים קיימים. אין לשמור פרטי כניסה אישיים, JWT של מנוי או מפתחות DRM. מזהה אטום בכתובת ציבורית לבדו אינו מוכיח שמדובר בפרטי חשבון.

**מקורות רשמיים לאימות שיוך לחבילה:**

- HOT: https://www.hot.net.il/heb/tv/channels/hotchannels/
- yes / STING+: https://www.yes.co.il/content/channels-index/ ; https://www.yes.co.il/content/stingplus/
- FreeTV: https://freetv.tv/tvchannels
- סלקום TV+: https://cellcom.co.il/production/Private/cellcomtv/channels/
- NEXT TV: לבדוק את רשימת NEXT עצמאית; אין להניח שכל ערוץ HOT כלול.
- Disney+ ישראל: https://www.disneyplus.com/en-il
- HBO Max ישראל: https://www.hbomax.com/il/he

**עדיפות מחקר:** סרטים וסדרות בעברית או באנגלית: HOT Cinema 2–5, HOT Comedy/REAL, yes TV Drama/Action/Comedy, yes Movies Drama/Comedy/Kids, ערוצי הסרטים והסדרות של סלקום, ותוספות ייחודיות של FreeTV. תכני Disney+/HBO Max צריכים להיות מזוהים עם השירות בישראל; שם ערוץ HBO או Disney ממדינה אחרת אינו מספיק. דף VOD אינו כתובת שידור חי.

## סבב ממוקד לאחר תיקון ההיקף – 22.11.2026

נמצאו שלושה קישורי שידור חדשים לערוצים באנגלית הנכללים ב־HOT. שלושתם נוספו לקבוצת **חדשים לבדיקה**, ללא כפל עם CNN Fast או FOX Live Now. סך הרשומות כעת **290**, ב־21 קבוצות. אין עדיין אישור ניגון ב־LG/SS IPTV. [שינוי הפלייליסט](https://github.com/doronvodka-del/-Israel-Live-TV-/commit/9b81bb0af0d4a482c864cdc154c4ed77e32d6ae7).

| ערוץ | שיוך לחבילה | בדיקה טכנית | הערה |
|---|---|---|---|
| CNN International Europe | HOT, אפיק 205 | master, מדיה ומקטע MPEG-TS החזירו 200; H.264 1280×720, AAC עם שפה eng | תמונת CNN Newsroom חי עם שעון CET אומתה; master מציע גם 1080p |
| FOX News Channel | HOT, אפיק 202 | master, מדיה ומקטע החזירו 200; H.264 768×432, AAC בבדיקה השנייה | בדיקה ראשונה ללא אודיו; יש לשים לב ליציבות הקול. מיתוג FOX News חי אומת |
| Fox Business Network | HOT, אפיק 206 | master, מדיה ומקטע החזירו 200; H.264 768×432 ו־AAC | בזמן הבדיקה תוכנית פרסומית; התוכנית תאמה לדגימה מהתצוגה הרשמית, אך לא נראה לוגו ערוץ |

מקור שלוש הכתובות: [iptv-org/iptv, streams/us.m3u](https://github.com/iptv-org/iptv/blob/master/streams/us.m3u), קובץ SHA `215833e367019644ab880a054d72dbd437ae5b11`. אין במניפסטי המדיה שנבדקו EXT-X-KEY או ENDLIST. הלוגואים נלקחו מ־iptv-org/database/data/logos.csv ונבדקו כקובצי PNG נגישים.

כתובות master שנמצאו:

- CNN International: https://d3bp6dwmpbdajl.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ury0meh5m4nzm/index.m3u8
- FOX News: https://tvsen6.aynaott.com/foxnews/index.m3u8
- Fox Business: https://tvsen6.aynaott.com/foxbusiness/index.m3u8

### מקורות נוספים שנמצאו אך לא אומתו להפעלה

- **HOT Cinema 1–4, HOT8, HOT Comedy:** ב־[adir92781/ADIR, EVERYworld.m3u8](https://github.com/adir92781/ADIR/blob/72db56ae3493a9c7e01c65f3d87abd9de04d2d12/EVERYworld.m3u8) וב־[Mogo1346/mogostream](https://github.com/Mogo1346/mogostream/blob/main/channels.html) נמצאו כתובות str2.iptvhd.ru. הכתובות המדויקות Gold/action/fun/drama/channel8/HOTComedy החזירו 403. בגוף תגובת Gold הודעת הגנת שרת השידור. אין אימות HLS, שפה או מקטע. אותן בדיקות ב־Channel8 וב־HOTCOMEDY באותיות שונות החזירו 404.
- **ערוצי yes סרטים, סדרות ודוקו:** [asheramram1-cloud/Playlist-1](https://github.com/asheramram1-cloud/Playlist-1/blob/main/playlist1.m3u) ו־Mogo מפרסמים תשעה קישורים שונים, לרבות חלופה ל־yes Movies Action הקיים. דומיין הממסר נחסם בסביבת הבדיקה עם `x-openai-site-blocked: true`; אין להסיק מכך שהקישורים מתים.
- **yes Movies Kids/Action/Comedy:** שלוש כתובות zekonew.newkso.ru שפורסמו ב־[rotemgrim/rooster-x, streams-old2.m3u](https://github.com/rotemgrim/rooster-x/blob/master/streams-old2.m3u) נחסמו אף הן בסביבת הבדיקה. לא נעשו ניסיונות עקיפה.
- חלופות yes TV Drama ממקורות אחרים החזירו 401/404/503. המקורות הנוספים של סלקום לא סיפקו בסבב זה תוספת חדשה שאומתה.
- Discovery MEA החזיר וידאו וקול באנגלית אך נראו כתוביות ערביות צרובות, ולא אומתה גרסת ישראל; אינו נכלל בתוספת.
- לא נמצאה בסבב זה תוספת חדשה שאומתה עבור FreeTV, NEXT, Disney+ ישראל או HBO Max ישראל. ערוצי FreeTV המקוריים המרכזיים כבר מופיעים בפלייליסט.

## היסטוריית מחקר — ההוראה העדכנית בראש הקובץ גוברת

הסעיפים הבאים מתעדים סבבים קודמים, כולל ההיקף הרחב שהיה בתוקף אז. אין להשתמש בהם כהיתר להרחיב את החיפוש הנוכחי.

## שידורים קהילתיים וחבילות GitHub – 22.11.2026

**תוצאה תפעולית:** נוספו **4 רשומות** לקבוצת **חדשים לבדיקה**: רדיו סול בווידאו, JBS, BFM TV ו־Canal 24 Horas. סך הרשומות **287**, ב־21 קבוצות. בנוסף תוקנו השם והערת המקור של ILTV בצרפת. כל כתובות השידור והלוגואים של 283 הרשומות הקיימות נשמרו. [שינוי הפלייליסט](https://github.com/doronvodka-del/-Israel-Live-TV-/commit/f2699f7133da74f0bf18d4e5da497dddc8e3bc65).

### הערוצים שנוספו

| ערוץ | התאמה להיקף | כתובת ה־master שנשמרה |
|---|---|---|
| רדיו סול — וידאו | רדיו חברתי ישראלי עם שידור אולפן מצולם | https://cdna.streamgates.net/RadioSol/LiveVideo/playlist.m3u8 |
| JBS — טלוויזיה יהודית באנגלית | ערוץ קהילתי יהודי מארה״ב; לא נטען שהוא חלק מחבילת HOT/yes | https://rpn3.tulixcdn.com/jbstv-srt/srt-push/jbstv/playlist.m3u8 |
| BFM TV — חדשות בצרפתית | מופיע ב־HOT באפיק 142 | https://live-cdn-stream-euw1.bfmtv.bct.nextradiotv.com/master.m3u8 |
| Canal 24 Horas — חדשות בספרדית | מופיע ב־HOT באפיק 158 | https://rtvelivestream.rtve.es/rtvesec/24h/24h_main_dvr.m3u8 |

**מקור ובדיקה לכל ערוץ:**

- **רדיו סול:** כתובת הווידאו נמצאה ב[חבילת junguler](https://github.com/junguler/m3u-radio-music-playlists/blob/main/keep_one/israel.m3u) ואומתה בתוך video/src וב־radiosolConfig.liveVideo של [דף השידור הרשמי](https://radiosol.co.il/live). [דף האודות](https://radiosol.co.il/aboutradiosol) מתאר תחנה חברתית עם פעילות קהילתית, ראיונות ומוזיקה. Master ומניפסט מדיה: HTTP 200; מקטע: HTTP 206 בבקשת Range; H.264 Baseline/AAC, ‏720p50, ללא KEY או ENDLIST במניפסט שנבדק. הלוגו הרשמי PNG נבדק.
- **JBS:** הגילוי התחיל ב[חבילת iptv-org האמריקאית](https://github.com/iptv-org/iptv/blob/master/streams/us.m3u). [דף הצפייה הרשמי](https://jbstv.org/watch-live) מטמיע את [נגן Tulix הציבורי](https://jbsdvr.tulix.tv/player/jbstv.php), שמפרסם את כתובת tulixcdn שנשמרה. [תיאור הערוץ](https://jbstv.org/faq) מאשר שידור חופשי ללא מטרת רווח בנושאי קהילה, ישראל, תרבות וסרטים, באנגלית או עם כתוביות באנגלית. Master ומדיה: HTTP 200; מקטע: HTTP 206, חתימת MPEG-TS, ‏4,096 בתים; H.264/AAC, ‏720p59.94, ללא KEY או ENDLIST. הלוגו מתוך הנגן הרשמי הוא PNG ‏852×480 והחזיר HTTP 200. JBS שונה מ־JLTV שכבר נמצא ברשימה.
- **BFM TV:** נמצא ב[חבילת LITUATUI/M3UPT](https://github.com/LITUATUI/M3UPT/blob/main/M3U/M3UPT.m3u); אותו URL אומת ב־data-video-url ב[דף השידור הרשמי](https://www.bfmtv.com/en-direct/). [HOT](https://www.hot.net.il/heb/tv/channels/hotchannels/) מפרסמת את הערוץ באפיק 142. Master, מדיה ומקטע MPEG-TS: HTTP 200; ‏HLS v3/H.264/AAC, ללא KEY או ENDLIST. הלוגו הרשמי PNG החזיר HTTP 200.
- **Canal 24 Horas:** נמצא ב־LITUATUI/M3UPT וב־iptv-org/streams/es.m3u. [דף RTVE הרשמי](https://www.rtve.es/play/videos/directo/24h/) מפרסם נגן חי עם idGolumi=rtvesec/24h/24h_main_, ‏hasDRM=false ו־requireLogged=false. מדובר בערוץ הראשי; [HOT](https://www.hot.net.il/heb/tv/channels/foreignchannels/) מפרסמת אפיק 158. Master, מדיה ומקטע MPEG-TS: HTTP 200; ‏H.264/AAC, ללא KEY או ENDLIST. הלוגו נלקח מאתר HOT.

**משמעות הבדיקה:** התקבלו פלייליסטים חיים ומקטעי מדיה מסביבת הבדיקה. לא בוצע ניגון חזותי מלא ולא נבדקה טלוויזיית LG/SS IPTV בישראל. ארבע הרשומות נשארות בקבוצת **חדשים לבדיקה**. נשמרו כתובות master בלבד, ללא פרמטרי סשן של מניפסטים פנימיים.

### תיקון זיהוי קיים: ILTV

השם **ILTV ישראל בצרפתית - בדיקה** היה שגוי. הערוץ הוא ILTV של אגד הערים **Hénin-Carvin בצרפת**, כפי שמתואר ב[אתר הערוץ](https://www.iltv.fr/presentation/) וב[אתר הרשות המקומית](https://www.agglo-henincarvin.fr/site-internet-diltv-en-maintenance). דף השידור הרשמי מטמיע נגן Creacast עם su=iltv; נגן זה מפרסם **בדיוק את כתובת ה־HLS הקיימת ברשימה**. השם תוקן ל־**ILTV - טלוויזיה מקומית בצרפת - בדיקה**, יחד עם הערת המקור. הכתובת, הלוגו והקבוצה נשמרו.

### חבילות נוספות שנבדקו — למניעת סריקה חוזרת

| מקור | תוצאה |
|---|---|
| xpwmaster/IPTV-IL/IL-TiviMate-EPG.m3u | 142 רשומות דרך אותו ממסר עם קוד גישה, כולל ערוץ 98; לא הועתקו כתובות ההרשאה. |
| plymbnc/IPTV-Israel/Israel.m3u | 40 רשומות; הערוצים או גרסאותיהם כבר נמצאים. Kan Kids הוא כאן חינוכית. |
| BitBOY21/IsraTV-app-android-Israel-IPTV/app/src/main/assets/channels.json | 6 ערוצי ברודקאסט קיימים. |
| ak4153/israeli-iptv/channels.json | חפיפה למקורות Fishenzon; אין תוספת נפרדת. |
| AvielNachmias2/iptv-playlist/israel_and_us.m3u | 29 הרשומות הישראליות כבר קיימות; החלק האמריקאי אינו הוכחת שייכות לחבילה ישראלית. |
| Fishenzon/repo/plugin.video.idanplus/channels.json | רוב הרשומות כפולות; 891FM וידאו לא אומת, האח הגדול החזיר 503. קבלה ברוסית עברה HTTP/מקטע, אך תועדה כגרסת שפה נוספת ולא נספרה כערוץ חדש. |
| szaionz/zipzup/app/channels.json | ערוצי ברודקאסט קיימים ותחנות רדיו; לא אותר ערוץ טלוויזיה חדש. |
| Mudales/stremio-tv-il/channels.json | מיפוי שמות ומזהים של ערוצים קיימים; אין מקור חדש עצמאי. |
| Free-TV/IPTV/lists/israel.md | מקורות לערוצי ברודקאסט שכבר קיימים. |
| shayanline/iptv-iran/playlists/iran.m3u | Israel Pars TV הוא שידור לקהילה האיראנית בישראל לפי האתר הרשמי, אך כתובת ה־master החזירה 403 בסביבת הבדיקה. לא נוסף; אין בכך הוכחה שאינו נגיש בישראל. |

**מועמדים שטרם הבשילו:** ערוץ 98 והמגזינים הקהילתיים של נתניה/כפר סבא/חדרה — נמצא מידע על שידורים מתוזמנים וארכיוני YouTube, לא HLS עצמאי של ערוץ רציף. הרדיו החברתי הראשון ו־891FM — קיים דף צפייה, אך לא אותר HLS וידאו שניתן לאמת. ARTE החזיר 403; RTVI לא זוהה עם מקור ציבורי מאומת. אין תוספת חדשה בסבב הזה לערוצי הסרטים והסדרות הייעודיים של HOT/yes/סלקום.

## תוספת ממקורות רשמיים – 22.11.2026

**תוצאה:** נוספו שני ערוצים שאינם מופיעים ברשימה הקודמת לקבוצת **חדשים לבדיקה**. סך הרשומות עלה מ־281 ל־283; מספר הקבוצות נשאר 21. 281 הרשומות הקיימות, כתובותיהן, שמותיהן והלוגואים שלהן נשמרו ללא שינוי. [שינוי הפלייליסט](https://github.com/doronvodka-del/-Israel-Live-TV-/commit/2d5d0694dc6e6a6524cf0429cb98cfd2b332fb58).

### METV — גרסת האינטרנט הרשמית

- **שיוך לשירות המבוקש:** METV מופיע באפיק 150 ב[אינדקס HOT הרשמי](https://www.hot.net.il/heb/tv/channels/hotchannels/).
- **מקור:** [הנגן הציבורי באתר METV](https://www.metv.org/livestream/); קטלוג הנגן המוטמע מזהה את השידור בשם METV Digital.
- **כתובת קבועה שנוספה:** https://content.uplynk.com/channel/9d35b73c264946d5945db6cdff26336e.m3u8
- **בדיקה:** master ואיכות החזירו HTTP 200; מניפסט חי ללא ENDLIST; בקשת Range למקטע החזירה HTTP 206 ו־1,024 בתים. המניפסט מציע H.264 ו־HE-AAC. יש HLS AES-128 בנגן הציבורי; לא בוצע פענוח או ניגון חזותי בבדיקה.
- **מגבלה:** האתר הרשמי מזהיר שחלק מתוכניות שידור הטלוויזיה אינן כלולות בגרסת האינטרנט בשל זכויות. לכן השם ברשימה מציין במפורש **גרסת אינטרנט**. זהו Middle East Television, ולא MeTV האמריקאי.
- **סטטוס:** מקור ישיר שנגיש מסביבת הבדיקה; טרם נבדק בישראל או ב־LG/SS IPTV. נשמרה רק כתובת ה־master, ללא כתובות איכות זמניות.

### Current Time — חדשות ודוקו ברוסית

- **שיוך לשירות המבוקש:** [רשימת המפיצים הרשמית של הערוץ](https://www.currenttime.tv/partners) כוללת **yes בישראל**. אין להסיק מכך זמינות ב־STING.
- **מקור:** הכתובת פורסמה בתגית source ובמטא־נתוני [דף השידור הרשמי](https://www.currenttime.tv/live).
- **כתובת קבועה שנוספה:** https://rferl-ingest.akamaized.net/hls/live/2121657/tvmc05/playlist.m3u8
- **בדיקה:** master ואיכות 1080p החזירו HTTP 200; רצף המקטעים התקדם בבדיקה חוזרת מ־1118379 ל־1118382; אין ENDLIST. מקטע וידאו החזיר HTTP 200, מסוג video/MP2T, ונקראו 4,096 בתים עם חתימת MPEG-TS. HLS v3, H.264/AAC, ללא EXT-X-KEY במניפסט שנבדק.
- **לוגו:** קובץ PNG מהאתר הרשמי הוחזר ב־HTTP 200.
- **סטטוס:** שידור חי נגיש מסביבת הבדיקה; טרם נבדק בישראל או ב־LG/SS IPTV. הכתובת שנוספה אינה כוללת אסימון גישה או פרטי חשבון.

### כיוונים שנבדקו ולא נוספו בסבב הזה

- **ערוץ 98:** נמצא באינדקס HOT; לא אותרה כתובת HLS ציבורית רציפה של הערוץ המלא. כתבות ורצועות של מפיקים אינן תחליף לשידור המלא.
- **FreeTV:** לא אותר ערוץ נוסף להוספה אחרי השוואה לרשימה הפעילה. כתובות Mako ללא חתימה לנינג'ה, חתונה ממבט ראשון והכוכב הבא, שנמצאו ב־k33n26/iptv2, החזירו HTTP 403 מסביבת הבדיקה. זו אינה הוכחה לחסימה בישראל. [הדף הרשמי של FreeTV מוזיקה](https://freetv.tv/tvchannels/free-tv-music-channel) מאשר שתוכני הכוכב הבא כבר כלולים בערוץ המוזיקה הקיים ברשימה.
- **ערוצי הסרטים והסדרות של HOT/yes/סלקום:** לא אותר בסבב זה מקור ישיר חדש מתאים להוספה. רשימות חתומות או ממסרים שנבדקו בעבר לא נספרו כתגלית חדשה.

**כלל סטטוס:** הצלחת בדיקת HTTP ומקטע מדיה אינה אישור ניגון בטלוויזיה. ערוץ חדש יכול להיכנס ל־**חדשים לבדיקה** לפני בדיקת המשתמש; העברה לקבוצת תוכן כערוץ שאושר תיעשה לפי תוצאת בדיקתו.

## מחקר עומק ממוקד – 22.11.2026

**תוצאה תפעולית:** נמצאו ערוצים מתאימים ודאיים בקטלוגי המפעילים, אך **לא אותר בסריקה קישור HLS חדש שניתן לאמת בניגון בישראל מחוץ לאפליקציית המפעיל**. אין לנפח את קובץ ה־M3U בקישורים ששמם נכון אך ניגונם לא נבדק. סך הרשומות ב־M3U בעת מחקר זה: 281. אין שינוי ל־M3U במחקר זה.

### רשימת יעדים חדשה שאומתה לפי קטלוג

**yes / yes+ (מועמדים בעדיפות עליונה לחיפוש קישור):**
- [ ] yes+ LOVE — סרטי רומנטיקה, אפיק 0, השקה 12.03.2026, ללקוחות yes+ בלבד
- [ ] yes+ DARK — מותחנים, אפיק 7, השקה 12.03.2026, ללקוחות yes+ בלבד
- [ ] yes+ CINEMA — קולנוע בינלאומי, אפיק 5 של yes+, הוכרז כבר ב־2024
- [ ] yes+ DIAMONDS — קלאסיקות קולנוע, אפיק 6 של yes+; לוח התוכן הרשמי של yes מתעד שידור ב־05.06.2026
- [ ] במה ישראלית — הופעות מוזיקה, אפיק 201 yes+, השקה ב־2026
- [ ] yes Movies Drama / Comedy ו־yes TV Drama / Action / Comedy — קיימים כאפיקים נפרדים; אין זרם HLS חדש שהניגון שלו אומת
- [ ] ערוץ דרמות יומיות — ב־yes+ וב־STING+; קיים כבר ערוץ בשם זה ממקור FreeTV בפלייליסט, לכן לבדוק תוכן לפני יצירת רשומה שנייה
- [ ] Beautyz — הושק ב־yes, אך מותג זה כבר קיים בפלייליסט

מקור yes הרשמי, עליית LOVE/DARK ב־12.03.2026: https://www.yes.co.il/content/yes-magazine/yesrec_2026-03-12/
מקור yes לארבעה ערוצים נוספים (כולל במה ישראלית): https://www.yes.co.il/content/yes-magazine/new-exciting-channels-feb-26/
מקור yes לתוכני DIAMONDS: https://www.yes.co.il/content/yes-magazine/yesrec_2026-05-28/
מקור הודעת yes ל־CINEMA: https://www.youtube.com/watch?v=efzOiC9zRkA

**HOT / NEXT TV:**
- [ ] HOT Cinema 2, 3, 4, 5; HOT קולנוע ישראלי; HOT REAL; HOT Comedy; HOT בידור
- [ ] NEXT TV — ברשימה באתר הרשמי הישן: HOT Cinema 4 בחבילת הבסיס; ב־MORE ערוצי HOT 8, HOT REAL, HOT Senior ו־HOT Comedy Central. **מסמך NEXT הוא בן כשנה וארבעה חודשים, יש לאמת את ההרכב הנוכחי**.
- קישורי HOT Cinema 1–5, HOT Comedy ו־yes Movies שנמצאו בפלייליסט ציבורי אחר הגיעו מממסר צד שלישי עם נתיבי גישה אטומים; לא אומתו בישראל ואינם מוכיחים זכויות. לא הועתקו למאגר.
- מקור HOT: https://www.hot.net.il/heb/tv/channels/hotchannels/
- מקור NEXT (מסמך ישן): https://www.nexttv.co.il/media/xqzaevbl/channels.pdf
- אתר NEXT: https://campaign.nexttv.co.il/web/newnexttv/v1/index.html

**סלקום TV+:**
- [ ] סלקום Action Movies, Comedy Movies, Drama Movies, Family Movies, סדרות, דוקו, Kids Movies, קולנוע ישראלי
- אתר סלקום הרשמי מאשר אפיקים 1–8 ואפיק 70; יש גם ערוצי פרימיום. מאגר הקהילה il90il90/m3u-tv/cell.m3u מכיל 87 רשומות עם טוקנים חתומים בכתובת Cellcom CDN; לא אומתו כניגון מחוץ לסלקום, ולא הועתקו לפרויקט ציבורי.
- מקור רשמי: https://cellcom.co.il/production/Private/cellcomtv/channels/
- מקור קהילה (למחקר בלבד): https://github.com/il90il90/m3u-tv/blob/main/cell.m3u

**FreeTV:**
- האתר הרשמי מציג מעל 60 ערוצים, כולל 10 ערוצי סרטים. בסריקה של הרשימה הפעילה אותרו כבר רוב מותגי FreeTV, ואין להוסיף אותם בכפילויות.
- [ ] להשלים בדיקה ל־נינג'ה, חתונה ממבט ראשון, ערוץ דוק והכוכב הבא — זוהו במדריך EPG ציבורי אך לא זוהו בקטלוג הראשי כערוצים פעילים; קישורים חתומים שנמצאו ברשת פגו, ואין כתובת HLS קבועה מוכחת.
- מקור: https://freetv.tv/tvchannels

**Disney+ ישראל / HBO Max ישראל:**
- Disney+ פועל בעיקר כשירות VOD, ללא חבילת ערוצים ליניארית ל־M3U; ערוץ Disney Channel אצל ספק מקומי אינו Disney+.
- HBO Max הושק בישראל 13.01.2026, כולל ספריית VOD וספורט חי באפליקציה, אך **לא אותר ערוץ HBO Max ישראל עם כתובת M3U8 קבועה ופתוחה**. גם אם מתקיים משחק חי באפליקציה, זו אינה רשומת IPTV קבועה.
- מקור השקה רשמי: https://press.wbd.com/na/media-release/hbo-max/hbo-max-goes-live-eight-new-countries-including-germany-and-italy-highly-anticipated
- מקור HBO Max Live: https://www.hbomax.com/il/he/sports

### איכות המקורות שנבדקו
1. **מקור רשמי של מפעיל** — מאמת קיום ערוץ והשתייכות לשירות, לא כתובת ניגון ב־SS IPTV.
2. **רשימות EPG** — עשויות לאמת שם ולוח תוכניות, לא קישור מדיה; אתר cbilling-tv.app דורש קובץ M3U של המשתמש לצפייה.
3. **מאגרים עם קישורים חתומים/ממסרי צד שלישי** — קישור יכול להיות לא נגיש, חסום, לא מורשה או מתחלף; אין סימון "תקין" לפני ניסיון ב־LG של המשתמש.
4. **תיעדוף הבא:** קישור קבוע או מקור חלופי אמין ל־yes+ LOVE/DARK/CINEMA/DIAMONDS; HOT Cinema 2–5; סלקום סדרות וסרטים; אימות NEXT נוכחי.


## סריקה נוספת ממוקדת – 22.11.2026

**היקף:** HOT, yes, STING+, NEXT TV, FreeTV, סלקום TV+, Disney+ ישראל, HBO Max ישראל בלבד. אין להוסיף ערוצי מדינות זרות שאינם מוצעים בידי ספקים אלה.

**מקורות חדשים והחלטות:**

1. [asheramram1-cloud/Playlist-1](https://github.com/asheramram1-cloud/Playlist-1/blob/main/playlist1.m3u) – מאגר ציבורי שנדחף ב־22.11.2026. מופיעים בו 40 ערוצים וביניהם HOT Cinema 1–5, HOT Comedy, HOT Israeli Cinema, yes TV Comedy, yes Movies Drama/Comedy/Action ו־yes Israeli. **הקישורים עוברים דרך ממסר צד שלישי עם מקטע הרשאה משותף בנתיב**. לא בוצעה בדיקת ניגון ולא נמצאה אסמכתא להרשאת הפצה; לא להעתיק את הנתיבים לפלייליסט הציבורי ללא בדיקת גישה, קביעות וסיכון לחשיפת הרשאות.
2. [aria-tv/aria ישראל](https://github.com/aria-tv/aria/blob/main/aria%2B/israel.m3u) – כולל HOT Comedy בכתובת ישירה `http://str2.iptvhd.ru:8080/HOTCOMEDY/index.m3u8`, אך מטא־נתוני המאגר מציינים **not-working**. במראה של המאגר היא אף סומנה כ־HOT Senior על אף שם URL אחר. **סיווג: קישור חשוד/לא אמין; לא להוסיף ל־M3U בלי אישור ניגון**.
3. [ianir-horn/IPTVIL/M3U1](https://github.com/ianir-horn/IPTVIL/blob/master/M3U1) – 48 מקורות לכאורה מהפצת סלקום, כולל Nat Geo Wild, National Geographic, E!, Food Network ו־Disney Junior. אולם מועד העדכון האחרון של המאגר הוא **2019-09-22**. מדובר במקור היסטורי ולא חדש; אין להסיק מהקישורים שהוא פעיל ב־2026.
4. FreeTV – השוואה מול [הקטלוג הרשמי](https://freetv.tv/tvchannels) ומול `Israel_Live_TV_Doron.m3u` העלתה שכבר קיימות רשומות לערוצי הסרטים (Action, Comedy, Drama, Thriller, Horror, Romantic, Feel Good, Family, Israeli, 10STARS), הקומדיה והדרמה. לא להוסיף אותן מחדש תחת שם אחר.
5. [סלקום tv+ – אינדקס רשמי](https://cellcom.co.il/production/Private/cellcomtv/channels/) – אישר קיומם של סלקום Action/Comedy/Drama/Family Movies, סדרות, דוקו, סרטים ישראליים, ערוץ קומדיות קלאסיות, E!, Discovery, National Geographic ו־Nat Geo Wild. במאגר הקהילה [cell.m3u](https://github.com/il90il90/m3u-tv/blob/main/cell.m3u) 87 רשומות עם URL חתום, ללא אימות ניגון ב־LG.
6. yes+ LOVE ו־yes+ DARK אושרו בדף [yes הרשמי](https://www.yes.co.il/content/yes-magazine/yesrec_2026-03-12/), אבל לא נמצא מקור HLS פשוט וקבוע שאומת בישראל. Disney+ ו־HBO Max ישראל: לא נמצא קישור ישיר לערוץ ליניארי; אתרי השירות מציגים בעיקר ספריות VOD.
7. [IPTV Cat – ישראל](https://iptvcat.net/asia/43) מסמן בתאריך 21.11.2026 את yes Movies Action כ־**לא נגיש**, כך שאין ראיה שקישור הציבורי הקיים יחזור לעבוד. לבדוק רק מקור שונה בפועל.

**סיכום סריקה:** נמצאו *מקורות מחקר חדשים ושמות ערוצים חסרים*, אך אין כרגע קישור חדש שאומת כנגיש ב־SS IPTV בישראל ושאינו כפול. **לא שונה הפלייליסט הפעיל** (281 רשומות בזמן הסריקה). עלות החלפת קישורים תקינים בקישורי צד שלישי לא יציבים גבוהה מהתועלת.

**עדיפות לסבב הבא:** תחילה HOT Cinema 2–5 / HOT Comedy ממקור שידור שונה ושאינו תלוי בהרשאת לקוח מזדמנת; אחר כך yes+ LOVE/DARK ו־yes Movies Drama/Comedy, סלקום סדרות וסרטים. לבדוק שהערוץ אכן ישראלי ושהשידור אינו ערוץ בינלאומי בעל שם דומה.


---

## מחקר היסטורי מלפני שינוי ההיקף (לייחוס בלבד; אינו הוראה להמשך חיפוש)

# ערוצים לאיתור קישור שידור – Israel Live TV

עדכון: 20.11.2026. רשימת מעקב לערוצים שמזוהים בקטלוגים של ספקיות או אתרי תוכן, אך ללא כתובת שידור ישירה מאומתת להפעלה ב-SS IPTV. אין להוסיף ערוץ לקובץ M3U הפעיל ללא כתובת אמיתית; קישור לדף האתר אינו קישור ניגון.

סטטוס קישורים: **לא נמצא קישור M3U8 פתוח ומורשה שאומת לצפייה בישראל** לערוצים שלהלן. זכויות, זמינות כתוביות ודיבוב מחייבות בדיקה נפרדת. ייתכנו חפיפות ושמות מסחריים שונים לאותו שידור שכבר ברשימה.

ערוצים לשידורי ניסיון עם כתובות חלופיות כבר נוספו לקובץ הפעיל: **ספורט 5 פלוס — מקור חלופי לבדיקה**, **ספורט 5 סטארס — מקור חלופי לבדיקה**.

## HOT
- [ ] HOT Comedy
- [ ] HOT בידור
- [ ] HOT REAL
- [ ] HOT Cinema 2
- [ ] HOT Cinema 3
- [ ] HOT Cinema 4
- [ ] HOT Cinema 5
- [ ] HOT קולנוע ישראלי
- [ ] HOT לולי
- [ ] ZOOM TOON
- [ ] ערוץ באזז

## yes
- [ ] yes TV DRAMA
- [ ] yes TV ACTION
- [ ] yes TV COMEDY
- [ ] yes Movies Comedy
- [ ] yes Movies Drama
- [ ] yes Movies Kids
- [ ] yes דוקו
- [ ] yes קולנוע ישראלי

## סלקום TV+
- [ ] סלקום Action Movies
- [ ] סלקום Comedy Movies
- [ ] סלקום Drama Movies
- [ ] סלקום Family Movies
- [ ] סלקום סדרות
- [ ] סלקום דוקו
- [ ] סלקום Kids Movies
- [ ] ערוץ הקולנוע הישראלי של סלקום

## פרטנר TV+
- [ ] ערוץ פשע אמיתי
- [ ] ערוץ גיבורים
- [ ] ערוץ הצדעה לגיבורי מערכות ישראל

## ערוצי תוכן עם שידור ישראלי
- [ ] National Geographic
- [ ] Nat Geo Wild
- [ ] Discovery Channel
- [ ] Animal Planet
- [ ] ערוץ ההיסטוריה
- [ ] Food Network
- [ ] TLC
- [ ] Travel Channel
- [ ] E!
- [ ] Disney Junior ישראל
- [ ] JimJam
- [ ] ערוץ הטיולים

## דרמות ויוה
- [ ] ויוה איסטנבול
- [ ] ויוה טלנובלות
- [ ] ויוה סיפור אהבה
- [ ] ויוה וינטג'
- [ ] ויוה בינג'
- [ ] דרמות טורקיות 2
- [ ] דרמות טורקיות 3
- [ ] דרמות ספרדיות
- [ ] ויוה לפני כולם

## מקורות אימות קטלוג
- ויוה: https://viva.mako.co.il/channels
- iptv-org (כתובות שידור פומביות לבדיקה, לא אישור זכויות): https://github.com/iptv-org/iptv/blob/master/streams/il.m3u

## כללי עדכון
- לערוצים חדשים מוסיפים group-title="חדשים לבדיקה" וקישור שידור ישיר בלבד.
- לא מוחקים ערוצים קיימים או משנים קישורים קיימים ללא אישור המשתמש.
- לאחר בדיקת משתמש, משייכים עובדים לקטגוריה המתאימה; כושלים ל'אין שידור כרגע'.

## מועמדי FreeTV נוספים — זוהו במדריך שידורים חיצוני (21.11.2026)

לא נמצאים בקובץ M3U הפעיל. השמות הופיעו בקובץ EPG חיצוני שמשתמש במזהי freetv.tv, אך **זמינותם כיום כערוצים חיים לא אומתה**, והם אינם מופיעים ברשימת הערוצים הראשית באתר FreeTV, למעט אזכור נינג'ה בתיאור קטגוריית הבידור. **לא נמצא עבורם קישור HLS קבוע ומורשה שניתן לאמת**; אל תכניסו קישור עם טוקן שפג תוקפו לרשימה הפעילה.

- [ ] ערוץ דוק — לבדוק אם פעיל ב-FreeTV ואם קיים קישור שידור ישיר רשמי
- [ ] ערוץ נינג'ה — לבדוק אם פעיל ב-FreeTV ואם קיים קישור שידור ישיר רשמי
- [ ] ערוץ חתונה ממבט ראשון — לבדוק אם פעיל ב-FreeTV ואם קיים קישור שידור ישיר רשמי
- [ ] ערוץ הכוכב הבא — לבדוק אם פעיל ב-FreeTV ואם קיים קישור שידור ישיר רשמי

מקור לזיהוי בלבד: https://github.com/SilentButeo2/webgrabplus-siteinipack/blob/master/siteini.pack/Israel/freetv.tv.channels.xml
קטלוג רשמי להשוואה: https://freetv.tv/tvchannels

