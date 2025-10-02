gamit = [
    ("1. sala", "computer", "shelf", "monoblock"),
    ("2. comshop", "keyboard", "mouse", "headset"),
    ("3. kusina", "kutsara", "tinidor", "baso"),
    ]

(kwarto1, kwarto2, kwarto3) = gamit
(_, comp, shelf, monoblock) = kwarto1
(_, keyb, mouse, heads) = kwarto2
(_, kuts, tini, baso) = kwarto3


for k in gamit:
    print(k[0])

saan = int(input("San ka punta?: "))

match saan:
    case 1:
        print(comp, shelf, monoblock)
        sala = input("Pumili ka ng gamit: ")

        match sala:
            case "computer":
                print("Nag roblox")
            case "shelf":
                print("May adult magazine")
            case "monoblock":
                print("Umupo ka sa monoblock at nalasak")
    case 2:
        print(keyb, mouse, heads)
        comshop = input("Pumili ka ng gamit: ")

        match comshop:
            case "keyb":
                print("Nag-nakaw ng keyboard")
            case "mouse":
                print("Hinampas mo mouse sa bata")
            case "heads":
                print("Tails")
    case 3:
        print(kuts, tini, baso)
        kusina = input("Pumili ka ng gamit: ")

        match kusina:
            case "kuts":
                print("Kumain ka")
            case "tini":
                print("May tinusok ka")
            case "baso":
                print("Ginalaw mo ang baso")