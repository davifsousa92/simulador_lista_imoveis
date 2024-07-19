import os
import random

imoveis = [{'Endereço':'Rua Tibiriçá','Cidade':'Santo André','Bairro':'Vila Sacadura Cabral','CEP':'09060820','Complemento':'apt1','Código':462}]

def exibir_tela_inicial():
    print("""
        
        Imóveis Paulista
        
        """)

def exibir_opcoes():
    print('1. Cadastro de imóveis')
    print('\n2. Lista de imóveis')
    print('\n3. Pesquisa de imóveis')

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    os.system('cls')
    print('\nOpção inválida\n')
    voltar_ao_menu_principal()

def cadastrando_imoveis():
    os.system('cls')
    print('\nBem-vindo ao cadastro de imóveis!\n')
    print('Por favor, preencha com os dados do imóvel:\n')

    endereco = input('Endereço: ')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    cep = input('CEP: ')
    complemento = input('Complemento: ')
    
    codigo = random.randint(1, 1000)
    print(f'Número do código: {codigo}')

    dados_do_imovel = {
        'Endereço': endereco,
        'Cidade': cidade,
        'Bairro': bairro,
        'CEP': cep,
        'Complemento': complemento,
        'Código': codigo
    }
    imoveis.append(dados_do_imovel)
    print('\nCadastro realizado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_imoveis():
    os.system('cls')
    
    for imovel in imoveis:
        endereco = imovel['Endereço']
        cidade = imovel['Cidade']
        bairro = imovel['Bairro']
        cep = imovel['CEP']
        complemento = imovel['Complemento']
        codigo = imovel['Código']
        print(f'Endereço: {endereco}')
        print(f'Cidade: {cidade}') 
        print(f'Bairro: {bairro}')
        print(f'CEP: {cep}')
        print(f'Complemento: {complemento}')
        print(f'Código: {codigo}\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    
    if opcao_escolhida == 1:
        cadastrando_imoveis()
    elif opcao_escolhida == 2:
        listar_imoveis()
    elif opcao_escolhida == 3:
        pesquisar_imovel()
    else:
        opcao_invalida()

def pesquisar_imovel():
    os.system('cls')
    pesquisa = int(input('Digite o código do imóvel:'))
    encontrado = False
    
    for imovel in imoveis:
        if imovel['Código'] == pesquisa:
            endereco = imovel['Endereço']
            cidade = imovel['Cidade']
            bairro = imovel['Bairro']
            cep = imovel['CEP']
            complemento = imovel['Complemento']
            codigo = imovel['Código']
        
            print(f'\nEndereço: {endereco}')
            print(f'Cidade: {cidade}') 
            print(f'Bairro: {bairro}')
            print(f'CEP: {cep}')
            print(f'Complemento: {complemento}')
            print(f'Código: {codigo}\n')
            encontrado = True
            break
    
    if not encontrado:
        print('Código não encontrado')
    
    voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_tela_inicial()
    exibir_opcoes()
    escolher_opcao()
  
if __name__ == '__main__':
    main()