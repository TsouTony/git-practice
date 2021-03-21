import random
import pygame
pygame.init()
pygame.NOFRAME
WHITE = (255,255,255)
BLACK = (0,0,0)
PIPE = (117,190,49)
SKY = (78,192,202)
GROUND = (224,215,146)
DARK_GROUND = (124,115,46)
BIRD = (241,186,62)
count=0

speed=0

#創建視窗
size = (800,700)
screen = pygame.display.set_mode(size)

#標題
pygame.display.set_caption("Flappy Block")

done = False

clock = pygame.time.Clock()

#字體
arial18 = pygame.font.SysFont('arial',18, False, False)
arial30 = pygame.font.SysFont('arial',30, False, False)

gameState = 1

pipes = []

score = 0
highScore = 0

class Bird():
    def __init__(self):
        self.x = 250
        self.y = 250
        self.yV = 0

    #定義按一下空白格鳥上升距離
    def flap(self):
        self.yV = -10
    
    #重新設定鳥
    def update(self):
        self.yV += 0.5
        self.y += self.yV
        if self.y >= 608:
            self.y = 608
            self.yV = 0
        if self.yV > 20:
            self.yV = 20
    
    def draw(self):
        pygame.draw.rect(screen,BIRD,(self.x,self.y,40,40))
    
    def reset(self):
        self.x = 250
        self.y = 250
        self.yV = 0

bird = Bird()

class Pipe():
    def __init__(self):
        self.centerY = random.randrange(130,520)
        self.x = 800
        self.size = 100
    
    def update(self):
        global pipes
        global bird
        global gameState
        global score
        global speed
        
        #print('speed:%d count:%d'%(speed,count) )
        self.x -= speed


            
        if self.x>296 and self.x<304:
            pipes.append(Pipe())
        if self.x <= -100:
            del pipes[0]
        #if self.x >= 170 and self.x <= 290 and bird.y <= (self.centerY - self.size) or self.x >= 170 and self.x <= 290 and (bird.y + 40) >= (self.centerY + self.size):
            #gameState = 3
        if self.x>165 and self.x<171:
            score += 1
        #if bird.y >= 608:
            #gameState = 3
        
    
    def draw(self):
        pygame.draw.rect(screen,PIPE,(self.x,0,80,(self.centerY - self.size)))
        pygame.draw.rect(screen,PIPE,(self.x,(self.centerY + self.size),80,(548 - self.centerY)))

pipes.append(Pipe())

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    #設定離開條件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #如果有按鍵往下按
        if event.type == pygame.KEYDOWN:
        	#如果是空白鍵
            if event.key == pygame.K_SPACE:
            	#如果遊戲狀態是1，改為2
                if gameState == 1:
                    gameState = 2
                #如果遊戲狀態是3
                elif gameState == 3:
                    bird.reset()
                    pipes = []
                    pipes.append(Pipe())
                    gameState = 2
                    score = 0
                else:
                    bird.flap()
    
    #設定背景
    screen.fill(SKY)
    pygame.draw.rect(screen,GROUND,(0,650,800,50))
    pygame.draw.line(screen,DARK_GROUND,(0,650),(800,650),5)
    pygame.draw.line(screen,DARK_GROUND,(0,650),(800,650),5)
    
    #階段一起始畫面
    if gameState == 1:
        pygame.draw.rect(screen,GROUND,(300,300,200,100))
        pygame.draw.rect(screen,DARK_GROUND,(300,300,200,100),5)
        text = arial18.render("Press space to play",True,DARK_GROUND)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(350 - (textY / 2))))
    
    #階段二開始遊戲
    if gameState == 2:
        if(score<10):
            speed=4
        elif(score>=10 and score<20):
            speed=5
        else:
            speed=6
        #print('Im in gamestate2')
        bird.update()
        bird.draw()
        
        for pipe in pipes:
            pipe.update()
            pipe.draw()
            #count+=1
            #print('Im in pip')
        if score > highScore:
            highScore = score
        
        text = arial30.render(str(score),True,WHITE)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(50 - (textY / 2))))
    
    #階段三
    if gameState == 3:
        for pipe in pipes:
            pipe.draw()
        bird.draw()
        
        pygame.draw.rect(screen,GROUND,(300,250,200,200))
        pygame.draw.rect(screen,DARK_GROUND,(300,250,200,200),5)
        text = arial18.render(("Score: " + str(score)),True,DARK_GROUND)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(300 - (textY / 2))))
        text = arial18.render(("High Score: " + str(highScore)),True,DARK_GROUND)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(350 - (textY / 2))))
        text = arial18.render("Press space to play",True,DARK_GROUND)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(400 - (textY / 2))))
        text = arial30.render(str(score),True,WHITE)
        textX = text.get_rect().width
        textY = text.get_rect().height
        screen.blit(text,((400 - (textX / 2)),(50 - (textY / 2))))
    
    #刷新畫面
    pygame.display.flip()
    
    #fps
    clock.tick(60)

pygame.quit()
