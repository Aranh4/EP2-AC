def cor(baralho):
    i = 0
    while i < len(baralho):
        if "♣" in baralho[i]:
            print("{}. \033[30m{}\033[0;0m ".format(i+1,baralho[i]))
        if "♠" in baralho[i]:
            print("{}. \033[30m{}\033[0;0m ".format(i+1,baralho[i]))
        if "♥" in baralho[i]:
            print("{}. \033[31m{}\033[0;0m ".format(i+1,baralho[i]))
        if "♦" in baralho[i]:
            print("{}. \033[31m{}\033[0;0m ".format(i+1,baralho[i]))
        i+=1
    return baralho