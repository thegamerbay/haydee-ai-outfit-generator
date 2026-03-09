> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# مُولّد أزياء [Haydee](https://store.steampowered.com/app/530890/Haydee/) (مدعوم بواسطة Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


مسار بايثون مؤتمت (Pipeline) لإنشاء إكساءات أزياء (Textures) مخصصة للعبة [Haydee](https://store.steampowered.com/app/530890/Haydee/) باستخدام واجهة برمجة تطبيقات Google Gemini.

> [!TIP]
> **لست من محبي سطر الأوامر؟** تحقق من [واجهة المستخدم الرسومية لمولّد أزياء Haydee بالذكاء الاصطناعي](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! إنها واجهة رسومية حديثة وجاهزة للاستخدام تتيح لك بسهولة إنشاء أزياء مخصصة دون الحاجة للتعامل مع الطرفية (Terminals) أو متغيرات البيئة. قم بتنزيل أحدث إصدار للبدء فورًا!

## ✨ أمثلة على التوليد

| | | | |
| :---: | :---: | :---: | :---: |
| [![Lunar Scout Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672592226.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672592226) | [![Neon Surge Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672586107.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672586107) | [![Steam Gear Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672258053.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672258053) | [![Tomb Awakened Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672251317.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672251317) |
| [Lunar Scout Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672592226) | [Neon Surge Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672586107) | [Steam Gear Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672258053) | [Tomb Awakened Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672251317) |
| [![Waaagh Bot Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672243330.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672243330) | [![Wastelander Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672236521.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672236521) | [![Xenomorph Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672227514.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672227514) | [![Berry Sweet Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672221390.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672221390) |
| [Waaagh Bot Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672243330) | [Wastelander Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672236521) | [Xenomorph Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672227514) | [Berry Sweet Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672221390) |
| [![Tech-Priestess Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672191643.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672191643) | [![Astro White Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672182479.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672182479) | [![Battle Sister Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672168153.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672168153) | [![Gothic Automaton Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672159225.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672159225) |
| [Tech-Priestess Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672191643) | [Astro White Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672182479) | [Battle Sister Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672168153) | [Gothic Automaton Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672159225) |
| [![Candy Pop Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672150985.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672150985) | [![Hellwalker Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672058503.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672058503) | [![Retrowave Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672013495.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672013495) | [![Iron Utopia Outfit](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3671983563.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3671983563) |
| [Candy Pop Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672150985) | [Hellwalker Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672058503) | [Retrowave Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3672013495) | [Iron Utopia Outfit](https://steamcommunity.com/sharedfiles/filedetails/?id=3671983563) |

## 📋 المتطلبات الأساسية

- **Python 3.12+**

### 🔑 الحصول على مفتاح Gemini API

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/app/apikey).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. انقر على زر **"Create API key"**.
4. إذا طُلب منك، اقرأ شروط الخدمة ووافق عليها.
5. انقر على **"Create API key in new project"** (أو استخدم مشروعًا حاليًا).
6. انسخ المفتاح المُوَلَّد. ستحتاج إليه في ملف `.env` ضمن خطوات الإعداد أدناه.

## 💻 الإعداد (محلياً)

### التثبيت عبر pip (مُوصى به)
أسهل طريقة لتثبيت المُولّد هي مباشرةً من PyPI:
```bash
pip install haydee-outfit-generator
```

### التثبيت من المصدر
1. قم باستنساخ (Clone) المستودع.
2. قم بتثبيت الاعتماديات:
   ```bash
   pip install .
   ```

3. انسخ `.env.example` إلى `.env` (أو قم بإنشاء واحد) وقم بتكوين متغيراتك:
* `GEMINI_API_KEY`: مفتاح واجهة برمجة تطبيقات Google Gemini الخاص بك.
* `HAYDEE_PATH`: المسار المطلق (Absolute path) لمجلد تثبيت لعبة Haydee.
* `IMAGE_RESOLUTION`: (اختياري) دقة الإخراج. القيمة الافتراضية هي `4K`. يمكن ضبطها على `2K` (2048x2048) إذا لزم الأمر.
* `MODEL_NAME`: (اختياري) نموذج الذكاء الاصطناعي Gemini المراد استخدامه. الافتراضي هو `gemini-3.1-flash-image-preview`.

## 🐳 الإعداد (عبر Docker)

إذا كنت تفضل تشغيل المشروع دون تثبيت Python محليًا، يمكنك استخدام Docker.

1. قم بتثبيت [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. قم بإنشاء ملف `.env` الخاص بك وعيِّن `GEMINI_API_KEY` و `HAYDEE_PATH`.
   * ملاحظة: **يجب** أن يكون `HAYDEE_PATH` في ملف `.env` هو المسار المطلق على جهاز Windows المضيف (على سبيل المثال، `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 الاستخدام

### التشغيل محلياً

**1. توليد زي واحد**
قم بتشغيل الأمر `generate` عن طريق توفير اسم المود (mod)، ووصف النمط المطلوب، واسم المؤلف (اختياريًا):

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(تلميح: يمكنك حذف الكلمة المفتاحية `generate` لكتابة أمر أقصر: `haydee-gen --name ...`)*

**معاملات التوليد الجزئي (Partial Generation)**
يمكنك تخطي أجزاء من عملية التوليد بشكل انتقائي لتوفير الوقت أو استدعاءات الـ API إذا كنت قد قمت بتوليدها بالفعل في عمليات سابقة:
* `--skip-d`: يتخطى عملية إنشاء إكساء الانتشار (Diffuse texture) (`Suit_D.dds`). يجب أن يكون هناك إكساء مُوَلَّد مسبقًا، وإلا سيفشل الأمر. إذا تم توفير هذه العلامة (Flag)، فلن يكون الوسيط `--style` إلزاميًا.
* `--skip-s`: يتخطى عملية إنشاء قناع المواد (Material mask) وخريطة الانعكاس (Specular map) (`Suit_S.dds`).
* `--skip-n`: يتخطى عملية إنشاء خريطة النواظم (Normal map) (`Suit_N.dds`).

عند تخطي إنشاء الخرائط (`--skip-s` أو `--skip-n`) دون توليدها مسبقًا، سيعود الزي المُنشأ بأمان ويستخدم خرائط Haydee المحايدة الأساسية لتلك الخانات.

سيقرأ السكربت الإكساء الأساسي تلقائيًا، ويتصل بـ Gemini API لتوليد إكساء الانتشار (`Suit_D.dds`)، ثم يطلب قناع مواد يُحزم في خريطة الانعكاس (`Suit_S.dds`). بالإضافة إلى ذلك، يتم إنشاء خريطة نواظم (Tangent Space Normal Map) مخصصة (`Suit_N.dds`) بجانب إكساء الانتشار لإعطاء المواد الجديدة المُنشأة بالذكاء الاصطناعي بروزًا وتفاصيل ثلاثية الأبعاد متطابقة. سيتم إنشاء المود النهائي داخل مجلد `Haydee/Outfits` الخاص بك، ليكون جاهزًا للاستخدام!

**2. تجميع الأزياء في مود متعدد (Multi-Mod)**
إذا قمت بتوليد عدة أزياء وترغب في تجميعها في مود واحد مع اختلافات قابلة للتبديل (على سبيل المثال، في زي "Rainbow" واحد بخانات ألوان مختلفة):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` هي علامة (Flag) اختيارية ستقوم بحذف المجلدات والتكوينات (configs) الأصلية للمودات الفردية بعد نجاح تجميعها.

### التشغيل باستخدام Docker

يمكنك استخدام Docker Compose لربط مجلد Haydee الخاص بك تلقائيًا وتشغيل الأوامر:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 النشر على Steam Workshop

عندما تكون مستعدًا لمشاركة الزي الذي تم إنشاؤه، يمكنك رفعه مباشرة إلى Steam Workshop باستخدام الأدوات المدمجة في اللعبة.

### 1. تجهيز صورة مصغرة (Thumbnail)
- قم بإنشاء صورة معاينة للمود الخاص بك (`preview.png` أو `preview.jpg`).
- يجب أن تكون الصورة مربعة (مثلًا 512x512 أو 256x256).
- ضع هذه الصورة في مجلد المود الخاص بك.

### 2. تشغيل محرر Edith
أدوات الرفع موجودة في محرر اللعبة، وليس في اللعبة نفسها:
- اذهب إلى المجلد الرئيسي لتثبيت Haydee.
- قم بتشغيل `Edith.exe`.
- من شريط القوائم العلوي، اختر **Tool -> Workshop Uploader**.

### 3. ملء بيانات أداة الرفع (Uploader Data)
في نافذة الرفع، املأ الحقول التالية:
- **محتوى المود (Mod Content):** في الجزء العلوي من نموذج الرفع، يوجد حقل نصي وبأسفله زر **تصفح (Browse)**. ستستخدم هذا لإنشاء قائمة الملفات المراد رفعها:
  1. انقر على **Browse** وأضف المجلد الرئيسي للمود الخاص بك (على سبيل المثال، حدد `Outfits/NeonSurge`).
  2. انقر على **Browse** مرة أخرى وأضف ملف تعريف الـ `.outfit` الخاص بك (على سبيل المثال، حدد `Outfits/NeonSurge.outfit`).
  *(يضمن ذلك تضمين المجموعة الكاملة من الملفات المطلوبة لعمل المود).*
- **العنوان (Title):** اسم الزي الخاص بك (سيتم عرضه على Steam).
- **الوصف (Description):** وصف قصير للمود (ماهيته، الميزات الخاصة، إلخ).
- **الرؤية (Visibility):** يُوصى بضبط هذا على **خاص (Private)** أولاً للتحقق من مظهر كل شيء على صفحة Steam، وتغييره إلى **عام (Public)** لاحقًا.
- **صورة المعاينة (Preview Image):** اختر الصورة المصغرة التي قمت بتجهيزها في الخطوة 1.

بمجرد ملء البيانات، انقر على **رفع (Upload)**. إذا سارت الأمور بشكل جيد، ستظهر الحالة في الأسفل كـ **"نجاح (Success)"**.

## 🧪 الاختبار

يستخدم هذا المشروع `pytest` لإجراء الاختبارات المؤتمتة.

1. قم بتثبيت اعتماديات التطوير:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. قم بتشغيل مجموعة الاختبارات مع التغطية (coverage):
   ```bash
   pytest
   ```
   *ملاحظة: **لا يلزم** وجود مفاتيح API صالحة أو تثبيت حقيقي للعبة Haydee لتشغيل الاختبارات، حيث يتم محاكاة (Mocking) الاعتماديات الخارجية ونظام الملفات بشكل آمن.*

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [الترخيص (LICENSE)](LICENSE) للحصول على التفاصيل.