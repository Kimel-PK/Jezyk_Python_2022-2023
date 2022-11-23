import pygame
from random import randint

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

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.y < 0:
           self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.y > 400:
           self.rect.y = 400



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
        self.velocity = [randint(4, 8), randint(-8, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 10, 100)
rakietkaA.rect.x = 20
rakietkaA.rect.y = 200

rakietkaB = Rakietka(BIALY, 10, 100)
rakietkaB.rect.x = 670
rakietkaB.rect.y = 200

pileczka = Pilka(BIALY,10,10)
pileczka.rect.x = 345
pileczka.rect.y = 195

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(rakietkaA)
all_sprites_list.add(rakietkaB)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
scoreA = 0
scoreB = 0

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rakietkaA.moveUp(5)
    if keys[pygame.K_s]:
        rakietkaA.moveDown(5)
    if keys[pygame.K_UP]:
        rakietkaB.moveUp(5)
    if keys[pygame.K_DOWN]:
        rakietkaB.moveDown(5)

    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
    if pileczka.rect.x>=690:
        scoreA+=1
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.x<=0:
        scoreB+=1
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.y>490:
        pileczka.velocity[1] = -pileczka.velocity[1]
    if pileczka.rect.y<0:
        pileczka.velocity[1] = -pileczka.velocity[1]

    # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
    if pygame.sprite.collide_mask(pileczka, rakietkaA) or pygame.sprite.collide_mask(pileczka, rakietkaB):
      pileczka.bounce()

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)
    # cienka linia przez środek boiska
    pygame.draw.line(screen, BIALY, [349, 0], [349, 500], 5)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, BIALY)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, BIALY)
    screen.blit(text, (420,10))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()