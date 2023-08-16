def __init_glyph():
    """
    Initialises and returns an instance of the Glyphoji class from the __main module.

    This function encapsulates the creation of a Glyphoji object, ensuring that
    the Glyphoji class itself is not exposed outside of this module.

    :return: An instance of the Glyphoji class.
    """
    from .main import Glyphoji
    
    return Glyphoji()

glyph = __init_glyph()

__author__ = glyph.settings()["program"]["author"]["name"]
__email__ = glyph.settings()["program"]["author"]["email"]
__version__ = glyph.settings()["program"]["version"]
__description__ = glyph.settings()["program"]["about"]
