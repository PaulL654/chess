from src.pieces import *

turn = "white"

score_white = 0
score_black = 0

black_bishop = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\bb.png"), (75, 75)
)
black_king = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\bk.png"), (75, 75)
)
black_knight = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\bn.png"), (75, 75)
)
black_pawn = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\bp.png"), (75, 75)
)
black_queen = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\bq.png"), (75, 75)
)
black_rook = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\br.png"), (75, 75)
)
white_bishop = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wb.png"), (75, 75)
)
white_king = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wk.png"), (75, 75)
)
white_knight = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wn.png"), (75, 75)
)
white_pawn = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wp.png"), (75, 75)
)
white_queen = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wq.png"), (75, 75)
)
white_rook = pygame.transform.scale(
    pygame.image.load(r"assets\pieces\wr.png"), (75, 75)
)


def init_pieces():
    global board
    for i in range(8):
        board.append(Pawn(i, 1, "white", white_pawn))
        board.append(Pawn(i, 6, "black", black_pawn))

    board.append(Rook(0, 0, "white", white_rook))
    board.append(Rook(7, 0, "white", white_rook))

    board.append(Knight(1, 0, "white", white_knight))
    board.append(Knight(6, 0, "white", white_knight))

    board.append(Bishop(2, 0, "white", white_bishop))
    board.append(Bishop(5, 0, "white", white_bishop))

    board.append(Queen(4, 0, "white", white_queen))
    board.append(King(3, 0, "white", white_king))

    # ================================

    board.append(Rook(0, 7, "black", black_rook))
    board.append(Rook(7, 7, "black", black_rook))

    board.append(Knight(1, 7, "black", black_knight))
    board.append(Knight(6, 7, "black", black_knight))

    board.append(Bishop(2, 7, "black", black_bishop))
    board.append(Bishop(5, 7, "black", black_bishop))

    board.append(Queen(3, 7, "black", black_queen))
    board.append(King(4, 7, "black", black_king))


def draw_board(screen):
    screen.fill(pygame.Color(55, 107, 48))
    screen.fill(pygame.Color(28, 99, 33), (0, 0, 600, 600))
    color = "white"
    step = 0
    side = 1
    for y in range(0, 600, 75):
        step = 0
        side += 1
        for x in range(0, 600, 75):
            if step % 2 == side % 2:
                pygame.draw.rect(screen, color, pygame.Rect(x, y, 75, 75), 0)
            step += 1


def draw_pieces(screen, selected_piece=None, drag_offset=None):
    for piece in board:
        if piece is not selected_piece and piece.alive:
            screen.blit(piece.texture, (piece.x * 75, piece.y * 75))

    if selected_piece is not None and drag_offset is not None:
        position = pygame.Vector2(pygame.mouse.get_pos()) + drag_offset
        screen.blit(selected_piece.texture, position)


def switch_turn():
    global turn
    if turn == "white":
        turn = "black"
    else:
        turn = "white"


def show_eaten(screen):
    offset_x_black = 0
    offset_x_white = 0
    offset_y_black = 0
    offset_y_white = 0
    for e in board:
        if not e.alive:
            if e.color == "white":
                if type(e) == Pawn:
                    screen.blit(
                        pygame.transform.scale(white_pawn, (30, 30)),
                        (600 + offset_x_black, 560 + offset_y_black),
                    )
                elif type(e) == Knight:
                    screen.blit(
                        pygame.transform.scale(white_knight, (30, 30)),
                        (600 + offset_x_black, 560 + offset_y_black),
                    )
                elif type(e) == Bishop:
                    screen.blit(
                        pygame.transform.scale(white_bishop, (30, 30)),
                        (600 + offset_x_black, 560 + offset_y_black),
                    )
                elif type(e) == Rook:
                    screen.blit(
                        pygame.transform.scale(white_rook, (30, 30)),
                        (600 + offset_x_black, 560 + offset_y_black),
                    )
                elif type(e) == Queen:
                    screen.blit(
                        pygame.transform.scale(white_queen, (30, 30)),
                        (600 + offset_x_black, 560 + offset_y_black),
                    )
                offset_x_black += 20
                if offset_x_black >= 120:
                    offset_x_black = 0
                    offset_y_black -= 30
            else:
                if type(e) == Pawn:
                    screen.blit(
                        pygame.transform.scale(black_pawn, (30, 30)),
                        (600 + offset_x_white, 10 + offset_y_white),
                    )
                elif type(e) == Knight:
                    screen.blit(
                        pygame.transform.scale(black_knight, (30, 30)),
                        (600 + offset_x_white, 10 + offset_y_white),
                    )
                elif type(e) == Bishop:
                    screen.blit(
                        pygame.transform.scale(black_bishop, (30, 30)),
                        (600 + offset_x_white, 10 + offset_y_white),
                    )
                elif type(e) == Rook:
                    screen.blit(
                        pygame.transform.scale(black_rook, (30, 30)),
                        (600 + offset_x_white, 10 + offset_y_white),
                    )
                elif type(e) == Queen:
                    screen.blit(
                        pygame.transform.scale(black_queen, (30, 30)),
                        (600 + offset_x_white, 10 + offset_y_white),
                    )
                offset_x_white += 20
                if offset_x_white >= 120:
                    offset_x_white = 0
                    offset_y_white += 30


def update_score(target):
    global score_black
    global score_white

    if target.color == "white":
        if type(target) == Pawn:
            score_white += 1
        elif type(target) == Knight:
            score_white += 3
        elif type(target) == Bishop:
            score_white += 3
        elif type(target) == Rook:
            score_white += 5
        elif type(target) == Queen:
            score_white += 9

    if target.color == "black":
        if type(target) == Pawn:
            score_black += 1
        elif type(target) == Knight:
            score_black += 3
        elif type(target) == Bishop:
            score_black += 3
        elif type(target) == Rook:
            score_black += 5
        elif type(target) == Queen:
            score_black += 9


def show_score(screen, font):
    text1 = font.render(f"Score: {score_black}", True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (675, 150)
    screen.blit(text1, textRect1)

    text1 = font.render(f"Score: {score_white}", True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (675, 450)
    screen.blit(text1, textRect1)


def can_play(piece):
    return piece.color == turn


def check_game_over(screen, font):
    winner = "White"
    for e in board:
        if type(e) == King and not e.alive:
            if turn == "white":
                winner = "Black"
            text1 = font.render(f"{winner} Win !", True, (200, 200, 200))
            textRect1 = text1.get_rect()
            textRect1.center = (300, 300)
            screen.fill(pygame.Color(0, 0, 0), (0, 265, 750, 60))
            screen.blit(text1, textRect1)
            return True
    return False


def show_turn(screen, font):
    text1 = font.render(f"turn: {turn}", True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (675, 300)
    screen.blit(text1, textRect1)
