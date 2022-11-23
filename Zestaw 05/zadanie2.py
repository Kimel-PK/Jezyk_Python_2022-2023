import pygame, sys
pygame.init()

def main() :
	clock = pygame.time.Clock ()

	pygame.display.set_caption ('Piłka')
	icon = pygame.image.load ('ball.gif')
	pygame.display.set_icon (icon)

	pygame.mixer.music.load (r'music.mp3')
	pygame.mixer.music.play (-1)

	size = width, height = 800, 600
	screen = pygame.display.set_mode (size)

	image = pygame.image.load (r'moon.jpg')
	image = pygame.transform.scale (image, size)

	surf_center = (
		(width-image.get_width ()) / 2,
		(height-image.get_height()) / 2
	)
	
	screen.blit (image, surf_center)
	ball = pygame.image.load ('ball.gif')
	ball = pygame.transform.scale (ball, (ball.get_width () // 2, ball.get_height () // 2))

	screen.blit (ball, (width / 2, height / 2))

	ballrect = ball.get_rect (center = (width / 2, height / 2))
	pygame.display.flip ()
	
	speed = [10, -17]
	gravity = [0, 9.81]
	gravityMultiplier = 0.1
	accel = 0.5
	
	while True:
		clock.tick (60)
		
		for event in pygame.event.get ():
			if event.type == pygame.QUIT: sys.exit()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]: sys.exit()
		
		if keys[pygame.K_UP]:
			speed[1] -= accel
		elif keys[pygame.K_DOWN]:
			speed[1] += accel
		if keys[pygame.K_LEFT]:
			speed[0] -= accel
		elif keys[pygame.K_RIGHT]:
			speed[0] += accel
		
		screen.blit(image,surf_center)
		screen.blit(ball,ballrect)
		pygame.display.flip()
		
		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
			continue
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]
			continue
		
		speed[0] += gravity[0] * gravityMultiplier
		speed[1] += gravity[1] * gravityMultiplier

if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()