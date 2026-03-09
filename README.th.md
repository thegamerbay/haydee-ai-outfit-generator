> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# เครื่องมือสร้างชุดสำหรับ [Haydee](https://store.steampowered.com/app/530890/Haydee/) (ขับเคลื่อนโดย Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ไปป์ไลน์ Python อัตโนมัติสำหรับสร้างพื้นผิวชุดคัสตอมสำหรับเกม [Haydee](https://store.steampowered.com/app/530890/Haydee/) โดยใช้ Google Gemini API

> [!TIP]
> **ไม่ชอบการใช้คอมมานด์ไลน์ใช่ไหม?** ลองดู [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui) สิ! มันเป็นอินเทอร์เฟซแบบกราฟิกที่ทันสมัยและพร้อมใช้งาน ซึ่งช่วยให้คุณสร้างชุดคัสตอมได้อย่างง่ายดายโดยไม่ต้องยุ่งยากกับเทอร์มินัลหรือตัวแปรสภาพแวดล้อม ดาวน์โหลดเวอร์ชันล่าสุดเพื่อเริ่มต้นใช้งานได้ทันที!

### 🤖 การตรวจสอบความถูกต้องด้วย LLM-as-a-Judge แบบสองรูปภาพและหลายเกณฑ์ (Two-Image Multi-Criteria)
โปรเจกต์นี้มีระบบ **Quality Assurance Feedback Loop (ลูปข้อเสนอแนะเพื่อประกันคุณภาพ)** อัตโนมัติขั้นสูง ในขณะที่โมเดลที่ทำงานเร็ว (เช่น `gemini-3.1-flash-image`) ทำหน้าที่วาดพื้นผิว โมเดลที่มีความสามารถในการใช้เหตุผลสูงกว่า (เช่น `gemini-3.1-pro`) จะทำหน้าที่เป็นผู้ตรวจสอบ QA อย่างเข้มงวด โดยใช้วิธีการ **Two-Image Multi-Criteria (สองรูปภาพและหลายเกณฑ์)** 

ผู้ตรวจสอบจะเปรียบเทียบพื้นผิว UV ที่สร้างขึ้นมาเทียบกับเทมเพลตเปล่าต้นฉบับแบบเคียงข้างกัน เพื่อประเมินกฎเกณฑ์โครงสร้างเฉพาะอย่างเป็นอิสระต่อกัน:
1. **กฎใบหน้า (Face Rule):** ตรวจสอบให้แน่ใจว่าหมวกกันน็อกของตัวละครยังคงไม่มีใบหน้าใดๆ อย่างสมบูรณ์ (ไม่มีลักษณะของมนุษย์ แว่นตา หรือหน้ากากช่วยหายใจ)
2. **กฎรอยต่อลำตัว (Torso Seam Rule):** ตรวจสอบว่าชิ้นส่วนเสื้อผ้า/ชุดเกราะบริเวณลำตัวด้านหน้าและด้านหลังเข้ากันได้อย่างสมบูรณ์ เพื่อป้องกันไม่ให้เห็นรอยต่อในรูปแบบ 3 มิติ
3. **กฎขาทั้งสองข้าง (Legs Rule):** ตรวจสอบให้แน่ใจว่าขาซ้ายและขาขวาถูกแยกเป็นส่วนของแขนขาอย่างอิสระ เพื่อป้องกันไม่ให้ AI วาดขาทั้งสองข้างรวมอยู่ในรูปทรงเดียวกัน

หากมีการละเมิดกฎใดๆ ผู้ตรวจสอบจะปฏิเสธรูปภาพนั้น พร้อมให้ข้อเสนอแนะที่เฉพาะเจาะจงว่าส่วนใดที่ผิดพลาด และบังคับให้เครื่องมือสร้างวาดพื้นผิวใหม่เพื่อแก้ไขข้อผิดพลาดเหล่านั้นโดยเฉพาะ

## ✨ ตัวอย่างผลงานที่สร้าง

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

## 📋 ข้อกำหนดเบื้องต้น

- **Python 3.12+**

### 🔑 วิธีรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/app/apikey)
2. เข้าสู่ระบบด้วยบัญชี Google ของคุณ
3. คลิกปุ่ม **"Create API key"**
4. หากมีการแจ้งเตือน ให้อ่านและยอมรับเงื่อนไขการให้บริการ
5. คลิกที่ **"Create API key in new project"** (หรือใช้โปรเจกต์ที่มีอยู่แล้ว)
6. คัดลอกคีย์ที่สร้างขึ้นมา คุณจะต้องใช้มันสำหรับไฟล์ `.env` ในขั้นตอนการติดตั้งด้านล่าง

## 💻 การติดตั้ง (Local)

### ติดตั้งผ่าน pip (แนะนำ)
วิธีที่ง่ายที่สุดในการติดตั้งเครื่องมือสร้างคือการติดตั้งโดยตรงจาก PyPI:
```bash
pip install haydee-outfit-generator
```

