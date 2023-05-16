import os
import vaxla

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-växlare-\n")

    pris = input("\tMata in pris på varan i kr:")
    inbet = input("\tInbetalt belopp i kr: ")

    exChangeNow(int(pris),int (inbet))


def exChangeNow(priset, inbetalning):
    print("test" + str(priset))


main()