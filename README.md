![hieroglyph](https://github.com/rly0nheart/glyphoji/assets/74001397/612da558-c52b-48c0-b820-95cce741467e)
*Modern hieroglyphs in the terminal.*

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
[![CodeQL](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml)
[![Upload Python Package](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml)

Glyphoji lets you easily print and format emojis anywhere, with the latest emoji's support.

# ⬇️ Installation
## 🐍 PyPI
Glyphoji can be installed from PyPI with `pip` by running the command;
```
pip install glyphoji
```
## ❔ GitHub
Intstalling the unreleased version of Glyphoji can also be done with `pip`, unless you want to build it yourself from source.
```
pip install git+https://github.com/rly0nheart/glyphoji.git
```
***
# 📖 Code Examples
## 🔣 Available emojis
All emojis can be printed by calling the *`glyphs`* attribute from *`glyph`*
```Python
from glyphoji import glyph


print(glyph.glyphs)
```

Output;
```
🗣️: {'aliases': ['speaking_head'], 'description': 'Speaking head.'}
👤: {'aliases': ['bust_in_silhouette'], 'description': 'Bust in silhouette.'}
🧠: {'aliases': ['brain'], 'description': 'A brain.'}
🫀: {'aliases': ['anatomical_heart'], 'description': 'An anatomical heart.'}
🫁: {'aliases': ['lungs'], 'description': 'Lungs.'}
🦷: {'aliases': ['tooth'], 'description': 'A tooth.'}
🦴: {'aliases': ['bone'], 'description': 'A bone.'}
👀: {'aliases': ['eyes', 'see'], 'description': 'A pair of eyes.'}
👅: {'aliases': ['tongue'], 'description': 'A tongue.'}
👄: {'aliases': ['mouth'], 'description': 'A mouth.'}
🪥: {'aliases': ['toothbrush'], 'description': 'A toothbrush.'}
👣: {'aliases': ['footprints'], 'description': 'Footprints.'}
🧬: {'aliases': ['dna'], 'description': 'A DNA double helix.'}
🩸: {'aliases': ['drop_of_blood'], 'description': 'A drop of blood.'}
❤️‍🔥: {'aliases': ['heart_on_fire'], 'description': 'A heart on fire.'}
...
```

## 📄 Formatting glyphs in strings
A Gyphoji glyph/emoji can be formatted and used anywhere. Glyphs can be called from *`glyph`* by specifying the glyph name or alias as the attribute.

```Python
from glyphoji import glyph


print(f"This {glyph.burger} is a burger!")
```
Output;
```
This 🍔 is a burger!
```
## 🔍 Searching Glyphs
Glyphoji also lets users search for a specific glyph, and returns all results that closely match with the query. The query can be the glyph name or a description of the glyph.

```Python
from glyphoji import glyph


query = "alien spacecraft"
print(glyph.search(query))
```

Output;
```
🛸: {'aliases': ['ufo', 'spaceship', 'spacecraft'], 'description': 'An alien spacecraft.'}
```
***

Made with 🖤 by [Richard Mwewa](https://about.me/rly0nheart)
