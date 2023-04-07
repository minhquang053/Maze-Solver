from graphics import Window, Line, Point, Cell
import unittest
from maze import Maze

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(1,1), Point(100,100)), "black")
    cell = Cell(x1=20,x2=40,y1=30,y2=50, win=win, 
                has_left_wall=True, 
                has_right_wall=True, 
                has_top_wall=True,
                has_bottom_wall=True)
    cell.draw()
    win.wait_for_close()

main()

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
    