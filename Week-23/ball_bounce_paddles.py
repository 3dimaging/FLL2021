import pygame
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
            
class Paddle(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([620, 20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
img_file = "wackyball.bmp"


ball = Ball(img_file, [200, 200], [10, -10])

paddle1 = Paddle([10, 170])
paddle2 = Paddle([10, 370])
# Adds each ball to the list as it’s created

def animate(group):
    screen.fill([255,255,255])
    #for ball in group:
    #group.remove(ball)
    # Removes sprite from the group
    ball.move()
    if pygame.sprite.spritecollide(ball, group, False):  # Checks for collisions between the sprite and the group
        #ball.speed[0] = -ball.speed[0]
        ball.speed[1] = -ball.speed[1]

      # Adds ball back into the group
    
    screen.blit(ball.image, ball.rect)
    screen.blit(paddle1.image, paddle1.rect)
    screen.blit(paddle2.image, paddle2.rect)
    pygame.display.flip()
    pygame.time.delay(20)

group = pygame.sprite.Group()
group.add(paddle1)
group.add(paddle2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Redraws the screen
    animate(group)
    


pygame.quit()
