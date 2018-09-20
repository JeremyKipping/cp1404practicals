"""CP1404 Practical
    ProgrammingLanguage"""


class ProgrammingLanguage:
    """Represent programming languages"""
    def __init__(self, program, typing, reflection, year):
        """stores languages and information"""
        self.program = program
        self.typing = typing
        self.reflection = reflection
        self.year = year




    def __str__(self):
        return("{}, {}, Reflection={}, First appeared in {}".format(self.program, self.typing, self.reflection, self.year))
