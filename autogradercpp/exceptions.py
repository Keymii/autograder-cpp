from autogradercpp import ansi_colors
class TestBenchValidationException(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
    def __str__(self) -> str:
        return ansi_colors.colorize_line(self.message, ansi_colors.ERROR_COLOR)

class GccCompilerException(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
    def __str__(self) -> str:
        return ansi_colors.colorize_line(self.message, ansi_colors.ERROR_COLOR)
