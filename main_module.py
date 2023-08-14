from engines.ahmia import search_with_selenium as search_with_selenium_ahmia
from engines.tordex import search_with_selenium as search_with_selenium_tordex

def select_option():
    print("Selecione uma opção:")
    print("1. Executar módulo Ahmia")
    print("2. Executar módulo Tordex")
    print("3. Executar ambos")

    choice = input("Digite o número da opção: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = select_option()

        if choice == "1":
            search_query = input("Insira a palavra-chave para o módulo Ahmia: ")
            search_with_selenium_ahmia(search_query)
        elif choice == "2":
            search_query = input("Insira a palavra-chave para o módulo Tordex: ")
            search_with_selenium_tordex(search_query)
        elif choice == "3":
            search_query = input("Insira a palavra-chave para ambos os módulos: ")
            search_with_selenium_ahmia(search_query)
            search_with_selenium_tordex(search_query)
        
        restart = input("Deseja executar novamente? (s/n): ")
        if restart.lower() != 's':
            break
