> 🌐 **Languages:** [English](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.md) | [Русский](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ru.md) | [ไทย](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.th.md) | [中文](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.zh.md) | [Español](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.es.md) | [العربية](https://github.com/thegamerbay/haydee-ai-outfit-generator/blob/main/README.ar.md)

# [Haydee](https://store.steampowered.com/app/530890/Haydee/) 服装生成器（由 Gemini 驱动）

[![Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/lint.yml)
[![Publish](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator/branch/main/graph/badge.svg)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator)
[![PyPI version](https://img.shields.io/pypi/v/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Downloads](https://img.shields.io/pypi/dm/haydee-outfit-generator.svg)](https://pypi.org/project/haydee-outfit-generator/)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

自动化 Python 管道，使用 Google Gemini API 为游戏 [Haydee](https://store.steampowered.com/app/530890/Haydee/) 生成自定义服装纹理。

> [!TIP]
> **不喜欢使用命令行？** 快来看看 [Haydee AI Outfit Generator GUI](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui)！这是一款现代化的、开箱即用的图形界面工具，让您无需处理终端或环境变量即可轻松生成自定义服装。下载最新版本即可立即开始使用！

### 🤖 双图多重标准大语言模型裁判验证
该项目具有高级自动化的**质量保证反馈循环**。当一个快速模型（如 `gemini-3.1-flash-image`）绘制纹理时，一个更强大的推理模型（如 `gemini-3.1-pro`）将扮演严格的质检员角色，采用**双图多重标准**方法。

质检员会将生成的 UV 纹理与原始空白模板进行并排对比，独立评估特定的结构规则：
1. **面部规则：** 确保角色的头盔保持完全无面部特征（没有人类特征、眼镜或呼吸面罩）。
2. **躯干接缝规则：** 验证前后躯干的衣物/装甲部件完美匹配，防止在 3D 模型中出现可见接缝。
3. **腿部规则：** 确保左右腿被视为独立的肢体，防止 AI 在单个形状内绘制出两条腿。

如果违反了任何规则，质检员将拒收该图像，针对究竟哪里出了问题提供具体的反馈，并强制生成器重新绘制纹理以纠正这些特定的错误。

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

## 📋 先决条件

- **Python 3.12+**

### 🔑 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)。
2. 登录您的 Google 账号。
3. 点击 **"Create API key"**（创建 API 密钥）按钮。
4. 如果出现提示，请阅读并接受服务条款。
5. 点击 **"Create API key in new project"**（在新项目中创建 API 密钥）（或使用现有项目）。
6. 复制生成的密钥。您将在下方设置步骤中的 `.env` 文件里用到它。

## 💻 安装设置（本地）

### 通过 pip 安装（推荐）
安装该生成器最简单的方法是直接从 PyPI 安装：
```bash
pip install haydee-outfit-generator
```

### 从源码安装
1. 克隆此仓库。
2. 安装依赖：
   ```bash
   pip install .
   ```

3. 将 `.env.example` 复制为 `.env`（或新建一个），并配置您的变量：
* `GEMINI_API_KEY`：您的 Google Gemini API 密钥。
* `HAYDEE_PATH`：Haydee 安装目录的绝对路径。
* `IMAGE_RESOLUTION`：（可选）输出分辨率。默认为 `4K`。如果需要，可以设置为 `2K` (2048x2048)。
* `MODEL_NAME`：（可选）用于生成纹理的 Gemini AI 模型。默认为 `gemini-3.1-flash-image-preview`。
* `VALIDATOR_MODEL`：（可选）用于质检的推理模型。默认为 `gemini-3.1-pro-preview`。

## 🐳 安装设置（Docker）

如果您不想在本地安装 Python，可以使用 Docker 来运行此项目。

1. 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。
2. 创建您的 `.env` 文件，并设置 `GEMINI_API_KEY` 和 `HAYDEE_PATH`。
   * 注意：`.env` 中的 `HAYDEE_PATH` **必须** 是您宿主机 Windows 上的绝对路径（例如：`C:\Program Files (x86)\Steam\steamapps\common\Haydee`）。

## 🚀 使用方法

### 本地运行

**1. 生成单件服装**
运行 `generate` 命令，提供模组名称、所需的样式描述，以及可选的作者信息：

```bash
haydee-gen generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor" --author "TheGamerBay"
```
*（提示：您可以省略 `generate` 关键字以缩短命令：`haydee-gen --name ...`）*

**部分生成参数**
如果您在之前的运行中已经生成了部分内容，您可以选择性地跳过生成过程的某些步骤，以节省时间或 API 调用：
* `--skip-d`：跳过漫反射纹理（`Suit_D.dds`）的生成。必须存在之前生成的纹理，否则命令将失败。如果提供了此标志，则 `--style` 参数不是必须的。
* `--skip-s`：跳过材质遮罩和高光贴图（`Suit_S.dds`）的生成。
* `--skip-n`：跳过法线贴图（`Suit_N.dds`）的生成。
* `--max-retries`：（可选）如果纹理未通过质量保证（QA）验证，最大重新生成尝试次数。默认为 `3`。

在没有提前生成贴图的情况下跳过贴图生成（`--skip-s` 或 `--skip-n`），生成的服装将会安全地回退，并在这些槽位使用 Haydee 的基础中性贴图。

脚本将自动读取基础纹理，调用 Gemini API 生成漫反射纹理（`Suit_D.dds`，使用自动化的双图 QA 验证循环），然后请求材质遮罩将其打包到高光贴图（`Suit_S.dds`）中。此外，它还会在漫反射纹理之外生成一张自定义的切线空间法线贴图（`Suit_N.dds`），为全新 AI 生成的材质提供相匹配的 3D 浮雕与细节。最终模组将生成在您的 `Haydee/Outfits` 文件夹中，随时可以使用！

**2. 将服装组合成包含变体的模组**
如果您生成了多套服装，并希望将它们组合成一个带有可切换变体的单一模组（例如，一个带有不同颜色槽位的单一“Rainbow”服装）：

```bash
haydee-gen group --name "Rainbow" --mods red green blue --slot-category "color" --author "TheGamerBay" --delete-sources
```
* `--delete-sources` 是一个可选标志，成功组合后将删除原始的单模组文件夹和配置文件。

### 使用 Docker 运行

您可以使用 Docker Compose 自动挂载您的 Haydee 目录并运行相关命令：

```bash
docker-compose run --rm generator generate --name "NeonSurge" --style "cyberpunk neon lights with dark carbon fiber armor"
```

## 📤 发布到 Steam 创意工坊

准备好分享您生成的服装时，您可以使用游戏内置的工具直接将其上传到 Steam 创意工坊。

### 1. 准备缩略图
- 为您的模组创建一张预览图（`preview.png` 或 `preview.jpg`）。
- 图像应该是正方形的（例如 512x512 或 256x256）。
- 将此图像放置在您的模组文件夹中。

### 2. 启动 Edith 编辑器
上传工具位于游戏的编辑器中，而不是游戏本体：
- 前往您的 Haydee 根安装文件夹。
- 运行 `Edith.exe`。
- 在顶部菜单栏中，选择 **Tool -> Workshop Uploader**。

### 3. 填写上传数据
在上传器窗口中，填写以下字段：
- **Mod Content（模组内容）：** 在上传表单的最顶部，有一个文本框，下方有一个 **Browse**（浏览）按钮。您将使用它来构建要上传的文件列表：
  1. 点击 **Browse** 并添加您的模组主文件夹（例如，选择 `Outfits/NeonSurge`）。
  2. 再次点击 **Browse** 并添加您的 `.outfit` 定义文件（例如，选择 `Outfits/NeonSurge.outfit`）。
  *（这确保您囊括了使模组正常工作所需的全部文件）。*
- **Title（标题）：** 您服装的名称（这将显示在 Steam 上）。
- **Description（描述）：** 模组的简短说明（它是什么，有什么特色等）。
- **Visibility（可见性）：** 建议首先将其设置为 **Private**（私密），以便在 Steam 页面上验证外观是否正常，稍后再改为 **Public**（公开）。
- **Preview Image（预览图）：** 选择您在第一步中准备好的缩略图。

填写完毕后，点击 **Upload**（上传）。如果一切顺利，底部的状态将显示为 **"Success"**（成功）。

## 🧪 测试

本项目使用 `pytest` 进行自动化测试。

1. 安装开发依赖：
   ```bash
   pip install -r requirements-dev.txt
   ```
2. 运行测试套件并包含覆盖率报告：
   ```bash
   pytest
   ```
   *注意：运行测试**不需要**有效的 API 密钥或真实的 Haydee 安装环境，因为外部依赖和文件系统已经被安全地模拟（mocked）。*

## 📄 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。