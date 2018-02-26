import os

def renomear_arquivos():
    #Obter o nome dos arquivos de uma pasta
    lista_arquivos = os.listdir("/home/victorshgo/Desktop/Python Projects/rename-files/images-for-example")
    #Qual o diretorio atual
    pasta_atual = os.getcwd()
    print("A pasta atual e: " + pasta_atual)
    #Entrando no diretorio correto
    os.chdir("/home/victorshgo/Desktop/Python Projects/rename-files/images-for-example")
    for nome_arquivo in lista_arquivos:
        print("Nome anterior: " + nome_arquivo)
        print("Nome atual: " + nome_arquivo.translate(None, "0123456789"))
        print("")
        #Removendo todos os numeros dos nomes dos arquivos
        os.rename(nome_arquivo, nome_arquivo.translate(None, "0123456789"))
    os.chdir(pasta_atual)
renomear_arquivos()