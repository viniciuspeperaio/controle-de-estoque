

from datetime import datetime

estoque = []
contador = 1
while True:
    menu = int(input('\ndigite [1] para cadastrar um produto \ndigite [2] para vizualizar os produtos ja cadastrados \ndigite [3] para sair \n Opção:'))

    match menu:
        case 1:
            print()
            produto = dict(
                id = contador,
                nome = str(input('Digite o nome do PRODUTO: ')).lower(), 
                preco =  float(input('Digite o preço do produto: ')),
                dt_hr = datetime.now().strftime('%d/%m/%Y | %H:%M:%S'),
                funcionario = str(input('Digite o SEU nome: ')).title()
            )

            estoque.append(produto)
            contador += 1
            
        case 2:
            print()
            for produto in estoque: #responsavel por toda lista
                for chave, valor in produto.items(): #responsavel pelo 1o item
                    print(f'{chave} -> {valor}')
                print ()
        case 3:
            break

        case _: 
            print('resposta inválida!')
