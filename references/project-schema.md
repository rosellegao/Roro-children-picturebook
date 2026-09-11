# Project structure and story data

Use one independent directory for each book. A practical structure is:

```text
book-project/
|-- story.json
|-- character-bible.md
|-- assets/
|   |-- references/
|   `-- pages/
|-- audio/
|   |-- references/
|   |-- clips/
|   |-- pages/
|   `-- manifest.json
|-- rendered/
|-- output/
|   |-- html/
|   |-- pdf/
|   `-- video/
`-- versions/
```

`story.json` is the governing source for page order, visible copy, spoken copy, illustrations, page audio, and localized reader controls. The reusable scripts accept this shape:

```json
{
  "book": {
    "series": "Sam's First Adventures",
    "title": "Sam's New Story",
    "subtitle": "A warm story about trying and friendship.",
    "language": "en",
    "output_basename": "sam-new-story"
  },
  "ui": {
    "bookLabel": "Picture book",
    "start": "🔊 Play and start the story",
    "navigation": "Picture book navigation",
    "previous": "Previous page",
    "toggle": "Play or pause",
    "replay": "Replay this page",
    "next": "Next page",
    "continueAudio": "Tap play to continue listening to this page.",
    "cover": "Cover",
    "audioError": "This page’s audio could not load. Please try again."
  },
  "speakers": {
    "Narrator": { "color": "#EC745F" },
    "Protagonist": { "color": "#E96E86" },
    "Friend": { "color": "#E1A43B" }
  },
  "pages": [
    {
      "chapter": "Series name",
      "title": "Book title",
      "cover": true,
      "image": "assets/pages/page-01.png",
      "audio": "audio/pages/page-01.mp3",
      "alt": "A short description of the illustration",
      "lines": [
        { "text": "A cover subtitle that may remain unspoken.", "spoken": false }
      ]
    },
    {
      "chapter": "Act One",
      "title": "Page title",
      "image": "assets/pages/page-02.png",
      "audio": "audio/pages/page-02.mp3",
      "alt": "A short description of the illustration",
      "lines": [
        { "speaker": "Narrator", "text": "Visible and spoken narration." },
        { "speaker": "Protagonist", "text": "Character dialogue.", "speech_text": "Optional synthesis-friendly wording." },
        { "text": "A decisive closing idea.", "emphasis": true }
      ]
    }
  ]
}
```

Rules:

- Use the user's language unless they explicitly choose another for the book. Set `book.language` to its BCP 47 tag and localize every `ui` value.
- `image` is required for every page; `audio` is optional until narration is produced.
- A line without a `speaker` is narration or cover copy.
- `spoken: false` excludes a displayed line from narration.
- `speech_text` changes synthesis input only; readers still see `text`.
- `emphasis: true` is for a small number of decisive sentences, usually the earned closing idea.
- `output_basename` must be safe as a filename and must not contain a path.

Update this source first when copy or localization changes, then regenerate audio, HTML, PDF, and video so the formats do not drift apart.

