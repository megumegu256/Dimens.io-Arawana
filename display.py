import math
import numpy as np
import pygame as pg

def main(rp):
  
  pg.init() 
  pg.display.set_caption('Dimens.io')
  disp_w, disp_h = 1200, 720 # DisplaySize(WindowSize)
  grid = 100 #200>X>50
  screen = pg.display.set_mode((disp_w,disp_h)) 
  clock  = pg.time.Clock()
  exit_flag = False
  exit_code = '000'



  poses = []
  poses.append([1,1,1])

  rotation = [0,0,0]

  lines = []


  while not exit_flag:

    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
      if event.type == pg.KEYDOWN:  # キーの押下
        if event.key == pg.K_ESCAPE:
          exit_flag = True
          exit_code = "002"


    screen.fill(pg.Color("#ffffff"))




    Grid_L = pg.Color(0,150,150)
    Grid_S = pg.Color(0,175,175)
    

    font1 = pg.font.SysFont("UDデジタル教科書体", int(3*grid/10))
    font2 = pg.font.SysFont("UDデジタル教科書体", 50)
    font3 = pg.font.SysFont("UDデジタル教科書体", 30)
    font4 = pg.font.SysFont("UDデジタル教科書体", 60)

    #グリッド
    pg.draw.line(screen, Grid_L, (disp_w/2,0), (disp_w/2,disp_h), 2)
    pg.draw.line(screen, Grid_L, (0,disp_h/2), (disp_w,disp_h/2), 2)
    

    #原点
    screen.blit(font1.render("0", True, (0,0,0)), (disp_w//2-15, disp_h//2+10))
    #x軸
    for w in range(disp_w//grid//2+1):
      if w != 0:
        pg.draw.line(screen, Grid_S, (w*grid+disp_w//2,0), (w*grid+disp_w//2,disp_h), 1)
        screen.blit(font1.render(f"{int(w)}", True, (0,0,0)), (w*grid-grid/20+disp_w//2, disp_h/2+grid/10))
        pg.draw.line(screen, Grid_S, ((-w*grid+disp_w//2),0), (-w*grid+disp_w//2,disp_h), 1)
        screen.blit(font1.render(f"{int(-w)}", True, (0,0,0)), (-w*grid-grid/20+disp_w//2, disp_h/2+grid/10))
    #y軸
    for h in range(disp_h//grid//2+1):
      #pg.draw.line(screen, Grid_S, (0,h*grid), (disp_w,h*grid), 1)
      if h != 0:
        pg.draw.line(screen, Grid_S, (0,h*grid+disp_h//2), (disp_w,h*grid+disp_h//2), 1)
        screen.blit(font1.render(f"{int(-h)}", True, (0,0,0)), (disp_w/2+grid/10,h*grid-grid/10+disp_h//2))
        pg.draw.line(screen, Grid_S, ((0,-h*grid+disp_h//2)), (disp_w,-h*grid+disp_h//2), 1)
        screen.blit(font1.render(f"{int(h)}", True, (0,0,0)), (disp_w/2+grid/10,-h*grid-grid/10+disp_h//2))

    
  
      for i in range(len(poses)):
        pg.draw.circle(screen,"blue",(rp[0][0]*grid+disp_w/2,disp_h/2-rp[0][1]*grid),5)
        screen.blit(font1.render(f"{i}", True, (0,0,0)), (rp[0][0]*grid+disp_w/2+4,disp_h/2-rp[0][1]*grid-4))


    # 画面出力の更新と同期
    pg.display.update()
    clock.tick(30) # 最高速度を 30フレーム/秒 に制限

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')