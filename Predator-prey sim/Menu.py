import pygame, sys
from Init import *
pygame.init()

SCREEN = pygame.display.set_mode((1300, 1000),pygame.RESIZABLE)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
prey_c = 300
pred_c = 80
do_count = True

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def play():
    global prey_c
    global pred_c
    pygame.display.set_caption("Predator-Prey simulation")
    create_map(0, 5, 50, 50, plants)
    for i in range(pred_c):
        create_animal(foxes, None, None)
        create_animal(bears, None, None)
    for i in range(prey_c):
        create_animal(rabbits, None, None)
        create_animal(birds, None, None)
    while True:
        pg.draw.rect(sc, "White", pg.Rect(0, 0, 1025, 1000))
        pg.draw.rect(sc, "Black", pg.Rect(1025,0,1300,1000))
        plants.draw(sc)
        Draw(foxes)
        Draw(rabbits)
        Draw(bears)
        Draw(birds)
        collide()
        death()
        if do_count:
            update_text(len(rabbits), len(foxes), len(bears), len(birds))
        foxes.update(H, W-300, None)
        rabbits.update(H, W-300, None)
        bears.update(H, W-300, None)
        birds.update(H, W-300, None)
        plants.update()
        clock.tick(FPS)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(1300 - 140, 1000 - 75),
                           text_input="BACK", font=get_font(35), base_color="White", hovering_color="Red")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(sc)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == TIMER:
                update_map()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    for fox in foxes:
                        fox.kill()
                    for bear in bears:
                        bear.kill()
                    for rabbit in rabbits:
                        rabbit.kill()
                    for bird in birds:
                        bird.kill()
                    for plant in plants:
                        plant.kill()
                    main_menu()
            elif event.type == pg.USEREVENT:
                pressed = pg.key.get_pressed()
                if pressed[pg.K_f]:
                    create_animal(foxes, None, None)
                if pressed[pg.K_r]:
                    create_animal(rabbits, None, None)

