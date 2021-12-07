import pygame
import sys

# создаём группы спрайтов
all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
towers_sprites = pygame.sprite.Group()
tiles_sprites = pygame.sprite.Group()
icon_sprites = pygame.sprite.Group()


def load_tile(name):  # функция для загрузки спрайтов
    fullname = f'map/tile/{name}'
    image = pygame.image.load(fullname)
    return image


def load_icon(name):  # функция для загрузки иконок
    fullname = f'map/icons/{name}'
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
        self.weight = 800
        self.height = 600
        self.fps = 60
        self.win = pygame.display.set_mode((self.weight, self.height))
        pygame.display.set_caption('Pixel Defense')
        self.clock = pygame.time.Clock()

    def terminate(self):  # функция для корректного выхода из программы
        pygame.quit()
        sys.exit()

    def run(self):  # основной игровой цикл
        running = True
        self.win.fill(pygame.Color('black'))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            tiles_sprites.draw(self.win)
            enemies_sprites.draw(self.win)

            pygame.display.flip()
            self.clock.tick(self.fps)

        self.terminate()

    def load_lvl(self, name):  # загрузка текстового файла с уровнем
        fullname = f'map/levels/{name}'
        with open(fullname, 'r') as lvl_file:
            lvl_map = []
            for line in lvl_file:
                lvl_map.append(line.strip())
        return lvl_map

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
                    Icon('can_build_tower', x, y)
                elif lvl_map[x][y] == '!':
                    Tile('way', x, y)
                    Icon('monster_portal', x, y)
                elif lvl_map[x][y] == '%':
                    Tile('way', x, y)
                    Icon('your_chest', x, y)
        return x, y  # возврат размера поля в клетках


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
    Game().run()