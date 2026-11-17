# pastpapers-data

Past papers ka **structured data** — PDF nahi. App isi se sawal, chapter weightage aur
paper ki tafseel render karti hai.

| File | Kya |
|---|---|
| `manifest.json` | Sab se pehle ye. Version + kaunsi file may kya hai (sha256 ke sath) |
| `<class>/<subject>.json` | Aik class + subject ka poora data (sawal, chapters, papers) |

## Base URL

```
https://cdn.jsdelivr.net/gh/awaisiub689/pastpapers-data@main/manifest.json
```
Fallback: `https://raw.githubusercontent.com/awaisiub689/pastpapers-data/main/manifest.json`

## Update

`manifest.json` → `content_version` badalne par app ko naya data mil jata hai.
