# ANSI escape codes
FG_BLACK = "\033[90m"
FG_RED = "\033[91m"
FG_GREEN = "\033[92m"
FG_YELLOW = "\033[93m"
FG_BLUE = "\033[94m"
FG_MAGENTA = "\033[95m"
FG_CYAN = "\033[96m"
FG_WHITE = "\033[97m"
BG_BLACK = "\033[100m"
BG_RED = "\033[101m"
BG_GREEN = "\033[102m"
BG_YELLOW = "\033[103m"
BG_BLUE = "\033[104m"
BG_MAGENTA = "\033[105m"
BG_CYAN = "\033[106m"
BG_WHITE = "\033[107m"
REGULAR = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
RAPID_BLINK = "\033[6m"
NEGATIVE = "\033[7m"
HIDDEN = "\033[8m"
STRIKE_THROUGH = "\033[9m"
RESET = "\033[0m"
# ~ANSI escape codes

rainbow_colors = [1, 3, 2, 4, 6, 5, 7]


def print_rainbow(text, end="\n"):
    for i, char in enumerate(text):
        print(f"\033[9{rainbow_colors[i % 7]}m{char}", end="")
    print(RESET, end=end)
