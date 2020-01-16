import pygame
import time


def one_day(pole):
	x = 0
	for radka in pole:
		y = 0
		for sloupec in radka:
			nbc = 0  # neighbourcount
			around = (
				(x-1, y-1),
				(x, y-1),
				(x+1, y-1),
				(x-1, y),
				(x+1, y),
				(x-1, y+1),
				(x, y+1),
				(x+1, y+1),
			)
			for a in around:
				try:
					if pole[a[0]][a[1]] in (1, 2):
						nbc += 1
				except:
					pass
			if (pole[x][y] == 1):  # if it is alive
				if (nbc < 2) or (nbc > 3):
					pole[x][y] = 2
			if (pole[x][y] == 0):  # if it is dead
				if nbc == 3:
					pole[x][y] = 3

			y += 1
		x += 1


	x = 0
	for radka in pole:
		y = 0
		for sloupec in radka:
			if (pole[x][y] == 2):  # die
				pole[x][y] = 0
			if (pole[x][y] == 3):  # resurrect
				pole[x][y] = 1
			y += 1
		x += 1
	print(pole)

	x = 0
	screen.fill(bg_color)
	for radka in pole:
		y = 0
		for ctverec in radka:
			screen.blit(obrazky[pole[y][x]], (x*24, y*24))
			y += 1
		x += 1
	pygame.display.update()
	time.sleep(0.25)



pygame.init() #potřeba zadat
screen = pygame.display.set_mode((768,768)) #vel.okna
pygame.display.set_caption("GOLOD")#název okna
clock = pygame.time.Clock()

font = pygame.font.SysFont("conzolas", 14)

obrazky= [pygame.image.load("pole2.png")]

for i in range(1,20):
	pole2 = pygame.Surface((24, 24))
	pole2.fill((255/20*i, 0, 0))

	obrazky.append(pole2)

bg_color = (60, 60, 60)

#0...mrtvi
#1...zivi
#3...ozivnou
#2...zemrou
#5...border
pole = [
	[0]*32 + [5] for row in range(32)
]
pole.append(
	[5]*33
)
print(pole)
z = 0
mouse_hold = False
while z == 0:
	for event in pygame.event.get():
		'''
		Hold LMB to create points,
		hold RMB to delete them.
		Press K_UP to start the thing.
		'''
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_hold = True
			if event.button == 1:  # LMB
				create = True
			elif event.button == 3:  # RMB
				create = False
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_hold = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				z = 1

	if mouse_hold:
		(Y, X) = pygame.mouse.get_pos()
		X = X//24
		Y = Y//24
		if create:
			pole[X][Y] = 1
		else:
			pole[X][Y] = 0

	x = 0
	screen.fill(bg_color)
	for radka in pole:
		y = 0
		for ctverec in radka:
			screen.blit(obrazky[pole[y][x]], (x*24, y*24))
			y += 1
		x += 1
	pygame.display.update()

for i in range(1000):
	one_day(pole)

time.sleep(150)
