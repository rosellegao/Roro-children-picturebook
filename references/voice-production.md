# Voice production

## Voice reference and permission

Before choosing voices, ask whether the user has a voice sample they are authorized to use or prefers newly selected general voices. A sample may guide pace, warmth, energy, pitch, and pronunciation without authorizing an exact imitation. Treat cloning or creation of a custom voice as a separate decision that requires the relevant speaker's consent and a synthesis route that supports it. When authorization or capability is unclear, use a general voice rather than promising a replica.

## Voice design

Build voice cards from the approved story cast before generating the full book. Do not start from a fixed family or four-role template. Create one card for each distinct speaking role, including a narrator only when the chosen book uses one. Record:

- the role's function and personality in this story;
- apparent age or character type;
- pitch or vocal register, pace, warmth, energy, and articulation;
- pronunciation and performance notes;
- the selected engine, model, voice, and authorized reference, if any;
- how this voice stays distinguishable from the other recurring voices.

Two roles may share an underlying voice only when the user prefers it and their delivery can remain clearly distinct. For example, narration may be more spacious while direct speech is more conversational.

## Audition before batch generation

Choose a short set that exposes likely weaknesses:

- an opening narration line;
- a question with a comma or semantic turn;
- a delighted or surprised line;
- an onomatopoeic phrase;
- one longer child sentence;
- one line per supporting character.

Ask the user to choose or refine these samples. Preserve approved voices and regenerate only the affected lines when later feedback is local.

## Natural delivery

Speed, pitch, and inserted silence do not by themselves create natural speech. Listen for:

- an unwanted intake of breath at the beginning;
- tension or strain inherited from the reference recording;
- a stretched sentence ending that sounds imitative rather than conversational;
- mechanical pauses at every comma;
- a missing pause at a real change of thought;
- unnatural emphasis around a name;
- literal, stiff pronunciation of onomatopoeia.

Split or rewrite the spoken form when the speech engine needs help, while preserving the displayed wording. For example, displayed `骨碌、骨碌` may be spoken as a playful `咕噜噜、咕噜噜……`. Keep a manifest with both `text` and optional `speech_text` so the difference is auditable.

Read titles more slowly than normal narration. Do not narrate a cover subtitle unless requested.

## Synthesis route

### Discover what is actually callable

At the start of the voice stage, inspect the current environment rather than assuming that a tool used on another computer is present here:

1. identify callable audio or text-to-speech tools exposed in the current task;
2. check suitable local engines and their available reference voices when local execution is possible;
3. check configured speech providers or APIs without exposing credentials;
4. when a provider or tool can list its supported models and voices, query that list at runtime;
5. when it cannot list them but official documentation is available, verify the current speech-generation documentation before choosing;
6. confirm with a minimal generation that the route can return a usable audio file.

A model listed in a catalog is not available for this project until an executable tool or authenticated API route succeeds. Do not describe conversational voice playback as a production route unless it can export the required page audio.

For an OpenAI Speech route, use the currently supported speech endpoint and verify its model and voice list at the time of use. `gpt-4o-mini-tts` is a suitable initial candidate as of this revision because it supports performance instructions, but treat that name as a candidate to verify, not a permanent hard-coded dependency.

### Recommend a route and auditions

Choose by the user's need, not by a universal engine ranking:

- for an authorized reference voice or stronger identity matching, prefer a capable local or custom-voice route;
- for a new general voice with expressive direction, prefer an available speech model that supports style instructions;
- for privacy or offline requirements, prefer a verified local route;
- when several routes are viable, compare them on the same short lines before recommending one.

Query the available models and voices, then present only executable candidates. Recommend two or three suitable voice candidates for each distinct voice category, with the exact model, voice name or reference, and a short reason. Generate comparable auditions and record the user's chosen model-and-voice pair in each voice card.

If the preferred engine is unavailable, try the next verified route. If none is callable, explain the specific missing capability and ask whether the user wants to authorize or configure another route, provide recordings, or defer audio. Produce a silent deliverable only when the user explicitly accepts that scope.

### Generate the selected route

Generate clips deterministically where possible, trim only genuine leading or trailing silence, normalize conservatively, and retain raw clips when post-processing a voice.

Keep per-line clips, per-page masters, compressed delivery audio, and a manifest. Each page master should follow the visible line order exactly. Do not silently omit, duplicate, or reorder lines.

## Acceptance

Technical checks cover file existence, duration, sample rate, clipping, and decoding. Listening checks cover naturalness, role distinction, pacing, emotion, pronunciation, and text fidelity. Both are required before full-book approval.

