![glyphoji-snake](https://github.com/rly0nheart/glyphoji/assets/74001397/1b32fe5a-ef9a-48b6-89f7-0e0bd647704c)

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![PyPI - Downloads](https://img.shields.io/pypi/dm/glyphoji?logo=pypi)
[![CodeQL](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/codeql.yml)
[![Upload Python Package](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/glyphoji/actions/workflows/python-publish.yml)

*Glyphoji is a simple and lightweight emoji library that lets you easily print and format emojis anywhere in the terminal.*
***

# ℹ️ Getting Started
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
### 🔣 Available Glyphs/Emojis
All glyphs/emojis can be printed by accessing the *`glyphs`* attribute from the *`glyph`* instance.
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
A Gyphoji glyph/emoji can be formatted and used anywhere. Glyphs can be accessed from the *`glyph`* instance by specifying the glyph name/alias as the attribute.

```Python
from glyphoji import glyph


print(f"This {glyph.burger} is a burger!")
```
Output;
```
This 🍔 is a burger!
```
### 🔍 Searching Glyphs
Glyphoji also lets users search for a specific glyph, and returns all results that closely match with the query. The query can be the glyph name/alias or a description of the glyph.

```Python
from glyphoji import glyph


query = "flying saucer"
print(glyph.search(query))
```

Output;
```
[close matches to `flying saucer`]
🛸: {'aliases': ['flying_saucer', 'ufo', 'spaceship', 'spacecraft'], 'description': 'A flying saucer.'}
```
***
![python-powered](https://github.com/rly0nheart/glyphoji/assets/74001397/797adebc-2b98-41bc-9019-2b0079fc32dc)

*Made with 🖤 by [Richard Mwewa](https://about.me/rly0nheart)*
