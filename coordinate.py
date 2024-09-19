import pygame, random

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình
WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("___")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

size = 30
# Vị trí ban đầu của nhân vật
player_pos = [0, (HEIGHT - size) // 2]

# Danh sách các nút (nodes)
nodes = [
    [60, HEIGHT // 2],
    [120, HEIGHT // 2],
    [150, HEIGHT // 2],
]

# Tải hình ảnh xúc xắc
dice_images = [pygame.image.load(f'die{i}.png') for i in range(1, 7)]

clock = pygame.time.Clock()

# Hàm hiển thị xúc xắc
def roll_dice():
    return random.randint(0, 5)

def move(saved_dice, step=size):
    global player_pos
    for _ in range(saved_dice):
        player_pos[0] += step  # Di chuyển sang phải
        if player_pos[0] > WIDTH:  # Nếu đi quá màn hình, quay lại đầu
            player_pos[0] = 0
