> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# [Haydee](https://store.steampowered.com/app/530890/Haydee/) Outfit Generator (ขับเคลื่อนโดย Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ไปป์ไลน์ Python อัตโนมัติสำหรับสร้างเทกซ์เจอร์ชุดแต่งกายแบบกำหนดเองสำหรับเกม [Haydee](https://store.steampowered.com/app/530890/Haydee/) โดยใช้ Google Gemini API

> [!TIP]
> **ไม่ถนัดใช้งานคอมมานด์ไลน์ใช่ไหม?** ลองใช้ [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui) ดูสิ! มันคืออินเทอร์เฟซแบบกราฟิกที่ทันสมัยและพร้อมใช้งาน ซึ่งช่วยให้คุณสร้างชุดคอสตูมแบบกำหนดเองได้อย่างง่ายดาย โดยไม่ต้องยุ่งยากกับเทอร์มินัลหรือตัวแปรสภาพแวดล้อม ดาวน์โหลดเวอร์ชันล่าสุดเพื่อเริ่มต้นใช้งานได้ทันที!

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

## 📋 สิ่งที่ต้องเตรียมพร้อม

- **Python 3.12+**

### 🔑 วิธีรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/app/apikey)
2. ลงชื่อเข้าใช้ด้วยบัญชี Google ของคุณ
3. คลิกปุ่ม **"Create API key"**
4. หากมีข้อความแจ้งเตือน ให้อ่านและยอมรับข้อกำหนดในการให้บริการ
5. คลิกที่ **"Create API key in new project"** (หรือใช้โปรเจกต์ที่มีอยู่แล้ว)
6. คัดลอกคีย์ที่สร้างขึ้น คุณจะต้องใช้มันสำหรับไฟล์ `.env` ในขั้นตอนการตั้งค่าด้านล่าง

## 💻 การติดตั้ง (Local)

### ติดตั้งผ่าน pip (แนะนำ)
วิธีที่ง่ายที่สุดในการติดตั้งเครื่องมือสร้างนี้คือติดตั้งโดยตรงจาก PyPI:
```bash
pip install haydee-outfit-generator
```

### ติดตั้งจาก Source Code
1. โคลน Repository
2. ติดตั้ง dependencies:
   ```bash
   pip install .
   ```

