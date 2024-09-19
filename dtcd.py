import pygame
from coordinate import WIDTH, HEIGHT, nodes, WHITE, BLUE, RED

# Khởi tạo Pygame
pygame.init()

running = True


if __name__ == '__main__':
    # Vị trí ban đầu của nhân vật
    player_pos = [50, HEIGHT // 2]
    player_size = 30

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Đi trên con đường")

    while running:
        screen.fill(WHITE)  # Xóa màn hình

        # Vẽ nhân vật
        pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))

        # Vẽ các nút
        for node in nodes:
            pygame.draw.circle(screen, RED, node, 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_pos[0] += 50  # Di chuyển sang phải
                    if player_pos[0] > WIDTH:  # Nếu đi quá màn hình, quay lại đầu
                        player_pos[0] = 0
                elif event.key == pygame.K_LEFT:
                    player_pos[0] -= 50  # Di chuyển sang trái
                    if player_pos[0] < 0:  # Nếu đi quá màn hình bên trái, quay lại cuối đường
                        player_pos[0] = WIDTH

        # Kiểm tra nếu nhân vật đi vào một nút
        for node in nodes:
            if abs(player_pos[0] - node[0]) < 15:
                print("Mở trò chơi mới!")  # Ở đây bạn có thể gọi một game mới
                break

        pygame.display.flip()

    pygame.quit()
