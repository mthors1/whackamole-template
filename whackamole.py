import pygame, random

mole_image = pygame.image.load("mole.png")
screen = pygame.display.set_mode((640, 512))
clock = pygame.time.Clock()

def draw_grid():
   for x in range(1, 16): # horizontal - 16 rows
       pygame.draw.line(
           screen,
           (216, 230, 202),
           (0, x*32),
           (640, x*32),
           1
       )
   for y in range(1, 20): # vertical - 20 columns
       pygame.draw.line(
           screen,
           (216, 230, 202),
           (y*32, 0),
           (y*32, 512),
           1
       )
def clear_grid():
    screen.fill((157, 186, 127))
    draw_grid()

def initialize_grid():
    return [["-" for y in range(20)] for x in range(16)]

def print_grid(grid):
    for row in grid: # row: ["-", "-", "-"]
        for col in row:
            print(col, end=" ")
        print()

def mark_square(grid, row, col):
    grid[row][col] = "m"

def unmark_square(grid, row, col):
    grid[row][col] = "-"

def print_mole_random(grid):
    row = random.randrange(0, 16)
    col = random.randrange(0, 20)
    screen.blit(mole_image, mole_image.get_rect(topleft=((32 * col), (32 * row))))
    mark_square(grid, row, col)

def check_for_mole(grid, row, col):
    return grid[row][col] == "m"

def main():
    try:
        grid = initialize_grid()
        pygame.init()
        clear_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mark_square(grid, 0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // 32
                    row = y // 32
                    if 0 <= row < 16 and 0 <= col < 20:
                        if check_for_mole(grid, row, col):
                            unmark_square(grid, row, col)
                            clear_grid()
                            print_mole_random(grid)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
