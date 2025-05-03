from os import system

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKtCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    repos = open("repos", "r").read()
    software = open("software", "r").read()

    for repo in repos.split("\n\n"):
        print(repo)
        system(f"{repo}")

    for program in software.split():
        print(program)
        system(f"sudo dnf install {program}")

except Exception as e:
    print(bcolors.FAIL + f"Fail: {e}" + \
          bcolors.ENDC)

system("git clone https://github.com/MrStewie404/aesthetic-wallpapers.git ~/Downloads/")
system("cp ./applications/* /usr/applications")
system("cp ./dotfiles/* ~/.config/")
