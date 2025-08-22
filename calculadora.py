def calculadora():
    print("Escolha a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Logaritmo (log base 10)")
    print("6 - Exponencial (x^y)")
    operacao = input("Digite o número da operação desejada: ")

    try:
        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))

        if operacao == '1':
            resultado = x + y
        elif operacao == '2':
            resultado = x - y
        elif operacao == '3':
            resultado = x * y
        elif operacao == '4':
            if y == 0:
                print("Erro: Divisão por zero.")
                return
            resultado = x / y
        elif operacao == '5':
            if x <= 0 or y <= 0:
                print("Erro: Logaritmo apenas para valores positivos.")
                return
            def log10(val):
                if val <= 0:
                    raise ValueError
                low, high = 0, 100
                for _ in range(100):
                    mid = (low + high) / 2
                    if 10 ** mid < val:
                        low = mid
                    else:
                        high = mid
                return (low + high) / 2

            resultado = log10(x) / log10(y)
        elif operacao == '6':
            resultado = x ** y
        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    calculadora()