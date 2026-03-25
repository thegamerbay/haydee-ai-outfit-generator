> 🌐 **Языки:** [English](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.md) | [Русский](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ru.md) | [ไทย](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.th.md) | [中文](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.zh.md) | [Español](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.es.md) | [العربية](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ar.md)

# Генератор нарядов для [Haydee](https://store.steampowered.com/app/530890/Haydee/) (на базе Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Автоматизированный Python-пайплайн для генерации пользовательских текстур нарядов для игры [Haydee](https://store.steampowered.com/app/530890/Haydee/) с использованием Google Gemini API.

> [!TIP]
> **Не любите командную строку?** Обратите внимание на [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! Это современный, готовый к использованию графический интерфейс, который позволяет легко создавать пользовательские наряды, не связываясь с терминалами или переменными окружения. Скачайте последний релиз, чтобы начать прямо сейчас!

### 🤖 Многокритериальная проверка по двум изображениям с использованием LLM-судьи
В этом проекте реализована передовая автоматизированная **петля обратной связи для контроля качества (QA)**. В то время как быстрая модель (например, `gemini-3.1-flash-image`) рисует текстуры, более мощная модель рассуждения (например, `gemini-3.1-pro`) выступает в роли строгого QA-инспектора, используя подход **многокритериальной оценки по двум изображениям**. 

Инспектор сравнивает сгенерированную UV-текстуру бок о бок с оригинальным пустым шаблоном для независимой оценки конкретных структурных правил:
1. **Правило лица (Face Rule):** Гарантирует, что шлем персонажа остается полностью безликим (никаких человеческих черт, очков или респираторов).
2. **Правило швов туловища (Torso Seam Rule):** Проверяет, что элементы одежды/брони на передней и задней частях туловища идеально совпадают, чтобы предотвратить видимые швы в 3D.
3. **Правило ног (Legs Rule):** Гарантирует, что левая и правая ноги рассматриваются как отдельные конечности, предотвращая ситуацию, когда ИИ рисует две ноги внутри одной формы.

Если какое-либо правило нарушено, инспектор отклоняет изображение, предоставляет конкретную обратную связь о том, что именно пошло не так, и заставляет генератор перерисовать текстуру, исправив эти конкретные ошибки.

## ✨ Примеры генерации

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

## 📋 Предварительные требования

- **Python 3.12+**

### 🔑 Получение API-ключа Gemini

1. Перейдите в [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Войдите с помощью вашей учетной записи Google.
3. Нажмите кнопку **"Create API key"**.
4. Если потребуется, прочитайте и примите условия обслуживания.
5. Нажмите на **"Create API key in new project"** (или используйте существующий проект).
6. Скопируйте сгенерированный ключ. Он понадобится вам для файла `.env` в шагах настройки ниже.

## 💻 Установка (Локально)

### Установка через pip (Рекомендуется)
Самый простой способ установить генератор — напрямую из PyPI:
```bash
pip install haydee-outfit-generator
```

### Установка из исходного кода
1. Склонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install .
   ```

3. Скопируйте `.env.example` в `.env` (или создайте новый) и настройте ваши переменные:
* `GEMINI_API_KEY`: Ваш API-ключ Google Gemini.
* `HAYDEE_PATH`: Абсолютный путь к каталогу установки Haydee.
* `IMAGE_RESOLUTION`: (Опционально) Выходное разрешение. По умолчанию `4K`. При необходимости можно установить `2K` (2048x2048).
* `MODEL_NAME`: (Опционально) ИИ-модель Gemini, используемая для генерации текстур. По умолчанию `gemini-3.1-flash-image-preview`.
* `VALIDATOR_MODEL`: (Опционально) Модель рассуждения для QA-проверки. По умолчанию `gemini-3.1-pro-preview`.

## 🐳 Установка (Docker)

Если вы предпочитаете запускать проект без локальной установки Python, вы можете использовать Docker.

1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Создайте файл `.env` и укажите `GEMINI_API_KEY` и `HAYDEE_PATH`.
   * Примечание: `HAYDEE_PATH` в файле `.env` **должен** быть абсолютным путем на вашей хост-машине с Windows (например, `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 Использование

### Локальный запуск

**1. Генерация одного наряда**
Выполните команду `generate`, указав название мода, желаемое описание стиля и, при желании, автора:

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(Совет: Вы можете опустить ключевое слово `generate` для более короткой команды: `haydee-gen --name ...`)*

**Параметры частичной генерации**
Вы можете выборочно пропускать части процесса генерации, чтобы сэкономить время или вызовы API, если вы уже сгенерировали их в предыдущих запусках:
* `--skip-d`: Пропускает генерацию диффузной текстуры (`Suit_D.dds`). Ранее сгенерированная текстура должна существовать, иначе команда завершится ошибкой. Если указан этот флаг, аргумент `--style` не является обязательным.
* `--skip-s`: Пропускает генерацию маски материалов и карты отражений (specular map) (`Suit_S.dds`).
* `--skip-n`: Пропускает генерацию карты нормалей (`Suit_N.dds`).
* `--max-retries`: (Опционально) Максимальное количество попыток повторной генерации в случае провала QA-проверки. По умолчанию `3`.

При пропуске генерации карт (`--skip-s` или `--skip-n`), если они не были сгенерированы ранее, созданный наряд безопасно переключится на использование базовых нейтральных карт Haydee для этих слотов.

Скрипт автоматически прочитает базовую текстуру, свяжется с Gemini API для генерации диффузной текстуры (`Suit_D.dds` с использованием автоматизированного цикла QA-проверки по двум изображениям), затем запросит маску материалов, которая упаковывается в карту отражений (`Suit_S.dds`). Кроме того, вместе с диффузной текстурой генерируется пользовательская карта нормалей в касательном пространстве (Tangent Space Normal Map, `Suit_N.dds`), чтобы придать новым материалам от ИИ соответствующий 3D-рельеф и детализацию. Финальный мод будет сгенерирован внутри вашей папки `Haydee/Outfits` и готов к использованию!

**2. Группировка нарядов в мультимод (Multi-Mod)**
Если вы сгенерировали несколько нарядов и хотите сгруппировать их в один мод с переключаемыми вариациями (например, в один наряд "Rainbow" с различными цветовыми слотами):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` — это опциональный флаг, который удалит исходные папки одиночных модов и конфигурации после их успешной группировки.

### Запуск с использованием Docker

Вы можете использовать Docker Compose для автоматического монтирования вашего каталога Haydee и выполнения команд:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 Публикация в Мастерской Steam (Steam Workshop)

Когда вы будете готовы поделиться сгенерированным нарядом, вы можете загрузить его напрямую в Мастерскую Steam с помощью встроенных инструментов игры.

### 1. Подготовка миниатюры
- Создайте изображение предпросмотра для вашего мода (`preview.png` или `preview.jpg`).
- Изображение должно быть квадратным (например, 512x512 или 256x256).
- Поместите это изображение в папку вашего мода.

### 2. Запуск редактора Edith
Инструменты загрузки находятся в редакторе игры, а не в самой игре:
- Перейдите в корневую папку установки Haydee.
- Запустите `Edith.exe`.
- В верхнем меню выберите **Tool -> Workshop Uploader**.

### 3. Заполнение данных загрузчика
В окне загрузчика заполните следующие поля:
- **Mod Content (Содержимое мода):** В самом верху формы загрузки есть текстовое поле, под которым находится кнопка **Browse**. С ее помощью вы сформируете список файлов для загрузки:
  1. Нажмите **Browse** и добавьте основную папку вашего мода (например, выберите `Outfits/NeonSurge`).
  2. Нажмите **Browse** еще раз и добавьте файл определения `.outfit` (например, выберите `Outfits/NeonSurge.outfit`).
  *(Это гарантирует включение полного набора файлов, необходимых для работы мода).*
- **Title (Название):** Название вашего наряда (оно будет отображаться в Steam).
- **Description (Описание):** Краткое описание мода (что это такое, особенности и т. д.).
- **Visibility (Видимость):** Рекомендуется сначала установить значение **Private**, чтобы проверить, как всё выглядит на странице в Steam, а позже изменить на **Public**.
- **Preview Image (Превью-изображение):** Выберите миниатюру, которую вы подготовили на шаге 1.

После заполнения нажмите **Upload**. Если всё прошло успешно, статус внизу покажет **"Success"**.

## 🧪 Тестирование

Этот проект использует `pytest` для автоматизированного тестирования.

1. Установите зависимости для разработки:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Запустите набор тестов с проверкой покрытия:
   ```bash
   pytest
   ```
   *Примечание: Действительные API-ключи или реальная установка Haydee **не требуются** для запуска тестов, так как внешние зависимости и файловая система безопасно эмулируются (mocked).*

## 📄 Лицензия

Этот проект лицензирован по лицензии MIT — подробности см. в файле [LICENSE](LICENSE).