    number = random.randint(0, len(closed) - 1)

    print("")
    print("==========================================================================================")
    print(closed[number]["question"])
    print("")
    print("a:", closed[number]["options"]["a"])
    print("b:", closed[number]["options"]["b"])
    print("c:", closed[number]["options"]["c"])
    print("d:", closed[number]["options"]["d"])
    print("")
    
    answer = input()

    if answer == closed[number]["answer"]:
        print("Poprawna odpowiedź!")
    else:
        print("Błędna odpowiedź! Poprawną odpowiedzią było:", closed[number]["answer"])

    print("Aby wylosować kolejne pytanie wciśnij ENTER")
    print("==========================================================================================")
    input()