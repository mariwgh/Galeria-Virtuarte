class Matematica:

    def __init__(self, numeroBase):         #atributo inteiro a variável _numeroBase, cujo valor deverá ser estabelecido pelo programa
        self._numeroBase = numeroBase           #numero base é o l(n) é o horizontal

    def fatorial(self, x : int):
        #calcula e retorna o fatorial do parâmetro x(igual ao produtório de todos os inteiros positivos entre 2 e x)

        prod = 1
        contador = 1
        while contador <= x:
            prod *= contador
            contador += 1
        return prod

    def triangulo_de_Pascal(self):          #recebe como parametro a quantidade de linhas que o usuario quer
        triangulo = []                      #inicia uma lista que será usada para armazenar as linhas do Triângulo de Pascal

        for n in range(self._numeroBase):   #use o valor do atributo _numeroBase da classe como sendo o número de linhas L
            #n começa com 0, a cada passagem aumenta 1 e N representa as linhas horizontais
            linha = ""                      #string vazia é inicializada para armazenar os valores de cada linha

            for k in range(n + 1):          #itera sobre todos os valores de k de 0 até n, que representam as colunas em cada linha
                coeficiente = self.fatorial(n) // (self.fatorial(k) * self.fatorial(n - k))
                #coeficiente binomial (o valor de cada célula no Triângulo de Pascal) é calculado usando a fórmula do coeficiente binomial: C(n, k) = n! / (k! * (n - k)!), onde n é o número da linha e k é o número da coluna
                
                coef_str = str(coeficiente)                                       #converte para string para poder colocar na lista
                linha += coef_str + " " * (3 - len(coef_str))                     #formata a linha para ser exibida corretamente
                
                #o numero que vem dentro dos parenteses diz o tamanho dos espaçoes
                
                if k != n:                           #adiciona espaços apenas entre coeficientes
                    linha += " "

            triangulo.append(linha)         #dps de calcular todos os valores da linha atual, a string linha é adicionada à lista triangulo, representando uma linha completa do Triângulo de Pascal

        return triangulo                    #retorne uma lista de strings onde cada posição contenha uma linha do Triângulo correspondente a esse número de linhas