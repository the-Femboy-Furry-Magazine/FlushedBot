BOT_PREFIX = "f!"


def load_list_from_txt(filename):
    file = open(filename, "r")
    output = file.readlines()
    for i in range(len(output)):
        output[i] = output[i].removesuffix('\n')

    file.close()
    return output

def load_list_from_txt_b(filename):
    file = open(filename, "r")
    output = file.read()

    file.close()
    return output


slurs = load_list_from_txt("slurs.txt")
eight_ball = load_list_from_txt("8ball.txt")
uwu_emotes = load_list_from_txt("uwu.txt")
startup = load_list_from_txt_b("startup.txt")

moderators = ["1", "873014876275114005"]

servmods = ["1"]
slurred = False
version = "0.4"
github_link = "https://github.com/the-Femboy-Furry-Magazine/FlushedBot"

print(bot_data.startup)

print(slurs)
print(eight_ball)
print(uwu_emotes)