### ติดตั้งจาก Source
1. โคลน (Clone) พื้นที่เก็บข้อมูล (repository)
2. ติดตั้ง dependencies:
   ```bash
   pip install .
   ```

3. คัดลอกไฟล์ `.env.example` เป็น `.env` (หรือสร้างไฟล์ใหม่) และกำหนดค่าตัวแปรของคุณ:
* `GEMINI_API_KEY`: คีย์ Google Gemini API ของคุณ
* `HAYDEE_PATH`: พาธสัมบูรณ์ (Absolute path) ไปยังไดเรกทอรีที่ติดตั้งเกม Haydee
* `IMAGE_RESOLUTION`: (ไม่บังคับ) ความละเอียดของเอาต์พุต ค่าเริ่มต้นคือ `4K` สามารถตั้งค่าเป็น `2K` (2048x2048) ได้หากต้องการ
* `MODEL_NAME`: (ไม่บังคับ) โมเดล AI ของ Gemini ที่จะใช้สำหรับการสร้างพื้นผิว ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`
* `VALIDATOR_MODEL`: (ไม่บังคับ) โมเดลการใช้เหตุผลที่จะใช้สำหรับการตรวจสอบ QA ค่าเริ่มต้นคือ `gemini-3.1-pro-preview`

## 🐳 การติดตั้ง (Docker)

หากคุณต้องการเรียกใช้โปรเจกต์โดยไม่ต้องติดตั้ง Python ลงในเครื่อง คุณสามารถใช้ Docker ได้

1. ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. สร้างไฟล์ `.env` ของคุณ และตั้งค่า `GEMINI_API_KEY` และ `HAYDEE_PATH`
   * หมายเหตุ: `HAYDEE_PATH` ในไฟล์ `.env` **ต้องเป็น** พาธสัมบูรณ์บนเครื่องโฮสต์ Windows ของคุณ (เช่น `C:\Program Files (x86)\Steam\steamapps\common\Haydee`)

## 🚀 วิธีใช้งาน

### การเรียกใช้งานในเครื่อง (Locally)

**1. การสร้างชุดเดี่ยว (Single Outfit)**
เรียกใช้คำสั่ง `generate` โดยระบุชื่อม็อด คำอธิบายสไตล์ที่ต้องการ และสามารถระบุชื่อผู้สร้าง (author) ได้หากต้องการ:

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(เคล็ดลับ: คุณสามารถละเว้นคำว่า `generate` เพื่อให้คำสั่งสั้นลงได้: `haydee-gen --name ...`)*

**พารามิเตอร์การสร้างบางส่วน (Partial Generation)**
คุณสามารถเลือกข้ามบางส่วนของกระบวนการสร้างเพื่อประหยัดเวลาหรือการเรียกใช้ API ได้ หากคุณได้สร้างสิ่งเหล่านั้นไปแล้วในการรันครั้งก่อนหน้า:
* `--skip-d`: ข้ามการสร้างพื้นผิวแบบกระจายแสง (diffuse texture) (`Suit_D.dds`) ต้องมีพื้นผิวที่สร้างไว้ก่อนหน้านี้อยู่ มิฉะนั้นคำสั่งจะล้มเหลว หากใช้พารามิเตอร์นี้ อาร์กิวเมนต์ `--style` จะไม่บังคับ
* `--skip-s`: ข้ามการสร้างมาสก์วัสดุและแผนที่สะท้อนแสง (specular map) (`Suit_S.dds`)
* `--skip-n`: ข้ามการสร้างนอร์มอลแมป (normal map) (`Suit_N.dds`)
* `--max-retries`: (ไม่บังคับ) จำนวนครั้งสูงสุดในการพยายามสร้างใหม่หากพื้นผิวไม่ผ่านการตรวจสอบ QA ค่าเริ่มต้นคือ `3`

เมื่อข้ามการสร้างแมป (`--skip-s` หรือ `--skip-n`) โดยไม่ได้สร้างไว้ก่อนหน้านี้ ชุดที่สร้างขึ้นจะสามารถใช้งานได้อย่างปลอดภัยโดยจะย้อนกลับไปใช้แมปพื้นฐานของเกม Haydee สำหรับสล็อตเหล่านั้นแทน

สคริปต์จะอ่านพื้นผิวฐานโดยอัตโนมัติ ติดต่อไปยัง Gemini API เพื่อสร้างพื้นผิวแบบกระจายแสง (`Suit_D.dds` โดยใช้ลูปตรวจสอบ QA อัตโนมัติแบบสองรูปภาพ) จากนั้นจะขอมาสก์วัสดุซึ่งจะถูกแพ็กลงในแผนที่สะท้อนแสง (`Suit_S.dds`) นอกจากนี้ Tangent Space Normal Map (`Suit_N.dds`) แบบคัสตอมจะถูกสร้างขึ้นควบคู่กับพื้นผิวแบบกระจายแสง เพื่อให้วัสดุใหม่ที่สร้างโดย AI มีรายละเอียดและมิติความนูน 3 มิติที่เข้ากัน ม็อดขั้นสุดท้ายจะถูกสร้างขึ้นในโฟลเดอร์ `Haydee/Outfits` ของคุณและพร้อมใช้งานได้ทันที!

**2. การจัดกลุ่มชุดเป็น Multi-Mod**
หากคุณสร้างชุดไว้หลายชุดและต้องการจัดกลุ่มให้รวมอยู่ในม็อดเดียวโดยมีตัวเลือกให้สลับเปลี่ยนได้ (เช่น ในชุด "Rainbow" ชุดเดียวที่มีสล็อตสีต่างๆ ให้เลือก):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` เป็นแฟล็กเสริมที่จะลบโฟลเดอร์ม็อดเดี่ยวต้นฉบับและไฟล์คอนฟิกออกหลังจากจัดกลุ่มสำเร็จแล้ว

