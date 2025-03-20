def calcular_saldo(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldo = vitorias - derrotas
    return saldo

def classificar_nivel(vitorias):
    # Classifica o nível com base no número de vitórias
    if vitorias < 10:
        return "Ferro"
    elif 10 <= vitorias <= 20:
        return "Bronze"
    elif 21 <= vitorias <= 50:
        return "Prata"
    elif 51 <= vitorias <= 80:
        return "Ouro"
    elif 81 <= vitorias <= 90:
        return "Diamante"
    elif 91 <= vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

def main():
    # Solicita a quantidade de vitórias e derrotas
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))
    except ValueError:
        print("Por favor, insira números válidos para vitórias e derrotas.")
        return

    # Calcula o saldo
    saldo_vitorias = calcular_saldo(vitorias, derrotas)

    # Classifica o nível
    nivel = classificar_nivel(vitorias)

    # Exibe a mensagem final
    print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}.")

# Chama a função principal
main()