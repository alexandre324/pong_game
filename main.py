import pygame, time
from random import randint

def angle_ball(ball_angle):
    if ball_angle == -4:
        return -0.10
    elif ball_angle == -3:
        return -0.08
    elif ball_angle == -2:
        return -0.05
    elif ball_angle == -1:
        return -0.02
    elif ball_angle == 0:
        return 0
    elif ball_angle == 1:
        return 0.02
    elif ball_angle == 2:
        return 0.05
    elif ball_angle == 3:
        return 0.08
    elif ball_angle == 4:
        return 0.10

    
def text(the_text):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = font.render(the_text, False, (0, 0, 255))
    window.blit(window,(0,0))
    
pygame.init()
window = pygame.display.set_mode((800, 510))
pos_x_paddle = 340
ball_state = 0

while True:
    pygame.display.update()
    pygame.draw.rect(window,(255,255,255),(pos_x_paddle,450,100,10), border_radius=5)

    if ball_state == 0:
        ball_pos_x = pos_x_paddle+50
        ball_pos_y = 440
    elif ball_state == 1 and ball_pos_y > 10:
        pygame.draw.circle(window, (0,0,0), (ball_pos_x,ball_pos_y), 10, 10)
        ball_pos_y -= 0.35
        ball_pos_x += angle_ball(ball_angle)
        if ball_pos_x > 790:
            ball_angle = -ball_angle
        elif ball_pos_x < 10:
            ball_angle = -ball_angle
    elif ball_pos_y < 10:
        ball_state = 2
        pygame.draw.circle(window, (0,0,0), (ball_pos_x,ball_pos_y), 10, 10)
        ball_pos_y += 0.3
        ball_pos_x += angle_ball(ball_angle)
    elif ball_state == 2 and ball_pos_y < 490:
        pygame.draw.circle(window, (0,0,0), (ball_pos_x,ball_pos_y), 10, 10)
        ball_pos_y += 0.3
        ball_pos_x += angle_ball(ball_angle)
        if ball_pos_y > 440 and ball_pos_y < 450 and ball_pos_x > pos_x_paddle and ball_pos_x-5 < pos_x_paddle+105:
            ball_state = 1
            if ball_angle < 4 and ball_angle > 2:
                ball_angle = randint(ball_angle-1, ball_angle+1)
            elif ball_angle >= 4:
                ball_angle = randint(ball_angle-2, ball_angle)
            else:
                ball_angle = randint(ball_angle, ball_angle+2)
        elif ball_pos_x > 790:
            ball_angle = -ball_angle
        elif ball_pos_x < 10:
            ball_angle = -ball_angle
    elif ball_pos_y > 490:
        ball_state = 0
    if ball_pos_y < 440:
        ball_pos_x += angle_ball(ball_angle)
        pygame.draw.circle(window, (255,255,255), (ball_pos_x,ball_pos_y), 10, 10)    
    else:
        pygame.draw.circle(window, (40, 40, 40), (ball_pos_x,ball_pos_y), 10, 10)  
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            pygame.draw.circle(window, (0,0,0), (pos_x_paddle+50,440), 10, 10)
            if event.key == pygame.K_LEFT:
                if pos_x_paddle > 20:
                    pygame.draw.rect(window,(0,0,0),(pos_x_paddle,450,100,10), border_radius=5)
                    pos_x_paddle -= 40
                if pos_x_paddle == 20:
                    pygame.draw.rect(window,(0,0,0),(pos_x_paddle,450,100,10), border_radius=5)
                    pos_x_paddle -= 20
            elif event.key == pygame.K_RIGHT:
                if pos_x_paddle < 700:
                    pygame.draw.rect(window,(0,0,0),(pos_x_paddle,450,100,10), border_radius=5)
                    pos_x_paddle += 40
                if pos_x_paddle == 680:
                    pygame.draw.rect(window,(0,0,0),(pos_x_paddle,450,100,10), border_radius=5)
                    pos_x_paddle += 20
            elif event.key == pygame.K_SPACE and ball_state == 0:
                ball_state = 1
                ball_angle = randint(-4, 4)
