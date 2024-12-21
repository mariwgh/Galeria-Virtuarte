import os

class Obra:

    def __init__(self, nomeArq, paraGravacao):          #construtor da classe
                                                        #nomeArq = nome do arquivo onde as obras serão armazenadas
                                                        #paraGravacao = indica se o arquivo será aberto para gravação(True) ou leitura(False)
        self.AnoDaObra : str[4]= ''                             #string
        self.MesDaObra : str[2]= ''                             #string
        self.Estilo : str[15] = ''                              #string
        self.NomeDaObra : str[28] = ''                          #string
        self.AutorDaObra : str[20] = ''                         #string
        self.ValorEstimado : float = 0.0                        #não será string pois será somado logo mais
        self.UrlFoto : str[100] = ''                            #string

        self._abertoParaGravacao = paraGravacao         #atributo booleano que indica se o arquivo está aberto para gravação ou não, no caso, é igual ao paraGravacao 

        self._arquivo = None                    #inicializa o atributo _arquivo com None que representa o arquivo onde as obras serão armazenadas(nomeArq) 
        if paraGravacao == True:                #aberto em modo de escrita ('a') se paraGravacao for True (indica que o arquivo será aberto para gravação), ja que se for aberto para gravar pode escrever
            self._arquivo = open(nomeArq, 'a')
        else:                                   #e em modo de leitura ('r') caso contrário
            self._arquivo = open(nomeArq, 'r')

    @property
    def arquivo(self):
        return self._arquivo
   
    @property
    def gravar(self):
        return self._abertoParaGravacao


    def lerCamposDoArquivo(self):
                    
        if self._abertoParaGravacao == False:               #se abertoParaGravacao valer false
            linha = self._arquivo.readline().strip()        #será lida a próxima linha de dados do arquivo texto
            
            if linha:                                       #verifica se a linha não está vazia 
                #separa os campos da linha pelos espaços em branco:
                self.AnoDaObra = linha[0:4]
                self.MesDaObra = linha[4:6]
                self.Estilo = linha[6:21]
                self.NomeDaObra = linha[21:49]
                self.AutorDaObra = linha[49:69]
                self.ValorEstimado = float(linha[69:77])
                self.UrlFoto = linha[77:]

                return True                 #retorna True indicando sucesso na leitura dos campos
                
            else:
                    return False            #retorna False indicando que não há mais linhas para ler
        
    
    def gravarCamposNoArquivo(self):
        if self._abertoParaGravacao == True:            #se o campo abertoParaGravacao valer true
            #escrevendo no arquivo os dados da obra encapsulada no objeto
            self._arquivo.write(self.AnoDaObra + self.MesDaObra + self.Estilo + self.NomeDaObra + self.AutorDaObra + self.ValorEstimado + self.UrlFoto + '\n')
        else:       #se o arquivo não estiver aberto para gravação, não é possível gravar campos
            raise ValueError("O arquivo não está aberto para gravação e não pode ser escrito.")


    def preencherCampos(self, ano, mes, estilo, nome, autor, valor, url):   #receberá como parâmetros os valores dos campos de dados da obra
        #preenche os campos com espaços conforme necessário
        self.AnoDaObra = ano.ljust(4)
        self.MesDaObra = mes.ljust(2)                 #seria 2, mas eu estou colocando mais dois de espaço
        self.Estilo = estilo.ljust(15)
        self.NomeDaObra = nome.ljust(28)
        self.AutorDaObra = autor.ljust(20)                            
        self.ValorEstimado = valor.ljust(8)
        self.UrlFoto = url.ljust(100)
        #armazenará nos atributos de Obra que descrevem uma obra


    def fecharArquivo(self):
        self._arquivo.close()       #fecha o arquivo se este estiver aberto


    def __str__(self):
        #função que concatena os atributos de dados da obra e devolve a string com essa concatenação, para leitura (la no metodo principal)
        return f"{self.AnoDaObra} {self.MesDaObra} {self.Estilo} {self.NomeDaObra} {self.AutorDaObra} {self.ValorEstimado} {self.UrlFoto}"


    def compararCom(self, outraObra):       #recebendo como parâmetro uma outra instância de Obra
        #concatenação dos atributos AnoDaObra+MesDaObra+ AutorDaObra+NomeDaObra de cada uma:
        concatenacao_atual = self.AnoDaObra + self.MesDaObra + self.AutorDaObra + self.NomeDaObra

        concatenacao_outra = outraObra.AnoDaObra + outraObra.MesDaObra + outraObra.AutorDaObra + outraObra.NomeDaObra

        if concatenacao_atual < concatenacao_outra:
            return -1
        elif concatenacao_atual > concatenacao_outra:
            return 1
        else:
            return 0