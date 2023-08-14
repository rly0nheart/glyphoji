import unittest
from glyphoji import glyph


class TestGlyphoji(unittest.TestCase):
    def test_glyphs(self):
        # Testing the glyphs property to ensure it returns the correct format
        self.assertIsInstance(glyph.glyphs, str)
        self.assertTrue(": " in glyph.glyphs)

    def test_getattr(self):
        # Testing the __getattr__ method with a known alias.
        result = glyph.__getattr__("ufo")
        self.assertIsInstance(result, str)

        # Testing with an unknown alias
        unknown_result = glyph.__getattr__("unknown_alias")
        self.assertIsInstance(unknown_result, str)
        self.assertIn("🛸", result)  # Checking that the result contains the "🛸" emoji
        self.assertIn("did you mean", unknown_result)

    def test_search(self):
        # Testing the search method (used to find glyphs/emojis)
        result = glyph.search(query="unidentified flying object")
        self.assertIsInstance(result, str)

        # Testing with an unknown query
        unknown_result = glyph.search("unknown_query")
        self.assertIsInstance(unknown_result, str)
        self.assertIn("🛸", result)  # Checking that the result contains the "🛸" emoji
        self.assertIn("did you mean", unknown_result)

    def test_prettify_json(self):
        # Testing the __prettify_json static method
        json_object = {"a": 1, "b": 2}
        result = glyph._Glyphoji__prettify_json(json_object)
        self.assertIsInstance(result, str)
        self.assertIn("\n", result)

    def test_get_glyphs(self):
        # Testing the __get_glyphs static method
        dict_object = {"a": "value_a", "b": "value_b"}
        result = glyph._Glyphoji__get_glyphs(dict_object)
        self.assertIsInstance(result, str)
        self.assertIn("a: value_a", result)
        self.assertIn("b: value_b", result)


if __name__ == "__main__":
    unittest.main()
