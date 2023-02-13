#Made by KewlRadical
#Icons by gravisio on https://www.flaticon.com/free-icon/key_9679511?term=lock&page=1&position=7&origin=search&related_id=9679511
#           /^\/^\
#         _|__|  O|
#\/     /~     \_/ \
# \____|__________/  \
#        \_______      \
#                `\     \                 \
#                  |     |                  \
#                 /      /                    \
#                /     /                       \\
#              /      /                         \ \
#             /     /                            \  \
#           /     /             _----_            \   \
#          /     /           _-~      ~-_         |   |
#         (      (        _-~    _--_    ~-_     _/   |
#          \      ~-____-~    _-~    ~-_    ~-_-~    /
#            ~-_           _-~          ~-_       _-~
#               ~--______-~                ~-___-~#

import rumps
import pyperclip
import secrets, string



alphabet = string.ascii_letters + string.digits + string.punctuation

# generate a password
def generate_password(pwd_length):

    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    pyperclip.copy(pwd)    


class PasswordApp(rumps.App):
    @rumps.clicked("Create Password")
    def password(self, _):
        generate_password(16)
        rumps.notification("◈ | Passy", "Password Coppied to Clipboard", "", data=None)

if __name__ == "__main__":
    PasswordApp("Passy", "​", icon="icon.png").run()   