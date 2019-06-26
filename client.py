import urllib.request
import sys
import random
import time
import main

if len(sys.argv)==1:
	print("Voce deve especificar o numero do jogador (1 ou 2)\n\nExemplo:	./random_client.py 1")
	quit()

# Alterar se utilizar outro host
host = "http://localhost:8080"

player = int(sys.argv[1])

# Reinicia o tabuleiro
resp = urllib.request.urlopen("%s/reiniciar" % host)

done = False
while not done:
	# Pergunta quem eh o jogador
	resp = urllib.request.urlopen("%s/jogador" % host)
	player_turn = int(resp.read())

	# Se jogador == 0, o jogo acabou e o cliente perdeu
	if player_turn==0:
		print("I lose.")
		done = True

	# Se for a vez do jogador
	if player_turn==player:
		# Pega os movimentos possiveis
		resp = urllib.request.urlopen("%s/tabuleiro" % host)
		#print(resp.read())
		tabuleiro = eval(resp.read())

		# tabuleiro = [
		# 	[2, 1, 1, 2, 0], #0
		# 	[0, 0, 0, 0, 0, 0], #1
		# 	[0, 0, 0, 1, 1, 1, 0], #2
		# 	[0, 0, 0, 0, 0, 0, 0, 0], #3
		# 	[0, 0, 0, 0, 0, 0, 0, 0, 0], #4
		# 	[1, 2, 2, 0, 0, 0, 0, 0, 0, 0], #5
		# 	[1, 0, 0, 0, 0, 0, 0, 0, 0], #6
		# 	[1, 0, 0, 0, 0, 0, 0, 0], #7
		# 	[0, 0, 0, 0, 0, 0, 0], #8
		# 	[0, 0, 0, 0, 0, 0], #9
		# 	[0, 0, 0, 0, 0] #10
		# ]
		#movimentos = main.main(eval(resp.read()))
		print(tabuleiro)
		resp = urllib.request.urlopen("%s/movimentos" % host)
		movimentos = eval(resp.read())
		# Escolhe um movimento aleatoriamente
		movimento = main.main(tabuleiro, movimentos)
		print(movimento)
		# Executa o movimento
		resp = urllib.request.urlopen("%s/move?player=%d&coluna=%d&linha=%d" % (host,player,movimento[0]+1,movimento[1]+1))
		msg = eval(resp.read())

		# Se com o movimento o jogo acabou, o cliente venceu
		if msg[0]==0:
			print("I win")
			done = True
		if msg[0]<0:
			raise Exception(msg[1])
	
	# Descansa um pouco para nao inundar o servidor com requisicoes
	time.sleep(1)




