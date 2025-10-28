"""
Estimated Time: 20 mins
Actual Time: 14 mins
"""


class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection="", year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.reflection is True

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