3. คัดลอกไฟล์ `.env.example` ไปเป็น `.env` (หรือสร้างใหม่) และตั้งค่าตัวแปรของคุณ:
* `GEMINI_API_KEY`: คีย์ Google Gemini API ของคุณ
* `HAYDEE_PATH`: พาธแบบเต็ม (Absolute path) ไปยังโฟลเดอร์ที่ติดตั้งเกม Haydee ของคุณ
* `IMAGE_RESOLUTION`: (ตัวเลือก) ความละเอียดของเอาต์พุต ค่าเริ่มต้นคือ `4K` สามารถตั้งค่าเป็น `2K` (2048x2048) ได้หากต้องการ
* `MODEL_NAME`: (ตัวเลือก) โมเดล AI ของ Gemini ที่จะใช้ ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`

## 🐳 การติดตั้ง (Docker)

หากคุณต้องการรันโปรเจกต์โดยไม่ต้องการติดตั้ง Python บนเครื่องของคุณ คุณสามารถใช้ Docker ได้

1. ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. สร้างไฟล์ `.env` ของคุณ และตั้งค่า `GEMINI_API_KEY` กับ `HAYDEE_PATH`
   * หมายเหตุ: `HAYDEE_PATH` ในไฟล์ `.env` **ต้องเป็น** พาธแบบเต็มบนเครื่อง Windows โฮสต์ของคุณ (เช่น `C:\Program Files (x86)\Steam\steamapps\common\Haydee`)

## 🚀 การใช้งาน

### การรันบนเครื่อง Local

**1. การสร้างชุดแบบเดี่ยว (Single Outfit)**
รันคำสั่ง `generate` โดยระบุชื่อม็อด, คำอธิบายสไตล์ที่ต้องการ และชื่อผู้สร้าง (ระบุหรือไม่ก็ได้):

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(เคล็ดลับ: คุณสามารถละคำว่า `generate` เพื่อให้คำสั่งสั้นลงได้: `haydee-gen --name ...`)*

**พารามิเตอร์สำหรับการสร้างเพียงบางส่วน**
คุณสามารถเลือกที่จะข้ามบางส่วนของกระบวนการสร้างเพื่อประหยัดเวลา หรือลดการเรียกใช้ API ได้ หากคุณเคยสร้างมันไว้แล้วในการรันครั้งก่อนๆ:
* `--skip-d`: ข้ามการสร้าง Diffuse Texture (`Suit_D.dds`) จะต้องมีเทกซ์เจอร์ที่เคยถูกสร้างไว้ก่อนหน้านี้ มิฉะนั้นคำสั่งจะล้มเหลว หากใส่แฟล็กนี้ อาร์กิวเมนต์ `--style` จะไม่จำเป็นต้องระบุก็ได้
* `--skip-s`: ข้ามการสร้าง Material Mask และ Specular Map (`Suit_S.dds`)
* `--skip-n`: ข้ามการสร้าง Normal Map (`Suit_N.dds`)

เมื่อข้ามการสร้างแมป (`--skip-s` หรือ `--skip-n`) โดยที่ยังไม่เคยสร้างไว้ก่อนหน้านี้ ชุดที่ถูกสร้างขึ้นจะทำการสำรองและหันไปใช้แมปพื้นฐาน (Neutral Maps) ของ Haydee สำหรับสล็อตเหล่านั้นแทนได้อย่างปลอดภัย

สคริปต์จะอ่านเทกซ์เจอร์พื้นฐานโดยอัตโนมัติ, ติดต่อไปยัง Gemini API เพื่อสร้าง Diffuse Texture (`Suit_D.dds`), จากนั้นจะร้องขอ Material Mask ซึ่งจะถูกนำไปรวมไว้ใน Specular Map (`Suit_S.dds`) นอกจากนี้ ยังมีการสร้าง Tangent Space Normal Map (`Suit_N.dds`) แบบปรับแต่งขึ้นมาควบคู่ไปกับ Diffuse Texture เพื่อทำให้วัสดุที่สร้างโดย AI มีพื้นผิว 3 มิติและรายละเอียดที่สอดคล้องกัน ม็อดที่เสร็จสมบูรณ์จะถูกสร้างขึ้นในโฟลเดอร์ `Haydee/Outfits` ของคุณ พร้อมใช้งานได้ทันที!

**2. การจัดกลุ่มชุดเข้าด้วยกันเป็น Multi-Mod**
หากคุณสร้างชุดไว้หลายชุดและต้องการจัดกลุ่มให้เป็นม็อดเดียว โดยสามารถสลับตัวเลือกรูปแบบได้ (เช่น รวมเป็นชุด "Rainbow" ชุดเดียวที่มีตัวเลือกสลับสีต่างๆ):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` เป็นแฟล็กตัวเลือกที่จะลบโฟลเดอร์ม็อดเดี่ยวต้นฉบับและไฟล์คอนฟิกต่างๆ ทิ้ง หลังจากที่ทำการจัดกลุ่มสำเร็จแล้ว

### การรันด้วย Docker

คุณสามารถใช้ Docker Compose เพื่อเมานท์ไดเรกทอรี Haydee ของคุณโดยอัตโนมัติและรันคำสั่งต่างๆ:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 การเผยแพร่ไปยัง Steam Workshop

เมื่อคุณพร้อมที่จะแบ่งปันชุดที่คุณสร้างขึ้น คุณสามารถอัปโหลดไปยัง Steam Workshop ได้โดยตรงผ่านเครื่องมือที่มีอยู่ในเกม

