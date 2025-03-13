import pygame
import os

def load_piece_images(square_size):
    """Load chess piece images from the assets folder and resize them."""
    piece_images = {}
    piece_names = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    colors = ["white", "black"]

    for color in colors:
        for piece in piece_names:
            filename = f"assets/{color}-{piece}.png"  # Matches Piece.image_name()
            key = f"{color}-{piece}.png"  # Use the exact same format as image_name()
            if os.path.exists(filename):
                image = pygame.image.load(filename)
                piece_images[key] = pygame.transform.scale(image, (square_size, square_size))
            else:
                print(f"Missing image: {filename}")
    return piece_images