def options():
    global prey_c
    global pred_c
    global do_count
    pygame.display.set_caption("Options")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(30).render("Choose number on prey and predators", True, "#ffc000")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_PREYS = get_font(30).render("Prey", True, "#ffc000")
        OPTIONS_RECT2 = OPTIONS_PREYS.get_rect(center=(660, 230))
        SCREEN.blit(OPTIONS_PREYS, OPTIONS_RECT2)
        OPTIONS_PREDS = get_font(30).render("Predators", True, "#ffc000")
        OPTIONS_RECT3 = OPTIONS_PREDS.get_rect(center=(660, 380))
        SCREEN.blit(OPTIONS_PREDS, OPTIONS_RECT3)
        OPTIONS_VIS = get_font(30).render("Counter", True, "#ffc000")
        OPTIONS_RECTVIS = OPTIONS_VIS.get_rect(center=(660, 530))
        SCREEN.blit(OPTIONS_VIS, OPTIONS_RECTVIS)

        OPTIONS_NPREY = get_font(60).render(str(prey_c), True, "#ffc000")
        OPTIONS_RECT4 = OPTIONS_NPREY.get_rect(center=(660, 300))
        SCREEN.blit(OPTIONS_NPREY, OPTIONS_RECT4)
        OPTIONS_NPRED = get_font(60).render(str(pred_c), True, "#ffc000")
        OPTIONS_RECT5 = OPTIONS_NPRED.get_rect(center=(660, 450))
        SCREEN.blit(OPTIONS_NPRED, OPTIONS_RECT5)

        OPTIONS_ON = Button(image=None, pos=(550, 600),
                                   text_input="ON", font=get_font(45), base_color="#ffc000", hovering_color="Green")
        OPTIONS_OFF = Button(image=None, pos=(750, 600),
                             text_input="OFF", font=get_font(45), base_color="#ffc000", hovering_color="Red")
        OPTIONS_BACK = Button(image=None, pos=(660, 900),
                              text_input="BACK", font=get_font(45), base_color="#ffc000", hovering_color="Red")
        OPTIONS_PREY_P10 = Button(image=None, pos=(900, 300),
                              text_input="+10", font=get_font(45), base_color="#ffc000", hovering_color="Green")
        OPTIONS_PREY_P100 = Button(image=None, pos=(1100, 300),
                              text_input="+100", font=get_font(45), base_color="#ffc000", hovering_color="Green")
        OPTIONS_PREY_M10 = Button(image=None, pos=(400, 300),
                              text_input="-10", font=get_font(45), base_color="#ffc000", hovering_color="Red")
        OPTIONS_PREY_M100 = Button(image=None, pos=(200, 300),
                              text_input="-100", font=get_font(45), base_color="#ffc000", hovering_color="Red")
        OPTIONS_PRED_P10 = Button(image=None, pos=(900, 450),
                              text_input="+10", font=get_font(45), base_color="#ffc000", hovering_color="Green")
        OPTIONS_PRED_P100 = Button(image=None, pos=(1100, 450),
                              text_input="+100", font=get_font(45), base_color="#ffc000", hovering_color="Green")
        OPTIONS_PRED_M10 = Button(image=None, pos=(400, 450),
                              text_input="-10", font=get_font(45), base_color="#ffc000", hovering_color="Red")
        OPTIONS_PRED_M100 = Button(image=None, pos=(200, 450),
                              text_input="-100", font=get_font(45), base_color="#ffc000", hovering_color="Red")

        OPTIONS_ON.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ON.update(SCREEN)
        OPTIONS_OFF.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_OFF.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_PREY_P10.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PREY_P10.update(SCREEN)
        OPTIONS_PREY_P100.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PREY_P100.update(SCREEN)
        OPTIONS_PREY_M10.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PREY_M10.update(SCREEN)
        OPTIONS_PREY_M100.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PREY_M100.update(SCREEN)
        OPTIONS_PRED_P10.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PRED_P10.update(SCREEN)
        OPTIONS_PRED_P100.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PRED_P100.update(SCREEN)
        OPTIONS_PRED_M10.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PRED_M10.update(SCREEN)
        OPTIONS_PRED_M100.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PRED_M100.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_ON.checkForInput(OPTIONS_MOUSE_POS):
                    do_count = True
                if OPTIONS_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    do_count = False
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_PREY_P10.checkForInput(OPTIONS_MOUSE_POS):
                    prey_c+=10
                if OPTIONS_PREY_P100.checkForInput(OPTIONS_MOUSE_POS):
                    prey_c+=100
                if OPTIONS_PREY_M10.checkForInput(OPTIONS_MOUSE_POS):
                    if prey_c >=10:
                        prey_c-=10
                if OPTIONS_PREY_M100.checkForInput(OPTIONS_MOUSE_POS):
                    if prey_c >= 100:
                        prey_c-=100
                    else:
                        prey_c = 0
                if OPTIONS_PRED_P10.checkForInput(OPTIONS_MOUSE_POS):
                    pred_c+=10
                if OPTIONS_PRED_P100.checkForInput(OPTIONS_MOUSE_POS):
                    pred_c+=100
                if OPTIONS_PRED_M10.checkForInput(OPTIONS_MOUSE_POS):
                    if pred_c >=10:
                        pred_c-=10
                if OPTIONS_PRED_M100.checkForInput(OPTIONS_MOUSE_POS):
                    if pred_c >= 100:
                        pred_c-=100
                    else:
                        pred_c = 0

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(125).render("MAIN MENU", True, "#ffc000")
        MENU_RECT = MENU_TEXT.get_rect(center=(660, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Button1.png"), pos=(660, 350),
                             text_input="PLAY", font=get_font(75), base_color="#ffc000", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Button1.png"), pos=(660, 550),
                                text_input="OPTIONS", font=get_font(75), base_color="#ffc000", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Button1.png"), pos=(660, 750),
                             text_input="QUIT", font=get_font(75), base_color="#ffc000", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()