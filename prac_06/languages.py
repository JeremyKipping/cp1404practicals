"""CP1404 Practical
    Client code to use ProgrammingLanguage Class"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c++ = ProgrammingLanguage("C++", "Static", False, 1983)
    ruby = ProgrammingLanguage("Ruby","Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(java)
    print(c++)
    print(ruby)
    print(python)
    print(visual_basic)

main()

