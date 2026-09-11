# Children's Picturebook Studio / 儿童互动绘本制作

A Codex Skill for turning a child's interests, personality, and everyday world into a personalized illustrated storybook.

一个帮助家长把孩子的兴趣、性格和生活经历，变成专属互动绘本的 Codex Skill。

![儿童互动绘本制作流程](docs/picturebook-skill-overview-zh.png)

## 中文介绍

### 这个 Skill 是做什么的？

它会陪你从一个简单想法开始，一步步完成一本真正围绕孩子创作的绘本。

它不会默认套用某个孩子、角色或故事。开始制作前，它会先了解：

- 谁是故事的主角；
- 孩子喜欢什么角色；
- 你希望故事谈什么主题；
- 孩子的年龄、性格、兴趣和最近在意的事情。

孩子不只是出现在故事里，还会通过自己的选择和行动推动故事发展。

### 整体流程

1. **认识孩子**：了解主角、喜好、主题和孩子本身。
2. **选择故事**：先提供约 8–10 个不同方向，请家长挑选喜欢的路线。
3. **确定角色与画风**：根据照片或文字描述设计主角，并把喜欢的卡通风格转化成原创视觉方向。
4. **试听声音**：检查当前可用的语音工具，制作短试听后再决定。
5. **确认样页**：先看一页完整效果，满意后再继续制作整本。
6. **制作绘本**：用同一份故事资料统一文字、图片、配音和页序。
7. **检查与交付**：按需交付互动网页、高清 PDF 或有声视频。

### 语言

Skill 会跟随用户使用的语言。中文提问就用中文，英文提问就用英文；也可以另外指定绘本语言。故事文字、配音、网页按钮、图片说明和无障碍文字都会使用同一语言。

### 可以得到什么？

- 封面和完整绘本页面；
- 可直接分享、无需服务器的互动 HTML；
- 适合阅读或打印的高清 PDF；
- 带逐页配音的 MP4 视频；
- 可继续修改的故事资料、角色设定和语音设定。

具体交付形式由用户选择，不会默认把所有格式都做一遍。

## English

### What does this Skill do?

It guides a parent from a simple idea to a personalized illustrated picturebook built around the current child.

It does not assume a default child, cast, plot, art style, or voice. Before proposing stories, it first learns:

- who the protagonist is;
- what kinds of characters the child likes;
- what theme or situation the parent wants to explore;
- the child's age, personality, interests, relationships, wishes, or sensitivities.

The child is not merely placed inside the story. Their choices and actions move the story forward.

### Workflow

1. **Understand the child** — protagonist, interests, theme, and child context.
2. **Choose a story** — review roughly 8–10 meaningfully different directions.
3. **Align characters and style** — use an authorized photo or a written description, then translate favorite-cartoon preferences into an original visual brief.
4. **Audition voices** — inspect the speech tools actually available and compare short samples.
5. **Approve one sample page** — review the complete reading experience before full production.
6. **Produce the book** — keep text, images, narration, and page order aligned through one story source.
7. **Verify and deliver** — create only the selected formats: interactive HTML, high-resolution PDF, or narrated MP4.

### Language

The Skill follows the user's language unless another language is requested for the book. Intake, story text, narration, interface controls, image descriptions, accessibility labels, and delivery notes stay aligned to that choice.

### Outputs

- a cover and complete illustrated story pages;
- a portable, self-contained interactive HTML;
- an optional high-resolution PDF;
- an optional narrated MP4;
- reusable story data, character guidance, and voice direction.

## Installation

Install this repository as a Codex Skill, or clone/copy it into:

```text
<CODEX_HOME>/skills/children-picturebook-production
```

Then start with either:

```text
使用 $children-picturebook-production，帮我给孩子做一本专属绘本。
```

```text
Use $children-picturebook-production to help me create a personalized picturebook for my child.
```

## Optional production dependencies

- Image-generation access for illustrated pages.
- A callable speech engine or speech API for narration.
- Python with Pillow and ReportLab for PDF export.
- FFmpeg or `imageio-ffmpeg` for MP4 export.

The Skill checks what is actually available before recommending a voice route.

## Privacy and creative references

Only use a child's photo or a voice sample with the guardian's permission. Keep private reference files out of shared deliverables and public repositories unless the owner explicitly asks to include them.

Favorite cartoons are treated as preference signals for line, color, proportion, material, and mood—not as assets to copy.

## Repository contents

- `SKILL.md` — the main workflow and decision rules.
- `references/` — story, voice, layout, project schema, QA, and behavior guidance.
- `assets/` — the reusable story example and standalone HTML template.
- `scripts/` — validation and HTML, PDF, and MP4 build helpers.
- `agents/openai.yaml` — Codex-facing display metadata.

## License

No license has been selected yet. The repository is publicly viewable, but reuse rights are not granted until the owner adds a license.