### 1. เตรียมรูปขนาดย่อ (Thumbnail)
- สร้างรูปภาพพรีวิวสำหรับม็อดของคุณ (`preview.png` หรือ `preview.jpg`)
- รูปภาพควรเป็นสี่เหลี่ยมจัตุรัส (เช่น 512x512 หรือ 256x256)
- นำรูปภาพนี้ไปใส่ไว้ในโฟลเดอร์ม็อดของคุณ

### 2. เปิด Edith Editor
เครื่องมือสำหรับอัปโหลดจะอยู่ในเอดิเตอร์ของเกม ไม่ได้อยู่ในตัวเกมหลัก:
- ไปที่โฟลเดอร์หลักที่คุณติดตั้งเกม Haydee ไว้
- รันไฟล์ `Edith.exe`
- ที่แถบเมนูด้านบน ให้เลือก **Tool -> Workshop Uploader**

### 3. กรอกข้อมูลสำหรับอัปโหลด
ในหน้าต่างอัปโหลด ให้กรอกข้อมูลในช่องต่างๆ ดังนี้:
- **Mod Content:** ที่ด้านบนสุดของฟอร์มอัปโหลด จะมีช่องข้อความพร้อมปุ่ม **Browse** อยู่ด้านล่าง คุณจะต้องใช้ส่วนนี้เพื่อสร้างรายการไฟล์ที่จะทำการอัปโหลด:
  1. คลิก **Browse** แล้วเพิ่มโฟลเดอร์หลักของม็อดคุณ (เช่น เลือก `Outfits/NeonSurge`)
  2. คลิก **Browse** อีกครั้ง แล้วเพิ่มไฟล์รูปแบบกำหนดค่า `.outfit` ของคุณ (เช่น เลือก `Outfits/NeonSurge.outfit`)
  *(วิธีนี้จะช่วยให้มั่นใจได้ว่าคุณรวมไฟล์ทั้งหมดที่จำเป็นในการทำให้ม็อดทำงานได้ครบถ้วนแล้ว)*
- **Title:** ชื่อชุดของคุณ (ชื่อนี้จะแสดงบนหน้า Steam)
- **Description:** คำอธิบายสั้นๆ ของม็อด (ว่าเป็นม็อดเกี่ยวกับอะไร, มีคุณสมบัติพิเศษอะไรบ้าง ฯลฯ)
- **Visibility:** แนะนำให้ตั้งค่านี้เป็น **Private** (ส่วนตัว) ก่อน เพื่อตรวจสอบดูว่าทุกอย่างบนหน้า Steam แสดงผลถูกต้องหรือไม่ แล้วจึงค่อยเปลี่ยนเป็น **Public** (สาธารณะ) ในภายหลัง
- **Preview Image:** เลือกรูปภาพขนาดย่อที่คุณเตรียมไว้ในขั้นตอนที่ 1

เมื่อกรอกข้อมูลครบถ้วนแล้ว ให้คลิก **Upload** หากทุกอย่างเรียบร้อย สถานะที่ด้านล่างจะแสดงคำว่า **"Success"**

## 🧪 การทดสอบ

โปรเจกต์นี้ใช้ `pytest` สำหรับการทดสอบอัตโนมัติ

1. ติดตั้ง development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. รันชุดทดสอบพร้อมกับประเมินความครอบคลุม (coverage):
   ```bash
   pytest
   ```
   *หมายเหตุ: **ไม่จำเป็น** ต้องมี API Keys ที่ใช้งานได้จริง หรือตัวเกม Haydee ที่ติดตั้งไว้จริงเพื่อใช้ในการรันการทดสอบ เนื่องจากระบบจะทำการม็อค (mock) การอ้างอิงภายนอกและระบบไฟล์ไว้ให้อย่างปลอดภัยแล้ว*

## 📄 สัญญาอนุญาต (License)

โปรเจกต์นี้อยู่ภายใต้สัญญาอนุญาต MIT - ดูรายละเอียดเพิ่มเติมได้ในไฟล์ [LICENSE](LICENSE)