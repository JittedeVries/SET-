#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:41:02 2023

@author: jittedevries
"""
#alle nodige modules
import pygame,sys
import random
import itertools

#class van de kaarten van set met de eigenschappen gedefiniëerd 
class setkaarten():
    def __init__(self, kleur, vorm, vulling, veelvoud):
        self.kleur=kleur
        self.vorm=vorm
        self.vulling=vulling
        self.veelvoud=veelvoud

#dictionary die elke kaart gelijk stelt aan zijn eigenschappen
vectortocard = {'kaarten/greendiamondempty1.gif':setkaarten('g', 'd', 'e', 1), 
                'kaarten/greendiamondempty2.gif':setkaarten('g', 'd', 'e', 2),
                'kaarten/greendiamondempty3.gif':setkaarten('g', 'd', 'e', 3),
                'kaarten/greendiamondfilled1.gif':setkaarten('g', 'd', 'f', 1),
                'kaarten/greendiamondfilled2.gif':setkaarten('g', 'd', 'f', 2),
                'kaarten/greendiamondfilled3.gif':setkaarten('g', 'd', 'f', 3),
                'kaarten/greendiamondshaded1.gif':setkaarten('g', 'd', 's', 1),
                'kaarten/greendiamondshaded2.gif':setkaarten('g', 'd', 's', 2),
                'kaarten/greendiamondshaded3.gif':setkaarten('g', 'd', 's', 3),
                'kaarten/greenovalempty1.gif':setkaarten('g', 'o', 'e', 1),
                'kaarten/greenovalempty2.gif':setkaarten('g', 'o', 'e', 2),
                'kaarten/greenovalempty3.gif':setkaarten('g', 'o', 'e', 3),
                'kaarten/greenovalfilled1.gif':setkaarten('g', 'o', 'f', 1),
                'kaarten/greenovalfilled2.gif':setkaarten('g', 'o', 'f', 2),
                'kaarten/greenovalfilled3.gif':setkaarten('g', 'o', 'f', 3),
                'kaarten/greenovalshaded1.gif':setkaarten('g', 'o', 's', 1),
                'kaarten/greenovalshaded2.gif':setkaarten('g', 'o', 's', 2),
                'kaarten/greenovalshaded3.gif':setkaarten('g', 'o', 's', 3),
                'kaarten/greensquiggleempty1.gif':setkaarten('g', 's', 'e', 1),
                'kaarten/greensquiggleempty2.gif':setkaarten('g', 's', 'e', 2),
                'kaarten/greensquiggleempty3.gif':setkaarten('g', 's', 'e', 3),
                'kaarten/greensquigglefilled1.gif':setkaarten('g', 's', 'f', 1),
                'kaarten/greensquigglefilled2.gif':setkaarten('g', 's', 'f', 2),
                'kaarten/greensquigglefilled3.gif':setkaarten('g', 's', 'f', 3),
                'kaarten/greensquiggleshaded1.gif':setkaarten('g', 's', 's', 1),
                'kaarten/greensquiggleshaded2.gif':setkaarten('g', 's', 's', 2),
                'kaarten/greensquiggleshaded3.gif':setkaarten('g', 's', 's', 3),
                'kaarten/purplediamondempty1.gif':setkaarten('p', 'd', 'e', 1),
                'kaarten/purplediamondempty2.gif':setkaarten('p', 'd', 'e', 2),
                'kaarten/purplediamondempty3.gif':setkaarten('p', 'd', 'e', 3),
                'kaarten/purplediamondfilled1.gif':setkaarten('p', 'd', 'f', 1),
                'kaarten/purplediamondfilled2.gif':setkaarten('p', 'd', 'f', 2),
                'kaarten/purplediamondfilled3.gif':setkaarten('p', 'd', 'f', 3),
                'kaarten/purplediamondshaded1.gif':setkaarten('p', 'd', 's', 1),
                'kaarten/purplediamondshaded2.gif':setkaarten('p', 'd', 's', 2),
                'kaarten/purplediamondshaded3.gif':setkaarten('p', 'd', 's', 3),
                'kaarten/purpleovalempty1.gif':setkaarten('p', 'o', 'e', 1),
                'kaarten/purpleovalempty2.gif':setkaarten('p', 'o', 'e', 2),
                'kaarten/purpleovalempty3.gif':setkaarten('p', 'o', 'e', 3),
                'kaarten/purpleovalfilled1.gif':setkaarten('p', 'o', 'f', 1),
                'kaarten/purpleovalfilled2.gif':setkaarten('p', 'o', 'f', 2),
                'kaarten/purpleovalfilled3.gif':setkaarten('p', 'o', 'f', 3),
                'kaarten/purpleovalshaded1.gif':setkaarten('p', 'o', 's', 1),
                'kaarten/purpleovalshaded2.gif':setkaarten('p', 'o', 's', 2),
                'kaarten/purpleovalshaded3.gif':setkaarten('p', 'o', 's', 3),
                'kaarten/purplesquiggleempty1.gif':setkaarten('p', 's', 'e', 1),
                'kaarten/purplesquiggleempty2.gif':setkaarten('p', 's', 'e', 2),
                'kaarten/purplesquiggleempty3.gif':setkaarten('p', 's', 'e', 3),
                'kaarten/purplesquigglefilled1.gif':setkaarten('p', 's', 'f', 1),
                'kaarten/purplesquigglefilled2.gif':setkaarten('p', 's', 'f', 2),
                'kaarten/purplesquigglefilled3.gif':setkaarten('p', 's', 'f', 3),
                'kaarten/purplesquiggleshaded1.gif':setkaarten('p', 's', 's', 1),
                'kaarten/purplesquiggleshaded2.gif':setkaarten('p', 's', 's', 2),
                'kaarten/purplesquiggleshaded3.gif':setkaarten('p', 's', 's', 3),
                'kaarten/reddiamondempty1.gif':setkaarten('r', 'd', 'e', 1),
                'kaarten/reddiamondempty2.gif':setkaarten('r', 'd', 'e', 2),
                'kaarten/reddiamondempty3.gif':setkaarten('r', 'd', 'e', 3),
                'kaarten/reddiamondfilled1.gif':setkaarten('r', 'd', 'f', 1),
                'kaarten/reddiamondfilled2.gif':setkaarten('r', 'd', 'f', 2),
                'kaarten/reddiamondfilled3.gif':setkaarten('r', 'd', 'f', 3),
                'kaarten/reddiamondshaded1.gif':setkaarten('r', 'd', 's', 1),
                'kaarten/reddiamondshaded2.gif':setkaarten('r', 'd', 's', 2),
                'kaarten/reddiamondshaded3.gif':setkaarten('r', 'd', 's', 3),
                'kaarten/redovalempty1.gif':setkaarten('r', 'o', 'e', 1),
                'kaarten/redovalempty2.gif':setkaarten('r', 'o', 'e', 2),
                'kaarten/redovalempty3.gif':setkaarten('r', 'o', 'e', 3),
                'kaarten/redovalfilled1.gif':setkaarten('r', 'o', 'f', 1),
                'kaarten/redovalfilled2.gif':setkaarten('r', 'o', 'f', 2),
                'kaarten/redovalfilled3.gif':setkaarten('r', 'o', 'f', 3),
                'kaarten/redovalshaded1.gif':setkaarten('r', 'o', 's', 1),
                'kaarten/redovalshaded2.gif':setkaarten('r', 'o', 's', 2),
                'kaarten/redovalshaded3.gif':setkaarten('r', 'o', 's', 3),
                'kaarten/redsquiggleempty1.gif':setkaarten('r', 's', 'e', 1),
                'kaarten/redsquiggleempty2.gif':setkaarten('r', 's', 'e', 2),
                'kaarten/redsquiggleempty3.gif':setkaarten('r', 's', 'e', 3),
                'kaarten/redsquigglefilled1.gif':setkaarten('r', 's', 'f', 1),
                'kaarten/redsquigglefilled2.gif':setkaarten('r', 's', 'f', 2),
                'kaarten/redsquigglefilled3.gif':setkaarten('r', 's', 'f', 3),
                'kaarten/redsquiggleshaded1.gif':setkaarten('r', 's', 's', 1),
                'kaarten/redsquiggleshaded2.gif':setkaarten('r', 's', 's', 2),
                'kaarten/redsquiggleshaded3.gif':setkaarten('r', 's', 's', 3)}
#lijst van de kaarten die nog in het spel zitten na een tijdje spelen
cardsinthegame=['kaarten/greendiamondempty1.gif',
       'kaarten/greendiamondempty2.gif',
       'kaarten/greendiamondempty3.gif',
       'kaarten/greendiamondfilled1.gif', 
       'kaarten/greendiamondfilled2.gif', 
       'kaarten/greendiamondfilled3.gif', 
       'kaarten/greendiamondshaded1.gif', 
       'kaarten/greendiamondshaded2.gif', 
       'kaarten/greendiamondshaded3.gif', 
       'kaarten/greenovalempty1.gif', 
       'kaarten/greenovalempty2.gif', 
       'kaarten/greenovalempty3.gif',
       'kaarten/greenovalfilled1.gif',
       'kaarten/greenovalfilled2.gif',
       'kaarten/greenovalfilled3.gif',
       'kaarten/greenovalshaded1.gif',
       'kaarten/greenovalshaded2.gif',
       'kaarten/greenovalshaded3.gif',
       'kaarten/greensquiggleempty1.gif',
       'kaarten/greensquiggleempty2.gif',
       'kaarten/greensquiggleempty3.gif',
       'kaarten/greensquigglefilled1.gif',
       'kaarten/greensquigglefilled2.gif',
       'kaarten/greensquigglefilled3.gif',
       'kaarten/greensquiggleshaded1.gif',
       'kaarten/greensquiggleshaded2.gif',
       'kaarten/greensquiggleshaded3.gif',
       'kaarten/purplediamondempty1.gif',
       'kaarten/purplediamondempty2.gif',
       'kaarten/purplediamondempty3.gif',
       'kaarten/purplediamondfilled1.gif', 
       'kaarten/purplediamondfilled2.gif', 
       'kaarten/purplediamondfilled3.gif', 
       'kaarten/purplediamondshaded1.gif', 
       'kaarten/purplediamondshaded2.gif', 
       'kaarten/purplediamondshaded3.gif', 
       'kaarten/purpleovalempty1.gif', 
       'kaarten/purpleovalempty2.gif', 
       'kaarten/purpleovalempty3.gif',
       'kaarten/purpleovalfilled1.gif',
       'kaarten/purpleovalfilled2.gif',
       'kaarten/purpleovalfilled3.gif',
       'kaarten/purpleovalshaded1.gif',
       'kaarten/purpleovalshaded2.gif',
       'kaarten/purpleovalshaded3.gif',
       'kaarten/purplesquiggleempty1.gif',
       'kaarten/purplesquiggleempty2.gif',
       'kaarten/purplesquiggleempty3.gif',
       'kaarten/purplesquigglefilled1.gif',
       'kaarten/purplesquigglefilled2.gif',
       'kaarten/purplesquigglefilled3.gif',
       'kaarten/purplesquiggleshaded1.gif',
       'kaarten/purplesquiggleshaded2.gif',
       'kaarten/purplesquiggleshaded3.gif',
       'kaarten/reddiamondempty1.gif',
       'kaarten/reddiamondempty2.gif',
       'kaarten/reddiamondempty3.gif',
       'kaarten/reddiamondfilled1.gif', 
       'kaarten/reddiamondfilled2.gif', 
       'kaarten/reddiamondfilled3.gif', 
       'kaarten/reddiamondshaded1.gif', 
       'kaarten/reddiamondshaded2.gif', 
       'kaarten/reddiamondshaded3.gif', 
       'kaarten/redovalempty1.gif', 
       'kaarten/redovalempty2.gif', 
       'kaarten/redovalempty3.gif',
       'kaarten/redovalfilled1.gif',
       'kaarten/redovalfilled2.gif',
       'kaarten/redovalfilled3.gif',
       'kaarten/redovalshaded1.gif',
       'kaarten/redovalshaded2.gif',
       'kaarten/redovalshaded3.gif',
       'kaarten/redsquiggleempty1.gif',
       'kaarten/redsquiggleempty2.gif',
       'kaarten/redsquiggleempty3.gif',
       'kaarten/redsquigglefilled1.gif',
       'kaarten/redsquigglefilled2.gif',
       'kaarten/redsquigglefilled3.gif',
       'kaarten/redsquiggleshaded1.gif',
       'kaarten/redsquiggleshaded2.gif',
       'kaarten/redsquiggleshaded3.gif',]

#algoritme dat 12 willekeurige kaarten op het scherm projecteert

tablecards=[]
    

#initiëren van het speelscherm
pygame.init()
pygame.display.set_caption('SET!')
grootte= (800,800)
screen=pygame.display.set_mode((grootte))

clock=pygame.time.Clock()
run= True




set_menu=False

#class en initiatie van de starknop

class knop():
    def __init__(self, x, y, foto, schaal):
        breedte=foto.get_width()
        lengte= foto.get_height()
        self.foto=pygame.transform.scale(foto, (int(breedte*schaal), int(lengte*schaal)))
        self.rect=self.foto.get_rect()
        self.rect.topleft=(x, y)
        self.clicked=False
    def draw(self, surface):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        surface.blit(self.foto, (self.rect.x, self.rect.y))
        return action
    
makkelijkfoto=pygame.image.load('WhatsApp Image 2023-01-27 at 14.31.20.jpeg').convert_alpha()
normaalfoto=pygame.image.load('WhatsApp Image 2023-01-27 at 14.31.32.jpeg').convert_alpha()
moeilijkfoto=pygame.image.load('WhatsApp Image 2023-01-27 at 14.33.43.jpeg').convert_alpha()

makkelijkknop= knop(400,200,makkelijkfoto,0.2)
normaalknop= knop(400,600,normaalfoto,0.2)
moeilijkknop= knop(400,400,moeilijkfoto,0.2)

menu_state='moeilijkheid'
#startwaarden voor de timer
current_time=0
ingame_time=0
static_time = 0


#initiatie van de tekstbar
tekst=''
base_font = pygame.font.Font(None,32)
input_rect=pygame.Rect(0,150,140,32)
kleur=pygame.Color('lightskyblue3')
t=''

#score keeper
computer_boventekst=pygame.font.Font(None,50)
plaats_computer_boventekst=pygame.Rect(0,0,200,50)

computer_score_keeper=pygame.font.Font(None,90)
input_computer=pygame.Rect(0,50,100,100)
rood=pygame.Color(255,0,0)
computerscore='0'

speler_boventekst=pygame.font.Font(None,50)
plaats_speler_boventekst=pygame.Rect(675,0,200,50)

speler_score_keeper=pygame.font.Font(None,90)
input_speler=pygame.Rect(700,50,100,100)
spelerscore='0'

eindscherm=pygame.font.SysFont('verdana',70)
eindtekst=eindscherm.render('spel afgelopen',True,(255,0,0))

#nummering
nummer1=pygame.font.Font(None,35)
nummer1_plaats=pygame.Rect(100,200,20,40)

nummer2=pygame.font.Font(None,35)
nummer2_plaats=pygame.Rect(300,200,20,40)

nummer3=pygame.font.Font(None,35)
nummer3_plaats=pygame.Rect(500,200,20,40)

nummer4=pygame.font.Font(None,35)
nummer4_plaats=pygame.Rect(700,200,20,40)

nummer5=pygame.font.Font(None,35)
nummer5_plaats=pygame.Rect(100,400,20,40)

nummer6=pygame.font.Font(None,35)
nummer6_plaats=pygame.Rect(300,400,20,40)

nummer7=pygame.font.Font(None,35)
nummer7_plaats=pygame.Rect(500,400,20,40)

nummer8=pygame.font.Font(None,35)
nummer8_plaats=pygame.Rect(700,400,20,40)

nummer9=pygame.font.Font(None,35)
nummer9_plaats=pygame.Rect(100,600,20,40)

nummer10=pygame.font.Font(None,35)
nummer10_plaats=pygame.Rect(300,600,30,40)

nummer11=pygame.font.Font(None,35)
nummer11_plaats=pygame.Rect(500,600,30,40)

nummer12=pygame.font.Font(None,35)
nummer12_plaats=pygame.Rect(700,600,30,40)

sets = []

psets = list(itertools.combinations([0,1,2,3,4,5,6,7,8,9,10,11],3))
first_time = True
while run:
    
        
    
    current_time=pygame.time.get_ticks()

    #computer als tegenstander   
    if menu_state=='moeilijkheid':
        
        if makkelijkknop.draw(screen) == True:
            d=25000
            menu_state='setkaarten'
            set_menu=True
            static_time=pygame.time.get_ticks()
            
        if normaalknop.draw(screen) == True:
            d=20000
            menu_state='setkaarten'
            set_menu=True
            static_time=pygame.time.get_ticks()
            
        if moeilijkknop.draw(screen) == True:
            d=10000
            menu_state='setkaarten'
            set_menu=True
            static_time=pygame.time.get_ticks()
            
            
    if set_menu==True: 
        if first_time == True:
            screen.fill('black')
            x1=random.randint(0,len(cardsinthegame)-1)
            image1 = pygame.image.load(cardsinthegame[x1])
            image1_rect= image1.get_rect(topleft=(0,200))
            tablecards.append(cardsinthegame[x1])
            cardsinthegame.pop(x1)
            

            x2=random.randint(0,len(cardsinthegame)-1)
            image2 = pygame.image.load(cardsinthegame[x2])
            image2_rect= image2.get_rect(topleft=(200,200))
            tablecards.append(cardsinthegame[x2])
            cardsinthegame.pop(x2)
            


            x3=random.randint(0,len(cardsinthegame)-1)
            image3 = pygame.image.load(cardsinthegame[x3])
            image3_rect= image3.get_rect(topleft=(400,200))
            tablecards.append(cardsinthegame[x3])
            cardsinthegame.pop(x3)
            


            x4=random.randint(0,len(cardsinthegame)-1)
            image4 = pygame.image.load(cardsinthegame[x4])
            image4_rect= image4.get_rect(topleft=(600,200))
            tablecards.append(cardsinthegame[x4])
            cardsinthegame.pop(x4)
            


            x5=random.randint(0,len(cardsinthegame)-1)
            image5 = pygame.image.load(cardsinthegame[x5])
            image5_rect= image5.get_rect(topleft=(0,400))
            tablecards.append(cardsinthegame[x5])
            cardsinthegame.pop(x5)
            


            x6=random.randint(0,len(cardsinthegame)-1)
            image6 = pygame.image.load(cardsinthegame[x6])
            image6_rect= image6.get_rect(topleft=(200,400))
            tablecards.append(cardsinthegame[x6])
            cardsinthegame.pop(x6)
            


            x7=random.randint(0,len(cardsinthegame)-1)
            image7 = pygame.image.load(cardsinthegame[x7])
            image7_rect= image7.get_rect(topleft=(400,400))
            tablecards.append(cardsinthegame[x7])
            cardsinthegame.pop(x7)
            


            x8=random.randint(0,len(cardsinthegame)-1)
            image8 = pygame.image.load(cardsinthegame[x8])
            image8_rect= image4.get_rect(topleft=(600,400))
            tablecards.append(cardsinthegame[x8])
            cardsinthegame.pop(x8)
            


            x9=random.randint(0,len(cardsinthegame)-1)
            image9 = pygame.image.load(cardsinthegame[x9])
            image9_rect= image9.get_rect(topleft=(0,600))
            tablecards.append(cardsinthegame[x9])
            cardsinthegame.pop(x9)
            


            x10=random.randint(0,len(cardsinthegame)-1)
            image10 = pygame.image.load(cardsinthegame[x10])
            image10_rect= image10.get_rect(topleft=(200,600))
            tablecards.append(cardsinthegame[x10])
            cardsinthegame.pop(x10)
            


            x11=random.randint(0,len(cardsinthegame)-1)
            image11 = pygame.image.load(cardsinthegame[x11])
            image11_rect= image11.get_rect(topleft=(400,600))
            tablecards.append(cardsinthegame[x11])
            cardsinthegame.pop(x11)
            


            x12=random.randint(0,len(cardsinthegame)-1)
            image12 = pygame.image.load(cardsinthegame[x12])
            image12_rect= image12.get_rect(topleft=(600,600))
            tablecards.append(cardsinthegame[x12])
            cardsinthegame.pop(x12)

            #uiteindelijke weergave van de kaarten op het scherm
            screen.blit(image1, (image1_rect))
            screen.blit(image2, (image2_rect))
            screen.blit(image3, (image3_rect))
            screen.blit(image4, (image4_rect))
            screen.blit(image5, (image5_rect))
            screen.blit(image6, (image6_rect))
            screen.blit(image7, (image7_rect))
            screen.blit(image8, (image8_rect))
            screen.blit(image9, (image9_rect))
            screen.blit(image10, (image10_rect))
            screen.blit(image11, (image11_rect))
            screen.blit(image12, (image12_rect))
            
            pygame.draw.rect(screen,rood,nummer1_plaats)
            letter1=nummer1.render('1',True,(0,0,0))
            screen.blit(letter1, (nummer1_plaats.x+5,nummer1_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer2_plaats)
            letter2=nummer2.render('2',True,(0,0,0))
            screen.blit(letter2, (nummer2_plaats.x+5,nummer2_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer3_plaats)
            letter3=nummer3.render('3',True,(0,0,0))
            screen.blit(letter3, (nummer3_plaats.x+5,nummer3_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer4_plaats)
            letter4=nummer4.render('4',True,(0,0,0))
            screen.blit(letter4, (nummer4_plaats.x+5,nummer4_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer5_plaats)
            letter5=nummer5.render('5',True,(0,0,0))
            screen.blit(letter5, (nummer5_plaats.x+5,nummer5_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer6_plaats)
            letter6=nummer6.render('6',True,(0,0,0))
            screen.blit(letter6, (nummer6_plaats.x+5,nummer6_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer7_plaats)
            letter7=nummer7.render('7',True,(0,0,0))
            screen.blit(letter7, (nummer7_plaats.x+5,nummer7_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer8_plaats)
            letter8=nummer8.render('8',True,(0,0,0))
            screen.blit(letter8, (nummer8_plaats.x+5,nummer8_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer9_plaats)
            letter9=nummer9.render('9',True,(0,0,0))
            screen.blit(letter9, (nummer9_plaats.x+5,nummer9_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer10_plaats)
            letter10=nummer10.render('10',True,(0,0,0))
            screen.blit(letter10, (nummer10_plaats.x+5,nummer10_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer11_plaats)
            letter11=nummer11.render('11',True,(0,0,0))
            screen.blit(letter11, (nummer11_plaats.x+5,nummer11_plaats.y+5))
            
            pygame.draw.rect(screen,rood,nummer12_plaats)
            letter12=nummer12.render('12',True,(0,0,0))
            screen.blit(letter12, (nummer12_plaats.x+5,nummer12_plaats.y+5))



            first_time = False
        
        #algoritme dat alle mogelijke sets vindt in de 12 kaarten die op tafel liggen
        
        for h in range(len(psets)):

            kaart1 = tablecards[psets[h][0]]
            kaart2 = tablecards[psets[h][1]]
            kaart3 = tablecards[psets[h][2]]
            if (vectortocard[kaart1].kleur == vectortocard[kaart2].kleur and vectortocard[kaart2].kleur == vectortocard[kaart3].kleur) or (vectortocard[kaart1].kleur != vectortocard[kaart2].kleur and vectortocard[kaart1].kleur != vectortocard[kaart3].kleur and vectortocard[kaart2].kleur != vectortocard[kaart3].kleur):
               if (vectortocard[kaart1].vorm == vectortocard[kaart2].vorm and vectortocard[kaart2].vorm == vectortocard[kaart3].vorm) or (vectortocard[kaart1].vorm != vectortocard[kaart2].vorm and vectortocard[kaart1].vorm != vectortocard[kaart3].vorm and vectortocard[kaart2].vorm != vectortocard[kaart3].vorm):
                    if (vectortocard[kaart1].vulling == vectortocard[kaart2].vulling and vectortocard[kaart2].vulling == vectortocard[kaart3].vulling) or (vectortocard[kaart1].vulling != vectortocard[kaart2].vulling and vectortocard[kaart1].vulling != vectortocard[kaart3].vulling and vectortocard[kaart2].vulling != vectortocard[kaart3].vulling):
                        if (vectortocard[kaart1].veelvoud == vectortocard[kaart2].veelvoud and vectortocard[kaart2].veelvoud == vectortocard[kaart3].veelvoud) or (vectortocard[kaart1].veelvoud != vectortocard[kaart2].veelvoud and vectortocard[kaart1].veelvoud !=vectortocard[kaart3].veelvoud and vectortocard[kaart2].veelvoud != vectortocard[kaart3].veelvoud):
                            if [psets[h][0]+1, psets[h][1]+1, psets[h][2]+1] in sets:
                                sets=sets
                            else:
                                sets.append([psets[h][0]+1, psets[h][1]+1, psets[h][2]+1])
                           

        
        if current_time-static_time>d:      
            if len(sets)!=0:
                tekst+='SET!'
                nieuwe_computerscore=int(computerscore)+3
                computerscore=str(nieuwe_computerscore)
                j=sets[0][0]-1
                k=sets[0][1]-1
                l=sets[0][2]-1
                tablecards.pop(j)
                tablecards.pop(k-1)
                tablecards.pop(l-2)
                sets=[]
                j+=1
                k+=1
                l+=1
                if j==1 or k==1 or l==1:
                    x1=random.randint(0,len(cardsinthegame)-1)
                    image1 = pygame.image.load(cardsinthegame[x1])
                    image1_rect= image1.get_rect(topleft=(0,200))
                    tablecards.insert(0,cardsinthegame[x1])
                    cardsinthegame.pop(x1)
                if j==2 or k==2 or l==2:
                    x2=random.randint(0,len(cardsinthegame)-1)
                    image2 = pygame.image.load(cardsinthegame[x2])
                    image2_rect= image2.get_rect(topleft=(200,200))
                    tablecards.insert(1,cardsinthegame[x2])
                    cardsinthegame.pop(x2)
                if j==3 or k==3 or l==3:
                    x3=random.randint(0,len(cardsinthegame)-1)
                    image3 = pygame.image.load(cardsinthegame[x3])
                    image3_rect= image3.get_rect(topleft=(400,200))
                    tablecards.insert(2,cardsinthegame[x3])
                    cardsinthegame.pop(x3)
                if j==4 or k==4 or l==4:
                    x4=random.randint(0,len(cardsinthegame)-1)
                    image4 = pygame.image.load(cardsinthegame[x4])
                    image4_rect= image4.get_rect(topleft=(600,200))
                    tablecards.insert(3,cardsinthegame[x4])
                    cardsinthegame.pop(x4)
                if j==5 or k==5 or l==5:
                    x5=random.randint(0,len(cardsinthegame)-1)
                    image5 = pygame.image.load(cardsinthegame[x5])
                    image5_rect= image5.get_rect(topleft=(0,400))
                    tablecards.insert(4,cardsinthegame[x5])
                    cardsinthegame.pop(x5)
                if j==6 or k==6 or l==6:
                    x6=random.randint(0,len(cardsinthegame)-1)
                    image6 = pygame.image.load(cardsinthegame[x6])
                    image6_rect= image6.get_rect(topleft=(200,400))
                    tablecards.insert(5,cardsinthegame[x6])
                    cardsinthegame.pop(x6)
                if j==7 or k==7 or l==7:
                    x7=random.randint(0,len(cardsinthegame)-1)
                    image7 = pygame.image.load(cardsinthegame[x7])
                    image7_rect= image7.get_rect(topleft=(400,400))
                    tablecards.insert(6,cardsinthegame[x7])
                    cardsinthegame.pop(x7)
                if j==8 or k==8 or l==8:
                    x8=random.randint(0,len(cardsinthegame)-1)
                    image8 = pygame.image.load(cardsinthegame[x8])
                    image8_rect= image4.get_rect(topleft=(600,400))
                    tablecards.insert(7,cardsinthegame[x8])
                    cardsinthegame.pop(x8)
                if j==9 or k==9 or l==9:
                    x9=random.randint(0,len(cardsinthegame)-1)
                    image9 = pygame.image.load(cardsinthegame[x9])
                    image9_rect= image9.get_rect(topleft=(0,600))
                    tablecards.insert(8,cardsinthegame[x9])
                    cardsinthegame.pop(x9)
                if j==10 or k==10 or l==10:
                    x10=random.randint(0,len(cardsinthegame)-1)
                    image10 = pygame.image.load(cardsinthegame[x10])
                    image10_rect= image10.get_rect(topleft=(200,600))
                    tablecards.insert(9,cardsinthegame[x10])
                    cardsinthegame.pop(x10)
                if j==11 or k==11 or l==11:
                    x11=random.randint(0,len(cardsinthegame)-1)
                    image11 = pygame.image.load(cardsinthegame[x11])
                    image11_rect= image11.get_rect(topleft=(400,600))
                    tablecards.insert(10,cardsinthegame[x11])
                    cardsinthegame.pop(x11)
                if j==12 or k==12 or l==12:
                    x12=random.randint(0,len(cardsinthegame)-1)
                    image12 = pygame.image.load(cardsinthegame[x12])
                    image12_rect= image12.get_rect(topleft=(600,600))
                    tablecards.insert(11,cardsinthegame[x12])
                    cardsinthegame.pop(x12)
                if len(cardsinthegame)==0:
                    set_menu=False
                    screen.fill('black')
                    screen.blit(eindtekst,(100,50))
                    
     
                
                #uiteindelijke weergave van de kaarten op het scherm
                screen.blit(image1, (image1_rect))
                screen.blit(image2, (image2_rect))
                screen.blit(image3, (image3_rect))
                screen.blit(image4, (image4_rect))
                screen.blit(image5, (image5_rect))
                screen.blit(image6, (image6_rect))
                screen.blit(image7, (image7_rect))
                screen.blit(image8, (image8_rect))
                screen.blit(image9, (image9_rect))
                screen.blit(image10, (image10_rect))
                screen.blit(image11, (image11_rect))
                screen.blit(image12, (image12_rect))
                
            else:
                tablecards.pop(2)
                tablecards.pop(1)
                tablecards.pop(0)
                
                tekst+='CAPSET'
                
                x1=random.randint(0,len(cardsinthegame)-1)
                image1 = pygame.image.load(cardsinthegame[x1])
                image1_rect= image1.get_rect(topleft=(0,200))
                tablecards.insert(0,cardsinthegame[x1])
                cardsinthegame.pop(x1)
                
                x2=random.randint(0,len(cardsinthegame)-1)
                image2 = pygame.image.load(cardsinthegame[x2])
                image2_rect= image2.get_rect(topleft=(200,200))
                tablecards.insert(1,cardsinthegame[x2])
                cardsinthegame.pop(x2)
                
                x3=random.randint(0,len(cardsinthegame)-1)
                image3 = pygame.image.load(cardsinthegame[x3])
                image3_rect= image3.get_rect(topleft=(400,200))
                tablecards.insert(2,cardsinthegame[x3])
                cardsinthegame.pop(x3)
                
                screen.blit(image1, (image1_rect))
                screen.blit(image2, (image2_rect))
                screen.blit(image3, (image3_rect))
                
                if len(cardsinthegame)==0:
                    set_menu=False
                    screen.fill('black')
                    screen.blit(eindtekst,(100,120))
            
            static_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        
        #systeem afsluiten
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            run=False
        
          
        #tekstbar    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                tekst=tekst[:-1]
            else:
                tekst+=event.unicode
                t+=str(pygame.key.name(event.key))
            if event.key==pygame.K_RETURN:
                t=t[:-6]
                t=t.split('space')
                
                if len(t[0])>2 or len(t[1])>2 or len(t[2])>2:
                    tekst+='ongeldige invoer'
                else:
                    x=int(t[0])-1
                    y=int(t[1])-1
                    z=int(t[2])-1
                    kaart1=tablecards[x]
                    kaart2=tablecards[y]
                    kaart3=tablecards[z]

                    
                    #set checker
                    if x==y:
                        tekst+='ongeldige invoer'
                    if x!=y:
                        if (vectortocard[kaart1].kleur == vectortocard[kaart2].kleur and vectortocard[kaart2].kleur == vectortocard[kaart3].kleur) or (vectortocard[kaart1].kleur != vectortocard[kaart2].kleur and vectortocard[kaart1].kleur != vectortocard[kaart3].kleur and vectortocard[kaart2].kleur != vectortocard[kaart3].kleur):
                           if (vectortocard[kaart1].vorm == vectortocard[kaart2].vorm and vectortocard[kaart2].vorm == vectortocard[kaart3].vorm) or (vectortocard[kaart1].vorm != vectortocard[kaart2].vorm and vectortocard[kaart1].vorm != vectortocard[kaart3].vorm and vectortocard[kaart2].vorm != vectortocard[kaart3].vorm):
                                if (vectortocard[kaart1].vulling == vectortocard[kaart2].vulling and vectortocard[kaart2].vulling == vectortocard[kaart3].vulling) or (vectortocard[kaart1].vulling != vectortocard[kaart2].vulling and vectortocard[kaart1].vulling != vectortocard[kaart3].vulling and vectortocard[kaart2].vulling != vectortocard[kaart3].vulling):
                                    if (vectortocard[kaart1].veelvoud == vectortocard[kaart2].veelvoud and vectortocard[kaart2].veelvoud == vectortocard[kaart3].veelvoud) or (vectortocard[kaart1].veelvoud != vectortocard[kaart2].veelvoud and vectortocard[kaart1].veelvoud !=vectortocard[kaart3].veelvoud and vectortocard[kaart2].veelvoud != vectortocard[kaart3].veelvoud):
                                        tekst+='SET!'
                                        
                                        nieuwe_spelerscore=int(spelerscore)+3
                                        spelerscore=str(nieuwe_spelerscore)
                                        b=sorted([x+1,y+1,z+1])
                                        sets=[]
                                        tablecards.pop(b[2]-1)
                                        tablecards.pop(b[1]-1)
                                        tablecards.pop(b[0]-1)
                                        
                                        
                                        if x==0 or y==0 or z==0:
                                            x1=random.randint(0,len(cardsinthegame)-1)
                                            image1 = pygame.image.load(cardsinthegame[x1])
                                            image1_rect= image1.get_rect(topleft=(0,200))
                                            tablecards.insert(0,cardsinthegame[x1])
                                            cardsinthegame.pop(x1)
                                        if x==1 or y==1 or z==1:
                                            x2=random.randint(0,len(cardsinthegame)-1)
                                            image2 = pygame.image.load(cardsinthegame[x2])
                                            image2_rect= image2.get_rect(topleft=(200,200))
                                            tablecards.insert(1,cardsinthegame[x2])
                                            cardsinthegame.pop(x2)
                                        if x==2 or y==2 or z==2:
                                            x3=random.randint(0,len(cardsinthegame)-1)
                                            image3 = pygame.image.load(cardsinthegame[x3])
                                            image3_rect= image3.get_rect(topleft=(400,200))
                                            tablecards.insert(2,cardsinthegame[x3])
                                            cardsinthegame.pop(x3)
                                        if x==3 or y==3 or z==3:
                                            x4=random.randint(0,len(cardsinthegame)-1)
                                            image4 = pygame.image.load(cardsinthegame[x4])
                                            image4_rect= image4.get_rect(topleft=(600,200))
                                            tablecards.insert(3,cardsinthegame[x4])
                                            cardsinthegame.pop(x4)
                                        if x==4 or y==4 or z==4:
                                            x5=random.randint(0,len(cardsinthegame)-1)
                                            image5 = pygame.image.load(cardsinthegame[x5])
                                            image5_rect= image5.get_rect(topleft=(0,400))
                                            tablecards.insert(4,cardsinthegame[x5])
                                            cardsinthegame.pop(x5)
                                        if x==5 or y==5 or z==5:
                                            x6=random.randint(0,len(cardsinthegame)-1)
                                            image6 = pygame.image.load(cardsinthegame[x6])
                                            image6_rect= image6.get_rect(topleft=(200,400))
                                            tablecards.insert(5,cardsinthegame[x6])
                                            cardsinthegame.pop(x6)
                                        if x==6 or y==6 or z==6:
                                            x7=random.randint(0,len(cardsinthegame)-1)
                                            image7 = pygame.image.load(cardsinthegame[x7])
                                            image7_rect= image7.get_rect(topleft=(400,400))
                                            tablecards.insert(6,cardsinthegame[x7])
                                            cardsinthegame.pop(x7)
                                        if x==7 or y==7 or z==7:
                                            x8=random.randint(0,len(cardsinthegame)-1)
                                            image8 = pygame.image.load(cardsinthegame[x8])
                                            image8_rect= image4.get_rect(topleft=(600,400))
                                            tablecards.insert(7,cardsinthegame[x8])
                                            cardsinthegame.pop(x8)
                                        if x==8 or y==8 or z==8:
                                            x9=random.randint(0,len(cardsinthegame)-1)
                                            image9 = pygame.image.load(cardsinthegame[x9])
                                            image9_rect= image9.get_rect(topleft=(0,600))
                                            tablecards.insert(8,cardsinthegame[x9])
                                            cardsinthegame.pop(x9)
                                        if x==9 or y==9 or z==9:
                                            x10=random.randint(0,len(cardsinthegame)-1)
                                            image10 = pygame.image.load(cardsinthegame[x10])
                                            image10_rect= image10.get_rect(topleft=(200,600))
                                            tablecards.insert(9,cardsinthegame[x10])
                                            cardsinthegame.pop(x10)
                                        if x==10 or y==10 or z==10:
                                            x11=random.randint(0,len(cardsinthegame)-1)
                                            image11 = pygame.image.load(cardsinthegame[x11])
                                            image11_rect= image11.get_rect(topleft=(400,600))
                                            tablecards.insert(10,cardsinthegame[x11])
                                            cardsinthegame.pop(x11)
                                        if x==11 or y==11 or z==11:
                                            x12=random.randint(0,len(cardsinthegame)-1)
                                            image12 = pygame.image.load(cardsinthegame[x12])
                                            image12_rect= image12.get_rect(topleft=(600,600))
                                            tablecards.insert(11,cardsinthegame[x12])
                                            cardsinthegame.pop(x12)
                                        if len(cardsinthegame)==3:
                                            set_menu=False
                                            screen.fill('black')
                                            screen.blit(eindtekst,(100,120))
                                            
                             
                                        
                                        #uiteindelijke weergave van de kaarten op het scherm
                                        screen.blit(image1, (image1_rect))
                                        screen.blit(image2, (image2_rect))
                                        screen.blit(image3, (image3_rect))
                                        screen.blit(image4, (image4_rect))
                                        screen.blit(image5, (image5_rect))
                                        screen.blit(image6, (image6_rect))
                                        screen.blit(image7, (image7_rect))
                                        screen.blit(image8, (image8_rect))
                                        screen.blit(image9, (image9_rect))
                                        screen.blit(image10, (image10_rect))
                                        screen.blit(image11, (image11_rect))
                                        screen.blit(image12, (image12_rect))
                                        
                                        static_time=pygame.time.get_ticks()
                                    
                        else:
                            tekst+='geen geldige set' 

                t=''           
   
    
    #meer eigenschappen voor de tekstbar
    pygame.draw.rect(screen,kleur,input_rect)
    tekstbar=base_font.render(tekst,True,(255,255,255))
    screen.blit(tekstbar,(input_rect.x+5,input_rect.y+5))
    input_rect.w=max(100, tekstbar.get_width() +10)
    
    pygame.draw.rect(screen,rood,plaats_computer_boventekst)
    comp_stand=computer_boventekst.render('computer:',True,(0,0,0))
    screen.blit(comp_stand,(plaats_computer_boventekst.x+5,plaats_computer_boventekst.y+5))
    
    pygame.draw.rect(screen,rood,input_computer)
    computer_score=computer_score_keeper.render(computerscore,True, (0,0,0))
    screen.blit(computer_score, (input_computer.x+5,input_computer.y+5))
    
    pygame.draw.rect(screen,rood,plaats_speler_boventekst)
    speler_stand=speler_boventekst.render('speler:',True,(0,0,0))
    screen.blit(speler_stand,(plaats_speler_boventekst.x+5,plaats_speler_boventekst.y+5))
    
    pygame.draw.rect(screen,rood,input_speler)
    speler_score=speler_score_keeper.render(spelerscore,True, (0,0,0))
    screen.blit(speler_score, (input_speler.x+5,input_speler.y+5))
            


          

    #meer definities voor het starten
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
    








        
