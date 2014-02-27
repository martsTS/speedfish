import pygame, sys
from pygame.locals import *
import time

pygame.init()
pygame.display.set_caption('Panic Fish')
#sound = pygame.mixer.Sound('focus.wav')
clock = pygame.time.Clock()
#sound.play()
screen = pygame.display.set_mode((800, 600)) #width, then height
background = pygame.image.load("sealvl.png")
background = pygame.transform.scale(background, (3000, 1000))

fish = pygame.image.load("sunfish.png") #main character!
obs1 = pygame.image.load("obs1.png")
obs2 = pygame.image.load("obs2.png")
obs3 = pygame.image.load("obs3.png")
badfish = pygame.image.load("badfishv.png")
worm = pygame.image.load("googlebox.png")
rat = pygame.image.load("isthatarat.png")
jelly = pygame.image.load("jellyfish.png")
octo = pygame.image.load("octto1.png")

score = 0

myfont = pygame.font.SysFont("monospace", 32)
label = myfont.render("FISH PANIC!", 1, (255, 255, 0))

fish = pygame.transform.scale(fish, (200, 100))
badfish = pygame.transform.scale(badfish, (200, 100))
worm = pygame.transform.scale(worm, (300, 350))
rat = pygame.transform.scale(rat, (100, 50))
jelly = pygame.transform.scale(jelly, (200, 150))
octo = pygame.transform.scale(octo, (400, 350))

pygame.key.set_repeat(10,10)
#a = 300 #fish stays in same place, enviro moves around it. enviro includes the obstacles
#d = 350
s = 0
f = 0
fishRec = Rect(300, 300, 200, 100)
badfishRec = Rect((s+1000), (f+400), 200, 100)
wormRec = Rect((s+1200), (f+100), 300, 350)
ratRec = Rect((s+1400), (f+300), 100, 50)
jellyRec = Rect((s+1600), (f+400), 200, 150)
OctoRec = Rect((s+1800), (f+300), 400, 350)
bgRec = Rect(3000, 1000, 0, 0)
mx, my = pygame.mouse.get_pos()
while 1:
    print score
    if -250 < score < 100:
        print 'doing ok!'
    if -500<score<-250:
        print '...try harder!'
    if score<-500:
        print 'you are gonna get eaten!'
    print 'good luck fish!'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
            
        elif event.type == KEYDOWN and event.key == K_w:
            if f < 400:
                f+=15
        elif event.type == KEYDOWN and event.key == K_s:
            f-=15
        elif event.type == MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
        
            
    s-= 2 #b/c endless runner! poss make it so you can move back a tiny bit? would that be fairer?
    if fishRec.colliderect(badfishRec): #figure out some co ordinates!!!
        score-=1
        print score
    if fishRec.colliderect(wormRec): #figure out some co ordinates!!!
        score-=1
        print score
    if fishRec.colliderect(ratRec): #figure out some co ordinates!!!
        score-=1
        print score
    if fishRec.colliderect(jellyRec): #figure out some co ordinates!!!
        score-=1
        print score
    if fishRec.colliderect(OctoRec): #figure out some co ordinates!!!
        score-=1
        print score
        
    if bgRec.contains(fishRec):
        print "we're all going to die"
    screen.blit(label, (100, 100))
    screen.blit(background, (s,f))
    screen.blit(fish, (300, 300))
    screen.blit(badfish, (s+1000, f+400))
    badfishRec = Rect((s+1000), (f+400), 200, 100)
    screen.blit(worm, (s+1200, f+100))
    wormRec = Rect((s+1200), (f+100), 300, 350)
    screen.blit(rat, (s+1400, f+350))
    ratRec = Rect((s+1400), (f+300), 100, 50)
    screen.blit(jelly, (s+1600, f+400))
    jellyRec = Rect((s+1600), (f+400), 200, 150)
    screen.blit(octo, (s+1800, f+300))
    OctoRec = Rect((s+1800), (f+300), 400, 350)
    bgRec = Rect(3000, 1000, 0, 0)
    clock.tick(60)
    pygame.display.flip()
 
