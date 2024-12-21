from tkinter import filedialog      #módulo do tkinter é usado para mexer a caixa de diálogo do sistema para abrir e salvar e não precisará 'tkinter.filedialog' pode ser só filedialog
import os                           #para limpar o terminal depois
import webbrowser                   #usada para abrir URLs em um navegador da web padrão do sistema
import obras                        #importa o arquivo que contem a classe obra
import mat                          #importa o arquivo que contem a classe Matematica


tipos = [('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')]

def seletor():                                  #metodo fora da classe que printa
        print("Bem-vindo ao primeiro projeto de Técnicas de Programação de 2024")
        print("As opções são:")
        print("0 - Terminar a execução")
        print("1 - Cadastro de obras de arte")
        print("2 - Listagem de obras de arte")
        print("3 - Página web de obras de arte")
        print("4 - Triângulo de Pascal\n")


def principal():                                #metodo fora da classe

    opcao = 0
    while opcao != "0":                         #seletor repetitivo
        seletor()
        opcao = input("Faça sua escolha: ")
        os.system('cls') or None                #limpa o terminal

        match opcao:             

            case "1": 
                nome_arquivo = filedialog.askopenfilename(title = 'Selecione o arquivo',
                                                          multiple = False,
                                                          filetypes = tipos) 
                
                obra = obras.Obra(nome_arquivo, True)             #instanciando um obj da class Obra, informando o nome do arquivo escolhido, com abertura para gravação após seu final,
                            #nomeArq, paraGravacao          vai pegar o nome_arquivo, dizer que ele é = nomeArq e que poderá ser aberto para gravacao
                
                #solicitando ao usuário que digite cada um dos campos de dados da obra:
                ano = input("Ano da obra: ")

                if ano != '0':                      #o ano nao pode ser 0
                    mes = input("Mês da obra: ")
                    estilo = input("Estilo: ")
                    nome = input("Nome: ")
                    autor = input("Autor: ")
                    valor = input("Valor: ")
                    url = input("URL: ")

                else:                               #pq se ele for,
                    obra.fecharArquivo()            #o arquivo sera fechado,
                    principal()                     #e retornará ao seletor

                obra.preencherCampos(ano, mes, estilo, nome, autor, valor, url)         #passando os argumentos para preencher os espacos necessários
                obra.gravarCamposNoArquivo()                                            #vai gravar no arquivo escolhido

                print("Obra cadastrada com sucesso!\n")                                 #ocorrendo tudo certo, falará isso
                obra.fecharArquivo()                                                    #fechando o arquivo


            case "2":   
                nome_arquivo = filedialog.askopenfilename(title = 'Selecione o arquivo',
                                                          multiple = False,
                                                          filetypes = tipos)         #solicitando o nome do arquivo de obras com OpenDialog do TKinter que ele quer ver a listagem

                if nome_arquivo:                                #caso tiver selecionado algum nome de arquivo(não estiver vazio)
                    obra = obras.Obra(nome_arquivo, False)      #instanciando um obj da class Obra, abrindo o arquivo para leitura
                                #nomeArq, paraGravacao          vai pegar o nome_arquivo, dizer que ele é = nomeArq e que NÃO poderá ser aberto para gravacao
                    
                    print(" Ano  Mês  Est                 Nome                   Autor                Valor          URL")

                    total_valores = 0                       #variável para armazenar o total dos valores das obras
                    obras_lidas = 0                         #contador para armazenar o número de obras lidas
                    
                    while obra.lerCamposDoArquivo():
           
                        print(obra.__str__())
                        total_valores += float(obra.ValorEstimado)
                        obras_lidas += 1          


                    print(f"                              Número de obras : {obras_lidas}                     Valor: {total_valores}\n")    #exibir os totais

                    obra.fecharArquivo()                        #sempre fechar arquivo: abriu, fechou! fluxo retorna ao seletor repetitivo

                else:                                           #caso NÃO tiver selecionado algum nome de arquivo
                    print("Nenhum arquivo foi selecionado.")


            case "3":
            
                nome_arquivo = filedialog.askopenfilename(title = 'Selecione o arquivo',
                                                          multiple = False,
                                                          filetypes = tipos)            #solicitando com o OpenDialog do TKinter o nome de um arquivo de obras
                
                comando = f'sort {nome_arquivo} /o ordenado.txt /+1'                    #ordena o código
                os.system(comando) or None
                

                if nome_arquivo:                                #se um arquivo foi escolhido
                    obra = obras.Obra(nome_arquivo, False)            #usando um objeto da classe Obra, abrimos o arquivo escolhido
                                #nomeArq, paraGravacao          vai pegar o nome_arquivo, dizer que ele é = nomeArq e que NÃO poderá ser aberto para gravacao
                                
                    #criar uma string multilinha permitindo que você insira várias linhas de texto em uma única variável, no caso, formatacao da tabela
                    html_content = """                          
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Obras</title>
                        <style>
                            .fontedif{
                                font-family: Verdana, Geneva, Tahoma, sans-serif;
                                font-size: 14px;
                            }
                            .fontedif2{
                                font-family: Verdana, Geneva, Tahoma, sans-serif;
                                font-size: 13px;
                            }
                            table tr th, td {
                                border: 1px solid black;
                            }
                            table {
                                margin: auto;
                                width: auto;
                                border-collapse: collapse;
                            }
                            th, td {
                                padding: 11px;
                            }
                            #valorright {
                                text-align: right;
                            }
                            #ciano {
                                background-color: rgb(181, 247, 247);
                            }
                            #azulf {
                                background-color: rgb(123, 191, 230);
                            }
                            #yellow {
                                background-color: rgb(250, 241, 159);
                            }
                        </style>
                    </head>
                    <body>
                        <table>
                            <tr id="azulf" class="fontedif">
                                <th colspan="6">RELATORIO DE OBRAS DA GALERIA VIRTUAL</th>
                            </tr>
                            <tr id="ciano" class="fontedif2">
                                <th>Ano/Mes</th>
                                <th>Dados</th>
                                <th>Estilo</th>
                                <th>Autor</th>
                                <th>Valor</th>
                                <th>Imagem</th>
                            </tr>"""

                    total = 0.0                           #cria uma variavel para somar o total de UM ano
                    total_geral = 0.0                     #cria uma variavel para somar o total GERAL
                    ano_anterior = None                   #cria uma variável para armazenar o ano da obra anterior

                    contador = 1

                    while obra.lerCamposDoArquivo():                #enquanto houver linhas para ler
                        ano = obra.AnoDaObra                        #instancia

                        #tudo para mostrar somente o total:
                        
                        if ano_anterior == None or ano == ano_anterior:             #se não houver obra anterior ou o ano for igual ao anterior
                            total += obra.ValorEstimado                             #vai somar os valores DO ANO ESPECÍFICO

                        if ano != ano_anterior and ano_anterior != None:            #verifica se há uma mudança de ano, se houver, mostra o total já dos anos que foram somados anteriormente, e diferente de None para não aparecer no começo do arquivo(quebra de nível no HTML)
                            html_content += f"""<tr id="ciano">
                                <th colspan="4">Total</th>
                                <th id="valorright">{total}</th>
                                <th></th>
                            </tr>"""
                            total = obra.ValorEstimado                              #o valor estimado das obras desse ano printa!

                        ano_anterior = ano                                          #atualiza o ano anterior
                            

                        #mostrar dados da obra:

                        if contador % 2 == 0:                                       #se a linha for par, mostra amarelo
                            html_content += f"""<tr id="yellow">        
                                <td >{obra.AnoDaObra}/{obra.MesDaObra}</td>
                                <td >{obra.NomeDaObra}</td>
                                <td >{obra.Estilo}</td>
                                <td >{obra.AutorDaObra}</td>
                                <td id="valorright">{obra.ValorEstimado}</td>
                                <td ><img src="{obra.UrlFoto}" alt="Imagem da obra" width="100"></td>
                            </tr>"""

                        else:                                                       #se não, mostra branco
                            html_content += f"""<tr>        
                                <td>{obra.AnoDaObra}/{obra.MesDaObra}</td>
                                <td>{obra.NomeDaObra}</td>
                                <td>{obra.Estilo}</td>
                                <td>{obra.AutorDaObra}</td>
                                <td id="valorright">{obra.ValorEstimado}</td>
                                <td><img src="{obra.UrlFoto}" alt="Imagem da obra" width="100"></td>
                            </tr>"""


                        contador += 1
                    
                        total_geral += total                                        #o valor estimado da obra atual é somado ao total

                    ano_anterior = ano                                              #atualiza o ano anterior

                    #para que o último total (da última obra) apareça:
                    html_content += f"""<tr id="ciano">
                        <th colspan="4">Total</th>
                        <th id="valorright">{total}</th>
                        <th></th>
                    </tr>"""

                    total = obra.ValorEstimado                                      #só serve para adicional o total da última obra no total geral
                    total_geral += total                                            #adiciona o último total ao total geral

                    #quando não houver mais obras a serem colocadas, adiciona o total e fecha a tabela
                    html_content += f"""<tr id="azulf" class="fontedif">
                                <th colspan="4">Total Geral</th>
                                <th id="valorright">{total_geral}</th>
                                <th></th>
                            </tr>
                        </table>
                    </body>
                    </html>"""
                    
                    html_nome_arq = "obras.html"                    #define o nome do arquivo HTML que será gerado

                    with open(html_nome_arq, 'w') as file:          #abre o arquivo HTML em modo de escrita/gravação ('w'). 
                        #o arquivo é aberto dentro de um bloco with, o que garante que o arquivo será fechado corretamente após seu uso
                        file.write(html_content)                    #html_content é escrito no arquivo obras.html (formata)

                    print(f"Arquivo HTML gerado com sucesso: {html_nome_arq}\nVocê está sendo direcionado para a página...\n")

                    webbrowser.open(html_nome_arq)                  #abre a url

                    obra.fecharArquivo()                            #tem que fechar o arquivo depois (apenas)
        

                else:                                               #caso nenhum arquivo tenha sido escolhido
                    print("Nenhum arquivo selecionado.")


            case "4":   

                numero_linhas = int(input("Digite o número de linhas para o Triângulo de Pascal: "))

                mt = mat.Matematica(numero_linhas)          #instancia um objeto da classe Matematica passando como argumento o número de linhas(numeroBase)
                resultado = mt.triangulo_de_Pascal()

                for linha in resultado:                     #vai printando cada linha
                    print(linha)


            case _:         #representar qualquer valor que não corresponda aos casos anteriores que o usuário tenha digitado
                print("Opção inválida. Tente novamente.\n")       #volta pro seletor repetitivo


    print("Obrigado pela preferência!\nEncerrando...")      #quando o usuario digitar 0


if __name__ == "__main__":
    principal()