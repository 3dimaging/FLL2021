import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = -self.speed[1]
        
img_file = "wackyball.bmp"


ball = Ball(img_file, [200, 200], [3, 3])
# Adds each ball to the list as it’s created
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    # Redraws the screen
    screen.fill([255, 255, 255])
    ball.move()
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
pygame.quit()
