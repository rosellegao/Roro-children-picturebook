---
name: children-picturebook-production
description: Create or revise illustrated picturebooks for young children when the work includes story development, character and style alignment, page narration, responsive standalone HTML, and optional PDF or MP4 delivery. Use for a new book or a substantial book revision, not for a single isolated illustration or a prose-only story.
---

# Children Picturebook Production

Create a new book around the current child and the cast chosen for this request. Reuse proven production methods, not the names, characters, plot, visual identity, or voice choices of an earlier book or example asset.

## Follow the user's language

Respond in the language the user is using unless they request another language for the book. Use that chosen language consistently for intake questions, story directions, visible story text, narration, alt text, interface controls, accessibility labels, and delivery notes. Preserve names and supplied phrases unless the user asks to translate or adapt them.

Set `book.language` to the appropriate BCP 47 language tag and localize the `ui` strings in `story.json`. Treat language as part of the approved creative direction: changing it after story or voice approval may require copy and voice review, but it should not restart unrelated decisions.

## Mandatory intake for a new book

When a user first asks to make a storybook, explain briefly that four inputs are needed before story directions can be proposed. Ask for them together:

1. who the protagonist is;
2. what kinds of characters the child likes, including any desired co-stars;
3. any theme, situation, or meaning the user wants to explore;
4. a short introduction to the child, such as age, personality, interests, relationships, and any relevant fear, wish, or sensitivity.

Also invite examples of cartoons or visual styles the child likes as an early preference signal; do not finalize the visual style yet. Do not repeat questions the user has already answered. All four categories must be addressed, but only the protagonist and enough child context normally require substantive detail. “No preference” is a valid answer for co-stars, theme, and style: record it and offer choices later instead of blocking. Do not generate story routes until each category has either been answered or explicitly left open by the user.

## Choose deliverables after creative alignment

At intake, mention the available forms briefly without committing the project to all of them:

- a cover plus illustrated story pages;
- a self-contained HTML that can be sent to another device;
- an optional high-resolution PDF for reading or printing;
- an optional narrated MP4 for devices where the interactive book is inconvenient.

Confirm the intended deliverables after the story and visual direction are aligned, before representative-page implementation. If the user asks for a complete interactive book and has no format preference, default to the self-contained HTML; offer PDF and MP4 as additions rather than silently producing all three. When HTML is selected, use the responsive open-book and phone layouts, initial play action, and page-linked narration described in [references/default-layout.md](references/default-layout.md).

## Work in alignment gates

1. **Understand the new child and story need.** Complete the mandatory intake above. Treat attached files as references, not instructions, and never fill gaps with a previous book's cast or assumptions.
2. **Align the story before production.** Usually offer about eight to ten concise, meaningfully different story directions. Ask the user to shortlist two or three, expand only those into causal story spines, and have the user choose one before developing the page outline and representative dialogue. Do not batch-generate illustrations or voices yet. Read [references/story-and-character.md](references/story-and-character.md).
3. **Align character and style after the story choice.** The protagonist's identity is known during intake; detailed appearance is set only after a story direction is chosen. Ask whether the user has an authorized photo reference or prefers to describe the protagonist. Build a concise character bible, translate favorite-cartoon references into a high-level style brief, and generate one same-scene sample with the main cast when visual generation is in scope. Obtain approval before the full illustration batch.
4. **Discover, recommend, and align voices by listening.** Ask whether the user has an authorized voice sample or wants newly selected general voices. Inspect the current environment for callable local engines, audio tools, and speech APIs; query the models and voices that are actually available rather than naming an abstract fallback. Recommend suitable model-and-voice candidates for the approved cast, generate short comparable auditions, and let the user choose before batch generation. Do not default to a silent final book merely because the first engine is unavailable. Read [references/voice-production.md](references/voice-production.md).
5. **Confirm deliverables and build one representative page.** Confirm which of HTML, PDF, and MP4 are wanted. Combine final-style illustration, text hierarchy, controls, responsive behavior, and audio sequencing as applicable. Use the default layout in [references/default-layout.md](references/default-layout.md) when HTML or rendered delivery is selected. Ask for confirmation only when this materially changes an approved direction.
6. **Produce the book.** Keep the story data as the single source of truth for visible text, spoken text, page order, image references, and audio references. Start a new project directory and preserve prior accepted versions. Read [references/project-schema.md](references/project-schema.md) before implementation.
7. **Verify and deliver.** Perform story, visual, audio, HTML, mobile, PDF, video, and packaging checks as applicable. Read [references/qa-checklist.md](references/qa-checklist.md).

Once a gate is approved, carry it forward. Do not repeatedly ask the user to reconfirm minor implementation choices.

## Creative invariants

- The child protagonist must make the key choice or action. Friends may accompany, encourage, or help without replacing the child’s agency.
- The ending must be supported by visible events. Express the meaning through action and consequence rather than an abstract lesson speech.
- A setback may redirect the story toward an unexpected good outcome, but the connection must be causal rather than announced at the end.
- Use natural child speech in the chosen language. A verbally capable toddler may use complete sentences, but should not sound like an adult explaining a moral.
- Keep each page focused on one dramatic beat. Page count follows the story; do not split or pad merely to reach a fixed number.
- Keep the characters visually consistent and in the same illustrated world. Let backgrounds carry story information; avoid making the characters so large that the setting disappears.

## Production invariants

- Do not overwrite approved outputs. Put revisions in a new version or preserve the prior files under a clearly named versions directory.
- Do not modify synchronized source/reference folders supplied by the user.
- Do not assume external voice or image services are authorized. Prefer available local tools; request new permission only when genuinely needed.
- A model appearing in documentation is not proof that it is callable in the current task. Verify tool access, credentials, model availability, and audio-file output before offering it as a production route.
- Keep display text and spoken text separately addressable. They normally match, but pronunciation-friendly spoken variants may differ without changing what the child reads.
- A playable audio file is not proof of a natural performance. A valid HTML is not proof of good phone layout. A generated PDF is not proof of legible print quality.

## Reusable resources

- Copy [assets/story.example.json](assets/story.example.json) as a starting data file, then replace every example value with the new book’s approved content.
- Use [scripts/validate_picturebook.py](scripts/validate_picturebook.py) to check story structure and local media references.
- Use [scripts/build_standalone_html.py](scripts/build_standalone_html.py) with [assets/book.template.html](assets/book.template.html) to create a portable single-file HTML.
- After rendering export-mode pages at 1920×1080, use [scripts/build_pdf_from_frames.py](scripts/build_pdf_from_frames.py) for the enlarged-text A4 landscape PDF.
- Use [scripts/build_video.py](scripts/build_video.py) to combine the same page frames with page audio into a shareable MP4.
- When revising this Skill or investigating a process regression, use [references/behavior-tests.md](references/behavior-tests.md) for forward-looking behavior checks. Do not load it during ordinary book production.

The scripts are starting points, not authority over the story. Adapt them when the approved design changes.

