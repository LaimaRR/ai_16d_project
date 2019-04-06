import pygame
import random
import sys

pygame.init()

langas_plotis = 800
langas_aukstis = 600

langas_spalva = (102, 0, 32)
mano_langelis_spalva = (172, 230, 0)
krituliai_spalva = (51, 119, 255)

mano_langelis_dydis = 50
mano_langelis_pozicija = [langas_plotis/2, langas_aukstis-2*mano_langelis_dydis]

krituliai_dydis = 50
krituliai_pozicija = [random.randint(0, langas_plotis-krituliai_dydis), 0]
krituliai_listas = [krituliai_pozicija]
krituliai_greitis = 10

screen = pygame.display.set_mode((langas_plotis, langas_aukstis))

game_over = False

rezultatas = 0
rezultatas_spalva = (255, 255, 0)

clock = pygame.time.Clock()

sriftas = pygame.font.SysFont("comicsansms", 40)

def lygis_nustatymas(rezultatas, krituliai_greitis):
	if rezultatas < 20:
		krituliai_greitis = 5
	elif rezultatas <40:
		krituliai_greitis = 8
	elif rezultatas < 60:
		krituliai_greitis = 12
	else:
		krituliai_greitis = 15
	return krituliai_greitis


def krituliai_sumazinimas(krituliai_listas):
	kritul_uzlaikymas = random.random()
	if len(krituliai_listas) <10 and kritul_uzlaikymas < 0.1:
		x_pos = random.randint(0,langas_plotis-krituliai_dydis)
		y_pos = 0
		krituliai_listas.append([x_pos,y_pos])

def krituliai_papildymas(krituliai_listas):
	for krituliai_pozicija in krituliai_listas:
		pygame.draw.rect(screen, krituliai_spalva, (krituliai_pozicija[0], krituliai_pozicija[1], krituliai_dydis, krituliai_dydis))

def krituliai_kritimas(krituliai_listas, rezultatas):
	for idx, krituliai_pozicija in enumerate(krituliai_listas):
		if krituliai_pozicija[1] >= 0 and krituliai_pozicija[1] < langas_aukstis:
			krituliai_pozicija[1] += krituliai_greitis
		else:
			krituliai_listas.pop(idx)
			rezultatas += 1
	return rezultatas

def susidurimas_patikra(krituliai_listas, mano_langelis_pozicija):
	for krituliai_pozicija in krituliai_listas:
		if susidurimas(mano_langelis_pozicija, krituliai_pozicija):
			return True
	return False

def susidurimas(mano_langelis_pozicija, krituliai_pozicija):
	mano_x = mano_langelis_pozicija[0]
	mano_y = mano_langelis_pozicija[1]

	krituliai_x = krituliai_pozicija[0]
	krituliai_y = krituliai_pozicija[1]

	if (krituliai_x >= mano_x and krituliai_x < (mano_x + mano_langelis_dydis)) or (mano_x >= krituliai_x and mano_x < (krituliai_x + krituliai_dydis)):
		if (krituliai_y >= mano_y and krituliai_y < (mano_y + mano_langelis_dydis)) or (mano_y >= krituliai_y and mano_y < (krituliai_y + krituliai_dydis)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = mano_langelis_pozicija[0]
			y = mano_langelis_pozicija[1]

			if event.key == pygame.K_LEFT:
				x -= mano_langelis_dydis
			elif event.key == pygame.K_RIGHT:
				x += mano_langelis_dydis

			mano_langelis_pozicija = [x,y]

	screen.fill(langas_spalva)


	krituliai_sumazinimas(krituliai_listas)
	rezultatas = krituliai_kritimas(krituliai_listas, rezultatas)
	krituliai_greitis = lygis_nustatymas(rezultatas, krituliai_greitis)

	tekstas = "Rezultatas: " + str(rezultatas)
	label = sriftas.render(tekstas, 1, rezultatas_spalva)
	screen.blit(label, (langas_plotis-350, langas_aukstis-50))

	if susidurimas_patikra(krituliai_listas, mano_langelis_pozicija):
		game_over = False
		break

	krituliai_papildymas(krituliai_listas)

	pygame.draw.rect(screen, mano_langelis_spalva, (mano_langelis_pozicija[0], mano_langelis_pozicija[1], mano_langelis_dydis, mano_langelis_dydis))


	clock.tick(30)

	pygame.display.update()



	#  Made by Laima Ramane
	#  Thanks to Keith Galli
	#  in https://www.youtube.com/watch?v=-8n91btt5d8
