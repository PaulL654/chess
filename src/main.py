import pygame
from src.pieces import *
from src.game_logic import *

pygame.init()
screen = pygame.display.set_mode((750, 600))
clock = pygame.time.Clock()
pygame.font.init()
running = True
selected_piece = None
drag_offset = None

init_pieces()

while running:
    game_on = check_game_over(screen, pygame.font.SysFont("freesanbold.ttf", 60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_on:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for piece in board:
                        piece_rect = pygame.Rect(piece.x * 75, piece.y * 75, 75, 75)
                        if piece_rect.collidepoint(event.pos) and piece.alive:
                            selected_piece = piece
                            drag_offset = (
                                pygame.Vector2(piece.x * 75, piece.y * 75) - event.pos
                            )
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and selected_piece is not None:
                    target_x = event.pos[0] // 75
                    target_y = event.pos[1] // 75
                    if 0 <= target_x < 8 and 0 <= target_y < 8:
                        target_piece = next(
                            (
                                piece
                                for piece in board
                                if piece.x == target_x
                                and piece.y == target_y
                                and piece.alive
                            ),
                            None,
                        )
                        if can_play(selected_piece):
                            if (
                                target_piece is None or not target_piece.alive
                            ) and selected_piece.valid_move(target_x, target_y):
                                selected_piece.x = target_x
                                selected_piece.y = target_y
                                switch_turn()
                            elif (
                                target_piece is not None
                                and selected_piece.can_eat(target_piece)
                                and target_piece.alive
                            ):
                                selected_piece.x = target_x
                                selected_piece.y = target_y
                                target_piece.alive = False
                                update_score(target_piece)
                                switch_turn()
                    selected_piece = None
                    drag_offset = None

            draw_board(screen)

            show_turn(screen, pygame.font.SysFont("freesanbold.ttf", 35))
            show_score(screen, pygame.font.SysFont("freesanbold.ttf", 25))
            show_eaten(screen)
            if selected_piece is not None and selected_piece.alive:
                selected_piece.show_food(screen)
                selected_piece.show_moves(screen)

                pygame.draw.rect(
                    screen,
                    "orange",
                    pygame.Rect(
                        selected_piece.x * 75 + 5, selected_piece.y * 75 + 5, 65, 65
                    ),
                    3,
                )

            draw_pieces(screen, selected_piece, drag_offset)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
