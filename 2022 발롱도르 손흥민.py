import random
from time import sleep

import pygame                #파이게임선언 
from pygame.locals import *

##파이게임에서 사용할 전역변수 선언
pygame.init()                        #파이게임 초기화
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("SuperSon")

#색깔지정
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,250,50)
RED = (250,50,50)

#1초에 몇프레임
FPS = 60



explosion_sounds2 = ("superson.wav")
explosion_sounds3 =  ("honaldo28.wav")  
gameover_sounds2 =  ("gameover2.wav")  
explosion_sound3 = pygame.mixer.Sound(explosion_sounds3)
gameover_sound2 = pygame.mixer.Sound(gameover_sounds2)
explosion_sounds4 = ("explosion02.wav")
explosion_sound4 = pygame.mixer.Sound(explosion_sounds4)
youngtak_sounds =  ("superyoungtak.wav")
youngtak_sound = pygame.mixer.Sound(youngtak_sounds)
ohmy_sounds =  ("ohmysuper.wav")
ohmy_sound = pygame.mixer.Sound(ohmy_sounds)




class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Fighter,self).__init__()
        self.image = pygame.image.load("fighter.png")
        self.rect = self.image.get_rect()
        #처음시작할떄 어디서 전투기시작?
        self.rect.x =int(WINDOW_WIDTH/2)
        self.rect.y =WINDOW_HEIGHT - self.rect.height
        #방향조정
        self.dx = 0
        self.dy = 0

        #비행기움직임조정
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x <0 or self.rect.x + self.rect.width > WINDOW_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.rect.y -= self.dy

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite

