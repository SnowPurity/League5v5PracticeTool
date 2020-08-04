# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readfiles():
    f = open('D:\Program Files\League of Legends\LeagueClient\lockfile', 'r')
    lockfile = f.read()
    s = lockfile.split(':')
    port = s[2]
    token = s[3]
    url = "https://riot:" + token + "@127.0.0.1:" + port + "/lol-lobby/v2/lobby"
    print(url)
    req1 = {
        "queueID": 430
    }
    req = {
        "customGameLobby": {
            "configuration": {
                "gameMode": "PRACTICETOOL",
                "gameMutator": "",
                "gameServerRegion": "",
                "mapId": 11,
                "mutators": {
                    "id": 1
                },
                "spectatorPolicy": "AllAllowed",
                "teamSize": 5
            },
            "lobbyName": "5v5训练模式",
            "lobbyPassword": None
        },
        "isCustom": True
    }
    requests.post(url=url,data=req)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readfiles()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
