def main():
    import pygame
    import random
    import math
    from pygame import mixer
    # Loading a window#
    pygame.init()
    DISPLAY_W, DISPLAY_H = 800, 600
    canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
    window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
    player_pos = [400, 500]
    player = pygame.Rect(player_pos, (53, 53))
    pygame.display.set_caption("Cube Drop")
    mixer.music.load("Lena Raine - Pigstep (Minecraft Music Disc).mp3")  # Music
    mixer.music.play(-1)
    LEFT, RIGHT, START1, START2 = False, False, False, False
    clock = pygame.time.Clock()
    color = 0
    enemy_size = 53
    enemy_pos = [random.randint(0, DISPLAY_W - enemy_size), 0]
    enemy_list = [enemy_pos]
    RED = (255, 0, 0)
    score = 0
    score_v = 0
    myFont = pygame.font.SysFont("monospace", 35)
    speed = 30
    BLUE = (0, 0, 225)
    number_for_collisoin = 10
    ###########################################################################################
    # Starting Controller
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()
    analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

    # Collision
    def detect_collision_2(player_pos, enemy_pos):
        distance = math.sqrt(((player_pos[0] - enemy_pos[0]) ** 2) + ((player_pos[1] - enemy_pos[1]) ** 2))
        if distance < 53.5:
            return True

    game_over = False

    # Game loop
    while not game_over:
        ################################# CHECK PLAYER INPUT #################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pass

            # HANDLES ANALOG INPUTS
            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value

                if abs(analog_keys[0]) > .04:
                    if analog_keys[0] < -.7:
                        LEFT = True
                    else:
                        LEFT = False
                    if analog_keys[0] > .7:
                        RIGHT = True
                    else:
                        RIGHT = False

        # Player movement (With controller)
        if LEFT:
            player.x -= 7  # *(-1 * analog_keys[0])
        if RIGHT:
            player.x += 7  # * analog_keys[0]
        player_pos = [player.x, 500]

        # Update Window  #
        canvas.fill((255, 255, 255))
        pygame.draw.rect(canvas, (BLUE), player)

        text = "Score: " + str(score)
        label = myFont.render(text, 1, (0, 0, 0))
        canvas.blit(label, (DISPLAY_W - 200, DISPLAY_H - 40))
        delay = random.random()
        if len(enemy_list) < 10 and delay < 0.1:
            x_pos = random.randint(0, DISPLAY_W - enemy_size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])

        for enemy_pos in enemy_list:
            if detect_collision_2(player_pos, enemy_pos):
                RED = ("#FFFFFF")
                BLUE = ("#FFFFFF")
                number_for_collisoin = 0
                speed = 0
                enemy_size = 1
                text2 = "Game Over! Your score was: " + str(score)
                text3 = "Move the Joystick left to restart!"
                text4 = "Move the Joystick right to exit!"
                label2 = myFont.render(text2, 1, (0, 0, 0))
                label3 = myFont.render(text3, 1, (0, 0, 0))
                label4 = myFont.render(text4, 1, (0, 0, 0))
                canvas.blit(label2, (85, 200))
                canvas.blit(label3, (85, 250))
                canvas.blit(label4, (85, 300))
                f = pygame.image.load("white.png")
                canvas.blit(f, (600, 500))
                mixer.music.load("8- bit explosion sound effect [SFX].mp3")
                mixer.music.play()

                if abs(analog_keys[0]) > .04:
                    if analog_keys[0] < -.7:
                        START1 = True
                    else:
                        START1 = False
                    if analog_keys[0] > .7:
                        START2 = True
                    else:
                        START2 = False
                if START1:
                    main()
                if START2:
                    quit()

        # Spawning Enemies#
        for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < DISPLAY_H:
                enemy_pos[1] += number_for_collisoin
            else:
                enemy_list.pop(idx)
                score = score + 1
        for enemy_pos in enemy_list:
            pygame.draw.rect(canvas, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
        if score == score_v + 10:
            speed = speed + 3
            score_v = score

        window.blit(canvas, (0, 0))
        clock.tick(speed)
        pygame.display.update()


main()  # For restarting game
