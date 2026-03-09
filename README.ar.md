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

مسار Python آلي لتوليد إكساءات أزياء (textures) مخصصة للعبة [Haydee](https://store.steampowered.com/app/530890/Haydee/) باستخدام واجهة برمجة تطبيقات Google Gemini (API).

> [!TIP]
> **لست من محبي سطر الأوامر؟** تحقق من [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! إنها واجهة رسومية حديثة وجاهزة للاستخدام تتيح لك توليد أزياء مخصصة بسهولة دون التعامل مع الطرفية (terminals) أو متغيرات البيئة. قم بتنزيل أحدث إصدار للبدء فوراً!

### 🤖 التحقق متعدد المعايير بصورتين باستخدام النماذج اللغوية الكبيرة كحكم (LLM-as-a-Judge)
يتميز هذا المشروع بوجود **حلقة ملاحظات لضمان الجودة** آلية ومتقدمة. بينما يقوم نموذج سريع (مثل `gemini-3.1-flash-image`) برسم الإكساءات، يعمل نموذج استنتاج أقوى (مثل `gemini-3.1-pro`) كمفتش صارم لضمان الجودة باستخدام نهج **متعدد المعايير بصورتين**.

يقوم المفتش بمقارنة إكساء UV المُولد جنباً إلى جنب مع القالب الفارغ الأصلي لتقييم قواعد هيكلية محددة بشكل مستقل:
1. **قاعدة الوجه:** تضمن بقاء خوذة الشخصية بدون أي ملامح للوجه تماماً (لا توجد ملامح بشرية، أو نظارات، أو أجهزة تنفس).
2. **قاعدة خط التماس في الجذع:** تتحقق من أن قطع الملابس/الدروع الأمامية والخلفية للجذع تتطابق تماماً لمنع ظهور خطوط تماس مرئية في العرض ثلاثي الأبعاد.
3. **قاعدة الساقين:** تضمن التعامل مع الساقين اليسرى واليمنى كأطراف منفصلة، مما يمنع الذكاء الاصطناعي من رسم ساقين داخل شكل واحد.

إذا تم انتهاك أي قاعدة، يرفض المفتش الصورة، ويقدم ملاحظات محددة حول ما تم خرقه بالضبط، ويجبر المُولّد على إعادة رسم الإكساء لتصحيح تلك الأخطاء المحددة.

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

### 🔑 الحصول على مفتاح API الخاص بـ Gemini

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/app/apikey).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. انقر على زر **"Create API key"** (إنشاء مفتاح API).
4. إذا طُلب منك، اقرأ شروط الخدمة ووافق عليها.
5. انقر على **"Create API key in new project"** (أو استخدم مشروعاً حالياً).
6. انسخ المفتاح المُولد. ستحتاج إليه في ملف `.env` في خطوات الإعداد أدناه.

## 💻 الإعداد (محلياً)

### التثبيت عبر pip (مستحسن)
أسهل طريقة لتثبيت المُولّد هي مباشرة من PyPI:
```bash
pip install haydee-outfit-generator
```

### التثبيت من المصدر
1. انسخ المستودع (Clone).
2. ثبّت الاعتمادات (dependencies):
   ```bash
   pip install .
   ```

3. انسخ `.env.example` إلى `.env` (أو قم بإنشاء واحد جديد) وقم بتكوين متغيراتك:
* `GEMINI_API_KEY`: مفتاح Google Gemini API الخاص بك.
* `HAYDEE_PATH`: المسار المطلق لمجلد تثبيت لعبة Haydee الخاص بك.
* `IMAGE_RESOLUTION`: (اختياري) دقة المخرجات. الافتراضي هو `4K`. يمكن ضبطه على `2K` (2048x2048) إذا لزم الأمر.
* `MODEL_NAME`: (اختياري) نموذج الذكاء الاصطناعي Gemini الذي سيتم استخدامه لتوليد الإكساء. الافتراضي هو `gemini-3.1-flash-image-preview`.
* `VALIDATOR_MODEL`: (اختياري) نموذج الاستنتاج الذي سيتم استخدامه لفحص ضمان الجودة. الافتراضي هو `gemini-3.1-pro-preview`.

## 🐳 الإعداد (Docker)

إذا كنت تفضل تشغيل المشروع بدون تثبيت Python محلياً، يمكنك استخدام Docker.

1. قم بتثبيت [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. أنشئ ملف `.env` الخاص بك وقم بتعيين `GEMINI_API_KEY` و `HAYDEE_PATH`.
   * ملاحظة: **يجب** أن يكون `HAYDEE_PATH` في ملف `.env` هو المسار المطلق على جهاز Windows المضيف الخاص بك (على سبيل المثال، `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 الاستخدام

### التشغيل محلياً

**1. توليد زي واحد**
قم بتشغيل أمر `generate` عن طريق تقديم اسم التعديل (mod)، ووصف النمط المطلوب، واسم المؤلف (اختياري):

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(نصيحة: يمكنك حذف الكلمة المفتاحية `generate` للحصول على أمر أقصر: `haydee-gen --name ...`)*

**معلمات التوليد الجزئي**
يمكنك تخطي أجزاء من عملية التوليد بشكل انتقائي لتوفير الوقت أو استدعاءات API إذا كنت قد قمت بتوليدها بالفعل في عمليات تشغيل سابقة:
* `--skip-d`: يتخطى توليد الإكساء الأساسي (diffuse texture) (`Suit_D.dds`). يجب أن يكون هناك إكساء مُولد مسبقاً، وإلا سيفشل الأمر. إذا تم توفير هذه العلامة، فلن يكون وسيط `--style` إلزامياً.
* `--skip-s`: يتخطى توليد قناع المواد (material mask) وخريطة الانعكاس (specular map) (`Suit_S.dds`).
* `--skip-n`: يتخطى توليد خريطة النتوءات (normal map) (`Suit_N.dds`).
* `--max-retries`: (اختياري) أقصى عدد لمحاولات إعادة التوليد إذا فشل الإكساء في التحقق من ضمان الجودة. الافتراضي هو `3`.

عند تخطي توليد الخرائط (`--skip-s` أو `--skip-n`) دون توليدها مسبقاً، سيتراجع الزي المُولد بأمان ويستخدم خرائط Haydee الأساسية المحايدة لتلك الخانات.

سيقوم السكربت تلقائياً بقراءة الإكساء الأساسي، والاتصال بـ Gemini API لتوليد الإكساء الأساسي (`Suit_D.dds` باستخدام حلقة التحقق الآلية لضمان الجودة بصورتين)، ثم طلب قناع مواد يتم تعبئته في خريطة انعكاس (`Suit_S.dds`). بالإضافة إلى ذلك، يتم توليد خريطة نتوءات فضاء التماس مخصصة (Tangent Space Normal Map) (`Suit_N.dds`) جنباً إلى جنب مع الإكساء الأساسي لإعطاء المواد الجديدة المُولدة بالذكاء الاصطناعي بروزاً وتفاصيل ثلاثية الأبعاد متطابقة. سيتم توليد التعديل النهائي داخل مجلد `Haydee/Outfits` الخاص بك، ليكون جاهزاً للاستخدام!

**2. تجميع الأزياء في تعديل متعدد (Multi-Mod)**
إذا قمت بتوليد أزياء متعددة وترغب في تجميعها في تعديل واحد مع تنويعات قابلة للتبديل (على سبيل المثال، في زي "Rainbow" واحد بخانات ملونة مختلفة):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` هي علامة اختيارية ستقوم بإزالة المجلدات وتكوينات التعديل الفردي الأصلية بعد تجميعها بنجاح.

### التشغيل باستخدام Docker

يمكنك استخدام Docker Compose لربط مجلد Haydee الخاص بك تلقائياً وتشغيل الأوامر:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 النشر على Steam Workshop

عندما تكون مستعداً لمشاركة زيك المُولد، يمكنك رفعه مباشرة إلى Steam Workshop باستخدام الأدوات المدمجة في اللعبة.

### 1. تحضير صورة مصغرة
- قم بإنشاء صورة معاينة للتعديل الخاص بك (`preview.png` أو `preview.jpg`).
- يجب أن تكون الصورة مربعة (على سبيل المثال، 512x512 أو 256x256).
- ضع هذه الصورة في مجلد التعديل الخاص بك.

### 2. تشغيل محرر Edith
توجد أدوات الرفع في محرر اللعبة، وليس في اللعبة نفسها:
- اذهب إلى مجلد التثبيت الرئيسي للعبة Haydee.
- قم بتشغيل `Edith.exe`.
- من شريط القائمة العلوي، حدد **Tool -> Workshop Uploader**.

### 3. ملء بيانات أداة الرفع
في نافذة أداة الرفع، املأ الحقول التالية:
- **محتوى التعديل (Mod Content):** في الجزء العلوي من نموذج الرفع، يوجد حقل نصي وبأسفله زر **Browse** (استعراض). ستستخدم هذا لإنشاء قائمة الملفات المراد رفعها:
  1. انقر على **Browse** وأضف المجلد الرئيسي للتعديل الخاص بك (على سبيل المثال، حدد `Outfits/NeonSurge`).
  2. انقر على **Browse** مرة أخرى وأضف ملف تعريف الزي `.outfit` الخاص بك (على سبيل المثال، حدد `Outfits/NeonSurge.outfit`).
  *(يضمن هذا تضمين المجموعة الكاملة من الملفات المطلوبة لعمل التعديل).*
- **العنوان (Title):** اسم الزي الخاص بك (سيتم عرضه على Steam).
- **الوصف (Description):** وصف قصير للتعديل (ما هو، والميزات الخاصة، وما إلى ذلك).
- **الرؤية (Visibility):** يوصى بتعيين هذا على **Private** (خاص) أولاً للتحقق من كيف يبدو كل شيء على صفحة Steam، وتغييره إلى **Public** (عام) لاحقاً.
- **صورة المعاينة (Preview Image):** حدد الصورة المصغرة التي قمت بتحضيرها في الخطوة 1.

بمجرد الانتهاء من ملء البيانات، انقر على **Upload** (رفع). إذا سار كل شيء على ما يرام، ستظهر الحالة في الأسفل **"Success"** (نجاح).

## 🧪 الاختبار

يستخدم هذا المشروع `pytest` للاختبار الآلي.

1. ثبّت اعتمادات التطوير:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. قم بتشغيل حزمة الاختبارات مع التغطية (coverage):
   ```bash
   pytest
   ```
   *ملاحظة: مفاتيح API الصالحة أو تثبيت حقيقي للعبة Haydee **ليست مطلوبة** لتشغيل الاختبارات، حيث يتم عمل محاكاة (mocking) بأمان للاعتمادات الخارجية ونظام الملفات.*

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [LICENSE](LICENSE) للحصول على التفاصيل.