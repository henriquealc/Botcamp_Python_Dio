class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas # Inicializa o número de patas do animal

    def __str__(self):
        # Método especial que retorna uma representação em string do objeto
        # Retorna o nome da classe e todos os atributos do objeto formatados como chave=valor  
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw): # Se usar o '**kw' deve fazer argumentos posicionais
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self,cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo= cor_pelo, 
                         cor_bico= cor_bico, nro_patas = nro_patas)


# Devido o uso do '**kw' deve passar argumentos nomeados
gato = Gato(nro_patas = 4, cor_pelo= "Branco e Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas = 4, cor_bico="Amarelo", cor_pelo= "laranja")
print(ornitorrinco)

cachorro = Cachorro(nro_patas= 4, cor_pelo= "Amarelo")
print(cachorro)