import random
import pygame
import pygame.freetype
from my_car import MyCar
from road import Road
from traffic import TrafficCar

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('Traffic racer')
background_color = (0, 0, 0)

my_car_sound = pygame.mixer.Sound('sounds/engine.wav')
my_car_sound.play(-1)

crash_sound = pygame.mixer.Sound('sounds/crash.wav')

font = pygame.freetype.Font(None, 20)

road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

traffic_cars_group = pygame.sprite.Group()
spawn_traffic_time = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_traffic_time, 1000)

coin_group = pygame.sprite.Group()
spawn_coin_time = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_coin_time, 2000)

def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

my_car_image = get_car_image('images/mercedes.png', (100, 70), -90)
road_image = pygame.image.load('images/road.png')
road_image = pygame.transform.scale(road_image, (500, 800))

traffic_car_images = []
traffic_car1 = get_car_image('images/traffic_car1.png', (100, 70), 90)
traffic_car2 = get_car_image('images/traffic_car2.png', (100, 70), -90)
traffic_car3 = get_car_image('images/traffic_car3.png', (100, 70), -90)
traffic_car_images.extend((traffic_car1, traffic_car2, traffic_car3))

coin_image = pygame.image.load('images/coin.png')

road = Road(road_image, (250, 400))
road_group.add(road)
road = Road(road_image, (250, 0))
road_group.add(road)

def spawn_road():
    road_bg = Road(road_image, (250, -600))
    road_group.add(road_bg)

def spawn_traffic():
    position = (random.randint(40, 460), random.randint(-60, -40))
    speed = 7
    traffic_car = TrafficCar(random.choice(traffic_car_images), position, speed)
    traffic_cars_group.add(traffic_car)

def spawn_coin():
    scale = random.uniform(0.5, 1.0)
    coin = Coin(pygame.transform.scale(coin_image, (int(30 * scale), int(30 * scale))),
                (random.randint(50, 450), -30), scale)
    coin_group.add(coin)

def draw_all():
    road_group.update()
    road_group.draw(screen)
    traffic_cars_group.update()
    traffic_cars_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    my_car.draw(screen)

    font.render_to(screen, (400, 10), f"Coins: {coins_collected}", (255, 255, 255))

class Coin(pygame.sprite.Sprite):
    def __init__(self, image, position, scale):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.speed = 5
        self.scale = scale

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()

def check_collisions():
    global coins_collected
    for coin in coin_group:
        if pygame.sprite.collide_rect(my_car, coin):
            coin.kill()
            coins_collected += 1
            if coins_collected % 2 == 0:
                increase_enemy_speed()

def increase_enemy_speed():
    for car in traffic_cars_group:
        car.speed += 3

coins_collected = 0

my_car = MyCar((300, 600), my_car_image)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()
        if event.type == spawn_traffic_time:
            spawn_traffic()
        if event.type == spawn_coin_time:
            spawn_coin()

    screen.fill(background_color)
    if my_car.game_status == 'game':
        my_car.move()
        draw_all()
        my_car.crash(crash_sound, traffic_cars_group)
        check_collisions()
    elif my_car.game_status == 'game_over':
        font.render_to(screen, (30, 300), 'Game Over', (255, 255, 255))
        my_car_sound.stop()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
