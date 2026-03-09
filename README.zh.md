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

一个自动化的 Python 管道，使用 Google Gemini API 为游戏 [Haydee](https://store.steampowered.com/app/530890/Haydee/) 生成自定义服装纹理。

> [!TIP]
> **不喜欢使用命令行？** 快来看看 [Haydee AI 服装生成器 GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)！它是一个现代、开箱即用的图形界面，让您可以轻松生成自定义服装，而无需与终端或环境变量作斗争。下载最新版本即可立即开始体验！

### 🤖 双图多重标准 LLM 裁判验证
本项目具有高级的自动化**质量保证（QA）反馈循环**。当一个快速模型（如 `gemini-3.1-flash-image`）绘制纹理时，一个更强大的推理模型（如 `gemini-3.1-pro`）则作为严格的 QA 检查员，采用**双图多重标准**方法进行评估。

检查员将生成的 UV 纹理与原始的空白模板进行并排对比，独立评估特定的结构规则：
1. **面部规则 (Face Rule)：** 确保角色的头盔保持完全无面孔状态（没有人类特征、眼镜或呼吸面罩）。
2. **躯干接缝规则 (Torso Seam Rule)：** 验证躯干前后的衣服/盔甲部件完美匹配，防止在 3D 模型中出现可见接缝。
3. **腿部规则 (Legs Rule)：** 确保左右腿被视为独立的肢体，防止 AI 在单个形状内画出两条腿。

如果违反了任何规则，检查员将拒绝该图像，提供关于具体哪里出错的详细反馈，并强制生成器重新绘制纹理以纠正这些特定错误。

## ✨ 生成示例

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

## 📋 前置要求

- **Python 3.12+**

### 🔑 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)。
2. 使用您的 Google 账号登录。
3. 点击 **"Create API key"** 按钮。
4. 如果有提示，请阅读并接受服务条款。
5. 点击 **"Create API key in new project"**（或使用现有项目）。
6. 复制生成的密钥。您需要在下方设置步骤中的 `.env` 文件里用到它。

## 💻 安装设置（本地）

### 通过 pip 安装（推荐）
安装生成器最简单的方法是直接从 PyPI 安装：
```bash
pip install haydee-outfit-generator
```

### 从源码安装
1. 克隆本仓库。
2. 安装依赖项：
   ```bash
   pip install .
   ```

3. 将 `.env.example` 复制为 `.env`（或创建一个新的），并配置您的变量：
* `GEMINI_API_KEY`: 您的 Google Gemini API 密钥。
* `HAYDEE_PATH`: Haydee 安装目录的绝对路径。
* `IMAGE_RESOLUTION`: (可选) 输出分辨率。默认为 `4K`。如有需要可设置为 `2K` (2048x2048)。
* `MODEL_NAME`: (可选) 用于生成纹理的 Gemini AI 模型。默认为 `gemini-3.1-flash-image-preview`。
* `VALIDATOR_MODEL`: (可选) 用于 QA 检查的推理模型。默认为 `gemini-3.1-pro-preview`。

## 🐳 安装设置（Docker）

如果您不想在本地安装 Python 也能运行本项目，可以使用 Docker。

1. 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。
2. 创建 `.env` 文件并设置 `GEMINI_API_KEY` 和 `HAYDEE_PATH`。
   * 注意：`.env` 中的 `HAYDEE_PATH` **必须** 是您 Windows 宿主机上的绝对路径（例如：`C:\Program Files (x86)\Steam\steamapps\common\Haydee`）。

## 🚀 使用方法

### 本地运行

**1. 生成单套服装**
通过提供模组名称、期望的风格描述以及可选的作者信息来运行 `generate` 命令：

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*（提示：您可以省略 `generate` 关键字以使用更简短的命令：`haydee-gen --name ...`）*

**部分生成参数**
如果您在之前的运行中已经生成了某些部分，可以有选择地跳过部分生成过程，以节省时间或 API 调用：
* `--skip-d`: 跳过漫反射纹理 (`Suit_D.dds`) 的生成。必须存在之前生成的纹理，否则命令将失败。如果提供此标志，则 `--style` 参数不是必须的。
* `--skip-s`: 跳过材质遮罩和高光贴图 (`Suit_S.dds`) 的生成。
* `--skip-n`: 跳过法线贴图 (`Suit_N.dds`) 的生成。
* `--max-retries`: (可选) 纹理未通过 QA 验证时的最大重新生成尝试次数。默认为 `3`。

在没有提前生成相关贴图的情况下跳过贴图生成（`--skip-s` 或 `--skip-n`），生成的服装将安全地回退，并在这些槽位使用 Haydee 的基础中性贴图。

脚本将自动读取基础纹理，联系 Gemini API 生成漫反射纹理（使用自动化的双图 QA 验证循环生成 `Suit_D.dds`），然后请求材质遮罩并将其打包到高光贴图（`Suit_S.dds`）中。此外，还会与漫反射纹理一起生成一个自定义的切线空间法线贴图（`Suit_N.dds`），为新生成的 AI 材质提供匹配的 3D 浮雕和细节。最终的模组将生成在您的 `Haydee/Outfits` 文件夹中，随时可以使用！

**2. 将多套服装组合为多子模组 (Multi-Mod)**
如果您已经生成了多套服装，并且希望将它们组合成一个带有可切换变体的单一模组（例如，在单一的“Rainbow”服装下拥有不同颜色的槽位）：

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` 是一个可选标志，它会在成功组合后删除原始的单个模组文件夹和配置文件。

### 使用 Docker 运行

您可以使用 Docker Compose 自动挂载您的 Haydee 目录并运行命令：

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 发布到 Steam 创意工坊

当您准备好分享生成的服装时，可以使用游戏内置的工具将其直接上传到 Steam 创意工坊。

### 1. 准备缩略图
- 为您的模组创建一张预览图（`preview.png` 或 `preview.jpg`）。
- 图片应当是正方形（例如 512x512 或 256x256）。
- 将此图片放置在您的模组文件夹中。

### 2. 启动 Edith 编辑器
上传工具位于游戏编辑器中，而不是游戏本身：
- 前往您的 Haydee 根安装目录。
- 运行 `Edith.exe`。
- 在顶部菜单栏中，选择 **Tool -> Workshop Uploader**。

### 3. 填写上传工具数据
在上传工具窗口中，填写以下字段：
- **模组内容 (Mod Content):** 在上传表单的最顶部，有一个文本字段，下面有一个 **Browse (浏览)** 按钮。您将使用它来构建要上传的文件列表：
  1. 点击 **Browse** 并添加模组的主文件夹（例如，选择 `Outfits/NeonSurge`）。
  2. 再次点击 **Browse** 并添加您的 `.outfit` 配置文件（例如，选择 `Outfits/NeonSurge.outfit`）。
  *（这确保您包含模组运行所需的完整文件集）。*
- **标题 (Title):** 您的服装名称（这将显示在 Steam 上）。
- **描述 (Description):** 模组的简短说明（它是什么、有什么特色等）。
- **可见度 (Visibility):** 建议先将其设置为 **Private（私密）** 以验证 Steam 页面上的显示效果，确认无误后再更改为 **Public（公开）**。
- **预览图 (Preview Image):** 选择您在第 1 步中准备的缩略图。

填写完成后，点击 **Upload (上传)**。如果一切顺利，底部的状态将显示为 **"Success"**。

## 🧪 测试

本项目使用 `pytest` 进行自动化测试。

1. 安装开发依赖项：
   ```bash
   pip install -r requirements-dev.txt
   ```
2. 运行带覆盖率分析的测试套件：
   ```bash
   pytest
   ```
   *注意：运行测试**不需要**有效的 API 密钥或真实的 Haydee 安装，因为外部依赖和文件系统已经被安全地模拟 (mock)。*

## 📄 许可证

本项目采用 MIT 许可证 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。