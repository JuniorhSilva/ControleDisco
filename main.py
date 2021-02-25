dic_usuarios = {}
porcentagem_lista = []
try:
    print('Coloque o arquivo dentro da pasta')
    with open('arquivo.txt', 'r') as arquivo:
        usuarios_linha = arquivo.readlines()
        for linha in usuarios_linha:
            lista_usuarios = linha.strip().split()
            nome = lista_usuarios[0]
            memoria = float(lista_usuarios[1])
            dic_usuarios[nome] = memoria
except FileNotFoundError:
    print('Arquivo não encontrado')
except ValueError:
    print('Valores das memorias incorretos')
except Exception as error:
    print('Error')


def converter_para_mb(valor):
    for chave, byte in valor.items():
        resultado = 0.0024 * (int(byte) / 2500)
        valor[chave] = resultado


def percentual(lista, dic):
    soma = 0
    for mb in dic.values():
        soma += mb
    for chave, mb in dic.items():
        porcentagem = (mb / soma) * 100
        porcentagem = porcentagem
        lista.append(porcentagem)


converter_para_mb(dic_usuarios)
percentual(porcentagem_lista, dic_usuarios)
try:
    n = 0
    soma = 0
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write(
            'ACME Inc.\t\tUso do espaço em disco pelos usuarios\n')
        arquivo.write('-' * 58)
        arquivo.write('\n')
        arquivo.write('Nr.  Usuário\t\tEspaço utilizado\t% do uso\n')
        for chave, valor in dic_usuarios.items():
            soma += valor
            valor = f'{valor:.2f} MB'
            porcentagem_lista[n] = f'{porcentagem_lista[n]:.2f}%'
            arquivo.write(f'{n+1:<2}- {chave:<20}')
            arquivo.write(f'{valor:<25}'.replace('.', ','))
            arquivo.write(f'{porcentagem_lista[n]:<20}'.replace('.', ','))
            arquivo.write('\n')
            n += 1
        arquivo.write('\n')
        arquivo.write(f'Espaço total ocupado: {soma:.2f} MB\n')
        arquivo.write(f'Espaço média ocupado: {soma/len(dic_usuarios):.2f} MB')
except Exception as error:
    print('erro', error)
