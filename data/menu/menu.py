import pygame
import pygame_gui


class Menu:
    def __init__(self):
        self.size = self.width, self.height = 1280, 720
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Net Guardians')
        self.clock = pygame.time.Clock()
        self.fps = 60

        pygame.mixer.init()

        pygame.mixer.music.load('data/menu/bg_menu_music.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)

        self.select_snd = pygame.mixer.Sound('data/menu/select.mp3')
        self.select_snd.set_volume(0.2)

    def start_screen(self):
        pygame.init()
        pygame.mixer.init()

        fon = pygame.transform.scale(pygame.image.load('data/fon.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((1280, 720), 'data/menu/theme.json')

        select_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 275), (290, 60)),
                                                    text='SELECT LEVEL',
                                                    manager=manager)
        story_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 335), (290, 60)),
                                                     text='MAIN STORY',
                                                     manager=manager)
        howtoplay_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 395), (290, 60)),
                                                     text='HOW TO PLAY',
                                                     manager=manager)
        leaderboard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 455), (290, 60)),
                                                     text='LEADERBOARD',
                                                     manager=manager)
        exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 515), (290, 60)),
                                                     text='EXIT',
                                                     manager=manager)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == select_button:
                            self.select_snd.play()
                            self.select_level()
                            terminate()
                        if event.ui_element == story_button:
                            self.select_snd.play()
                            self.story()
                            terminate()
                        if event.ui_element == howtoplay_button:
                            self.select_snd.play()
                            self.how_to_play()
                            terminate()
                        if event.ui_element == leaderboard_button:
                            self.select_snd.play()
                            self.leaderboard()
                            terminate()
                        if event.ui_element == exit_button:
                            self.select_snd.play()
                            terminate()

                manager.process_events(event)

            manager.update(self.clock.tick(self.fps))

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()

    def leaderboard(self):
        pygame.init()

        fon = pygame.transform.scale(pygame.image.load('data/other_win.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((800, 600), 'data/menu/theme.json')

        test_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 375), (290, 60)),
                                                   text='Leaderboard в разработке',
                                                   manager=manager)

        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 515), (290, 60)),
                                                   text='BACK',
                                                   manager=manager)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.select_snd.play()
                            self.start_screen()
                            terminate()

                manager.process_events(event)

            manager.update(self.clock.tick(self.fps))

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()

    def select_level(self):
        pygame.init()

        fon = pygame.transform.scale(pygame.image.load('data/other_win.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((800, 600), 'data/menu/theme.json')

        level_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 375), (290, 60)),
                                                   text='Level 1',
                                                   manager=manager)

        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 515), (290, 60)),
                                                   text='BACK',
                                                   manager=manager)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.select_snd.play()
                            self.start_screen()
                            terminate()
                        if event.ui_element == level_button:
                            self.select_snd.play()
                            pygame.mixer.music.stop()
                            Game().run()
                            terminate()

                manager.process_events(event)

            manager.update(self.clock.tick(self.fps))

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()

    def how_to_play(self):
        pygame.init()

        fon = pygame.transform.scale(pygame.image.load('data/other_win.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((800, 600), 'data/menu/theme.json')

        test_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 375), (290, 60)),
                                                   text='How to play в разработке',
                                                   manager=manager)

        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 515), (290, 60)),
                                                   text='BACK',
                                                   manager=manager)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.select_snd.play()
                            self.start_screen()
                            terminate()

                manager.process_events(event)

            manager.update(self.clock.tick(self.fps))

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()

    def story(self):
        pygame.init()

        fon = pygame.transform.scale(pygame.image.load('data/other_win.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((800, 600), 'data/menu/theme.json')

        test_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 375), (290, 60)),
                                                   text='please stand by',
                                                   manager=manager)

        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 515), (290, 60)),
                                                   text='BACK',
                                                   manager=manager)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.select_snd.play()
                            self.start_screen()
                            terminate()
                manager.process_events(event)

            manager.update(self.clock.tick(self.fps))

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()