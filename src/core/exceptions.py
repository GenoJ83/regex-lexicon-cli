class RegexLexiconError(Exception):
    """Base exception."""

class InvalidPatternError(RegexLexiconError):
    """Raised when regex pattern fails compilation."""

class CatastrophicBacktrackError(RegexLexiconError):
    """Raised when regex execution exceeds safe execution steps."""
