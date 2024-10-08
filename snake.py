import pygame
import random
import time

pygame.init()

width = 400
height = 400
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_blue = (0, 0, 255)
color_white = (255,255,255)
color_green = (0,255,0)
speed = 300
random_number_height = 0
random_number_width = 0
score = 0

clock = pygame.time.Clock()
time_elapsed_since_last_action = 0

direction = "RIGHT"
x1 = 10
y1 = 10
x1_change = 0
y1_change = 0

snake_head = [x1, y1]
snake_body = []
snake_length = 1


menu_running = False
menu_select = [("Start"),("Option"),("Quit")]
active_menu_item = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

def summonFruit():
    pygame.draw.rect(screen, color_red, pygame.Rect(random_number_width, random_number_height, 10, 10))

def update_random_number():
    global random_number_height, random_number_width
    random_number_width = random.randint(2, (width // 10) - 3) * 10
    random_number_height = random.randint(2, (height // 10) - 3) * 10

def summonSnake():
    screen.fill(color_black)
    pygame.draw.rect(screen, color_blue, pygame.Rect(snake_head[0], snake_head[1], 10, 10))

def change_direction(newDirection):
    global direction
    if (direction == "RIGHT" and newDirection == "LEFT") or (direction == "LEFT" and newDirection == "RIGHT") or (direction == "UP" and newDirection == "DOWN") or (direction == "DOWN" and newDirection == "UP"):
        print("Can't change direction")
    else:
        direction = newDirection
        print("Direction : " + direction)

def move_snake():
    if direction == "RIGHT":
        move_right()
    elif direction == "LEFT":
        move_left()
    elif direction == "UP":
        move_up()
    elif direction == "DOWN":
        move_down()

def move_right():
    global x1_change, y1_change
    x1_change = 10
    y1_change = 0
    update_snake_pos()

def move_left():
    global x1_change, y1_change
    x1_change = -10
    y1_change = 0
    update_snake_pos()

def move_up():
    global x1_change, y1_change
    x1_change = 0
    y1_change = -10
    update_snake_pos()

def move_down():
    global x1_change, y1_change
    x1_change = 0
    y1_change = 10
    update_snake_pos()

def update_snake_pos():
    global snake_head, snake_body, snake_length, x1, y1
    
    number = 0

    x1 += x1_change
    y1 += y1_change
    snake_head = [x1, y1]

    #Wall collision
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over()

    # Himself collision
    if [x1, y1] in snake_body:
        game_over()

    #Fruit collision
    if x1 == random_number_width and y1 == random_number_height:
        update_score()
        fruit_update()

    # Add body
    snake_body.insert(0, list(snake_head))
    if len(snake_body) > snake_length:
        snake_body.pop()

    #Draw 
    screen.fill(color_black)
    summonFruit()
    #for each part of the body 

    for segment in snake_body:
       
        if number % 2 == 0:
            pygame.draw.rect(screen, color_blue, pygame.Rect(segment[0], segment[1], 10, 10))
            number += 1
        else:
            pygame.draw.rect(screen, color_green, pygame.Rect(segment[0], segment[1], 10, 10))
            number += 1

    #head
    pygame.draw.rect(screen, color_white, pygame.Rect(snake_head[0], snake_head[1], 10, 10))

    pygame.display.flip()

def game_over():

    font_style = pygame.font.SysFont(None, 27)    
    mesg = font_style.render("You lose with the score of : " + str(score), True, color_red)
    screen.blit(mesg, [width / 4, height / 4])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

def fruit_update():
    global snake_length
    update_random_number()
    snake_length += 1

def update_score():
    global score
    score += 1

def hud_menu(active_menu_item):
    
    start_color = color_white
    option_color = color_white
    quit_color = color_white
    
    if active_menu_item == 0:
        start_color = color_red
    elif (active_menu_item == 1):
        option_color = color_red
    elif (active_menu_item == 2):
        quit_color = color_red
    

    font_style = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 20)  
    
    title = font_style.render("Snake", True, color_white)
    
    start_mesg = small_font.render("Start", True, start_color)
    option_mesg = small_font.render("Options", True, option_color)
    quit_mesg = small_font.render("Quit", True, quit_color)
    
    instruction_mesg = small_font.render("Use the arrow keys to navigate, Enter to select", True, color_white)
    
    screen.fill(color_black)
    
    title_rect = title.get_rect(center=(width / 2, height / 2 - 100))
    screen.blit(title, title_rect.topleft)
    instruction_rect = instruction_mesg.get_rect(center=(width / 2, height / 2 - 50))
    screen.blit(instruction_mesg, instruction_rect.topleft)
 
    start_rect = start_mesg.get_rect(center=(width / 2, height / 2 + 0))
    screen.blit(start_mesg, start_rect.topleft)
    option_rect = option_mesg.get_rect(center=(width / 2, height / 2 + 40))
    screen.blit(option_mesg, option_rect.topleft)
    quit_rect = quit_mesg.get_rect(center=(width / 2, height / 2 + 80))
    screen.blit(quit_mesg, quit_rect.topleft)
    

    pygame.display.update()

def hud_option(active_menu_item):
    global speed
    
    speed_color = color_white
    back_menu_color = color_white

    if active_menu_item == 0:
        speed_color = color_red
    elif (active_menu_item == 1):
        back_menu_color = color_red
        
    screen.fill(color_black)
    
    font_style = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 30)
    
    option_title = font_style.render("Options", True, color_white)
    speed_mesg = small_font.render("Speed  < or > : " + str(speed), True, speed_color)
    main_menu_mesg = small_font.render("Main Menu", True, back_menu_color)
    
    option_title_rect = option_title.get_rect(center=(width / 2, height / 2 - 100))
    speed_mesg_rect = speed_mesg.get_rect(center=(width / 2, height / 2 + 0))
    main_menu_rect = main_menu_mesg.get_rect(center=(width / 2, height / 2 + 40))
    
    screen.blit(option_title, option_title_rect.topleft)
    screen.blit(speed_mesg, speed_mesg_rect.topleft)
    screen.blit(main_menu_mesg, main_menu_rect.topleft)
    
    pygame.display.update()

def load_option():
    
    global speed
    active_menu_item = 0

    menu_running = True
    hud_option(active_menu_item)
    
    while menu_running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    active_menu_item = (active_menu_item - 1) % 2
                    hud_option(active_menu_item)
                    
                elif event.key == pygame.K_DOWN:
                    active_menu_item = (active_menu_item + 1) % 2
                    hud_option(active_menu_item)
                
                elif event.key == pygame.K_RETURN:
                    if active_menu_item == 1:
                        menu_running = False
                        active_menu_item = 0
                        load_menu()
                
                elif event.key == pygame.K_LEFT and active_menu_item == 0:
                    speed -= 50
                    print("Speed changed to: " + str(speed))
                    hud_option(0)
                
                elif event.key == pygame.K_RIGHT and active_menu_item == 0:
                    speed += 50
                    print("Speed changed to: " + str(speed))
                    hud_option(0)
                    
def load_menu():

    menu_running = False
    menu_select = [("Start"),("Option"),("Quit")]
    active_menu_item = 0

    hud_menu(active_menu_item)
 
    menu_running = True
    while menu_running:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                        if active_menu_item - 1 < 0:
                            active_menu_item = 2
                        else:
                            active_menu_item -= 1
                        
                        print(active_menu_item)
                        hud_menu(active_menu_item)
                        
                if event.key == pygame.K_DOWN:
                        if active_menu_item + 1 > 2:
                            active_menu_item = 0
                        else:
                            active_menu_item += 1
                            
                        print(active_menu_item)
                        hud_menu(active_menu_item)
                if event.key == pygame.K_RETURN:
                        print(active_menu_item)
                        print(menu_select[active_menu_item])
                    
                if event.key == pygame.K_RETURN and active_menu_item == 0:
                            menu_running = False
                            start_game()
                if event.key == pygame.K_RETURN and active_menu_item == 1:
                            load_option()
                            active_menu_item = 0
                if event.key == pygame.K_RETURN and active_menu_item == 2:
                            menu_running = False
                            pygame.quit()
                            quit()

def start_game():
    global time_elapsed_since_last_action, clock
     
    update_random_number()
    summonFruit()   

    run = True
    while run:
        pygame.time.delay(100)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Key listener
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            change_direction("LEFT")
        if keys[pygame.K_RIGHT]:
            change_direction("RIGHT")
        if keys[pygame.K_UP]:
            change_direction("UP")
        if keys[pygame.K_DOWN]:
            change_direction("DOWN")

        # Each tick
        tick = clock.tick()
        time_elapsed_since_last_action += tick
        if time_elapsed_since_last_action > speed:  # 0.250s
            move_snake()
            time_elapsed_since_last_action = 0


        font_style = pygame.font.SysFont(None, 30)
        mesg = font_style.render(str(score), True, color_white)
        screen.blit(mesg, [5, 5])
        pygame.display.update()

load_menu()
update_random_number()
summonFruit()
update_score()

pygame.quit()
