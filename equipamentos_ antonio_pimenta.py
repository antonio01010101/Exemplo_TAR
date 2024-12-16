# Nome do programa: equipamentos_antonio_pimenta.py

def main():
    try:
        with open("devices.txt", "r") as file:
            equipamentos = [linha.strip() for linha in file.readlines()]
    except FileNotFoundError:
        print("Erro: O arquivo devices.txt não foi encontrado.")
        return

    while True:
        equipamento_a_procurar = input("Equipamento a procurar (sair p/terminar): ").strip()

        if equipamento_a_procurar.lower() == "sair":
            print("Programa encerrado.")
            break

        encontrados = [equipamento for equipamento in equipamentos if equipamento_a_procurar.lower() in equipamento.lower()]

        if encontrados:
            print(f"Equipamentos encontrados ({len(encontrados)}):")
            for equipamento in encontrados:
                print(f"- {equipamento}")
        else:
            print("Equipamento Não existe na Lista!")

if __name__ == "__main__":
    main()
