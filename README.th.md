> 🌐 **Languages:** [English](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.md) | [Русский](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ru.md) | [ไทย](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.th.md) | [中文](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.zh.md) | [Español](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.es.md) | [العربية](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ar.md)

# เครื่องมือสร้างชุด [Haydee](https://store.steampowered.com/app/530890/Haydee/) (ขับเคลื่อนโดย Gemini)

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
> **ไม่ถนัดใช้งานคอมมานด์ไลน์ใช่ไหม?** ลองดู [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui) สิ! มันเป็นอินเทอร์เฟซแบบกราฟิกที่ทันสมัยและพร้อมใช้งาน ซึ่งช่วยให้คุณสร้างชุดคัสตอมได้อย่างง่ายดายโดยไม่ต้องยุ่งยากกับเทอร์มินัลหรือตัวแปรสภาพแวดล้อม ดาวน์โหลดรีลีสล่าสุดเพื่อเริ่มต้นใช้งานได้ทันที!

### 🤖 การตรวจสอบความถูกต้องด้วย LLM-as-a-Judge แบบสองรูปภาพหลายเกณฑ์ (Two-Image Multi-Criteria)
โปรเจกต์นี้มีระบบ **ลูปฟีดแบ็กการประกันคุณภาพ (QA)** อัตโนมัติขั้นสูง ในขณะที่โมเดลที่ทำงานได้เร็ว (เช่น `gemini-3.1-flash-image`) ทำหน้าที่วาดพื้นผิว (texture) โมเดลที่มีความสามารถในการให้เหตุผลสูงกว่า (เช่น `gemini-3.1-pro`) จะทำหน้าที่เป็นผู้ตรวจสอบ QA ที่เข้มงวด โดยใช้แนวทางแบบ **สองรูปภาพหลายเกณฑ์ (Two-Image Multi-Criteria)** 

ผู้ตรวจสอบจะเปรียบเทียบพื้นผิว UV ที่สร้างขึ้นมาแบบวางเคียงข้างกันกับเทมเพลตเปล่าต้นฉบับ เพื่อประเมินกฎเกณฑ์โครงสร้างเฉพาะอย่างเป็นอิสระต่อกัน:
1. **กฎใบหน้า (Face Rule):** ตรวจสอบให้แน่ใจว่าหมวกกันน็อกของตัวละครจะต้องไม่มีใบหน้าโดยสมบูรณ์ (ไม่มีลักษณะของมนุษย์ แว่นตา หรือหน้ากากช่วยหายใจ)
2. **กฎรอยต่อลำตัว (Torso Seam Rule):** ตรวจสอบว่าชิ้นส่วนเสื้อผ้า/ชุดเกราะบริเวณลำตัวด้านหน้าและด้านหลังเข้ากันได้อย่างพอดี เพื่อป้องกันไม่ให้เห็นรอยต่อในรูปแบบ 3 มิติ
3. **กฎขาทั้งสองข้าง (Legs Rule):** ตรวจสอบให้แน่ใจว่าขาซ้ายและขาขวาถูกแยกออกจากกันเป็นคนละส่วน เพื่อป้องกันไม่ให้ AI วาดขาทั้งสองข้างซ้อนกันอยู่ในรูปทรงเดียว

หากมีการละเมิดกฎใดๆ ผู้ตรวจสอบจะปฏิเสธรูปภาพนั้น พร้อมทั้งให้ฟีดแบ็กที่เจาะจงว่าส่วนใดที่ผิดพลาด และบังคับให้ตัวสร้างชุดทำการวาดพื้นผิวขึ้นมาใหม่เพื่อแก้ไขข้อผิดพลาดเหล่านั้นโดยเฉพาะ

## ✨ ตัวอย่างสิ่งที่สร้างขึ้น

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

## 📋 สิ่งที่ต้องเตรียมพร้อม

- **Python 3.12+**

### 🔑 การรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/app/apikey)
2. ลงชื่อเข้าใช้ด้วยบัญชี Google ของคุณ
3. คลิกปุ่ม **"Create API key"**
4. หากมีข้อความแจ้งเตือน ให้อ่านและยอมรับเงื่อนไขการให้บริการ
5. คลิกที่ **"Create API key in new project"** (หรือใช้โปรเจกต์ที่มีอยู่แล้ว)
6. คัดลอกคีย์ที่สร้างขึ้น คุณจะต้องใช้คีย์นี้สำหรับไฟล์ `.env` ในขั้นตอนการติดตั้งด้านล่าง

## 💻 การติดตั้ง (ในเครื่อง Local)

### ติดตั้งผ่าน pip (แนะนำ)
วิธีที่ง่ายที่สุดในการติดตั้งเครื่องมือสร้างชุดคือการติดตั้งโดยตรงจาก PyPI:
```bash
pip install haydee-outfit-generator
```

### ติดตั้งจากซอร์สโค้ด (Source)
1. โคลน (Clone) repository
2. ติดตั้ง dependencies:
   ```bash
   pip install .
   ```

