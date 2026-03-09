> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Генератор костюмов для [Haydee](https://store.steampowered.com/app/530890/Haydee/) (на базе Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Автоматизированный Python-пайплайн для генерации пользовательских текстур костюмов для игры [Haydee](https://store.steampowered.com/app/530890/Haydee/) с использованием Google Gemini API.

> [!TIP]
> **Не любите командную строку?** Ознакомьтесь с [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! Это современный, готовый к использованию графический интерфейс, который позволяет легко создавать собственные костюмы без возни с терминалами или переменными окружения. Скачайте последний релиз, чтобы начать работу прямо сейчас!

### 🤖 Многокритериальная проверка по двум изображениям с LLM в качестве судьи (LLM-as-a-Judge)
В этом проекте реализован передовой автоматизированный **цикл обратной связи для контроля качества (QA)**. В то время как быстрая модель (например, `gemini-3.1-flash-image`) рисует текстуры, более мощная модель рассуждений (например, `gemini-3.1-pro`) выступает в роли строгого QA-инспектора, используя **многокритериальный подход по двум изображениям**. 

Инспектор сравнивает сгенерированную UV-текстуру бок о бок с оригинальным пустым шаблоном для независимой оценки определенных структурных правил:
1. **Правило лица (Face Rule):** Гарантирует, что шлем персонажа остается полностью безликим (без человеческих черт, очков или респираторов).
2. **Правило швов торса (Torso Seam Rule):** Проверяет, что передняя и задняя части одежды/брони на торсе идеально совпадают, чтобы предотвратить появление видимых швов в 3D.
3. **Правило ног (Legs Rule):** Гарантирует, что левая и правая ноги рассматриваются как отдельные конечности, не позволяя ИИ рисовать две ноги внутри одной формы.

Если какое-либо правило нарушено, Инспектор отклоняет изображение, предоставляет конкретную обратную связь о том, что именно было нарушено, и заставляет генератор перерисовать текстуру с исправлением этих конкретных ошибок.

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

## 📋 Требования

- **Python 3.12+**

### 🔑 Получение API-ключа Gemini

1. Перейдите в [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Войдите с помощью своего аккаунта Google.
3. Нажмите кнопку **"Create API key"**.
4. Если появится запрос, прочитайте и примите условия использования.
5. Нажмите на **"Create API key in new project"** (или используйте существующий проект).
6. Скопируйте сгенерированный ключ. Он понадобится вам для файла `.env` в шагах настройки ниже.

## 💻 Настройка (Локально)

### Установка через pip (Рекомендуется)
Самый простой способ установить генератор — напрямую из PyPI:
```bash
pip install haydee-outfit-generator
```

### Установка из исходного кода
1. Клонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install .
   ```

3. Скопируйте `.env.example` в `.env` (или создайте новый) и настройте ваши переменные:
* `GEMINI_API_KEY`: Ваш API-ключ Google Gemini.
* `HAYDEE_PATH`: Абсолютный путь к директории установки Haydee.
* `IMAGE_RESOLUTION`: (Опционально) Разрешение на выходе. По умолчанию `4K`. При необходимости может быть установлено на `2K` (2048x2048).
* `MODEL_NAME`: (Опционально) ИИ-модель Gemini для генерации текстур. По умолчанию `gemini-3.1-flash-image-preview`.
* `VALIDATOR_MODEL`: (Опционально) Модель рассуждений (reasoning), используемая для QA-проверки. По умолчанию `gemini-3.1-pro-preview`.

## 🐳 Настройка (Docker)

Если вы предпочитаете запускать проект без локальной установки Python, вы можете использовать Docker.

1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Создайте файл `.env` и задайте `GEMINI_API_KEY` и `HAYDEE_PATH`.
   * Примечание: `HAYDEE_PATH` в `.env` **должен** быть абсолютным путем на вашем хост-компьютере с Windows (например, `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 Использование

### Локальный запуск

**1. Генерация одного костюма**
Запустите команду `generate`, указав имя мода, желаемое описание стиля и, по желанию, автора:

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(Совет: вы можете опустить ключевое слово `generate` для более короткой команды: `haydee-gen --name ...`)*

**Параметры частичной генерации**
Вы можете выборочно пропускать части процесса генерации, чтобы сэкономить время или вызовы API, если вы уже сгенерировали их в предыдущих запусках:
* `--skip-d`: Пропускает генерацию диффузной текстуры (`Suit_D.dds`). Ранее сгенерированная текстура должна существовать, иначе команда завершится ошибкой. Если указан этот флаг, аргумент `--style` не является обязательным.
* `--skip-s`: Пропускает генерацию маски материалов и карты отражений (specular map) (`Suit_S.dds`).
* `--skip-n`: Пропускает генерацию карты нормалей (`Suit_N.dds`).
* `--max-retries`: (Опционально) Максимальное количество попыток перегенерации, если текстура не прошла QA-проверку. По умолчанию `3`.

При пропуске генерации карт (`--skip-s` или `--skip-n`), если они не были сгенерированы ранее, созданный костюм безопасно переключится на использование базовых нейтральных карт Haydee для этих слотов.

Скрипт автоматически прочитает базовую текстуру, свяжется с Gemini API для генерации диффузной текстуры (`Suit_D.dds` с использованием автоматизированного цикла QA-проверки по двум изображениям), затем запросит маску материалов, которая упаковывается в карту отражений (`Suit_S.dds`). Кроме того, вместе с диффузной текстурой генерируется пользовательская карта нормалей в касательном пространстве (`Suit_N.dds`), чтобы придать новым материалам, созданным ИИ, соответствующий 3D-рельеф и детали. Итоговый мод будет сгенерирован внутри вашей папки `Haydee/Outfits`, готовый к использованию!

**2. Группировка костюмов в мульти-мод**
Если вы сгенерировали несколько костюмов и хотите сгруппировать их в один мод с переключаемыми вариациями (например, в один костюм "Rainbow" с различными цветовыми слотами):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` — это необязательный флаг, который удалит исходные папки и конфигурации одиночных модов после их успешной группировки.

### Запуск через Docker

Вы можете использовать Docker Compose, чтобы автоматически примонтировать вашу директорию Haydee и выполнять команды:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 Публикация в Steam Workshop

Когда вы будете готовы поделиться созданным костюмом, вы сможете загрузить его напрямую в Steam Workshop с помощью встроенных в игру инструментов.

### 1. Подготовка миниатюры
- Создайте изображение для превью вашего мода (`preview.png` или `preview.jpg`).
- Изображение должно быть квадратным (например, 512x512 или 256x256).
- Поместите это изображение в папку с вашим модом.

### 2. Запуск редактора Edith
Инструменты для загрузки находятся в редакторе игры, а не в самой игре:
- Перейдите в корневую папку установки Haydee.
- Запустите `Edith.exe`.
- В верхнем меню выберите **Tool -> Workshop Uploader**.

### 3. Заполнение данных загрузчика
В окне загрузчика заполните следующие поля:
- **Mod Content (Содержимое мода):** В самом верху формы загрузки есть текстовое поле с кнопкой **Browse** под ним. Используйте её для формирования списка файлов для загрузки:
  1. Нажмите **Browse** и добавьте главную папку вашего мода (например, выберите `Outfits/NeonSurge`).
  2. Нажмите **Browse** еще раз и добавьте ваш файл определения `.outfit` (например, выберите `Outfits/NeonSurge.outfit`).
  *(Это гарантирует, что вы включите полный набор файлов, необходимых для работы мода).*
- **Title (Название):** Название вашего костюма (будет отображаться в Steam).
- **Description (Описание):** Краткое описание мода (что это такое, особенности и т.д.).
- **Visibility (Видимость):** Рекомендуется сначала установить значение **Private** (Приватный), чтобы проверить, как всё выглядит на странице в Steam, а затем изменить на **Public** (Публичный).
- **Preview Image (Изображение превью):** Выберите миниатюру, которую вы подготовили на шаге 1.

После заполнения нажмите **Upload** (Загрузить). Если всё пройдет успешно, статус внизу покажет **"Success"** (Успешно).

## 🧪 Тестирование

В этом проекте используется `pytest` для автоматического тестирования.

1. Установите зависимости для разработки:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Запустите набор тестов с проверкой покрытия:
   ```bash
   pytest
   ```
   *Примечание: Рабочие API-ключи или реальная установка Haydee **не требуются** для запуска тестов, так как внешние зависимости и файловая система безопасно эмулируются (mocked).*

## 📄 Лицензия

Этот проект лицензирован по лицензии MIT — подробности смотрите в файле [LICENSE](LICENSE).