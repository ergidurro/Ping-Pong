from pygame import *
from time import time as timer

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


rel_time = False
score1 = 0
score2 = 0
max_score = 3
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 70)
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
lose1 = font2.render('PLAYER 1 WINS!', True, (255, 0, 0))
lose2 = font2.render('PLAYER 2 WINS!', True, (255, 0, 0))
scorer1 = font1.render('Score: ' + str(score1), 1, (255, 0, 0))
scorer2 = font1.render('Score: ' + str(score1), 1, (255, 0, 0))

game = True
finish = False
while game == True:
    if finish != True:
        game_window.blit(background, (0,0))
        game_window.blit(scorer1, (40,20))
        game_window.blit(scorer2, (550,20))
        paddle1.reset()
        paddle1.move1()
        paddle2.reset()
        paddle2.move()
        ball.reset()
        scorer1 = font1.render('Score: ' + str(score1), 1, (255, 0, 0))
        scorer2 = font1.render('Score: ' + str(score2), 1, (255, 0, 0))

        if rel_time == False:
            ball.rect.x += ballx
            ball.rect.y += bally

        if ball.rect.y < 0:
            bally *= -1

        elif ball.rect.y > 460:
            bally *= -1

        elif ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ballx *= -1

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.y = 250
            ball.rect.x = 350
            rel_time = True
            last_time = timer()


        if ball.rect.x > 670:
            score1 += 1
            ball.rect.y = 250
            ball.rect.x = 350
            rel_time = True
            last_time = timer()

        if score1 >= max_score:
            finish = True
            game_window.blit(lose1, (140, 230))

        if score2 >= max_score:
            finish = True
            game_window.blit(lose2, (140, 230))

        if rel_time == True:
            now_time = timer()

            if now_time - last_time < 1:
                reload = font1.render('Ready...', 1,(150, 0, 0))
                game_window.blit(reload, (260, 460))
            else:
                rel_time = False
                
            
                




    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()