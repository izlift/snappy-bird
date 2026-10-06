import pygame
pygame.init()
from sys  import exit
import random

Game_width=350
Game_Height=550

bird_x=Game_width/8
bird_y=Game_Height/2
bird_width=34
bird_height=24


class Bird(pygame.Rect):
    def __init__(self,img):
        pygame.Rect.__init__(self,bird_x,bird_y,bird_width,bird_width)
        self.img=img

pipe_x=Game_width
pipe_y=0
pipe_width=70
pipe_height=400

class pipe(pygame.Rect):
    def __init__(self,img):
        pygame.Rect.__init__(self,pipe_x,pipe_y,pipe_width,pipe_height)
        self.img=img
        self.passed=False


background_image=pygame.image.load("bk.jpeg")
bird_image=pygame.image.load("birdd.gif")
bird_image=pygame.transform.scale(bird_image,(bird_width,bird_height))

top_pipe_image=pygame.image.load("R.png")
top_pipe_image=pygame.transform.scale(top_pipe_image,(pipe_width,pipe_height))

bottom_pipe_image=pygame.image.load("R.png")
bottom_pipe_image=pygame.transform.scale(bottom_pipe_image,(pipe_width,pipe_height))
bottom_pipe_image=pygame.transform.flip(top_pipe_image,False,True)


bird=Bird(bird_image)
pipes=[]
velocity_x= -2 
velocity_y=0
gravity=0.4
score=0
game_over=False
text_font=pygame.font.Font(None,45)


def draw():
    window.blit(background_image,(0,0))
    window.blit(bird.img,bird)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

        text_str=str(int(score))

        text_font=pygame.font.SysFont("comic Sans Ms",45)
        text_render=text_font.render(text_str,True,"white")
        window.blit(text_render,(5,0))

def move():
    global velocity_y,score,game_over
    velocity_y+=gravity
    bird.y+=velocity_y
    bird.y=max(bird.y,0)

    if bird.y>Game_Height:
        game_over= True
        return
    for pipe in pipes:
        pipe.x+=velocity_x

        if not pipe.passed and bird.x> pipe.x+pipe_width:
            
            score+=0.5
            pipe.passed=True
        if bird.colliderect(pipe):
            game_over=True
            return
        
    while len(pipes)>0 and pipes[0].x<-pipe_width:

        pipes.pop(0)

def create_pipes():
    random_pipe_y=pipe_y-pipe_height/4-random.random()*(pipe_height/2)
    opening_space=Game_Height/4

    top_pipe=pipe(top_pipe_image)
    top_pipe.y=random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe=pipe(bottom_pipe_image)
    bottom_pipe.y=top_pipe.y +top_pipe.height +opening_space
    pipes.append(bottom_pipe)

print(len(pipes))

pygame.init()
window=pygame.display.set_mode((Game_width,Game_Height))
pygame.display.set_caption("Flappy Bird")
clock=pygame.time.Clock()

create_pipes_timer=pygame.USEREVENT+0
pygame.time.set_timer(create_pipes_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type== create_pipes_timer and not game_over:
            create_pipes()

        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE,pygame.K_x,pygame.K_UP):
                velocity_y=-6 

            
                if game_over:
                    bird.y=bird_y
                    pipes.clear()
                    score=0
                    game_over=False


    if not game_over:
        move()
        draw()
    
        pygame.display.update()
        clock.tick(60)



  


