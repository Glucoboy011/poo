from banda import Banda
from album import Album
from musico import Musico
from instrumentos import Guitarra, Bateria

def interface_console():
    banda = Banda('The Beatles')
    
    while True:
            print("\nEscolha uma opção:")
            print("1. Adicionar músico")
            print("2. Remover músico")
            print("3. Adicionar álbum")
            print("4. Remover álbum")
            print("5. Mostrar músicos")
            print("6. Mostrar álbuns")
            print("7. Sair")
            
            opcao = input("Opção: ")

            if opcao == '1':
                nome = input("Nome do músico: ")
                instrumento_tipo = input("Tipo de instrumento (guitarra/bateria): ").lower()
                if instrumento_tipo == 'guitarra':
                    instrumento = Guitarra('Fender Stratocaster', 'Cordas', 6)
                elif instrumento_tipo == 'bateria':
                    instrumento = Bateria('Yamaha Stage Custom', 'Percussão', 5)
                else:
                    print("Instrumento inválido.")
                    continue
                musico = Musico(nome, instrumento)
                banda.adicionar_musico(musico)

            elif opcao == '2':
                nome = input("Nome do músico a remover: ")
                banda.remover_musico(nome)

            elif opcao == '3':
                titulo = input("Título do álbum: ")
                ano = input("Ano de lançamento: ")
                faixa_principal = input("Faixa principal: ")
                album = Album(titulo, ano, faixa_principal)
                banda.adicionar_album(album)

            elif opcao == '4':
                titulo = input("Título do álbum a remover: ")
                banda.remover_album(titulo)

            elif opcao == '5':
                banda.mostrar_musicos()

            elif opcao == '6':
                banda.mostrar_albuns()

            elif opcao == '7':
                break

            else:
                print("Opção inválida. Tente novamente.")
                
    if __name__ == "__main__":
        interface_console()