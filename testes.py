print("\033[2J\033[H", end="")

class Veiculo:
    handicap = 0
    e_carro = 0
    nome = ""
    carta = ""
    matricula = ""
    preco = 0.0
    vip = 0
    entrada 
    saida

    def __init__(self, handicap, e_carro, carta , nome, matricula , preco , vip):
        self.handicap = handicap
        self.e_carro = e_carro
        self.nome = nome
        self.carta = carta
        self.preco = preco
        self.vip = vip
        self.matricula = matricula

    def vip(self):
        return self.vip
    
    def handicap(self):
        return self.handicap
    
    def e_carro(self):
        return self.e_carro
    
    def price(self):
        diferenca = saida - entrada
        minutos = diferenca.total_segundos() / 60 

        if minutos > 180:
            if self.vip == 1:
                return minutos * 0.4
            return (minutos * 0.2)
        else
            if self.vip == 1:
                return minutos * 0.3
            return minutos * 0.1
        
       
        
class Parque:


    lista_de_andar = []

    def __init__(self,lista_de_andar):
        self.lista_de_andar = lista_de_andares  


    def is_full(self, tipo):
        for i in self.lista_de_andar:
            





        

