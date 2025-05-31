import pygame
from coordinate import WIDTH, HEIGHT, dice_images, roll_dice, clock

# Khởi tạo Pygame
pygame.init()

running = True
rolling = True
current_dice = roll_dice()
saved_dice = None  # Biến lưu kết quả khi xúc xắc dừng

if __name__ == '__main__':
    while running:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Xúc xắc xoay")

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
