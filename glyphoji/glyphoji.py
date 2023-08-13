import os
import json
import difflib


def settings() -> dict:
    """
    Loads the program's settings from /data/settings.json.

    :return: Dictionary (JSON) containing program settings
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    settings_path = os.path.join(current_dir, "data", "settings.json")
    with open(settings_path, encoding="utf-8") as file:
        data = json.load(file)

    return data


class Glyphoji:
    def __init__(self):
        """
        Initializes the Glyphoji class by loading the glyphs from settings.
        """
        self.__glyph_dictionary = settings()["glyphs"]

    def __getattr__(self, name: str) -> str:
        """
        Retrieves the glyph associated with the given name or alias.

        :param name: Name or alias of the glyph
        :return: Glyph if found, or a search suggestion if not found
        """
        for glyph, details in self.__glyph_dictionary.items():
            if name in details["aliases"]:
                return glyph

        return self.search(query=name)

    @property
    def glyphs(self) -> str:
        """
        Returns a formatted string of all glyphs.

        :return: String containing all glyphs
        """
        return self.__get_glyphs(dict_object=self.__glyph_dictionary)

    def search(self, query: str) -> str:
        """
        Searches for a glyph by query and returns results or suggestions.

        :param query: Search query for glyph
        :return: Glyphs if found, or suggestions if not found
        """
        result = {}
        # suggestions = []
        for glyph, glyphs in self.__glyph_dictionary.items():
            if query in glyphs["aliases"] or query in glyphs["description"]:
                result[glyph] = glyphs

        if not result:
            all_aliases = [
                alias
                for glyph_data in self.__glyph_dictionary.values()
                for alias in glyph_data["aliases"]
            ]
            suggestions = difflib.get_close_matches(query, all_aliases)
            return f"(did you mean {', '.join(suggestions)}?)"

        return self.__get_glyphs(dict_object=result)

    @staticmethod
    def __prettify_json(json_object: dict) -> str:
        """
        Prettifies a JSON object with indentation.

        :param json_object: JSON object to prettify
        :return: Prettified JSON string
        """
        return json.dumps(json_object, indent=6, ensure_ascii=False)

    @staticmethod
    def __get_glyphs(dict_object: dict) -> str:
        """
        Formats the dictionary of glyphs into a string.

        :param dict_object: Dictionary of glyphs
        :return: Formatted string of glyphs
        """
        return "\n".join([f"{key}: {value}" for key, value in dict_object.items()])
