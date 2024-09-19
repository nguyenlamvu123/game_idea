import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xúc xắc xoay")

# Tải hình ảnh xúc xắc
dice_images = [pygame.image.load(f'die{i}.png') for i in range(1, 7)]

# Hàm hiển thị xúc xắc
def roll_dice():
    return random.randint(0, 5)

running = True
rolling = True
current_dice = roll_dice()
saved_dice = None  # Biến lưu kết quả khi xúc xắc dừng

clock = pygame.time.Clock()


if __name__ == '__main__':
    while running:
        screen.fill((255, 255, 255))  # Xóa màn hình
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                rolling = not rolling
                if not rolling:  # Nếu dừng, lưu kết quả
                    saved_dice = current_dice + 1
                    print(saved_dice)

        # Xúc xắc xoay liên tục
        if rolling:
            current_dice = roll_dice()

        screen.blit(dice_images[current_dice], (WIDTH//2 - 50, HEIGHT//2 - 50))
        pygame.display.flip()
        clock.tick(10)  # Giữ tốc độ xoay hợp lý

    pygame.quit()
