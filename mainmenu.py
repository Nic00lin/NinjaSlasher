import pygame
import game
class MainMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font('data/fonts/Roboto.ttf', 32)
        self.main_menu_font = pygame.font.Font('data/fonts/Roboto.ttf', 40)
        self.menu_items = ["Start Game", "Quit"]
        self.selected_item = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    if self.selected_item == 0:
                        # Start Game
                        return True
                    elif self.selected_item == 1:
                        pygame.quit()

        return False

    def draw(self, title, color):

        image = pygame.image.load('data/images/menu.jpg')
        self.game.screen.blit(image,(0,0))
        title_text = self.main_menu_font.render(title, True, color)
        title_x = self.game.screen.get_width() // 8 - title_text.get_width() // 2
        self.game.display.blit(title_text, (title_x, 50))

        for i, item in enumerate(self.menu_items):
            text_color = (255, 255, 255) if i == self.selected_item else (150, 150, 150)
            item_text = self.font.render(item, True, text_color)
            item_x = self.game.screen.get_width() // 8 - item_text.get_width() // 2
            self.game.display.blit(item_text, (item_x, 100 + i *50))

        self.game.screen.blit(pygame.transform.scale(self.game.display, self.game.screen.get_size()), (0, 0))
        pygame.display.update()

    def run(self, title, color):
        while True:
            if self.handle_events():
                break
            self.draw(title, color)
            self.game.clock.tick(60)

