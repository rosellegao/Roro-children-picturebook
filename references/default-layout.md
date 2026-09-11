# Default picturebook layout

## Experience model

The default should feel like opening a purchased picturebook, not reading a long webpage.

- Cover: full-bleed illustration, a warm paper-like title card, a visible series name, and the story title as the largest text. A short subtitle may appear but is not narrated unless the user asks.
- Story page: illustration on the left, text page on the right, soft cream paper, rounded outer book frame, warm colors, and restrained decorative details.
- Text hierarchy: small act label, large page title, then narration and dialogue. Speaker chips make roles easy to scan. A decisive closing sentence may use a gentle highlighted box.
- Characters should not fill the whole illustration. Show enough classroom, playground, home, path, weather, or props for the setting to explain what is happening.

## Responsive behavior

Desktop and phone landscape use a two-panel spread. Start near a 59/41 illustration-to-text split and adjust for the page’s actual copy. Phone landscape needs larger right-side text than a scaled-down desktop layout.

Phone portrait stacks the illustration above the text and keeps controls within easy thumb reach. The text panel may scroll only when necessary; first shorten or repaginate overlong copy and use responsive type before accepting hidden or obstructed text.

Use device-independent CSS breakpoints and viewport units rather than requiring the reader to choose “mobile” manually. Include viewport metadata, safe-area padding, large touch targets, swipe navigation, keyboard navigation, and visible focus states.

## Playback behavior

Mobile browsers require a user gesture before audio. Therefore:

1. show a localized “play and start the story” action on the cover;
2. start cover audio only after that action;
3. after the story has started, changing pages automatically plays the new page;
4. provide play/pause and replay without changing the page order;
5. do not auto-advance to the next page unless the user chooses a continuous-listening mode.

The current speaker, next action, and page count should always be understandable. Never let a replay control corrupt story progression.

## Standalone HTML

The shareable HTML must contain its CSS, JavaScript, illustrations, and audio. It must not depend on `localhost`, a development server, a CDN, or sibling asset folders. Test the exact delivered file, not only the development site.

Provide an export mode that can open a chosen page without controls. A practical contract is `?export=1&page=0`, where page is zero-based. Render every page at 1920×1080 for PDF and video production.

## PDF

Default to A4 landscape. Place each uncropped 16:9 export frame at full printable width and center it vertically. Use warm bands above and below rather than stretching or cropping. Embed the original 1920×1080 frame so the right-side text remains sharp. Preserve an earlier accepted PDF under a different filename.

## MP4

Use the same 1920×1080 page frames and the same approved per-page audio. A useful default is a short pause of roughly half a second between pages and a slightly longer hold on the ending. Encode broadly compatible H.264 video with `yuv420p`, AAC audio, and fast-start metadata. Do not lower the type size for the video simply because the frame is 1080p.

## Visual quality test

Inspect representative desktop, phone portrait, and phone landscape views, then inspect all export frames as a contact sheet. Check the densest text page and ending at full size. A passing layout has no clipped text, covered controls, accidental scrollbars, distorted art, or unreadably small phone-landscape type.

