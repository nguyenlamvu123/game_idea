from coordinate import *

running = True
rolling = True
current_dice = roll_dice()
saved_dice = None  # Biến lưu kết quả khi xúc xắc dừng


if __name__ == '__main__':
    while running:
        screen.fill(WHITE)  # Xóa màn hình

        # Vẽ nhân vật
        pygame.draw.rect(screen, BLUE, (*player_pos, size, size))

        # Vẽ các nút
        for node in nodes:
            pygame.draw.circle(screen, RED, node, size//2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                rolling = not rolling
                if not rolling:  # Nếu dừng, lưu kết quả
                    saved_dice = current_dice + 1
                    move(saved_dice)

                    # Kiểm tra nếu nhân vật đi vào một nút
                    for node in nodes:
                        if player_pos[0] - node[0] == 0:
                            print("Mở trò chơi mới!")  # Ở đây bạn có thể gọi một game mới
                            break

        # Xúc xắc xoay liên tục
        if rolling:
            current_dice = roll_dice()

        screen.blit(dice_images[current_dice], (WIDTH-70, 0))
        pygame.display.flip()
        clock.tick(10)  # Giữ tốc độ xoay hợp lý

    pygame.quit()
