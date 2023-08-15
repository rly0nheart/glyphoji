![hieroglyph](https://github.com/rly0nheart/glyphoji/assets/74001397/612da558-c52b-48c0-b820-95cce741467e)
*Modern hieroglyphs in the terminal.*

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
[![CodeQL](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml)
[![Upload Python Package](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml)

*Glyphoji is a simple and lightweight emoji library that lets you easily print and format emojis anywhere in the terminal.*
***
## ⬇️ Installation
### 🐍 PyPI
Glyphoji can be installed from PyPI with `pip` by running the command;
```
pip install glyphoji
```
### ❔ GitHub
Intstalling the unreleased version of Glyphoji can also be done with `pip`, unless you want to build it yourself from source.
```
pip install git+https://github.com/rly0nheart/glyphoji.git
```
***
## 📖 Code Examples
### 🔣 Available emojis
All emojis can be printed by calling the *`glyphs`* attribute from *`glyph`*
```Python
from glyphoji import glyph


print(glyph.glyphs)
```

Output;
```
🥑: {'aliases': ['avocado'], 'description': 'An avocado.'}
🍆: {'aliases': ['eggplant'], 'description': 'An eggplant.'}
🥔: {'aliases': ['potato'], 'description': 'A potato.'}
🥕: {'aliases': ['carrot'], 'description': 'A carrot.'}
🌽: {'aliases': ['ear_of_corn', 'corn', 'maize'], 'description': 'An ear of corn.'}
🌶️: {'aliases': ['hot_pepper'], 'description': 'A hot pepper.'}
🫑: {'aliases': ['bell_pepper'], 'description': 'A bell pepper.'}
...
```

### 📄 Formatting glyphs in strings
A Gyphoji glyph/emoji can be formatted and used anywhere. Glyphs can be called from *`glyph`* by specifying the glyph name or alias as the attribute.

```Python
from glyphoji import glyph


print(f"This {glyph.burger} is a burger!")
```
Output;
```
This 🍔 is a burger!
```
### 🔍 Searching Glyphs
Glyphoji also lets users search for a specific glyph, and returns all results that closely match with the query. The query can be the glyph name or a description of the glyph.

```Python
from glyphoji import glyph


query = "flying saucer"
print(glyph.search(query))
```

Output;
```
Close matches to `flying saucer`:
🛸: {'aliases': ['flying_saucer', 'ufo', 'spaceship', 'spacecraft'], 'description': 'A flying saucer.'}
```
***

Made with 🖤 by [Richard Mwewa](https://about.me/rly0nheart)
