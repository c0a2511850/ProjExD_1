import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習1
    bg2_img = pg.transform.flip(bg_img, True, False)#練習8
    kouka_img = pg.image.load("fig/3.png")#練習3
    kouka_img = pg.transform.flip(kouka_img, True, False)#練習3
    kouka_rct=kouka_img.get_rect()
    kouka_rct.center = 300, 200#練習10-2こうかとん初期座標
    screen.blit(kouka_img, kouka_rct)#練習10-1こうかとんrect習得
    tmr = 0
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#練習10-3
        #kouka_rct.move_ip((-1,0))
        #if key_lst[pg.K_UP]:#練習10-4
        #    kouka_rct.move_ip((0, -1))#練習10-4
        #if key_lst[pg.K_DOWN]:#練習10-4
        #    kouka_rct.move_ip((0, +1))#練習10-4
        #if key_lst[pg.K_LEFT]:#練習10-4
        #    kouka_rct.move_ip((-1, 0))#練習10-4
        #if key_lst[pg.K_RIGHT]:#練習10-4
        #    kouka_rct.move_ip((+2, 0))#練習10-4
        a=0
        b=-1
        if key_lst[pg.K_UP]:
            a-=1
        if key_lst[pg.K_DOWN]:
            a+=1
        if key_lst[pg.K_LEFT]:
            b-=1
        if key_lst[pg.K_RIGHT]:
            b+=2
        kouka_rct.move_ip((b,a)) 
        


        x = tmr%3200#練習5#練習9
        screen.blit(bg_img, [-x, 0])#練習2#練習5
        screen.blit(bg2_img, [-x+1600, 0])#練習7#練習8
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kouka_img, kouka_rct)#練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()