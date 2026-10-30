import pygame

board = []


def get_piece(x, y):
    for p in board:
        if p.x == x and p.y == y and p.alive:
            return p
    return None


class Piece:
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def show_food(self, screen):
        for p in board:
            if self.can_eat(p):
                pygame.draw.rect(
                    screen, "red", pygame.Rect(p.x * 75 + 5, p.y * 75 + 5, 65, 65), 3
                )

    def show_moves(self, screen):
        for y in range(8):
            for x in range(8):
                if self.valid_move(x, y):
                    pygame.draw.rect(
                        screen, "black", pygame.Rect(x * 75 + 5, y * 75 + 5, 65, 65), 3
                    )


class Pawn(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        if self.x != x:
            return False

        if self.color == "white":
            if get_piece(self.x, self.y + 1) is not None:
                return False
            if self.y == 1 and y == 3:
                if get_piece(self.x, 3) is not None:
                    return False
                return True
            elif y == self.y + 1:
                return True
            else:
                return False

        if self.color == "black":
            if get_piece(self.x, self.y - 1) is not None:
                return False
            if self.y == 6 and y == 4:
                if get_piece(self.x, 4) is not None:
                    return False
                return True
            elif y == self.y - 1:
                return True
            else:
                return False

    def can_eat(self, p):
        if self.color == "black":
            if (
                (self.x + 1) == p.x
                and (self.y - 1) == p.y
                and p != None
                and p.color == "white"
                and p.alive
            ):
                return True
            if (
                (self.x - 1) == p.x
                and (self.y - 1) == p.y
                and p != None
                and p.color == "white"
                and p.alive
            ):
                return True
        else:
            if (
                (self.x + 1) == p.x
                and (self.y + 1) == p.y
                and p != None
                and p.color == "black"
                and p.alive
            ):
                return True
            if (
                (self.x - 1) == p.x
                and (self.y + 1) == p.y
                and p != None
                and p.color == "black"
                and p.alive
            ):
                return True
        return False


class Bishop(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        if abs(self.x - x) != abs(self.y - y):
            return False

        target_piece = get_piece(x, y)
        if target_piece is not None:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True

    def can_eat(self, p):
        x, y = p.x, p.y
        if abs(self.x - x) != abs(self.y - y):
            return False

        target = get_piece(p.x, p.y)
        if target is not None and target.color == self.color:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True


class Knight(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        target = get_piece(x, y)
        if target != None:
            return False
        if x == self.x + 2 and y == self.y + 1:
            return True
        elif x == self.x + 1 and y == self.y + 2:
            return True
        elif x == self.x - 2 and y == self.y - 1:
            return True
        elif x == self.x - 1 and y == self.y - 2:
            return True

        elif x == self.x + 2 and y == self.y - 1:
            return True
        elif x == self.x + 1 and y == self.y - 2:
            return True
        elif x == self.x - 2 and y == self.y + 1:
            return True
        elif x == self.x - 1 and y == self.y + 2:
            return True

        else:
            return False

    def can_eat(self, p):
        x, y = p.x, p.y
        target = get_piece(x, y)
        if target == None or target.color == self.color:
            return False
        if x == self.x + 2 and y == self.y + 1:
            return True
        elif x == self.x + 1 and y == self.y + 2:
            return True
        elif x == self.x - 2 and y == self.y - 1:
            return True
        elif x == self.x - 1 and y == self.y - 2:
            return True

        elif x == self.x + 2 and y == self.y - 1:
            return True
        elif x == self.x + 1 and y == self.y - 2:
            return True
        elif x == self.x - 2 and y == self.y + 1:
            return True
        elif x == self.x - 1 and y == self.y + 2:
            return True

        else:
            return False


class Rook(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        if (self.x == x and self.y == y) or (self.x != x and self.y != y):
            return False

        target_piece = get_piece(x, y)
        if target_piece is not None:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True

    def can_eat(self, p):
        x, y = p.x, p.y
        if (self.x == x and self.y == y) or (self.x != x and self.y != y):
            return False

        target = get_piece(p.x, p.y)
        if target is not None and target.color == self.color:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True


class Queen(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        if (abs(self.x - x) != abs(self.y - y)) and (
            (self.x == x and self.y == y) or (self.x != x and self.y != y)
        ):
            return False

        target_piece = get_piece(x, y)
        if target_piece is not None:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True

    def can_eat(self, p):
        x, y = p.x, p.y
        if (abs(self.x - x) != abs(self.y - y)) and (
            (self.x == x and self.y == y) or (self.x != x and self.y != y)
        ):
            return False

        target = get_piece(p.x, p.y)
        if target is not None and target.color == self.color:
            return False

        dir_x = 0 if x == self.x else (1 if x > self.x else -1)
        dir_y = 0 if y == self.y else (1 if y > self.y else -1)

        curr_x = self.x
        curr_y = self.y

        while (curr_x, curr_y) != (x, y):
            for p in board:
                if p is not self and p.alive and p.x == curr_x and p.y == curr_y:
                    return False
            curr_y += dir_y
            curr_x += dir_x

        return True


class King(Piece):
    alive = True

    def __init__(self, x, y, color, texture):
        self.x = x
        self.y = y
        self.color = color
        self.texture = texture

    def valid_move(self, x, y):
        target = get_piece(x, y)
        if target is not None or target is self:
            return False
        if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
            return True

    def can_eat(self, p):
        if abs(self.x - p.x) <= 1 and abs(self.y - p.y) <= 1:
            target = get_piece(p.x, p.y)
            if target is not None or target is self:
                if target.color != self.color:
                    return True
                return False
            return True
