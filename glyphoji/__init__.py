def __init_lib__():
    """
    Initialises and returns an instance of the Glyphoji class from the main module.

    This function encapsulates the creation of a Glyphoji object, ensuring that
    the Glyphoji class itself is not exposed outside of this module.

    :return: An instance of the Glyphoji class (glyph).
    """
    from .glyphoji import Glyphoji

    return Glyphoji()


__all__ = ["glyph"]
glyph = __init_lib__()
