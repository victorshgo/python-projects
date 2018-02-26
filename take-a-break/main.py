import time
import webbrowser

musicas = ["https://www.youtube.com/watch?v=R9zNNXuNW5A", "https://www.youtube.com/watch?v=dGwGXzHZD3s&list=PLZQF2uWHCjysaGhDssz-jiGaID-_UBB5T&index=6", "https://www.youtube.com/watch?v=UkIEGNd-Otw&list=PLZQF2uWHCjysaGhDssz-jiGaID-_UBB5T&index=3"]

#Define quantas vezes o programa vai executar o loop
total_paradas = 3
paradas_count = 0
while(paradas_count < total_paradas):
    #Faz o programa esperar 1h para iniciar
    time.sleep(3600)
    #Mostra a hora que o programa abriu a musica
    print("O programa iniciou as " + time.ctime())
    #Abrir o browser com o link disponibilizado
    webbrowser.open(musicas[paradas_count])
    paradas_count += 1