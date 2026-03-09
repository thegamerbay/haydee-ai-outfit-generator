> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# [Haydee](https://store.steampowered.com/app/530890/Haydee/) 服装生成器（由 Gemini 驱动）

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


一个自动化的 Python 管道，用于使用 Google Gemini API 为游戏 [Haydee](https://store.steampowered.com/app/530890/Haydee/) 生成自定义服装纹理。

> [!TIP]
> **不喜欢使用命令行？** 快来看看 [Haydee AI 服装生成器 GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)！它提供了一个现代且开箱即用的图形界面，让您可以轻松生成自定义服装，而无需与终端或环境变量作斗争。下载最新版本即可立即体验！

## ✨ 生成示例

| | | | |
| :---: | :---: | :---: | :---: |
| [![月球侦察兵服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672592226.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672592226) | [![霓虹狂潮服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672586107.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672586107) | [![蒸汽齿轮服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672258053.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672258053) | [![古墓苏醒服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672251317.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672251317) |
| [月球侦察兵服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672592226) | [霓虹狂潮服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672586107) | [蒸汽齿轮服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672258053) | [古墓苏醒服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672251317) |
| [![绿皮机器人服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672243330.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672243330) | [![废土客服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672236521.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672236521) | [![异形服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672227514.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672227514) | [![甜莓服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672221390.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672221390) |
| [绿皮机器人服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672243330) | [废土客服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672236521) | [异形服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672227514) | [甜莓服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672221390) |
| [![科技女祭司服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672191643.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672191643) | [![白色宇航服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672182479.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672182479) | [![战斗修女服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672168153.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672168153) | [![哥特自动机服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672159225.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672159225) |
| [科技女祭司服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672191643) | [白色宇航服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672182479) | [战斗修女服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672168153) | [哥特自动机服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672159225) |
| [![糖果波普服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672150985.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672150985) | [![地狱行者服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672058503.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672058503) | [![复古合成波服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3672013495.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3672013495) | [![钢铁乌托邦服装](https://raw.githubusercontent.com/thegamerbay/haydee-ai-outfit-generator/main/assets/3671983563.jpg)](https://steamcommunity.com/sharedfiles/filedetails/?id=3671983563) |
| [糖果波普服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672150985) | [地狱行者服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672058503) | [复古合成波服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3672013495) | [钢铁乌托邦服装](https://steamcommunity.com/sharedfiles/filedetails/?id=3671983563) |

## 📋 前置要求

- **Python 3.12+**

### 🔑 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)。
2. 登录您的 Google 账号。
3. 点击 **"Create API key"**（创建 API 密钥）按钮。
4. 如果出现提示，请阅读并接受服务条款。
5. 点击 **"Create API key in new project"**（在项目中创建 API 密钥）或使用现有项目。
6. 复制生成的密钥。在下方的配置步骤中，您需要将它填入 `.env` 文件。

## 💻 安装配置（本地）

### 通过 pip 安装（推荐）
安装此生成器最简单的方法是直接从 PyPI 安装：
```bash
pip install haydee-outfit-generator
```

### 从源码安装
1. 克隆本仓库。
2. 安装依赖：
   ```bash
   pip install .
   ```

3. 将 `.env.example` 复制为 `.env`（或新建一个文件）并配置您的变量：
* `GEMINI_API_KEY`: 您的 Google Gemini API 密钥。
* `HAYDEE_PATH`: 您的 Haydee 安装目录的绝对路径。
* `IMAGE_RESOLUTION`: （可选）输出分辨率。默认为 `4K`。如有需要，可设置为 `2K` (2048x2048)。
* `MODEL_NAME`: （可选）要使用的 Gemini AI 模型。默认为 `gemini-3.1-flash-image-preview`。

## 🐳 安装配置（Docker）

如果您不想在本地安装 Python，可以选择使用 Docker 运行本项目。

1. 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。
2. 创建您的 `.env` 文件并设置 `GEMINI_API_KEY` 和 `HAYDEE_PATH`。
   * 注意：`.env` 文件中的 `HAYDEE_PATH` **必须** 是宿主机 Windows 上的绝对路径（例如：`C:\Program Files (x86)\Steam\steamapps\common\Haydee`）。

## 🚀 使用方法

### 本地运行

**1. 生成单套服装**
运行 `generate` 命令，并提供模组名称、期望的风格描述以及（可选的）作者名称：

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*（提示：您可以省略 `generate` 关键字以缩短命令：`haydee-gen --name ...`）*

**部分生成参数**
如果在之前的运行中已经生成过部分贴图，您可以选择性地跳过某些生成步骤，以节省时间或 API 调用：
* `--skip-d`：跳过生成漫反射贴图（`Suit_D.dds`）。必须存在之前生成过的贴图，否则命令将失败。如果提供此标志，则 `--style` 参数不是必填项。
* `--skip-s`：跳过生成材质遮罩和高光贴图（`Suit_S.dds`）。
* `--skip-n`：跳过生成法线贴图（`Suit_N.dds`）。

在未提前生成对应贴图的情况下跳过贴图生成（`--skip-s` 或 `--skip-n`）时，生成的服装将安全地回退，并在这些槽位使用 Haydee 的基础中性贴图。

脚本会自动读取基础纹理，通过调用 Gemini API 生成漫反射贴图（`Suit_D.dds`），然后请求材质遮罩并将其打包到高光贴图（`Suit_S.dds`）中。此外，在生成漫反射贴图的同时，还会生成自定义的切线空间法线贴图（`Suit_N.dds`），赋予这些新生成的 AI 材质相匹配的 3D 浮雕与细节效果。最终的模组将被生成到您的 `Haydee/Outfits` 文件夹中，可以直接在游戏内使用！

**2. 将多套服装组合为单个包含变体的模组**
如果您已经生成了多套服装，并希望将它们组合成一个具有可切换变体的单一模组（例如：一套整合了不同颜色槽位的单一“Rainbow”服装）：

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` 是一个可选标志，它会在成功打包组合后删除原始的单个模组文件夹及其配置文件。

### 使用 Docker 运行

您可以使用 Docker Compose 自动挂载您的 Haydee 目录并运行相应的命令：

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 发布到 Steam 创意工坊

准备好分享您生成的服装时，您可以使用游戏内置的工具直接将其上传到 Steam 创意工坊。

### 1. 准备缩略图
- 为您的模组创建一张预览图（`preview.png` 或 `preview.jpg`）。
- 图片应该是正方形的（例如 512x512 或 256x256）。
- 将这张图片放在您的模组文件夹中。

### 2. 启动 Edith 编辑器
上传工具位于游戏编辑器中，而非游戏本身：
- 转到您的 Haydee 根安装文件夹。
- 运行 `Edith.exe`。
- 在顶部菜单栏中，选择 **Tool -> Workshop Uploader**。

### 3. 填写上传工具数据
在上传工具窗口中，填写以下字段：
- **Mod Content（模组内容）：** 在上传表单的最顶部，有一个文本框，其下方有一个 **Browse**（浏览）按钮。您将使用它来构建要上传的文件列表：
  1. 点击 **Browse** 并添加您的模组主文件夹（例如，选择 `Outfits/NeonSurge`）。
  2. 再次点击 **Browse** 并添加您的 `.outfit` 定义文件（例如，选择 `Outfits/NeonSurge.outfit`）。
  *（这可确保您包含了使模组正常工作所需的全部文件）。*
- **Title（标题）：** 您的服装名称（这将显示在 Steam 上）。
- **Description（描述）：** 对模组的简短描述（它是什么，有什么特色等）。
- **Visibility（可见性）：** 建议先将其设置为 **Private（私密）** 以验证 Steam 页面上的显示效果，确认无误后再将其更改为 **Public（公开）**。
- **Preview Image（预览图）：** 选择您在第 1 步中准备的缩略图。

填写完成后，点击 **Upload**（上传）。如果一切顺利，底部的状态栏将显示 **"Success"**（成功）。

## 🧪 测试

本项目使用 `pytest` 进行自动化测试。

1. 安装开发环境依赖：
   ```bash
   pip install -r requirements-dev.txt
   ```
2. 运行带有覆盖率报告的测试套件：
   ```bash
   pytest
   ```
   *注意：运行测试**不需要**有效的 API 密钥或真实的 Haydee 安装环境，因为外部依赖和文件系统都已被安全地 Mock（模拟）处理。*

## 📄 许可证

本项目基于 MIT 许可证开源 —— 详情请参阅 [LICENSE](LICENSE) 文件。