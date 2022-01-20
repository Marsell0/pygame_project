import pygame
import pygame_gui
import sys
import math
import os
from data.menu.menu import VerticalMenu
# from data.enemies.enemy import Enemy
# from data.menu.menu import Menu

# создаём группы спрайтов
all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
towers_sprites = pygame.sprite.Group()
tiles_sprites = pygame.sprite.Group()
icon_sprites = pygame.sprite.Group()

path = []


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


def load_img(name):  # функция для загрузки иконок
    fullname = f'data/enemies/img/{name}'
    image = pygame.image.load(fullname)
    return image


# словарь с тайлами игрового поля
enemy_images = {
    'easy_enemy': load_img('easy.png'),
    'normal_enemy': load_img('normal.png')
}

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
        #  создаём окно с уровнем
        self.size = self.weight, self.height = 750, 550
        self.fps = 60
        self.bg_color = (26, 28, 44)
        self.win = pygame.display.set_mode((self.weight, self.height))
        pygame.display.set_caption('Net Guardians')
        self.clock = pygame.time.Clock()
        self.pause = False

        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 250, side_img)

        self.path_for_enemies = []  # список с координатами пути врагов

        self.manager = pygame_gui.UIManager((self.weight, self.height), 'data/menu/theme.json')  # создание gui

        # подключаем звуковое сопровождение
        pygame.mixer.init()
        pygame.mixer.music.load('data/map/levels/bg_level_music.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(loops=-1)

    def run(self):  # основной игровой цикл
        running = True
        self.win.fill(self.bg_color)
        self.draw_lvl(self.load_lvl('lvl_1.txt'))
        enemies = []
        wave = [[10, 0]]

        for _ in range(wave[0][0]):
            enemies.append(Enemy('easy_enemy'))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.pause:
                            print('unpause')
                            self.pause_off()
                        if not self.pause:
                            print('pause')
                            self.pause_on()
                    # if event.key == pygame.K_SPACE:
                    #     print('ok')
                    #     # enemy.draw(self.win)
                    #     for enemy in enemies:
                    #         enemy.draw(self.win)
                    #         enemy.update()

            for enemy in enemies:
                enemy.draw(self.win)
                enemy.update()

            all_sprites.draw(self.win)
            enemies_sprites.draw(self.win)
            all_sprites.update()
            enemies_sprites.update()

            pygame.display.flip()
            self.clock.tick(self.fps)

        terminate()

    def shop(self):
        pass

    def pause_on(self):
        select_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 275), (290, 60)),
                                                     text='PAUSE',
                                                     manager=self.manager)
        self.pause = True

    def pause_off(self):
        self.pause = False

    def load_lvl(self, name):
        filename = f'data/map/levels/lvl_1/{name}'
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
                if lvl_map[x][y] == '.' or lvl_map[x][y] == '@' or lvl_map[x][y] == '%':
                    self.path_for_enemies.append([x * 50 - 25, y * 50 - 25])
        return x, y  # возврат размера поля в клетках


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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, wave=0):
        super().__init__(enemies_sprites, all_sprites)
        self.image = enemy_images[enemy_type]  # выбор моба
        self.path = [(477, 524), (473, 326), (372, 324), (377, 131), (224, 127), (221, 322), (280, 325),
                     (273, 421), (123, 426), (126, 175), (29, 170)]
        self.spawn = [self.path[0][0], self.path[0][1]]  # точка спавна врага
        self.finish = [self.path[-1][0], self.path[-1][1]]  # финиш пути врага (если враг дошел до сервера)
        self.rect = self.image.get_rect().move(self.spawn[0] - 25, self.spawn[1] - 25)
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.size = 50
        self.health = 5
        self.speed = 1
        self.point = 1
        self.reward = 10

    def update(self):
        move = self.mooving_calc(self.x, self.y, self.path[self.point][0], self.path[self.point][1])
        self.x += self.speed * move[0]
        self.y += self.speed * move[1]
        if move[2] <= self.speed:
            self.point += 1

    def mooving_calc(self, x1, y1, x2, y2):
        vec_x = x2 - x1
        vec_y = y2 - y1
        dist = math.sqrt(vec_x ** 2 + vec_y ** 2)
        norm_vec_x = vec_x / dist
        norm_vec_y = vec_y / dist
        angle = math.atan2(norm_vec_y, norm_vec_x)
        return norm_vec_x, norm_vec_y, dist, angle

    def draw(self, win):
        pygame.draw.circle(win, pygame.color.Color('red'), [self.x, self.y], self.size)

    def draw_health_bar(self, win):
        length = 50
        move_by = round(length / self.max_hp)
        health_bar = move_by * self.hp

        pygame.draw.rect(win, (255, 0, 0), (self.x - 30, self.y - 75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 30, self.y - 75, health_bar, 10), 0)

    def death(self):
        pass


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False

        self.menu = Menu(self, self.x, self.y, side_img, [2000, "MAX"])

        self.tower_imgs = []
        self.damage = 1

        self.place_color = (0, 0, 255, 100)

    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

        if self.selected:
            self.menu.draw(win)

    def draw_radius(self, win):
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self,win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, x, y):
        img = self.tower_imgs[self.level - 1]
        if x <= self.x - img.get_width()//2 + self.width and x >= self.x - img.get_width()//2:
            if y <= self.y + self.height - img.get_height()//2 and y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        """
        call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level-1]

    def upgrade(self):
        """
        upgrades the tower for a given cost
        :return: None
        """
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def get_upgrade_cost(self):
        """
        returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level-1]

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True





if __name__ == '__main__':
    Menu().start_screen()