class Missile(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Missile,self).__init__()
        self.image = pygame.image.load("missile.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound("missile.wav")
    def launch(self):
        self.sound.play()
    def update(self):
        self.rect.y -= self.speed        
        if self.rect.y + self.rect.height <0:
        
            self.kill()
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite

class Missile2(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Missile2,self).__init__()
        self.image = pygame.image.load("missile2.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound("missile.wav")
    def launch(self):
        self.sound.play()
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height <0:
            self.kill()
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite


class Missile3(Missile):
    

    def __init__(self,xpos,ypos,speed):
        super(Missile,self).__init__()
        self.image = pygame.image.load("missile3.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound("missile.wav")
    def update(self):
        self.rect.y -= self.speed
        self.rect.x += self.speed /2
        if self.rect.y + self.rect.height <0:
        
            self.kill()

class Missile4(Missile):
    def __init__(self,xpos,ypos,speed):
        super(Missile,self).__init__()
        self.image = pygame.image.load("missile4.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound("missile.wav")
    def update(self):
        self.rect.y -= self.speed
        self.rect.x -= self.speed /2
        if self.rect.y + self.rect.height <0:
        
            self.kill()


class Rock(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Rock,self).__init__()
        rock_images = ("rock01.png", "rock02.png","rock03.png", "rock04.png","rock05.png",\
                        "rock06.png", "rock07.png","rock08.png", "rock09.png","rock10.png",\
                        "rock11.png", "rock12.png","rock13.png", "rock14.png","rock15.png",\
                        "rock16.png", "rock17.png","rock18.png", "rock19.png","rock20.png",\
                        "rock21.png", "rock22.png","rock23.png", "rock24.png","rock25.png",\
                        "rock26.png", "rock27.png","rock28.png", "rock29.png","rock30.png")
        self.image = pygame.image.load(random.choice(rock_images))
        self.rect =self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True

class Rock2(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Rock2,self).__init__()
        rock2_images = ("rock31.png", "rock32.png","rock33.png", "rock34.png")
        self.image = pygame.image.load(random.choice(rock2_images))
        self.rect =self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True

class Rock3(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Rock3,self).__init__()
        rock3_images = ("rock35.png", "rock36.png","rock37.png","rock39.png")
        self.image = pygame.image.load(random.choice(rock3_images))
        self.rect =self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True

class Rock4(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Rock4,self).__init__()
        rock4_images = ("rock38.png")
        self.image = pygame.image.load(rock4_images)
        self.rect =self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True

class Win(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,speed):
        super(Win,self).__init__()
        win_images = ("sonbal.png")
        self.image = pygame.image.load(win_images)
        self.rect =self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True



def draw_text(text,font,surface,x,y,main_color):
    text_obj = font.render(text,True,main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj,text_rect)

def occur_explosion(surface,x,y):
    explosion_image = pygame.image.load("explosion.png")
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)


    explosion_sounds = ("explosion03.wav")
    explosion_sound = pygame.mixer.Sound(explosion_sounds)
        
    #explosion_sound.play() 너무 시끄러워서 봉인

def game_loop():
    default_font = pygame.font.Font("NanumGothic.ttf", 28)
    background_image = pygame.image.load("background.png")
    gameover_sound = pygame.mixer.Sound("gameover.wav")
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1)
    FPS_clock = pygame.time.Clock()
    one_time=True
    fighter = Fighter()
    missiles = pygame.sprite.Group()
    missiles2 = pygame.sprite.Group()
    missiles3 = pygame.sprite.Group()
    missiles4 = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    rocks2 = pygame.sprite.Group()
    rocks3 = pygame.sprite.Group()
    rocks4 = pygame.sprite.Group()
    wins = pygame.sprite.Group()
    occur_prob = 20
    occur_prob2 = 400
    occur_prob3 = 200
    occur_prob4 = 1000
    shot_count = 0
    count_missed = 3
    special_gaze = 0
    rock2_count = 499
    rock4_count = 49
    weapon_upgrade = 0
    young=True
    ohmy=True
    

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 5
                elif event.key == pygame.K_UP:
                    fighter.dy -= 5
                elif event.key == pygame.K_DOWN:
                    fighter.dy += 5
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx, fighter.rect.y, 10)
                    
                    missile.launch()
                    missiles.add(missile)
                    
                    if young == True:
                        if weapon_upgrade == 10:
                            youngtak_sound.play()
                            young = False

                    if weapon_upgrade >= 10:
                                           
                            
                        missile3 = Missile3(fighter.rect.centerx, fighter.rect.y, 10)
                        missile3.launch()

                        missiles.add(missile3)

                        
                    
                        if weapon_upgrade >= 20:
                            if ohmy == True:
                                ohmy_sound.play()
                                ohmy = False
                            missile4 = Missile4(fighter.rect.centerx, fighter.rect.y, 10)
                            missile4.launch()
                    
                            missiles.add(missile4)

                        

                    
                elif event.key == ord('z'):
                    if special_gaze == 1000:
                        
                        missile2 = Missile2(fighter.rect.centerx, fighter.rect.y, 3)
                        missile2.launch()
                        explosion_sound2 = pygame.mixer.Sound(explosion_sounds2)
                        explosion_sound2.play()
                        missiles2.add(missile2)
                        special_gaze -= 1000
                        
                        

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighter.dy = 0

        screen.blit(background_image, background_image.get_rect())
        #얼마나 많은 운석?
        occur_of_rocks =  1 + int(shot_count/300)
        min_rock_speed = 1 + int(shot_count/200)
        max_rock_speed = 1 + int(shot_count /100)

        occur_of_rocks2 =  1 + int(shot_count/300)
        min_rock2_speed = 1 + int(shot_count/200)
        max_rock2_speed = 1 + int(shot_count /100)

        occur_of_rocks3 =  1 + int(shot_count/300)
        min_rock3_speed = 1 + int(shot_count/200)
        max_rock3_speed = 1 + int(shot_count /100)

        occur_of_rocks4 = 1 + int(shot_count/300) 
        min_rock4_speed = 0.2
        max_rock4_speed = 0.2

        if random.randint(1, occur_prob) ==1:
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed,max_rock_speed)
                rock = Rock(random.randint(0,WINDOW_WIDTH -100),0,speed)
                rocks.add(rock)

        if random.randint(1, occur_prob2) ==1:
            for i in range(occur_of_rocks2):
                speed = random.randint(min_rock2_speed,max_rock2_speed)
                rock2 = Rock2(random.randint(0,WINDOW_WIDTH -100),0,speed)
                rocks2.add(rock2)

        if random.randint(1, occur_prob3) ==1:
            for i in range(occur_of_rocks3):
                speed = random.randint(min_rock3_speed,max_rock3_speed)
                rock3 = Rock3(random.randint(0,WINDOW_WIDTH -100),0,speed)
                rocks3.add(rock3)
                
        if 100<= shot_count<=101 or 200<= shot_count<=201 or 300<= shot_count<=301 or 400<= shot_count<=401 :
            if one_time==True: 

            
                one_time=False
                speed = 0.2
                rock4 = Rock4((120),-300,speed)
                rocks4.add(rock4)
            

        draw_text("발롱도르 점수: {}/446".format(shot_count),default_font,screen,140,40,YELLOW)
        draw_text("목숨: {}".format(count_missed), default_font, screen,410,40,BLACK)
        draw_text("필살기 {}%".format(special_gaze//10), default_font, screen,75,600,RED)
        draw_text("무기레벨 {}단계".format(weapon_upgrade//10+1), default_font, screen,380,570,BLACK)
        draw_text("경험치 {}%".format((weapon_upgrade*10)%100), default_font, screen,380,600,RED)


        for missile in missiles:
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen,rock.rect.x, rock.rect.y)
                shot_count += 1

        for missile2 in missiles2:
            rock = missile2.collide(rocks)
            if rock:
                
                rock.kill()
                occur_explosion(screen,rock.rect.x, rock.rect.y)
                shot_count += 1
        for rock in rocks:
            if rock.out_of_screen():
                rock.kill()
                count_missed -= 1

        for rock2 in rocks2:
            if rock2.out_of_screen():
                rock2.kill()
                count_missed -= 1

        for missile in missiles:
            rock2 = missile.collide(rocks2)
            
            if rock2:
                missile.kill()
                rock2_count -= 1
                
                if rock2_count%5 == 0 :
                    
                    missile.kill()
                    rock2.kill()
                    occur_explosion(screen,rock2.rect.x, rock2.rect.y)
                    shot_count += 2

        for missile2 in missiles2:
            rock2 = missile2.collide(rocks2)
            
            if rock2:
                               
                rock2.kill()
                occur_explosion(screen,rock2.rect.x, rock2.rect.y)
                shot_count += 2


        for rock3 in rocks3:
            rock3 = fighter.collide(rocks3)
            if rock3 :

                
                rock3.kill()
                explosion_sound4.play()
                shot_count += 1
                if weapon_upgrade <20:

                    weapon_upgrade += 1

        for rock4 in rocks4:
            if rock4.out_of_screen():
                rock4.kill()
                explosion_sound3.play()
                one_time=True
                
                count_missed -= 1

        for missile in missiles:
            rock4 = missile.collide(rocks4)
            
            if rock4:
                missile.kill()
                
                rock4_count -= 1
                
                if rock4_count%50 == 0 :
                    
                    missile.kill()
                    rock4.kill()
                    explosion_sound3.play()
                    one_time=True
                    

                    
                    occur_explosion(screen,rock4.rect.x, rock4.rect.y)
                    shot_count += 2

        for missile2 in missiles2:
            rock4 = missile2.collide(rocks4)
            
            if rock4:
                               
                rock4.kill()
                one_time=True
                
                occur_explosion(screen,rock4.rect.x, rock4.rect.y)
                shot_count += 10




        if special_gaze < 1000:
            special_gaze += 2
        else:
            special_gaze ==1000

        

        rocks.update()
        rocks.draw(screen)
        rocks2.update()
        rocks2.draw(screen)
        rocks3.update()
        rocks3.draw(screen) 
        rocks4.update()
        rocks4.draw(screen)
        
        missiles.update()
        missiles.draw(screen)
        missiles2.update()
        missiles2.draw(screen)
        missiles3.update()
        missiles3.draw(screen)
        missiles4.update()
        missiles4.draw(screen)
        fighter.update()
        fighter.draw(screen)
          
        pygame.display.flip()
        


        if fighter.collide(rocks) or count_missed == 0 or fighter.collide(rocks2) or fighter.collide(rocks4) :
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            pygame.display.update()
            gameover_sound.play()
            sleep(3)
            done = True

        if shot_count >= 446 :
            
            pygame.mixer_music.stop()
            gameover_sound2.play()
            
            
            speed = 0
            win = Win(0,150,speed)
            wins.add(win)
  
            wins.update()
            wins.draw(screen)
            font_70 = pygame.font.Font("NanumGothic.ttf",40)
            draw_text("손흥민 2022 발롱도르 수상!",font_70,screen,int(WINDOW_WIDTH/2),int(WINDOW_HEIGHT/2+100),RED)
            pygame.display.update()
            
            


            sleep(5)


            #영상트는거
            
            done = True

        
        

        


        FPS_clock.tick(FPS)

    return "game_menu"

def game_menu():
    start_image = pygame.image.load("background2.png")
    screen.blit(start_image,[0,0])
    draw_x = int(WINDOW_WIDTH/2)
    draw_y = int(WINDOW_HEIGHT/4)
    font_70 = pygame.font.Font("NanumGothic.ttf",40)
    font_40 = pygame.font.Font("NanumGothic.ttf",20)

    draw_text("2022 발롱도르 손흥민",font_70,screen,draw_x,draw_y-80,YELLOW)
    draw_text("Enter : 실행", font_40, screen, draw_x, draw_y+10,WHITE )
    draw_text("Space : 공격  Z : 필살기",font_40,screen,draw_x,draw_y+35,WHITE)
    draw_text("↑ : up   ↓ : down",font_40,screen,draw_x,draw_y+60,WHITE)
    draw_text("→ : right   ← : left",font_40,screen,draw_x,draw_y+85,WHITE)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "play"
        if event.type == QUIT:
            return "quit"
    return "game_menu"

def main():
    global screen
    action = "game_menu"
    while action != "quit":
        if action == "game_menu":
            action = game_menu()
        elif action == "play":
            action = game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
