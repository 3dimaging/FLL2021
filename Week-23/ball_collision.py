import sys, pygame
from random import choice

# The ball class definition
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

# The new `animate()` function
def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        group.remove(ball)  # Removes sprite from the group
        if pygame.sprite.spritecollide(ball, group, False):  # Checks for collisions between the sprite and the group
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)  # Adds ball back into the group
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)

size = width, height = 640, 480  # The main program starts here
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file1 = "wackyball.bmp"
img_file2 = "beach_ball.png"
  # Creates the sprite group
# Creates only four balls this time

location1 = [1 * 180 + 10, 1 * 180 + 10]
location2 = [1 * 180 + 10, 0 * 180 + 10]
speed1 = [2, 2]
speed2 = [2, 2]
ball1 = Ball(img_file1, location1, speed1)
ball2 = Ball(img_file2, location2, speed2)

group = pygame.sprite.Group()
group.add(ball1)
group.add(ball2) # Adds each ball to the group

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate(group)  # Calls `animate()` function, passing the group to it
pygame.quit()