3. คัดลอกไฟล์ `.env.example` ไปเป็น `.env` (หรือสร้างใหม่ขึ้นมา) และตั้งค่าตัวแปรต่างๆ ของคุณ:
* `GEMINI_API_KEY`: Google Gemini API Key ของคุณ
* `HAYDEE_PATH`: พาธแบบเต็ม (Absolute path) ไปยังไดเรกทอรีที่คุณติดตั้งเกม Haydee
* `IMAGE_RESOLUTION`: (ไม่บังคับ) ความละเอียดของไฟล์ผลลัพธ์ ค่าเริ่มต้นคือ `4K` สามารถตั้งเป็น `2K` (2048x2048) ได้หากต้องการ
* `MODEL_NAME`: (ไม่บังคับ) โมเดล Gemini AI ที่จะใช้สร้างพื้นผิว ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`
* `VALIDATOR_MODEL`: (ไม่บังคับ) โมเดลการให้เหตุผลที่จะใช้สำหรับการตรวจสอบ QA ค่าเริ่มต้นคือ `gemini-3.1-pro-preview`

## 🐳 การติดตั้ง (Docker)

หากคุณต้องการรันโปรเจกต์โดยไม่ต้องติดตั้ง Python ลงในเครื่อง คุณสามารถใช้ Docker ได้

1. ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. สร้างไฟล์ `.env` ของคุณ และกำหนดค่า `GEMINI_API_KEY` กับ `HAYDEE_PATH`
   * หมายเหตุ: ค่า `HAYDEE_PATH` ในไฟล์ `.env` **ต้อง** เป็นพาธแบบเต็มบนเครื่องโฮสต์ Windows ของคุณ (เช่น `C:\Program Files (x86)\Steam\steamapps\common\Haydee`)

## 🚀 การใช้งาน

### การรันบนเครื่อง Local

**1. การสร้างชุดแบบชุดเดียว**
รันคำสั่ง `generate` โดยระบุชื่อม็อด, คำอธิบายสไตล์ที่ต้องการ และสามารถใส่ชื่อผู้สร้างได้ (ไม่บังคับ):

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(เคล็ดลับ: คุณสามารถละเว้นคำว่า `generate` เพื่อให้คำสั่งสั้นลงได้: `haydee-gen --name ...`)*

**พารามิเตอร์การสร้างแบบบางส่วน (Partial Generation)**
คุณสามารถเลือกข้ามขั้นตอนบางส่วนในกระบวนการสร้างเพื่อประหยัดเวลาหรือการเรียกใช้งาน API ได้ หากคุณเคยสร้างส่วนนั้นๆ ไว้แล้วในการรันครั้งก่อนหน้า:
* `--skip-d`: ข้ามการสร้างพื้นผิวแบบ diffuse (`Suit_D.dds`) คุณจะต้องมีพื้นผิวที่สร้างไว้ก่อนหน้านี้อยู่แล้ว มิฉะนั้นคำสั่งจะล้มเหลว หากใช้แฟล็กนี้ อาร์กิวเมนต์ `--style` จะไม่ใช่สิ่งจำเป็น
* `--skip-s`: ข้ามการสร้างมาสก์วัสดุ (material mask) และ specular map (`Suit_S.dds`)
* `--skip-n`: ข้ามการสร้าง normal map (`Suit_N.dds`)
* `--max-retries`: (ไม่บังคับ) จำนวนครั้งสูงสุดที่จะพยายามสร้างใหม่ หากพื้นผิวไม่ผ่านการตรวจสอบความถูกต้องของ QA ค่าเริ่มต้นคือ `3`

เมื่อข้ามการสร้างแมป (`--skip-s` หรือ `--skip-n`) โดยที่ไม่ได้สร้างแมปเหล่านั้นไว้ก่อน ชุดที่สร้างขึ้นจะกลับไปใช้แมปแบบเป็นกลางพื้นฐานของเกม Haydee สำหรับสล็อตเหล่านั้นอย่างปลอดภัย

สคริปต์จะอ่านพื้นผิวฐานโดยอัตโนมัติ, ติดต่อกับ Gemini API เพื่อสร้างพื้นผิวแบบ diffuse (`Suit_D.dds` โดยใช้ลูปตรวจสอบความถูกต้อง QA แบบสองรูปภาพอัตโนมัติ) จากนั้นจะขอมัสก์วัสดุเพื่อนำมาแพ็กรวมไว้ใน specular map (`Suit_S.dds`) นอกจากนี้ ยังมีการสร้าง Tangent Space Normal Map แบบคัสตอม (`Suit_N.dds`) ไปพร้อมกับพื้นผิวแบบ diffuse เพื่อให้วัสดุที่สร้างด้วย AI ใหม่มีมิติและรายละเอียดแบบ 3 มิติที่เข้ากัน ม็อดขั้นสุดท้ายจะถูกสร้างขึ้นในโฟลเดอร์ `Haydee/Outfits` ของคุณ พร้อมใช้งานทันที!

**2. การจัดกลุ่มชุดเป็นแบบ Multi-Mod**
หากคุณสร้างชุดไว้หลายชุดและต้องการจัดกลุ่มให้เป็นม็อดเดียวที่มีตัวเลือกให้สลับเปลี่ยนได้ (เช่น สร้างชุด "Rainbow" ชุดเดียวแต่มีสล็อตเปลี่ยนสีต่างๆ ได้):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` เป็นแฟล็กเสริม (ไม่บังคับ) ที่จะทำการลบโฟลเดอร์ม็อดเดี่ยวและไฟล์ปรับแต่งต้นฉบับทิ้งหลังจากจัดกลุ่มเรียบร้อยแล้ว

