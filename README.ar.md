> 🌐 **اللغات:** [English](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.md) | [Русский](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ru.md) | [ไทย](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.th.md) | [中文](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.zh.md) | [Español](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.es.md) | [العربية](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ar.md)

# مُوَلِّد أزياء [Haydee](https://store.steampowered.com/app/530890/Haydee/) (مدعوم بواسطة Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

مسار عمل آلي بلغة Python لتوليد إكساءات (textures) أزياء مخصصة للعبة [Haydee](https://store.steampowered.com/app/530890/Haydee/) باستخدام واجهة برمجة تطبيقات Google Gemini.

> [!TIP]
> **لست من محبي سطر الأوامر؟** تحقق من [واجهة المستخدم الرسومية لمُولد أزياء Haydee بالذكاء الاصطناعي](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! إنها واجهة رسومية حديثة وجاهزة للاستخدام تتيح لك بسهولة إنشاء أزياء مخصصة دون التعامل مع الوحدات الطرفية أو متغيرات البيئة. قم بتنزيل أحدث إصدار للبدء فوراً!

### 🤖 التحقق باستخدام نموذج لغوي كبير كقاضٍ (LLM-as-a-Judge) بمعايير متعددة وصورتين
يتميز هذا المشروع بـ **حلقة ملاحظات لضمان الجودة** آلية ومتقدمة. بينما يقوم نموذج سريع (مثل `gemini-3.1-flash-image`) برسم الإكساءات، يعمل نموذج تفكير أقوى (مثل `gemini-3.1-pro`) كمفتش صارم لضمان الجودة باستخدام نهج **المعايير المتعددة بصورتين**. 

يقوم المفتش بمقارنة إكساء UV المُولد جنباً إلى جنب مع القالب الفارغ الأصلي لتقييم قواعد هيكلية محددة بشكل مستقل:
1. **قاعدة الوجه:** تضمن أن تظل خوذة الشخصية خالية تماماً من الملامح (لا توجد ملامح بشرية، أو نظارات، أو أجهزة تنفس).
2. **قاعدة خطوط اتصال الجذع:** تتحقق من أن قطع الملابس/الدروع الأمامية والخلفية للجذع تتطابق تماماً لمنع ظهور خطوط الاتصال (seams) في الأبعاد الثلاثية.
3. **قاعدة الساقين:** تضمن التعامل مع الساقين اليمنى واليسرى كأطراف فردية، مما يمنع الذكاء الاصطناعي من رسم ساقين داخل شكل واحد.

إذا تم انتهاك أي قاعدة، يرفض المفتش الصورة، ويقدم ملاحظات محددة حول ما تم كسره بالضبط، ويجبر المُوَلِّد على إعادة رسم الإكساء لتصحيح تلك الأخطاء المحددة.

## ✨ أمثلة التوليد

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

### 🔑 الحصول على مفتاح API لـ Gemini

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/app/apikey).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. انقر على زر **"Create API key"** (إنشاء مفتاح API).
4. إذا طُلب منك ذلك، اقرأ واقبل شروط الخدمة.
5. انقر على **"Create API key in new project"** (إنشاء مفتاح API في مشروع جديد) (أو استخدم مشروعاً موجوداً).
6. انسخ المفتاح المُولد. ستحتاجه لملف `.env` في خطوات الإعداد أدناه.

## 💻 الإعداد (محلياً)

### التثبيت عبر pip (موصى به)
أسهل طريقة لتثبيت المُوَلِّد هي مباشرة من PyPI:
```bash
pip install haydee-outfit-generator
```

### التثبيت من المصدر
1. استنسخ المستودع (Clone the repository).
2. ثبّت الاعتماديات:
   ```bash
   pip install .
   ```

3. انسخ `.env.example` إلى `.env` (أو قم بإنشاء واحد) وقم بتكوين متغيراتك:
* `GEMINI_API_KEY`: مفتاح Google Gemini API الخاص بك.
* `HAYDEE_PATH`: المسار المطلق لمجلد تثبيت لعبة Haydee.
* `IMAGE_RESOLUTION`: (اختياري) دقة المُخرجات. الافتراضي هو `4K`. يمكن تعيينه إلى `2K` (2048x2048) إذا لزم الأمر.
* `MODEL_NAME`: (اختياري) نموذج ذكاء Gemini الاصطناعي المستخدم لتوليد الإكساء. الافتراضي هو `gemini-3.1-flash-image-preview`.
* `VALIDATOR_MODEL`: (اختياري) نموذج التفكير المستخدم لفحص ضمان الجودة. الافتراضي هو `gemini-3.1-pro-preview`.

## 🐳 الإعداد (Docker)

إذا كنت تفضل تشغيل المشروع دون تثبيت Python محلياً، يمكنك استخدام Docker.

1. ثبّت [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. قم بإنشاء ملف `.env` الخاص بك وقم بتعيين `GEMINI_API_KEY` و `HAYDEE_PATH`.
   * ملاحظة: `HAYDEE_PATH` في `.env` **يجب** أن يكون المسار المطلق على جهاز Windows المضيف (مثل `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 الاستخدام

### التشغيل محلياً

**1. توليد زي واحد**
قم بتشغيل الأمر `generate` من خلال توفير اسم التعديل (mod)، ووصف النمط المطلوب، واسم المؤلف (اختيارياً):

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(تلميح: يمكنك حذف الكلمة الأساسية `generate` للحصول على أمر أقصر: `haydee-gen --name ...`)*

**معلمات التوليد الجزئي**
يمكنك تخطي أجزاء من عملية التوليد بشكل انتقائي لتوفير الوقت أو طلبات API إذا كنت قد قمت بتوليدها بالفعل في عمليات تشغيل سابقة:
* `--skip-d`: يتخطى توليد الإكساء الأساسي (diffuse texture) (`Suit_D.dds`). يجب أن يكون هناك إكساء مُولد مسبقاً موجوداً، وإلا سيفشل الأمر. إذا تم توفير هذه العلامة، فلن تكون المعلمة `--style` إلزامية.
* `--skip-s`: يتخطى توليد قناع المواد (material mask) وخريطة الانعكاس (specular map) (`Suit_S.dds`).
* `--skip-n`: يتخطى توليد الخريطة العادية (normal map) (`Suit_N.dds`).
* `--max-retries`: (اختياري) أقصى عدد لمحاولات إعادة التوليد إذا فشل الإكساء في التحقق من ضمان الجودة. الافتراضي هو `3`.

عند تخطي توليد الخرائط (`--skip-s` أو `--skip-n`) دون توليدها مسبقاً، سيعتمد الزي المُولد بأمان على الخرائط المحايدة الأساسية الخاصة بـ Haydee لتلك الفتحات.

سيقوم السكربت تلقائياً بقراءة الإكساء الأساسي، والاتصال بـ Gemini API لتوليد الإكساء الأساسي (`Suit_D.dds` باستخدام حلقة التحقق لضمان الجودة الآلية بصورتين)، ثم يطلب قناع مواد يتم تعبئته في خريطة انعكاس (`Suit_S.dds`). بالإضافة إلى ذلك، يتم إنشاء خريطة عادية مخصصة (Tangent Space Normal Map) (`Suit_N.dds`) جنباً إلى جنب مع الإكساء الأساسي لإعطاء المواد الجديدة المولدة بالذكاء الاصطناعي بروزاً وتفاصيل ثلاثية الأبعاد متطابقة. سيتم توليد التعديل (mod) النهائي داخل مجلد `Haydee/Outfits` الخاص بك، ليكون جاهزاً للاستخدام!

**2. تجميع الأزياء في تعديل متعدد (Multi-Mod)**
إذا قمت بتوليد أزياء متعددة وترغب في تجميعها في تعديل واحد مع تنويعات قابلة للتبديل (على سبيل المثال، في زي "Rainbow" واحد مع فتحات ملونة مختلفة):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` هي علامة اختيارية ستقوم بإزالة مجلدات التعديل الفردية الأصلية والإعدادات بعد تجميعها بنجاح.

### التشغيل باستخدام Docker

يمكنك استخدام Docker Compose لعمل ربط (mount) لمجلد Haydee الخاص بك تلقائياً وتشغيل الأوامر:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 النشر على Steam Workshop

عندما تكون مستعداً لمشاركة الزي الذي قمت بتوليده، يمكنك رفعه مباشرة إلى Steam Workshop باستخدام الأدوات المدمجة في اللعبة.

### 1. تجهيز صورة مصغرة
- قم بإنشاء صورة معاينة لتعديلك (`preview.png` أو `preview.jpg`).
- يجب أن تكون الصورة مربعة (مثال: 512x512 أو 256x256).
- ضع هذه الصورة في مجلد التعديل (mod) الخاص بك.

### 2. تشغيل مُحرر Edith
توجد أدوات الرفع في مُحرر اللعبة، وليس في اللعبة نفسها:
- اذهب إلى مجلد التثبيت الجذري للعبة Haydee.
- قم بتشغيل `Edith.exe`.
- من شريط القائمة العلوي، حدد **Tool -> Workshop Uploader**.

### 3. ملء بيانات الرفع
في نافذة الرفع، املأ الحقول التالية:
- **محتوى التعديل (Mod Content):** في الجزء العلوي من نموذج الرفع، يوجد حقل نصي أسفله زر **Browse** (استعراض). ستستخدم هذا لبناء قائمة الملفات المراد رفعها:
  1. انقر فوق **Browse** وأضف المجلد الرئيسي للتعديل (على سبيل المثال، حدد `Outfits/NeonSurge`).
  2. انقر فوق **Browse** مرة أخرى وأضف ملف تعريف `.outfit` الخاص بك (على سبيل المثال، حدد `Outfits/NeonSurge.outfit`).
  *(هذا يضمن تضمين المجموعة الكاملة من الملفات المطلوبة لعمل التعديل بنجاح).*
- **العنوان (Title):** اسم الزي الخاص بك (سيتم عرض هذا على Steam).
- **الوصف (Description):** وصف قصير للتعديل (ما هو، مميزاته الخاصة، إلخ).
- **الرؤية (Visibility):** يوصى بتعيين هذا على **Private** (خاص) أولاً للتحقق من كيف يبدو كل شيء على صفحة Steam، وتغييره إلى **Public** (عام) لاحقاً.
- **صورة المعاينة (Preview Image):** حدد الصورة المصغرة التي قمت بتجهيزها في الخطوة 1.

بمجرد ملء البيانات، انقر فوق **Upload** (رفع). إذا سار كل شيء على ما يرام، فستظهر الحالة في الأسفل كـ **"Success"** (نجاح).

## 🧪 الاختبار

يستخدم هذا المشروع `pytest` للاختبار الآلي.

1. ثبّت اعتماديات التطوير:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. قم بتشغيل حزمة الاختبارات مع التغطية (coverage):
   ```bash
   pytest
   ```
   *ملاحظة: مفاتيح API الصالحة أو التثبيت الحقيقي للعبة Haydee **غير مطلوبة** لتشغيل الاختبارات، حيث يتم محاكاة الاعتماديات الخارجية ونظام الملفات بأمان.*

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.