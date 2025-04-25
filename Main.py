import pygame
import random

pygame.init()

chicken = pygame.display.set_mode((500, 500)) 
cords = 10

cordplayer = 0
GameEnd = None

player1Score = 0
player2Score = 0


plyaerx = 20
plyaery = 0
plyaer2x = 480
plyaer2y = 0

ballcordsx= 250
ballcordsy= 250

linecordstart = []
linecordend = []
for i in range(10):
    linecordstart.append(cords) 
    cordsxy = cords + 30
    linecordend.append(cordsxy)
    cords += 50

movement = [-0.1,-0.1]



X = 400
Y = 400

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 12)

ballcolor = (255, 255, 255)
ballsize = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    chicken.fill((0, 0, 0))
    cordplayer+= 0.1

    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[0]),(250,linecordend[0]),3)   
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[1]),(250,linecordend[1]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[2]),(250,linecordend[2]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[3]),(250,linecordend[3]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[4]),(250,linecordend[4]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[5]),(250,linecordend[5]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[6]),(250,linecordend[6]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[7]),(250,linecordend[7]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[8]),(250,linecordend[8]),3)
    pygame.draw.line(chicken,(200,200,200),(250,linecordstart[9]),(250,linecordend[9]),3)



    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        plyaery -= 0.5
    if keys[pygame.K_s]:
        plyaery += 0.5

    if keys[pygame.K_UP]:
        plyaer2y -= 0.5
    if keys[pygame.K_DOWN]:
        plyaer2y += 0.5


    pygame.draw.rect(chicken,(255,255,255),(plyaerx-5,plyaery-5,10,50))
    pygame.draw.rect(chicken,(255,255,255),(plyaer2x-5,plyaer2y-5,10,50))
    
    if int(ballcordsy) in range (int(plyaery),int((plyaery+50))):
        print("Ball hit player 1 y")
        if int(ballcordsx) in range (int(plyaerx),int((plyaerx+5))):
            print("Ball hit player 1 x")
            movement[0] = random.uniform(0.1,0.1)
            movement[1] = random.uniform(-0.1,0.1)

    if int(ballcordsy) in range (int(plyaer2y),int((plyaer2y+50))):
        print("Ball hit player 2 y")
        if int(ballcordsx) in range (int(plyaer2x),int((plyaer2x+5))):
            print("Ball hit player 2 x")
            movement[0] = -random.uniform(0.1,0.1)
            movement[1] = -random.uniform(-0.1,0.1)

    if int(ballcordsy) <= 10:
        print("Ball hit wall")
        movement[1] = random.uniform(0.1,0.1)
    if int(ballcordsy) >= 490:
        print("Ball hit wall")
        movement[1] = -random.uniform(0.1,0.1)

    ballcordsx += movement[0]
    ballcordsy += movement[1]

    print("Ball:", int(ballcordsx), int(ballcordsy),"Play:", plyaerx, plyaery)




    if ballcordsx <= 10:
        player2Score += 1
        ballcordsx = 250
        ballcordsy = 250
        movement[0] = random.choice([0.1, -0.1])
        movement[1] = random.uniform(0.1, -0.1)

    if ballcordsx >= 490:
        player1Score += 1
        ballcordsx = 250
        ballcordsy = 250
        movement[0] = random.choice([0.1, -0.1])
        movement[1] = random.uniform(0.1, -0.1)

    if plyaery <= 0:
        plyaery = 0
    if plyaery >= 455:
        plyaery = 455

    if plyaer2y <= 0:
        plyaer2y = 0
    if plyaer2y >= 455:
        plyaer2y = 455
    
    if player2Score == 3:
        print("Player 2 wins")
        text = font.render("Player 2 wins", True, white)
        textRect = text.get_rect()
        textRect.center = (250, 250)
        chicken.blit(text, textRect)
        ballcordsx = 250
        ballcordsy = 250
        GameEnd = True
        ballcolor = (0, 0, 0)
        ballsize = 0

    if player1Score == 3: 
        print("Player 1 wins")
        text = font.render("Player 1 wins", True, white)
        textRect = text.get_rect()
        textRect.center = (250, 250)
        chicken.blit(text, textRect)
        ballcordsx = 250
        ballcordsy = 250
        GameEnd = True
        ballcolor = (0, 0, 0)
        ballsize = 0


    if GameEnd == True:
        text = font.render("Press R to restart", True, white)
        textRect = text.get_rect()
        textRect.center = (250, 300)
        chicken.blit(text, textRect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player1Score = 0
            player2Score = 0
            GameEnd = False
            ballcordsx = 250
            ballcordsy = 250
            ballcolor = (255, 255, 255)
            ballsize = 10
            



    text = font.render("Player 2 Score: " + str(player2Score), True, white)
    textRect = text.get_rect()
    textRect.center = (400, 20)
    chicken.blit(text, textRect)

    text = font.render("Player 1 Score: " + str(player1Score), True, white)
    textRect = text.get_rect()
    textRect.center = (100, 20)
    chicken.blit(text, textRect)


    ball = pygame.draw.circle(chicken,(ballcolor),(ballcordsx,ballcordsy),ballsize)
    pygame.display.update()