### การรันด้วย Docker

คุณสามารถใช้ Docker Compose เพื่อเมานต์ (mount) ไดเรกทอรี Haydee ของคุณโดยอัตโนมัติและรันคำสั่ง:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 การเผยแพร่ไปยัง Steam Workshop

เมื่อคุณพร้อมที่จะแบ่งปันชุดที่คุณสร้างขึ้น คุณสามารถอัปโหลดไปยัง Steam Workshop ได้โดยตรง โดยใช้เครื่องมือที่ติดมากับตัวเกม

### 1. เตรียมรูปขนาดย่อ (Thumbnail)
- สร้างรูปภาพพรีวิวสำหรับม็อดของคุณ (`preview.png` หรือ `preview.jpg`)
- รูปภาพควรเป็นสี่เหลี่ยมจัตุรัส (เช่น 512x512 หรือ 256x256)
- นำรูปภาพนี้ไปวางไว้ในโฟลเดอร์ม็อดของคุณ

### 2. เปิดโปรแกรม Edith Editor
เครื่องมืออัปโหลดจะอยู่ในตัวแก้ไข (editor) ของเกม ไม่ใช่ในตัวเกมโดยตรง:
- ไปที่โฟลเดอร์หลักที่คุณติดตั้งเกม Haydee ไว้
- รันไฟล์ `Edith.exe`
- ที่แถบเมนูด้านบน ให้เลือก **Tool -> Workshop Uploader**

### 3. กรอกข้อมูลการอัปโหลด
ในหน้าต่างการอัปโหลด ให้กรอกข้อมูลในช่องต่อไปนี้:
- **Mod Content:** ที่ด้านบนสุดของฟอร์มอัปโหลด จะมีช่องข้อความพร้อมกับปุ่ม **Browse** อยู่ด้านล่าง คุณจะใช้ปุ่มนี้เพื่อสร้างรายการไฟล์ที่จะอัปโหลด:
  1. คลิก **Browse** และเพิ่มโฟลเดอร์หลักของม็อดของคุณ (ตัวอย่างเช่น เลือก `Outfits/NeonSurge`)
  2. คลิก **Browse** อีกครั้ง และเพิ่มไฟล์กำหนดคุณสมบัติ `.outfit` ของคุณ (ตัวอย่างเช่น เลือก `Outfits/NeonSurge.outfit`)
  *(ขั้นตอนเหล่านี้เพื่อให้แน่ใจว่าคุณได้รวมไฟล์ทั้งหมดที่จำเป็นสำหรับการทำงานของม็อดไว้ครบถ้วน)*
- **Title:** ชื่อชุดของคุณ (ชื่อนี้จะแสดงบน Steam)
- **Description:** คำอธิบายสั้นๆ เกี่ยวกับม็อด (เป็นม็อดอะไร, ฟีเจอร์พิเศษ, ฯลฯ)
- **Visibility:** ขอแนะนำให้ตั้งค่าเป็น **Private** ก่อน เพื่อตรวจสอบความเรียบร้อยในหน้าเพจ Steam จากนั้นค่อยเปลี่ยนเป็น **Public** ในภายหลัง
- **Preview Image:** เลือกรูปภาพขนาดย่อที่คุณเตรียมไว้ในขั้นตอนที่ 1

เมื่อกรอกข้อมูลเรียบร้อยแล้ว ให้คลิก **Upload** หากทุกอย่างราบรื่น สถานะที่ด้านล่างจะแสดงคำว่า **"Success"**

## 🧪 การทดสอบ (Testing)

โปรเจกต์นี้ใช้ `pytest` สำหรับการทดสอบอัตโนมัติ

1. ติดตั้ง development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. รันชุดการทดสอบพร้อมกับดู coverage:
   ```bash
   pytest
   ```
   *หมายเหตุ: **ไม่จำเป็นต้อง** ใช้ API Keys ที่ใช้งานได้จริงหรือติดตั้งเกม Haydee ไว้สำหรับการรันทดสอบ เนื่องจากระบบที่ต้องพึ่งพาจากภายนอกและระบบไฟล์ได้ถูกจำลอง (mocked) ไว้แล้วอย่างปลอดภัย*

## 📄 ลิขสิทธิ์ (License)

โปรเจกต์นี้ได้รับอนุญาตภายใต้ MIT License - ดูรายละเอียดได้ที่ไฟล์ [LICENSE](LICENSE)