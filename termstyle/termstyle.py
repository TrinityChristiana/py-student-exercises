import time, sys, random

class f_color:
    default = '\033[99m'
    black = '\033[30m'
    grey = '\033[90m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    bright_black = '\033[30;1m'
    bright_red = '\033[31;1m'
    bright_green = '\033[32;1m'
    bright_yellow = '\033[33;1m'
    bright_blue = '\033[34;1m'
    bright_magenta = '\033[35;1m'
    bright_cyan = '\033[36;1m'
    bright_white = '\033[37;1m'
    test = '\033[38;5;1m'

    def _256(self, number):
        """ 1- 255 """
        return(f'\033[38;5;{number}m')

class style:
    end = '\033[0m'
    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    reverse_video = '\033[7m'
    conceal = '\033[8m'

class b_color:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'
    bright_black = '\033[100m'
    bright_red = '\033[101m'
    bright_green = '\033[102m'
    bright_yellow = '\033[103m'
    bright_blue = '\033[104m'
    bright_magenta = '\033[105m'
    bright_cyan = '\033[106m'
    bright_white = '\033[107m'

    def _256(self, number):
        """ 1- 255 """
        return(f'\033[48;5;{number}m')

class Progress():
    def percentage(self, set_time = .01, text = "Loading"):
        """
        set_time: number interval in seconds
        """
        print(f"{text}...")
        for i in range(0, 100):
            time.sleep(set_time)
            sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
            sys.stdout.flush()
        print

    def bar(self, count = 1, spaces = 25, seconds = .01, progress_text = "#", colors = False):

        """
        count - how many bars to show

        spaces - how many spaces to show on each bar

        seconds - interval between each add to progress

        progress_text - text used for progress bar

        colors - want random colors for each progress bar (True of false)
        """
        max_length = 100
        length = len(progress_text)
        if spaces * length > max_length:
            spaces = int(max_length / length)
        num = spaces * 4
        all_progress = [0] * count
        sys.stdout.write("\n" * count) # Make sure we have space to draw the bars
        while any(x < num for x in all_progress):
            time.sleep(seconds)
            # Randomly increment one of our progress values
            unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < num]
            index, _ = random.choice(unfinished)
            all_progress[index] += 1
            random.choice(range(0, 256))
            # Draw the progress bars
            sys.stdout.write(u"\u001b[1000D") # Move left
            sys.stdout.write(u"\u001b[" + str(count) + "A") # Move up
            for progress in all_progress: 
                width = int(progress / 4)
                space = " " * length
                
                random_color = random.choice(range(0, 265))
                b_or_f = random.choice([True, False])
                print( f"{b_color()._256(random_color) if colors and b_or_f else ''} {f_color()._256(random_color) if colors and not b_or_f else ''}[ {progress_text * width}{space * (spaces - width)}]")

def show_colors():
    print("**** Font Colors****")
    print(f"{f_color.red} Red {style.end}")
    print(f"{f_color.green} Green {style.end}")
    print(f"{f_color.blue} blue {style.end}")
    print(f"{f_color.cyan} cyan {style.end}")
    print(f"{f_color.white} white {style.end}")
    print(f"{f_color.yellow} yellow {style.end}")
    print(f"{f_color.magenta} magenta {style.end}")
    print(f"{f_color.grey} grey {style.end}")
    print(f"{f_color.black} black {style.end}")
    print(f"{f_color.default} default {style.end}")

def show_bright_colors():
    print("**** Bright Font Colors****")
    print(f"{f_color.bright_red} Red {style.end}")
    print(f"{f_color.bright_green} Green {style.end}")
    print(f"{f_color.bright_blue} blue {style.end}")
    print(f"{f_color.bright_cyan} cyan {style.end}")
    print(f"{f_color.bright_white} white {style.end}")
    print(f"{f_color.bright_yellow} yellow {style.end}")
    print(f"{f_color.bright_magenta} magenta {style.end}")
    print(f"{f_color.bright_black} black {style.end}")

def show_256_colors():
    string = ""
    for i in range(0, 256):
        string += f"{f_color()._256(i)} {i}"

    print(string)

def show_256_b_colors():
    string = ""
    for i in range(0, 256):
        string += f"{b_color()._256(i)} {i}"

    print(string)

def show_styles():
    print("**** Styles Font Colors****")
    print(f"{style.bold} Bold {style.end}")
    print(f"{style.dim} Dim {style.end}")
    print(f"{style.italic} Italic {style.end}")
    print(f"{style.underline} Underline {style.end}")
    print(f"{style.reverse_video} Reverse {style.end}")
    print(f"{style.conceal} Conceal {style.end} <-- Conceal")

def show_background():
    print("**** Fonts ****")
    print(f"{b_color.black} Black {style.end}")
    print(f"{b_color.red} red {style.end}")
    print(f"{b_color.green} green {style.end}")
    print(f"{b_color.yellow} yellow {style.end}")
    print(f"{b_color.blue} blue {style.end}")
    print(f"{b_color.magenta} magenta {style.end}")
    print(f"{b_color.cyan} cyan {style.end}")
    print(f"{b_color.white} white {style.end}")

def show_bright_background():
    print("**** Bright Background ****")
    print(f"{b_color.bright_black} bright Black {style.end}")
    print(f"{b_color.bright_red} bright red {style.end}")
    print(f"{b_color.bright_green} bright green {style.end}")
    print(f"{b_color.bright_yellow} bright yellow {style.end}")
    print(f"{b_color.bright_blue} bright blue {style.end}")
    print(f"{b_color.bright_magenta} bright magenta {style.end}")
    print(f"{b_color.bright_cyan} bright cyan {style.end}")
    print(f"{b_color.bright_white} bright white {style.end}")



load = Progress() 

load.bar(50, 500, .01, "MADRE ", colors=True)

