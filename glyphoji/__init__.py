from glyphoji.glyphoji import Glyphoji, settings

__author__ = settings()["program"]["author"]["name"]
__email__ = settings()["program"]["author"]["email"]
__version__ = settings()["program"]["version"]
__description__ = settings()["program"]["about"]


# Creating a singleton instance of the Glyphoji class.
# This instance will be shared throughout the application and can
# be accessed directly after importing the glyphoji package
glyph = Glyphoji()
