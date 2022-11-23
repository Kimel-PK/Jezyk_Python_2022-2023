import pygame
from random import randint
import os

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
	# klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

	def __init__(self, color, width, height):
		# wołamy najpierw konstruktor klasy bazowej (Sprite)
		# dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
		super().__init__()

		# przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
		self.image = pygame.Surface([width, height])
		self.image.fill(CZARNY)
		self.image.set_colorkey(CZARNY)

		# rysuję Rakietka jako prostokąt
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		# pobieramy prostokąt (jego rozmiary) z obiektu image
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels
		# sprawdzanie położenia brzegowego
		if self.rect.x > 400:
			self.rect.x = 400

	def moveLeft(self, pixels):
		self.rect.x -= pixels
		# sprawdzanie położenia brzegowego
		if self.rect.x < 0:
		   self.rect.x = 0



class Pilka(pygame.sprite.Sprite):
	# klasa Pilka dziedziczy ze "Sprite" w Pygame.

	def __init__(self, color, width, height):
		# wołamy konstruktor klasy bazowej
		super().__init__()

		# przekazujemy rozmiary, kolor, przezroczystość
		self.image = pygame.Surface([width, height])
		self.image.fill(CZARNY)
		self.image.set_colorkey(CZARNY)

		# rysowanie piłki (jako prostokącika)
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		# losowanie prędkości
		self.velocity = [randint(0, 4), -4]

		# pobieramy prostokąt (jego rozmiary) z obiektu image
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = randint(-5,5)
		self.velocity[1] = -self.velocity[1] - 0.1



# definiujemy rozmiary i otwieramy nowe okno
size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while True :

	rakietka = Rakietka(BIALY, 100, 10)
	rakietka.rect.x = 200
	rakietka.rect.y = 660

	pileczka = Pilka(BIALY,10,10)
	pileczka.rect.x = 240
	pileczka.rect.y = 50

	# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
	all_sprites_list = pygame.sprite.Group()

	# dodanie rakietki i piłeczki do listy
	all_sprites_list.add(rakietka)
	all_sprites_list.add(pileczka)

	# służy do kontroli liczby klatek na sekudnę (fps)
	clock = pygame.time.Clock()

	# Początkowy wynik
	score = 0
	hiscore = 0

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # zamknięcie okienka
				pygame.quit()
		
		# ruchy obiektu Rakietka klawisze strzałka prawa, lewa lub D i A
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
			rakietka.moveRight(5)
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			rakietka.moveLeft(5)

		# aktualizacja listy duszków
		all_sprites_list.update()

		# sprawdzenie czy piłeczka nie uderza w którąś ścianę
		# i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
		if pileczka.rect.x >= 490:
			pileczka.velocity[0] = -pileczka.velocity[0]
		if pileczka.rect.x <= 0:
			pileczka.velocity[0] = -pileczka.velocity[0]
		if pileczka.rect.y > 690:
			break
		if pileczka.rect.y < 0:
			pileczka.velocity[1] = -pileczka.velocity[1]

		# sprawdzenie kolizji piłeczki z rakietką
		if pygame.sprite.collide_mask(pileczka, rakietka):
			pileczka.bounce()
			score += 1

		# RYSOWANIE
		# czarny ekran
		screen.fill(CZARNY)

		# narysowanie obiektów
		all_sprites_list.draw(screen)

		# wyświetlanie wyników
		font = pygame.font.Font(None, 74)
		text = font.render(str(score), 1, BIALY)
		screen.blit(text, (250,10))

		# odświeżenie / przerysowanie całego ekranu
		pygame.display.flip()

		# 60 klatek na sekundę
		clock.tick(60)
		
	# koniec gry
	
	if not os.path.isfile("hiscore.txt") :
		f = open("hiscore.txt", "w")
		f.write("0")
		f.close()
	
	f = open("hiscore.txt", "r")
	hiscore = int (f.read())
	f.close()
		
	if score > hiscore :
		f = open("hiscore.txt", "w")
		f.write(str (score))
		f.close()
	
	while True :
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # zamknięcie okienka
				pygame.quit()
		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_SPACE] :
			break
			
		# RYSOWANIE
		# czarny ekran
		screen.fill(CZARNY)
		
		# wyświetlanie wyników
		font = pygame.font.Font(None, 64)
		text = font.render("Koniec gry", 1, BIALY)
		text_rect = text.get_rect(center=(250, 300))
		screen.blit(text, text_rect)
		text2 = font.render("Twój wynik: " + str (score), 1, BIALY)
		text_rect2 = text2.get_rect(center=(250, 350))
		screen.blit(text2, text_rect2)
		if score > hiscore :
			text3 = font.render("NOWY REKORD!", 1, BIALY)
		else :
			text3 = font.render("Obecny rekord: " + str (hiscore), 1, BIALY)
		text_rect3 = text3.get_rect(center=(250, 400))
		screen.blit(text3, text_rect3)
		
		font = pygame.font.Font(None, 30)
		text4 = font.render("Naciśnij SPACJE, żeby zagrać ponownie", 1, BIALY)
		text_rect4 = text4.get_rect(center=(250, 500))
		screen.blit(text4, text_rect4)

		# odświeżenie / przerysowanie całego ekranu
		pygame.display.flip()

		# 60 klatek na sekundę
		clock.tick(60)