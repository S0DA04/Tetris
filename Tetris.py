#창 구현을 위해 pygame 사용
import pygame

#색상값을 미리 넣어 지정
color = {'White':(225,225,225), 'Black':(0,0,0)}

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
block_map = [[0]*10 for i in range(20)]

#블럭색 지정을 위한 색 리스트
Color_list = ["White", "red", "Blue", "Green", "Yellow", "Pink", "Mint"]

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
                 [[0,7,0,0],[0,7,0,0],[0,7,0,0][0,7,0,0]],
                 [[0,0,0,0],[7,7,7,7],[0,0,0,0],[0,0,0,0]],
                 [[0,0,7,0],[0,0,7,0],[0,0,7,0],[0,0,7,0]],
                 [[0,0,0,0],[0,0,0,0],[7,7,7,7],[0,0,0,0]]
                ]
               ]

pygame.init()

#반복문 수행
running =True
while running:

    #프레임 지정
    clock.tick(30)

    #배경 색상 설정
    screen.fill(color['White'])

    #테트리스의 틀이 되는 선 그리기 위에서 부터 좌측 하단 우측
    pygame.draw.aaline(screen, color['Black'], [frame_x,frame_y],[frame_x,frame_y+Vertical],True)
    pygame.draw.aaline(screen, color['Black'], [frame_x,frame_y+Vertical],[frame_x+Horizontal,frame_y+Vertical],True)
    pygame.draw.aaline(screen, color['Black'], [frame_x+Horizontal,frame_y+Vertical],[frame_x+Horizontal,frame_y],True)

    #이벤트 수집
    pygame.display.update()
    for pyEvent in pygame.event.get():
        if pyEvent.type == pygame.QUIT:
            running = False
        
pygame.quit()