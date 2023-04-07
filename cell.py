from graphics import Point, Line, Window

class Cell():
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)))
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "white")  
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)))
        else:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "white")
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)))
        else:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "white")
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)))
        else:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "white")

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if not undo:
            color = "red"
        x_start = self.x1 + (self.x2 - self.x1) // 2
        y_start = self.y1 + (self.y2 - self.y1) // 2
        x_end = to_cell.x1 + (to_cell.x2 - to_cell.x1) // 2
        y_end = to_cell.y1 + (to_cell.y2 - to_cell.y1) // 2
        self.win.draw_line(Line(Point(x_start, y_start), Point(x_end, y_end)))
            