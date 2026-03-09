# [Haydee](https://store.steampowered.com/app/530890/Haydee/) Outfit Generator (Powered by Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Automated Python pipeline to generate custom outfit textures for the game [Haydee](https://store.steampowered.com/app/530890/Haydee/) using the Google Gemini API.

> [!TIP]
> **Not a fan of the command line?** Check out the [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! It's a modern, ready-to-use graphical interface that lets you easily generate custom outfits without messing with terminals or environment variables. Download the latest release to get started instantly!

## ✨ Generation Examples

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

## 📋 Prerequisites

- **Python 3.12+**

### 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Click the **"Create API key"** button.
4. If prompted, read and accept the terms of service.
5. Click on **"Create API key in new project"** (or use an existing project).
6. Copy the generated key. You will need it for the `.env` file in the setup steps below.

## 💻 Setup (Local)

### Install via pip (Recommended)
The easiest way to install the generator is directly from PyPI:
```bash
pip install haydee-outfit-generator
```

### Install from Source
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install .
   ```

3. Copy `.env.example` to `.env` (or create one) and configure your variables:
* `GEMINI_API_KEY`: Your Google Gemini API Key.
* `HAYDEE_PATH`: Absolute path to your Haydee installation directory.
* `IMAGE_RESOLUTION`: (Optional) Output resolution. Default is `4K`. Can be set to `2K` (2048x2048) if needed.
* `MODEL_NAME`: (Optional) The Gemini AI model to use. Default is `gemini-3.1-flash-image-preview`.

## 🐳 Setup (Docker)

If you prefer to run the project without installing Python locally, you can use Docker.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Create your `.env` file and set `GEMINI_API_KEY` and `HAYDEE_PATH`.
   * Note: `HAYDEE_PATH` in `.env` **must** be the absolute path on your host Windows machine (e.g., `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 Usage

### Running Locally

**1. Generating a Single Outfit**
Run the `generate` command by providing the mod name, the desired style description, and optionally an author:

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(Tip: You can omit the `generate` keyword for a shorter command: `haydee-gen --name ...`)*

**Partial Generation Parameters**
You can selectively skip parts of the generation process to save time or API calls if you've already generated them in previous runs:
* `--skip-d`: Skips the generation of the diffuse texture (`Suit_D.dds`). A previously generated texture must exist, otherwise the command will fail. If this flag is provided, the `--style` argument is not mandatory.
* `--skip-s`: Skips the generation of the material mask and specular map (`Suit_S.dds`).
* `--skip-n`: Skips the generation of the normal map (`Suit_N.dds`).

When skipping map generation (`--skip-s` or `--skip-n`) without generating them earlier, the generated outfit will safely fall back and use Haydee's base neutral maps for those slots.

The script will automatically read the base texture, contact the Gemini API to generate the diffuse texture (`Suit_D.dds`), then request a material mask which is packed into a specular map (`Suit_S.dds`). Additionally, a custom Tangent Space Normal Map (`Suit_N.dds`) is generated alongside the diffuse texture to give the new AI-generated materials matching 3D relief and details. The final mod will be generated inside your `Haydee/Outfits` folder, ready to use!

**2. Grouping Outfits into a Multi-Mod**
If you have generated multiple outfits and want to group them into a single mod with switchable variations (e.g., in a single "Rainbow" outfit with different colored slots):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` is an optional flag that will remove the original single-mod folders and configs after successfully grouping them.

### Running with Docker

You can use Docker Compose to automatically mount your Haydee directory and run the commands:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 Publishing to Steam Workshop

When you are ready to share your generated outfit, you can upload it directly to the Steam Workshop using the game's built-in tools.

### 1. Prepare a Thumbnail
- Create a preview image for your mod (`preview.png` or `preview.jpg`).
- The image should be square (e.g., 512x512 or 256x256).
- Place this image in your mod folder.

### 2. Launch Edith Editor
The upload tools are located in the game's editor, not the game itself:
- Go to your Haydee root installation folder.
- Run `Edith.exe`.
- In the top menu bar, select **Tool -> Workshop Uploader**.

### 3. Fill in the Uploader Data
In the uploader window, fill out the following fields:
- **Mod Content:** At the very top of the upload form, there is a text field with a **Browse** button beneath it. You will use this to build the list of files to upload:
  1. Click **Browse** and add your mod's main folder (for example, select `Outfits/NeonSurge`).
  2. Click **Browse** again and add your `.outfit` definition file (for example, select `Outfits/NeonSurge.outfit`).
  *(This ensures you include the full set of files required for the mod to work).*
- **Title:** The name of your outfit (this will be displayed on Steam).
- **Description:** A short description of the mod (what it is, special features, etc.).
- **Visibility:** It is recommended to set this to **Private** first to verify how everything looks on the Steam page, and change it to **Public** later.
- **Preview Image:** Select the thumbnail image you prepared in step 1.

Once filled out, click **Upload**. If everything goes well, the status at the bottom will show **"Success"**.

## 🧪 Testing

This project uses `pytest` for automated testing.

1. Install the development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Run the test suite with coverage:
   ```bash
   pytest
   ```
   *Note: Valid API Keys or a real Haydee installation are **not required** to run the tests, as external dependencies and the filesystem are safely mocked.*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
