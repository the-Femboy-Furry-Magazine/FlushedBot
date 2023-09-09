BOT_PREFIX = "f!"
moderators = ["1", "873014876275114005"]
servmods = ["1"]
slurred = False
version = "0.42"
github_link = "https://github.com/the-Femboy-Furry-Magazine/FlushedBot"

def load_list_from_txt(filename):
    try:
        file = open(filename, "r")
    except Exception as err:
        print(  '\n                                   +-+'
                '\n +----  +---+ +---+ +---+ +---+   ++#++'
                '\n |      |   | |   | |   | |   |  ++# #++'
                '\n +----  +--++ +--++ |   | +--++ ++## ##++'
                '\n |      |  |  |  |  |   | |  | -+#######++'
                '\n +----  |  +- |  +- +---+ |  +- #### ####|'
                '\n                                ----------+'
               f'\n{filename} could not be opened.'
               f'\n{err}'
               f'\nThis is probably not fatal, but certain commands\nmay be broken.\nIf slurs.txt is missing, then the bot won\'t be able to filter slurs.'
                '\nYou can download the text files from the GitHub, if you really need them.'
               f'\n{github_link}'
                )
        return
    output = file.readlines()
    for i in range(len(output)):
        output[i] = output[i].removesuffix('\n')

    file.close()
    return output

def load_list_from_txt_b(filename):
    try:
        file = open(filename, "r")
    except Exception as err:
        print(  '\n                                   +-+'
                '\n +----  +---+ +---+ +---+ +---+   ++#++'
                '\n |      |   | |   | |   | |   |  ++# #++'
                '\n +----  +--++ +--++ |   | +--++ ++## ##++'
                '\n |      |  |  |  |  |   | |  | -+#######++'
                '\n +----  |  +- |  +- +---+ |  +- #### ####|'
                '\n                                ----------+'
               f'\n{filename} could not be opened.'
               f'\n{err}'
               f'\nThis is not fatal. The bot can continue to run without startup text.')
        return
    output = file.read()

    file.close()
    return output


slurs = load_list_from_txt("slurs.txt")
eight_ball = load_list_from_txt("8ball.txt")
uwu_emotes = load_list_from_txt("uwu.txt")
startup = load_list_from_txt_b("startup.txt")

print(startup)
