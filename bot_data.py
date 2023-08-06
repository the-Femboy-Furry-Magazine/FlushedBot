BOT_PREFIX = "f!"


def load_list_from_txt(filename):
    file = open(filename, "r")
    output = file.readlines()
    for i in range(len(output)):
        output[i] = output[i].removesuffix('\n')

    file.close()
    return output


slurs = load_list_from_txt("slurs.txt")
eight_ball = load_list_from_txt("8ball.txt")
uwu_emotes = load_list_from_txt("uwu.txt")

moderators = ["1", "873014876275114005"]

servmods = ["1"]
slurred = False
version = "0.35-beta"
github_link = "https://github.com/p866e/FlushedBot"


print(slurs)
print(eight_ball)
print(uwu_emotes)
