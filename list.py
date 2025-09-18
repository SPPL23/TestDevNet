mySteamLibrary = ["Counter-Strike 2", "Wallpaper Engine", "Wuthering Waves", "Warframe"]
myHoyoLauncher = ["Genshin Impact", "Zenless Zone Zero"]
myName = ["S", "E", "A", "N"]

for i in range(2):
    print(myHoyoLauncher)

for x in myHoyoLauncher:
    x =+ i
    print(mySteamLibrary)

mySteamLibrary[0] = "Jaborant"
print(mySteamLibrary[0])

mySteamLibrary.insert(1, "Apex Legends")
print(mySteamLibrary)

mySteamLibrary.remove("Wallpaper Engine")
print(mySteamLibrary)

mySteamLibrary.pop(0)
print(mySteamLibrary)

mySteamLibrary.insert(4, "Counter-Strike 2")
print(mySteamLibrary)

del mySteamLibrary[0]
print(mySteamLibrary)

myHoyoLauncher.clear()
print(myHoyoLauncher)

myHoyoLauncher.insert(0, "Genshin Impact")
print(myHoyoLauncher)

for num, myName in enumerate(myName):
    print(myName)

for myName in enumerate(myName):
    print(myName)