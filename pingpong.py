from pygame import *

class loja(sprite.Sprite):
    def __init__(self, player,size1, size2, x1, y1, shpejtesi, x2, x3, y2, y3):
        super().__init__()

        self.imazh = transform.scale(image.load(player), (size1, size2))
        self.speed = shpejtesi

        self.rect = self.imazh.get_rect()
        self.rect.x = x1
        self.rect.y = y1

        self.x2 = x2
        self.x3 = x3
        self.y2 = y2
        self.y3 = y3

    def reset(self):
        game_window.blit(self.imazh, (self.rect.x,self.rect.y))

class Player(loja):
    def move(self):
        press_key = key.get_pressed()
        if press_key[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if press_key[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed

    def move1(self):
        key_press = key.get_pressed()
        if key_press[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_press[K_s] and self.rect.y < 405:
            self.rect.y += self.speed



font.init()
font = font.SysFont('Arial', 70)
bally = 3
ballx = 3
clock = time.Clock()
FPS = 60
game_window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.png'), (700, 500))
paddle1 = Player('paddle.png', 20, 100, 30, 250, 10,0,0,0,0)
paddle2 = Player('paddle.png', 20, 100, 650, 250, 10,0,0,0,0)
ball = Player('ball.png', 30, 30, 350, 250, 10,0,0,0,0)
lose1 = font.render('PLAYER 1 WINS!', True, (255, 0, 0))
lose2 = font.render('PLAYER 2 WINS!', True, (255, 0, 0))

game = True
finish = False
while game == True:
    if finish != True:
        game_window.blit(background, (0,0))
        paddle1.reset()
        paddle1.move1()
        paddle2.reset()
        paddle2.move()
        ball.reset()

        ball.rect.x += ballx
        ball.rect.y += bally

        if ball.rect.y < 0:
            bally *= -1

        elif ball.rect.y > 460:
            bally *= -1

        elif ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ballx *= -1

    if ball.rect.x < 0:
        finish = True
        game_window.blit(lose2, (150, 200))

    if ball.rect.x > 670:
        finish = True
        game_window.blit(lose1, (150, 200))




    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()