class Album:
    def __init__(self, titulo, ano, faixas):
       self.titulo = titulo
       self.ano = ano
       self.faixas = faixas
    def __str__(self):
        return f"Album: {self.titulo}, Ano: {self.ano}, Faixas: {''.join(self.faixas)}"