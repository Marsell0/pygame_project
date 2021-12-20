import pygame
import pygame_gui
import sys

# создаём группы спрайтов
all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
towers_sprites = pygame.sprite.Group()
tiles_sprites = pygame.sprite.Group()
icon_sprites = pygame.sprite.Group()


def terminate():  # функция для корректного выхода из программы
    pygame.quit()
    sys.exit()


def load_tile(name):  # функция для загрузки спрайтов
    fullname = f'data/map/tile/{name}'
    image = pygame.image.load(fullname)
    return image


def load_icon(name):  # функция для загрузки иконок
    fullname = f'data/map/icons/{name}'
    image = pygame.image.load(fullname)
    return image


# словарь с тайлами игрового поля
tile_images = {
    'wall': load_tile('grass_tile.png'),
    'way': load_tile('sand_tile.png')
}

# словарь с иконками для игрового поля
icons_images = {
    'can_build': load_icon('build_tower.png'),
    'your_chest': load_icon('chest.png'),
    'your_chest_lose': load_icon('chest_lose.png'),
    'monster_portal': load_icon('monster_portal.png'),
    'coin': load_icon('coin.png'),
    'life': load_icon('life.png')
}


class Game:
    """
    основной игровой класс
    """
    def __init__(self):
        #  создаём окно "Меню"
        self.weight = 550
        self.height = 550
        self.fps = 60
        self.win = pygame.display.set_mode((self.weight, self.height))
        pygame.display.set_caption('Net Guardians')
        self.clock = pygame.time.Clock()

    def run(self):  # основной игровой цикл
        running = True
        self.win.fill(pygame.Color('black'))
        level_x, level_y = self.draw_lvl(self.load_lvl('lvl_1.txt'))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.draw(self.win)

            pygame.display.flip()
            self.clock.tick(self.fps)

        terminate()

    def load_lvl(self, name):
        filename = f'data/map/levels/{name}'
        # читаем уровень, убирая символы перевода строки
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    def draw_lvl(self, lvl_map):  # прорисовка загруженого уровня
        x, y = None, None
        for y in range(len(lvl_map)):
            for x in range(len(lvl_map[y])):
                if lvl_map[x][y] == '#':
                    Tile('wall', x, y)
                elif lvl_map[x][y] == '.':
                    Tile('way', x, y)
                elif lvl_map[x][y] == '@':
                    Tile('wall', x, y)
                    Icon('can_build', x, y)
                elif lvl_map[x][y] == '!':
                    Tile('way', x, y)
                    Icon('monster_portal', x, y)
                elif lvl_map[x][y] == '%':
                    Tile('way', x, y)
                    Icon('your_chest', x, y)
        return x, y  # возврат размера поля в клетках


class Menu():
    def __init__(self):
        self.size = self.width, self.height = 1280, 720
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Net Guardians')
        self.clock = pygame.time.Clock()
        self.fps = 60

    def start_screen(self):
        pygame.init()

        fon = pygame.transform.scale(pygame.image.load('data/fon.png'), (self.width, self.height))
        self.win.blit(fon, (0, 0))

        manager = pygame_gui.UIManager((800, 600), 'data/menu/theme.json')

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

        clock = pygame.time.Clock()
        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == select_button:
                            Game().run()
                            terminate()
                        if event.ui_element == story_button:
                            pass
                        if event.ui_element == howtoplay_button:
                            pass
                        if event.ui_element == leaderboard_button:
                            pass
                        if event.ui_element == exit_button:
                            terminate()

                manager.process_events(event)

            manager.update(time_delta)

            self.win.blit(fon, (0, 0))
            manager.draw_ui(self.win)

            pygame.display.update()


class Tile(pygame.sprite.Sprite):
    """
    класс обработки тайлов
    """
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_sprites, all_sprites)
        self.image = tile_images[tile_type]  # выбор тайла
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)  # располагаем тайл на холсте


class Icon(pygame.sprite.Sprite):
    """
    класс обработки иконок
    """
    def __init__(self, icon_type, pos_x, pos_y):
        super().__init__(icon_sprites, all_sprites)
        self.image = icons_images[icon_type]  # выбор иконки
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)  # располагаем иконку на холсте


if __name__ == '__main__':
    Menu().start_screen()