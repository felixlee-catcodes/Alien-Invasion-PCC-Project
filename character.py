import pygame

class Character:
    """A class to manage and draw a character."""

    def __init__(self, ai_game):
        """Initialize the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character and get its rect
        self.image = pygame.image.load('images/monster_img.bmp')
        self.resized_image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.resized_image.get_rect()

        # Start the new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.resized_image, self.rect) 