import pygame


def load_img(name):  # функция для загрузки иконок
    fullname = f'data/enemies/img/{name}'
    image = pygame.image.load(fullname)
    return image


# словарь с тайлами игрового поля
enemy_images = {
    'easy_enemy': load_img('easy.png'),
    'normal_enemy': load_img('normal.png')
}


class Enemy:
    """
    класс проработки противников
    """
    def __init__(self, path):
        self.path = path
        self.spawn = [path[0][0], path[0][1]]  # точка спавна врага
        self.finish = [path[-1][0], path[-1][1]]  # финиш пути врага (если враг дошел до сервера)
        self.hp = 1
        self.dmg = 1
        self.location = self.x, self.y = self.path[0][0], self.path[0][1]
        self.size = self.width, self.height = 50, 50
        # self.rect =
        # self.img =
        # self.animation =

    def draw_enemy(self, win):
        pass

    def move(self):
        count = 0


class DrawEnemy(pygame.sprite.Sprite):
    """класс обработки тайлов"""
    def __init__(self, enemy_type, pos):
        super().__init__(enemies_sprites, all_sprites)
        self.image = enemy_images[enemy_type]  # выбор врага
        self.rect = self.image.get_rect().move(pos[0], pos[1])  # располагаем врага на холсте

