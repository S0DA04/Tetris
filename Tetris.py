#창 구현을 위해 pygame 사용
import pygame
#랜덤적인 블럭 생성을 위해 사용
import random

from pygame import event
from pygame.constants import K_w

#색상값을 미리 넣어 지정
color = {'White':(225,225,225), 'Black':(0,0,0), 'Red':(255,0,0), 'Blue':(0,0,255), 'Green': (0,255,0), 'Yellow': (255,255,0),'Purple':(128,0,255), 'Mint':(0,255,191), 'Pink':(230,25,230) }

# 테트리스 틀의 가로길이와 세로길이 지정
Vertical= 600
Horizontal = 300

#틀의 시작좌표
frame_x = 30
frame_y = 50

#윈도우 크기 설정
screen = pygame.display.set_mode((700,700))

#윈도우명 설정
pygame.display.set_caption("Tetris")

#프레임 설정을 위한?
clock = pygame.time.Clock()

#배치된 블록을 확인하기 위하여 배열 생성
block_map = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

#블럭색 지정을 위한 색 리스트
Color_list = ["White", "Red", "Blue", "Green", "Yellow", "Purple", "Mint",'Pink']

#블럭의 모양을 결정
#Block_Shape[0] = L모양  Block_Shape[1] = _l모양  Block_Shape[2] = ㅏ 모양  Block_Shape[3] = z 모양 Block_Shape[4] = reverse z 모양 Block_Shape[5] = ㅁ 모양  Block_Shape[6] = ㅣ 모양
Block_Shape = [
                #L모양 블럭
                [ 
                 [[0,0,1],[1,1,1],[0,0,0]],
                 [[0,1,0],[0,1,0],[0,1,1]],
                 [[0,0,0],[1,1,1],[1,0,0]],
                 [[1,1,0],[0,1,0],[0,1,0]]
                ],
                #_l 모양 블럭
                [
                 [[2,0,0],[2,2,2],[0,0,0]],
                 [[0,2,2],[0,2,0],[0,2,0]],
                 [[0,0,0],[2,2,2],[0,0,2]],
                 [[0,2,0],[0,2,0],[2,2,0]]
                ],
                #ㅏ 모양 블럭
                [
                 [[0,3,0],[3,3,3],[0,0,0]],
                 [[0,3,0],[0,3,3],[0,3,0]],
                 [[0,0,0],[3,3,3],[0,3,0]],
                 [[0,3,0],[3,3,0],[0,3,0]]
                ],
                #Z모양 블럭
                [
                 [[4,4,0],[0,4,4],[0,0,0]],
                 [[0,0,4],[0,4,4],[0,4,0]],
                 [[0,0,0],[4,4,0],[0,4,4]],
                 [[0,4,0],[4,4,0],[4,0,0]]
                ],
                #reverse z 모양 블럭
                [
                 [[0,5,5],[5,5,0],[0,0,0]],
                 [[0,5,0],[0,5,5],[0,0,5]],
                 [[0,0,0],[0,5,5],[5,5,0]],
                 [[5,0,0],[5,5,0],[0,5,0]]
                ],
                #ㅁ 모양 블럭
                [
                 [[0,6,6],[0,6,6],[0,0,0]],
                 [[0,0,0],[0,6,6],[0,6,6]],
                 [[0,0,0],[6,6,0],[6,6,0]],
                 [[6,6,0],[6,6,0],[0,0,0]]
                ],
                #ㅣ모양 블럭
                [
                 [[0,7,0,0],[0,7,0,0],[0,7,0,0],[0,7,0,0]],
                 [[0,0,0,0],[7,7,7,7],[0,0,0,0],[0,0,0,0]],
                 [[0,0,7,0],[0,0,7,0],[0,0,7,0],[0,0,7,0]],
                 [[0,0,0,0],[0,0,0,0],[7,7,7,7],[0,0,0,0]]
                ]
               ]

def Draw_Block_Map(Block_Map):
    x = 30
    y = 50
    for i in range(20):
        for j in range(10):
            if Block_Map[i][j] == 0:
                pass
            else:
                pygame.draw.rect(screen,color[Color_list[Block_Map[i][j]]],[x+(j*30),y+(i*30),30,30])



