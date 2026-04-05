class CodeGenerator:
    @staticmethod
    def to_python(pattern: str) -> str:
        return f"import re\n\nregex = re.compile(r'{pattern}')\nmatch = regex.search(input_text)"
        
    @staticmethod
    def to_javascript(pattern: str) -> str:
        return f"const regex = /{pattern}/;\nconst match = regex.exec(inputText);"
        
    @staticmethod
    def to_golang(pattern: str) -> str:
        return f"package main\n\nimport \"regexp\"\n\nvar rx = regexp.MustCompile(\"{pattern}\")"
