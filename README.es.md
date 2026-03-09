> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Generador de Trajes para [Haydee](https://store.steampowered.com/app/530890/Haydee/) (Impulsado por Gemini)

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Pipeline automatizado en Python para generar texturas de trajes personalizados para el juego [Haydee](https://store.steampowered.com/app/530890/Haydee/) utilizando la API de Google Gemini.

> [!TIP]
> **¿No eres fan de la línea de comandos?** ¡Échale un vistazo a [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)! Es una interfaz gráfica moderna y lista para usar que te permite generar trajes personalizados fácilmente sin lidiar con terminales o variables de entorno. ¡Descarga la última versión para empezar al instante!

## ✨ Ejemplos de Generación

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

## 📋 Requisitos previos

- **Python 3.12+**

### 🔑 Obtener una clave de API de Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en el botón **"Create API key"**.
4. Si se te solicita, lee y acepta los términos de servicio.
5. Haz clic en **"Create API key in new project"** (o usa un proyecto existente).
6. Copia la clave generada. La necesitarás para el archivo `.env` en los pasos de configuración a continuación.

## 💻 Configuración (Local)

### Instalar vía pip (Recomendado)
La forma más sencilla de instalar el generador es directamente desde PyPI:
```bash
pip install haydee-outfit-generator
```

### Instalar desde el código fuente
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install .
   ```

3. Copia `.env.example` a `.env` (o crea uno) y configura tus variables:
* `GEMINI_API_KEY`: Tu clave de API de Google Gemini.
* `HAYDEE_PATH`: Ruta absoluta a tu directorio de instalación de Haydee.
* `IMAGE_RESOLUTION`: (Opcional) Resolución de salida. El valor por defecto es `4K`. Se puede configurar a `2K` (2048x2048) si es necesario.
* `MODEL_NAME`: (Opcional) El modelo de IA de Gemini a utilizar. El valor por defecto es `gemini-3.1-flash-image-preview`.

## 🐳 Configuración (Docker)

Si prefieres ejecutar el proyecto sin instalar Python localmente, puedes usar Docker.

1. Instala [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Crea tu archivo `.env` y configura `GEMINI_API_KEY` y `HAYDEE_PATH`.
   * Nota: `HAYDEE_PATH` en `.env` **debe** ser la ruta absoluta en tu máquina host con Windows (por ejemplo, `C:\Program Files (x86)\Steam\steamapps\common\Haydee`).

## 🚀 Uso

### Ejecución Local

**1. Generar un Solo Traje**
Ejecuta el comando `generate` proporcionando el nombre del mod, la descripción del estilo deseado y, opcionalmente, un autor:

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*(Consejo: Puedes omitir la palabra clave `generate` para un comando más corto: `haydee-gen --name ...`)*

**Parámetros de Generación Parcial**
Puedes omitir selectivamente partes del proceso de generación para ahorrar tiempo o llamadas a la API si ya las has generado en ejecuciones anteriores:
* `--skip-d`: Omite la generación de la textura difusa (`Suit_D.dds`). Debe existir una textura generada previamente, de lo contrario el comando fallará. Si se proporciona esta bandera, el argumento `--style` no es obligatorio.
* `--skip-s`: Omite la generación de la máscara de material y el mapa especular (`Suit_S.dds`).
* `--skip-n`: Omite la generación del mapa de normales (`Suit_N.dds`).

Al omitir la generación de mapas (`--skip-s` o `--skip-n`) sin haberlos generado previamente, el traje generado recurrirá de forma segura a usar los mapas neutrales base de Haydee para esas ranuras.

El script leerá automáticamente la textura base, contactará la API de Gemini para generar la textura difusa (`Suit_D.dds`), y luego solicitará una máscara de material que se empaqueta en un mapa especular (`Suit_S.dds`). Además, se genera un mapa de normales de espacio tangente personalizado (`Suit_N.dds`) junto a la textura difusa para dar a los nuevos materiales generados por IA detalles y relieve 3D que coincidan. ¡El mod final se generará dentro de tu carpeta `Haydee/Outfits`, listo para usar!

**2. Agrupar Trajes en un Multi-Mod**
Si has generado varios trajes y deseas agruparlos en un solo mod con variaciones intercambiables (por ejemplo, en un único traje "Rainbow" con ranuras de diferentes colores):

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` es una bandera opcional que eliminará las carpetas y configuraciones originales de los mods individuales después de agruparlos con éxito.

### Ejecución con Docker

Puedes usar Docker Compose para montar automáticamente tu directorio de Haydee y ejecutar los comandos:

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 Publicar en Steam Workshop

Cuando estés listo para compartir tu traje generado, puedes subirlo directamente a Steam Workshop utilizando las herramientas integradas del juego.

### 1. Preparar una Miniatura
- Crea una imagen de vista previa para tu mod (`preview.png` o `preview.jpg`).
- La imagen debe ser cuadrada (por ejemplo, 512x512 o 256x256).
- Coloca esta imagen en la carpeta de tu mod.

### 2. Iniciar el Editor Edith
Las herramientas de subida se encuentran en el editor del juego, no en el juego en sí:
- Ve a la carpeta raíz de instalación de Haydee.
- Ejecuta `Edith.exe`.
- En la barra de menú superior, selecciona **Tool -> Workshop Uploader**.

### 3. Completar los Datos de Subida
En la ventana de subida, completa los siguientes campos:
- **Mod Content:** En la parte superior del formulario de subida, hay un campo de texto con un botón **Browse** debajo. Usarás esto para construir la lista de archivos a subir:
  1. Haz clic en **Browse** y añade la carpeta principal de tu mod (por ejemplo, selecciona `Outfits/NeonSurge`).
  2. Haz clic en **Browse** nuevamente y añade tu archivo de definición `.outfit` (por ejemplo, selecciona `Outfits/NeonSurge.outfit`).
  *(Esto asegura que incluyas el conjunto completo de archivos requeridos para que el mod funcione).*
- **Title:** El nombre de tu traje (este se mostrará en Steam).
- **Description:** Una breve descripción del mod (qué es, características especiales, etc.).
- **Visibility:** Se recomienda establecerlo en **Private** primero para verificar cómo se ve todo en la página de Steam, y cambiarlo a **Public** más tarde.
- **Preview Image:** Selecciona la imagen de miniatura que preparaste en el paso 1.

Una vez completado, haz clic en **Upload**. Si todo va bien, el estado en la parte inferior mostrará **"Success"**.

## 🧪 Pruebas

Este proyecto utiliza `pytest` para pruebas automatizadas.

1. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Ejecuta la suite de pruebas con cobertura:
   ```bash
   pytest
   ```
   *Nota: **No se requieren** claves de API válidas ni una instalación real de Haydee para ejecutar las pruebas, ya que las dependencias externas y el sistema de archivos están simulados (mocked) de forma segura.*

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.