#블럭을 그리는 코드  Shape_Num 은 블럭의 모양 결정 Rotate는 회전한 모양 결정 x,y는 3*3블럭 혹은 4*4 의 그리드에서 가장 좌측 상단의 칸의 좌측 상단의 좌표를 지정하는 코드이다.
def Draw_Block(Shape_Num,Rotate, grid_x, grid_y, x,y):

    #제일 왼쪽에 있는 블럭의 x좌푯값과 y좌푯값을 구하기
    Max_Left = 500
    Max_Right = 0
    Max_Bottom = 0

    #ㅣ모양 블럭 생성 얘만 4*4라 따로 제작
    if Shape_Num == 6:
        for i in range(4):
            for j in range(4):
                if Block_Shape[6][Rotate][i][j] == 0:
                    pass;
                else:
                    pygame.draw.rect(screen,color[Color_list[Block_Shape[6][Rotate][i][j]]],[x+(j*30),y+(i*30),30,30])
                    if Max_Left > x+(j*30):
                        Max_Left = x+(j*30)
                    if Max_Right < x+(j*30)+30:
                        Max_Right = x+(j*30)+30
                    if Max_Bottom < y+(i*30)+30:
                        Max_Bottom = y+(i*30)+30
                    if Max_Bottom == 650:
                        for k in range(4):
                            for l in range(4):
                                if Block_Shape[Shape_Num][Rotate][k][l] != 0:
                                    block_map[grid_y+k][grid_x+l] = Block_Shape[Shape_Num][Rotate][k][l]
                                else:
                                    pass
                        return "newa"     
                    if Block_Shape[Shape_Num][Rotate][i][j] != 0:            
                        if block_map[grid_y+1+i][grid_x+j] != 0:
                            for k in range(4):
                                for l in range(4):
                                    if Block_Shape[Shape_Num][Rotate][k][l] != 0:
                                        block_map[grid_y+k][grid_x+l] = Block_Shape[Shape_Num][Rotate][k][l]
                                    else:
                                        pass
                            return "new"

    #나머지 블럭 생성 코드
    else:
        for i in range(3):
            for j in range(3):
                if Block_Shape[Shape_Num][Rotate][i][j] == 0:
                    pass;
                else:
                    pygame.draw.rect(screen,color[Color_list[Block_Shape[Shape_Num][Rotate][i][j]]],[x+(j*30),y+(i*30),30,30])
                    if Max_Left > x+(j*30):
                        Max_Left = x+(j*30)
                    if Max_Right < x+(j*30)+30:
                        Max_Right = x+(j*30)+30
                    if Max_Bottom < y+(i*30)+30:
                        Max_Bottom = y+(i*30)+30
                    if Max_Bottom == 650:
                        for k in range(3):
                            for l in range(3):
                                if Block_Shape[Shape_Num][Rotate][k][l] != 0:
                                    block_map[grid_y+k][grid_x+l] = Block_Shape[Shape_Num][Rotate][k][l]
                                else:
                                    pass
                        return "newa"
                    if Block_Shape[Shape_Num][Rotate][i][j] != 0:
                        if block_map[grid_y+1+i][grid_x+j] != 0:
                            for k in range(3):
                                for l in range(3):
                                    if Block_Shape[Shape_Num][Rotate][k][l] != 0:
                                        block_map[grid_y+k][grid_x+l] = Block_Shape[Shape_Num][Rotate][k][l]
                                    else:
                                        pass
                            return "new"

    Wall = [Max_Left,Max_Right]
    return Wall 


def Random_Block():
    randompick = random.randrange(0,7)
    return randompick

pygame.init()

#임시용 블럭 랜덤 생성
randompick = Random_Block()

#반복문 수행
running =True

#로테이트값 초기화
Rotation = 0

#x,y값 초기화
Placing_x = 150
Placing_y = 50

#시작할때의 배열속 위치
x_Arr_ver = 4
y_Arr_ver = 0

#y그리드 갱신을 위해 사용
flag = 80

while running:

    #프레임 지정
    clock.tick(30)

    #배경 색상 설정
    screen.fill(color['White'])

    #테트리스의 틀이 되는 선 그리기 위에서 부터 좌측 하단 우측
    pygame.draw.aaline(screen, color['Black'], [frame_x,frame_y],[frame_x,frame_y+Vertical],True)
    pygame.draw.aaline(screen, color['Black'], [frame_x,frame_y+Vertical],[frame_x+Horizontal,frame_y+Vertical],True)
    pygame.draw.aaline(screen, color['Black'], [frame_x+Horizontal,frame_y+Vertical],[frame_x+Horizontal,frame_y],True)

    #랜덤적으로 블럭을 하나 그린다. Shape_Num을 결정지음 
    Wall = Draw_Block(randompick,0,x_Arr_ver,y_Arr_ver,Placing_x,Placing_y)
    
    #1/30초당 1씩 블럭이 내려가도록 설정
    Placing_y += 1

    #y의 그리드 갱신
    if Placing_y >= flag:
        y_Arr_ver += 1
        flag += 30

    #블럭이 다른 블럭에 닿으면 움직임을 멈추고 새로운 블럭 생성
    if Wall == "new":
        x_Arr_ver = 3
        y_Arr_ver = 0
        Placing_x = 150
        Placing_y = 50
        flag = 80
        randompick = Random_Block()
        Wall = Draw_Block(randompick,0,x_Arr_ver,y_Arr_ver,Placing_x,Placing_y)

    #블럭이 바닥에 닿게된다면 움직임을 멈추고 새로운 블럭 생성
    if Wall == "newa":
        x_Arr_ver = 3
        y_Arr_ver = 0
        Placing_x = 150
        Placing_y = 50
        flag = 80
        randompick = Random_Block()
        Wall = Draw_Block(randompick,0,x_Arr_ver,y_Arr_ver,Placing_x,Placing_y)
    
    Draw_Block_Map(block_map)

    #이벤트 수집
    pygame.display.update()
    for pyEvent in pygame.event.get():
        #키가 눌렸을 때
        if pyEvent.type == pygame.KEYUP:
            if pyEvent.key == pygame.K_DOWN:
                Placing_y += 10
                if Placing_y >= flag:
                    y_Arr_ver += 1
                    flag += 30
            #좌측화살표를 눌렀을 때
            if pyEvent.key == pygame.K_LEFT:
                #블럭이 칸을 넘어가는 것 방지
                if Wall[0] > 30:
                    Placing_x -= 30
                    x_Arr_ver -= 1
                else:
                    pass
            #오른쪽 키를 눌렀을 때
            if pyEvent.key == pygame.K_RIGHT:
                #블럭이 칸을 넘어가는 것 방지
                if Wall[1] < 330:
                    Placing_x += 30
                    x_Arr_ver += 1
                else:
                    pass
        #종료버튼을 눌렀을 때
        if pyEvent.type == pygame.QUIT:
            running = False
        
pygame.quit()