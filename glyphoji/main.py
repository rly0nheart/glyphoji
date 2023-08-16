import os
import json
import difflib


class Glyphoji:
    """
    A class that represents and manages Glyphoji, which enables access to
    various glyphs or emojis by their names and aliases. This class provides
    functionalities to retrieve glyphs by their name, search for glyphs, and
    format them.
    
    :attr _glyph_dictionary: A dictionary containing the details of all available glyphs.
    """
       
    def __init__(self):
        """
        Initialises the Glyphoji class by loading the glyphs from settings.
        """
        self._glyph_dictionary = self.__settings()["glyphs"]
        
    def __getattr__(self, name: str) -> str:
        """
        Retrieves the glyph associated with the given name or alias.

        :param name: Name or alias of the glyph
        :return: Glyph if found, or a search suggestion if not found
        """
        for glyph, details in self._glyph_dictionary.items():
            if name in details["aliases"]:
                return glyph

        return self.search(query=name)
        
    @property
    def glyphs(self) -> str:
        """
        Returns a formatted string of all glyphs.

        :return: String containing all glyphs
        """
        return self.__get_glyphs(dict_object=self._glyph_dictionary)

    def search(self, query: str) -> str:
        """
        Searches for a glyph by query and returns results or suggestions.

        :param query: Search query for glyph
        :return: Glyphs if found, or suggestions if not found
        """
        result = {}
        suggestions = []
        for glyph, data in self._glyph_dictionary.items():
            if query in data["aliases"] or query in data["description"]:
                result[glyph] = data

        if not result:
            all_aliases = [
                alias
                for glyph_data in self._glyph_dictionary.values()
                for alias in glyph_data["aliases"]
            ]
            suggestions = difflib.get_close_matches(query, all_aliases)
            return f"(did you mean {', '.join(suggestions)}?)"

        return f"Close matches to `{query}`:\n{self.__get_glyphs(dict_object=result)}"

    @staticmethod
    def __get_glyphs(dict_object: dict) -> str:
        """
        Formats the dictionary of glyphs into a string.

        :param dict_object: Dictionary of glyphs
        :return: Formatted string of glyphs
        """
        return "\n".join([f"{key}: {value}" for key, value in dict_object.items()])

    @staticmethod
    def __settings() -> dict:
        """
        Loads the program's settings from /data/settings.json.

        :return: Dictionary (JSON) containing program settings
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        settings_path = os.path.join(current_dir, "data", "settings.json")
        with open(settings_path, encoding="utf-8") as file:
            data = json.load(file)

        return data
