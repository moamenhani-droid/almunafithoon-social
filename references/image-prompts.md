# برومتات توليد الصور

## القاعدة الأولى — لا نص عربي في الصورة المولّدة

مولّدات الصور (Midjourney، GPT Image، Gemini، Flux، Higgsfield…) **تكتب العربية بحروف مقطّعة ومعكوسة ومخترعة**. لذلك:

1. **المولّد يصنع المشهد فقط** — بلا أي نص أو شعار أو أرقام.
2. **النص والشعار يُركَّبان فوقه** في قالب HTML (`assets/templates/`) ثم يُصدَّر PNG بـ `scripts/render.py`.
3. **اترك في البرومت مساحة فارغة مقصودة** حيث سيقع النص (negative space) وحدّد مكانها.

البرومتات بالإنجليزية لأن المولّدات تفهمها بدقة أعلى.

## بنية البرومت الرئيسية

```
[SUBJECT] — ما الذي في الصورة
[COMPOSITION] — أين العنصر، وأين المساحة الفارغة للنص
[LIGHT] — نوع الضوء ووقته
[PALETTE] — ألوان الهوية بالأسماء والرموز
[MATERIALS] — الخامات
[STYLE] — نوع التصوير والعدسة
[MOOD] — الإحساس
[CONSTRAINTS] — الممنوعات الثابتة
[FORMAT] — النسبة
```

### كتلة الهوية الثابتة — تُلصق في نهاية كل برومت

```
Color palette strictly limited to deep emerald green (#16352E), muted sage-teal
(#4A615E), brushed satin silver (#C8CBC9) and warm ivory (#F1EDE7).
Materials: brushed aluminium, warm limestone, pale travertine, light oak, clear glass.
Quiet luxury, institutional, timeless, calm confidence.
NO text, NO letters, NO numbers, NO logos, NO watermarks, NO signage,
NO gold, NO saturated colors, NO neon, NO lens flare,
NO distorted architecture, NO people's faces.
```

### معاملات النسبة
| المولّد | بوست 4:5 | ستوري 9:16 | مربع |
|---|---|---|---|
| Midjourney | `--ar 4:5 --style raw --v 7` | `--ar 9:16 --style raw --v 7` | `--ar 1:1` |
| GPT Image / Gemini | اكتب: `vertical 4:5 portrait format, 1080x1350` | `vertical 9:16, 1080x1920` | `square 1:1` |
| Flux / Higgsfield | اختر النسبة من الإعدادات + اذكرها في النص | | |

---

## البرومتات حسب القالب

### منظور مشروع (قالب ١ · ١١)
```
Architectural exterior visualization of a modern mid-rise residential
complex in Baghdad, clean vertical lines, limestone and glass facade with
slim brushed-aluminium fins, date palms at street level.
Composition: building occupies the upper 60% of the frame, shot from a low
three-quarter angle; the lower 40% is calm open plaza and soft shadow,
left empty for text overlay.
Light: warm low golden-hour sun from the right, long soft shadows, clear
pale sky.
Style: high-end architectural photography, 35mm tilt-shift lens,
corrected verticals, crisp detail, subtle film grain.
[كتلة الهوية الثابتة] [معامل النسبة]
```

### داخلي وحدة (قالب ٢)
```
Interior of a contemporary Iraqi family apartment living room, warm ivory
walls, pale travertine floor, light oak joinery, deep emerald velvet sofa,
brushed silver floor lamp, large window with sheer curtains and a glimpse
of palms outside.
Composition: room fills the upper half of the frame at eye level, straight
one-point perspective; lower half falls into soft clean floor and wall
area, left empty for an information card.
Light: soft diffused afternoon daylight, no harsh highlights.
Style: editorial interior photography, 24mm lens, natural color.
[كتلة الهوية الثابتة] [معامل النسبة]
```

