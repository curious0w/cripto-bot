feito por curious0w/m1000

import os

def menu():
    print("""             _.-;;-._ 
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|""")
    print("[3]investir automaticamente")
    print("[2]comprar sua moeda automaticamente")
    print("[1] Abrir central CriptoCoin")
    print("[0] Sair")
    
    choice = input("Escolha uma opção: ")
    
    if choice == '1':
        os.system('python c:/Users/celia/OneDrive/cryptocoin/CriptoCoin_head.py')
    elif choice == '0':
        print("Saindo...")
    elif choice == '2':
        os.system('python c:/Users/celia/OneDrive/cryptocoin/CriptoCoin_Brain.py')
    elif choice == '3':
        os.system('python c:/Users/celia/OneDrive/cryptocoin/CriptoCoin_Brain.py')
    else:
        print("Opção inválida. Tente novamente.")
        menu()

if __name__ == "__main__":
    menu()
