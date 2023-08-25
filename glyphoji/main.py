import os
import json
import difflib


class Glyphoji:
    """
    A class that represents and manages Glyphoji, which enables access to
    various glyphs or emojis by their names and aliases. This class provides
    functionalities to retrieve glyphs by their name, search for glyphs, and
    format them.

    :attr __glyph_dictionary: A dictionary containing the details of all available glyphs.
    """

    def __init__(self):
        """
        Initialises the Glyphoji class by loading the glyphs from data.json.
        """
        self.__glyph_dictionary = self.__data()["glyphs"]

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
        Searches for a glyph by query and returns close matches or suggestions.

        :param query: Search query for glyph
        :return: Glyphs if found, or suggestions if not found
        """
        result = {}
        suggestions = []

        # Check if the query is empty or only contains whitespace
        if query.strip() == "":
            return "[you provided an empty query]"

        # Iterate through the glyph dictionary
        for glyph, data in self.__glyph_dictionary.items():
            # Check if the query (ignoring case) is found in either the 'aliases' or 'description' of the glyph data
            if (
                query.lower() in data["aliases"]
                or query.lower() in data["description"].lower()
            ):
                result[glyph] = data

        # If no matches are found
        if not result:
            # Create a list of all aliases from the glyph dictionary
            all_aliases = [
                alias
                for glyph_data in self.__glyph_dictionary.values()
                for alias in glyph_data["aliases"]
            ]
            # Get close matches to the query from the aliases
            suggestions = difflib.get_close_matches(query, all_aliases)
            # If there are suggestions, return them
            if suggestions:
                return f"[did you mean {', '.join(suggestions)}?]"
            else:
                return f"[no matches found for `{query}`]"

        # If matches are found, return them
        return f"[close matches to `{query}`]\n{self.__get_glyphs(dict_object=result)}"

    @staticmethod
    def __get_glyphs(dict_object: dict) -> str:
        """
        Formats the dictionary of glyphs into a string.

        :param dict_object: Dictionary of glyphs
        :return: Formatted string of glyphs
        """
        return "\n".join([f"{key}: {value}" for key, value in dict_object.items()])

    @staticmethod
    def __data() -> dict:
        """
        Loads the program's data from /data/data.json.

        :return: Dictionary (JSON) containing program data.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, "data", "data.json")
        with open(data_path, encoding="utf-8") as file:
            data = json.load(file)

        return data
