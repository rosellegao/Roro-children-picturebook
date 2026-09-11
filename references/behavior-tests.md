# Behavior test scenarios

Use these scenarios after changing the Skill or when a real run suggests a process regression. Evaluate the produced behavior and artifacts, not whether the response repeats particular wording.

## 1. Bare storybook request

Prompt: `我想给孩子做一本故事书。`

Expected behavior:

- explain briefly what input is needed and ask the four intake categories together;
- do not invent a child, protagonist, co-star, theme, or visual style;
- do not carry over names or characters from an earlier project;
- do not start illustration, voice, or full-deliverable production.

## 2. Open preferences

Prompt: `主角是三岁的乐乐，她很外向，喜欢跑步。配角、主题和画风都没有想法。`

Expected behavior:

- accept the open preferences without another blocking question;
- offer about eight to ten concise and causally distinct story directions;
- wait for a shortlist before expanding complete story spines.

## 3. Character and style timing

Prompt state: the user has selected one story direction but has not supplied appearance references.

Expected behavior:

- ask whether an authorized photo or a text description should guide the protagonist;
- ask for favorite cartoons or illustrated works and translate them into reviewable high-level visual properties;
- create a character bible and one same-scene sample before batch illustration.

## 4. Multiple voice routes

Prompt state: the story and cast are approved, and more than one synthesis route may be available.

Expected behavior:

- inspect current callable tools, local engines, and configured speech APIs;
- query or verify the current model and voice choices for each viable route;
- recommend executable model-and-voice candidates based on reference matching, expressiveness, privacy, and export needs;
- generate comparable short auditions and wait for listening approval before the full batch;
- derive voice cards from the actual cast rather than a fixed family template.

## 5. No callable voice route

Prompt state: documentation names speech models, but no audio tool, local engine, or authenticated API route is callable.

Expected behavior:

- state which execution capability is missing instead of claiming that a listed model is available;
- offer to configure or authorize a route, accept user recordings, or defer the audio stage;
- do not silently finalize a no-audio book without user approval.

## 6. Limited deliverable request

Prompt: `我现在只想先把故事和角色设定做好，不需要网页、PDF 或视频。`

Expected behavior:

- stop after the requested story and character alignment outputs;
- do not produce or repeatedly sell HTML, PDF, MP4, illustration batches, or narration;
- preserve the aligned materials so production can continue later.

## 7. Previous-book contamination

Prompt state: the conversation or workspace contains an earlier child's book, and the new request does not name its cast.

Expected behavior:

- reuse only proven workflow and technical assets;
- do not reuse the earlier child's name, supporting characters, plot, clothing, visual identity, or voice choices;
- ask for the new book's inputs before proposing directions.

## 8. Language follows the user

Prompt: `I want to make a picturebook for my four-year-old.`

Expected behavior:

- respond and conduct intake in English without assuming the book should be Chinese;
- keep the selected language consistent across story text, narration, alt text, interface controls, accessibility labels, and delivery notes;
- set the matching BCP 47 language tag and localized `ui` strings in `story.json`;
- preserve names or phrases supplied in another language unless the user asks to adapt them.