### การเรียกใช้งานด้วย Docker

คุณสามารถใช้ Docker Compose เพื่อเมานต์ (mount) ไดเรกทอรี Haydee ของคุณโดยอัตโนมัติและเรียกใช้คำสั่งได้:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 การเผยแพร่ไปยัง Steam Workshop

เมื่อคุณพร้อมที่จะแชร์ชุดที่สร้างขึ้น คุณสามารถอัปโหลดไปยัง Steam Workshop ได้โดยตรง โดยใช้เครื่องมือที่ติดมากับตัวเกม

### 1. เตรียมรูปขนาดย่อ (Thumbnail)
- สร้างรูปภาพพรีวิวสำหรับม็อดของคุณ (`preview.png` หรือ `preview.jpg`)
- รูปภาพควรเป็นสี่เหลี่ยมจัตุรัส (เช่น 512x512 หรือ 256x256)
- วางรูปภาพนี้ไว้ในโฟลเดอร์ม็อดของคุณ

### 2. เปิดใช้งาน Edith Editor
เครื่องมืออัปโหลดจะอยู่ในตัวแก้ไขของเกม ไม่ได้อยู่ในตัวเกมหลัก:
- ไปที่โฟลเดอร์ติดตั้งหลักของเกม Haydee
- เรียกใช้ `Edith.exe`
- ในแถบเมนูด้านบน ให้เลือก **Tool -> Workshop Uploader**

### 3. กรอกข้อมูลใน Uploader
ในหน้าต่างอัปโหลด ให้กรอกข้อมูลในช่องต่อไปนี้:
- **Mod Content:** ที่ด้านบนสุดของแบบฟอร์มอัปโหลด จะมีช่องข้อความพร้อมปุ่ม **Browse** อยู่ด้านล่าง คุณจะใช้ปุ่มนี้เพื่อสร้างรายการไฟล์ที่จะอัปโหลด:
  1. คลิก **Browse** และเพิ่มโฟลเดอร์หลักของม็อดคุณ (เช่น เลือก `Outfits/NeonSurge`)
  2. คลิก **Browse** อีกครั้งและเพิ่มไฟล์คอนฟิก `.outfit` ของคุณ (เช่น เลือก `Outfits/NeonSurge.outfit`)
  *(การทำเช่นนี้เพื่อให้แน่ใจว่าคุณได้รวมไฟล์ทั้งหมดที่จำเป็นสำหรับการทำงานของม็อดอย่างครบถ้วน)*
- **Title:** ชื่อชุดของคุณ (ชื่อนี้จะแสดงบน Steam)
- **Description:** คำอธิบายสั้นๆ เกี่ยวกับม็อด (คืออะไร มีฟีเจอร์พิเศษอะไรบ้าง ฯลฯ)
- **Visibility:** แนะนำให้ตั้งค่าเป็น **Private** (ส่วนตัว) ก่อน เพื่อตรวจสอบความเรียบร้อยบนหน้า Steam แล้วค่อยเปลี่ยนเป็น **Public** (สาธารณะ) ในภายหลัง
- **Preview Image:** เลือกรูปภาพขนาดย่อที่คุณเตรียมไว้ในขั้นตอนที่ 1

เมื่อกรอกข้อมูลเรียบร้อยแล้ว ให้คลิก **Upload** หากทุกอย่างราบรื่น สถานะที่ด้านล่างจะแสดงคำว่า **"Success"**

## 🧪 การทดสอบ

โปรเจกต์นี้ใช้ `pytest` สำหรับการทดสอบอัตโนมัติ

1. ติดตั้ง development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. รันชุดการทดสอบพร้อมตรวจสอบ coverage:
   ```bash
   pytest
   ```
   *หมายเหตุ: **ไม่จำเป็น** ต้องใช้ API Key ที่ใช้งานได้จริง หรือการติดตั้งเกม Haydee จริงในการรันการทดสอบ เนื่องจาก dependencies ภายนอกและระบบไฟล์ได้ถูกจำลอง (mocked) ไว้แล้วอย่างปลอดภัย*

## 📄 สัญญาอนุญาต (License)

โปรเจกต์นี้ได้รับอนุญาตภายใต้ MIT License - ดูรายละเอียดเพิ่มเติมได้ที่ไฟล์ [LICENSE](LICENSE)