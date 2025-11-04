"""
Estimated Time: 20 mins
Actual Time: 14 mins
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, language="", typing="", reflection="", year=0):
        """Construct a ProgrammingLanguage from given values."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamic."""
        return self.reflection == "Dynamic"

    def __str__(self):
        """Return string representation."""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
