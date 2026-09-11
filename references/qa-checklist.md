# Acceptance checklist

## Language and localization

- Does the interaction and finished book follow the user's language unless they explicitly chose another?
- Does `book.language` use the correct BCP 47 tag?
- Are visible copy, narration, alt text, interface controls, notices, and accessibility labels localized consistently?
- Were names and supplied phrases preserved unless adaptation was requested?

## Story

- Were the protagonist, preferred character types, theme, and child introduction explicitly resolved or marked as open by the user?
- Was one story route approved before detailed character and style production began?
- Can the spine be stated in one or two sentences?
- Does each page cause or motivate the next?
- Does the child’s action change the outcome?
- Does the ending visibly prove its meaning?
- Do the characters sound like themselves when read aloud?

## Illustration

- If a child's photo was used, was permission confirmed and was the source photo excluded from the delivery package unless requested?
- Does the approved style brief reflect high-level preferences without accidentally importing an earlier book's cast or plot?
- Is the protagonist consistent with the approved character sample?
- Are clothing, bag, hair, skin tone, proportions, and recurring props stable?
- Do all characters share one illustration world?
- Is enough background visible to understand place and action?
- Do consecutive pages vary composition without breaking continuity?
- Does each image depict the same event as its text and audio?

## Audio

- Is every reference voice authorized for the way it is being used, with exact imitation treated separately from general vocal guidance?
- Was the current environment inspected for callable local engines, audio tools, and speech APIs?
- Were model and voice candidates queried or verified at the time of use rather than assumed from a static list?
- Does every voice card name the selected engine, model, voice or reference, and relevant performance direction?
- Was the selected synthesis route proven to return a usable audio file before batch generation?
- If no synthesis route was available, did the user explicitly approve deferring audio or receiving a silent deliverable?
- Has every approved voice been auditioned by listening?
- Are narrator and characters distinguishable without looking?
- Are beginnings free of odd breaths and endings free of unwanted stretching?
- Are questions, semantic turns, names, and onomatopoeia natural?
- Does every visible spoken line occur once, in order, with a stable voice?
- Do all files decode, have plausible duration, and avoid clipping?

## HTML

- Does the exact delivered file open without a server or network connection?
- Are all images, styles, scripts, and audio embedded?
- Does the first play action unlock audio on mobile?
- Does turning a page play only the new page after the story has started?
- Do previous, next, play/pause, replay, keyboard, and swipe controls work?
- Is the next action obvious and are disabled controls visibly disabled?

## Responsive layout

- Desktop: does the spread fit without unnecessary scrolling?
- Phone portrait: is the picture above the text, with controls reachable and text unobstructed?
- Phone landscape: is the story text large enough to read, not merely a scaled desktop view?
- Densest page: is every line visible or intentionally scrollable?
- Cover: does it look like a real children’s book cover, with the title dominant?

## PDF

- Is it high-resolution A4 landscape with uncropped pages?
- Is the right-side text comfortably legible at normal zoom and in print preview?
- Are all pages present and in order?
- Has the rendered PDF, not just the source frames, been visually inspected?

## MP4

- Does it use the final large-text frames and approved audio?
- Are page durations complete, with no cut-off speech?
- Is it 1920×1080 H.264 `yuv420p` with AAC audio and fast-start metadata?
- Does the entire file decode successfully?

## Delivery

- Does the package contain only the HTML, PDF, MP4, or other formats the user selected?
- Keep multiple selected formats under clear matching names.
- Preserve earlier accepted versions instead of overwriting them.
- If a ZIP is delivered, open it and verify that it contains the intended final files and no private source photographs or unnecessary working assets.
- Report only checks that actually passed. Separate technical validity from subjective quality that still awaits user approval.