### خلفية قيمة العلامة — ظل النخيل (قالب ٧)
```
Minimal warm ivory plaster wall, soft natural shadow of date palm fronds
falling across the top-left corner, gentle gradient of light.
Composition: 80% of the frame is calm empty wall for large typography;
shadows only in one corner.
Light: late morning sun, very soft edges on shadows.
Style: fine-art minimal photography, shallow tonal range, matte finish.
[كتلة الهوية الثابتة] [معامل النسبة]
```

### خلفية زمردية بملمس (قوالب ٥ · ٦ · ٨ · ١٢)
```
Abstract background of deep emerald green brushed-metal panels arranged
as tall vertical slabs with 45-degree chamfered corners, subtle satin
silver edges catching light, inspired by modern architectural facades.
Composition: panels concentrated on the right third; left two thirds
remain dark smooth emerald for text.
Light: single soft raking light from the top right.
Style: 3D render, octane, physically based materials, very subtle detail.
[كتلة الهوية الثابتة] [معامل النسبة]
```

### زخرفة المناسبات (قالب ١٠)
```
Elegant geometric pattern of thin satin-silver lines forming interlocking
chamfered rectangles on a deep emerald green background, extremely subtle,
low contrast, generous empty center area for a greeting.
Style: flat vector-like render, precise, minimal, no traditional ornament
clutter.
[كتلة الهوية الثابتة] [معامل النسبة]
```

### أيقونات المواصفات (قالب ٢)
**لا تولّدها.** استخدم أيقونات خطية جاهزة (Lucide / Phosphor) بخط 2px زمردي: `ruler` للمساحة، `bed-double` للغرف، `building-2` للطابق، `compass` للواجهة، `car` للموقف.

---

## برومت تصميم كامل (للأدوات التي تصمم البوست كله)

حين يطلب المالك برومتاً واحداً يلصقه في أداة تصميم بالذكاء الاصطناعي (Canva AI، Claude، أدوات القوالب)، استخدم هذه البنية — ومع ذلك **نبّه أن النص العربي يجب مراجعته حرفاً حرفاً بعد التوليد**:

```
صمّم بوست إنستغرام عمودي 1080×1350 لشركة «المنفذون — استثمار عقاري» في بغداد.

الهوية:
- الألوان: زمردي عميق #16352E أساسي، فضي مصقول #C8CBC9 ثانوي، عاجي دافئ #F1EDE7 للخلفيات الفاتحة. لا ذهبي ولا ألوان مشبعة.
- الخطوط: العناوين بـ Noto Kufi Arabic عريض، النص بـ IBM Plex Sans Arabic، اللاتيني بـ Montserrat بتباعد واسع.
- الطابع: فخامة هادئة مؤسسية — عمارة حديثة، خامات حجر وألمنيوم مصقول.
- العنصر المميز: إطارات وألواح بزوايا مشطوفة 45° مستوحاة من مونوغرام الشعار.

المحتوى:
- العنوان: [ ]
- السطر الثاني: [ ]
- الأرقام: [ ]
- الدعوة: [ ]

التخطيط: [وصف القالب من templates.md]

قيود: اتجاه من اليمين لليسار. هامش 80px. لا تباعد حروف على العربية. لا نص أصغر من 22px.
الشعار أعلى اليمين. لا ظلال ملوّنة ولا تدرجات صاخبة.
```

## التحقق من الصورة المولّدة قبل استخدامها
- [ ] لا حروف أو أرقام أو لافتات مختبئة في الصورة (افحص الواجهات والزجاج).
- [ ] الخطوط الرأسية للمبنى مستقيمة، لا انحناء ولا أعمدة مكرّرة مشوّهة.
- [ ] لا ذهبي — المعادن فضية.
- [ ] المساحة الفارغة للنص موجودة فعلاً حيث طُلبت.
- [ ] العمارة تشبه العراق لا دبي.
- [ ] لا وجوه بشرية مشوّهة أو أيدٍ بأصابع زائدة.
- [ ] **صورة مولّدة لا تُنسب لمشروع حقيقي على أنها صورته** — تُستخدم كمشهد تعبيري، أو تُكتب عليها «صورة تعبيرية».
