# Haydee Outfit Generator (Powered by Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Automated Python pipeline to generate custom outfit textures for the game Haydee using the Google Gemini API.

## Prerequisites

1. **Python 3.12+**
2. **ImageMagick**: Required for the `Wand` library to process `.dds` files.
   * Download from [ImageMagick.org](https://imagemagick.org/script/download.php).
   * **Important during installation (Windows):** Ensure you check the box that says *"Install legacy utilities (e.g. convert)"* and add it to your System PATH.

## Setup (Local)

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` (or create one) and configure your variables:
* `GEMINI_API_KEY`: Your Google Gemini API Key.
* `HAYDEE_PATH`: Absolute path to your Haydee installation directory.

## Setup (Docker)

If you prefer to run the project without installing Python and ImageMagick locally, you can use Docker.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Create your `.env` file and set `GEMINI_API_KEY` and `HAYDEE_PATH`.
   * Note: `HAYDEE_PATH` in `.env` **must** be the absolute path on your host Windows machine (e.g., `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## Usage

### Running Locally

Run the script by providing the mod name and the desired style description:

```bash
python main.py --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

### Running with Docker

You can use Docker Compose to automatically mount your Haydee directory and run the command:

```bash
docker-compose run --rm generator --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

The script will automatically read the base texture, contact the Gemini API, convert the formats, and generate the mod inside your `Haydee/Outfits` folder.

## Testing

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
