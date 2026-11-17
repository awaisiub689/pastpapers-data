# pastpapers-data

Past papers ka **structured data** — PDF nahi. App isi se sawal, chapter weightage aur
paper ki tafseel render karti hai.

## Files

| File | Kya |
|---|---|
| `manifest.json` | Sab se pehle ye. Version + kaunsi file may kya hai (sha256 ke sath) |
| `<class>/<subject>.json` | Aik class + subject ka poora data (sawal, chapters, papers) |

## App kaise padhti hai

1. `manifest.json` fetch → `content_version` dekho
2. Jo version cache may hai wohi? → cache se chalao (offline bhi)
3. Naya? → sirf wohi subject files download jo user kholta hai
4. `sha256` match → cache replace

## Base URL

```
https://cdn.jsdelivr.net/gh/<USER>/pastpapers-data@main/manifest.json
```
Fallback: `https://raw.githubusercontent.com/<USER>/pastpapers-data/main/manifest.json`

## Data ka aakhri update

`manifest.json` → `content_version` dekho.
