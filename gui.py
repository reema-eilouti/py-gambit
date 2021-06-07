import chessboard
from tkinter import *
import tkinter as tk
import chess
from bot import bot_move

class GUI:
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor = "khaki"
    rows = 8
    columns = 8
    dim_square = 64

    def __init__(self, parent, chessboard,board):
        self.chessboard = chessboard
        self.parent = parent
        # /////////////////////////////////
        self.play_mode = 'single_player'
        self.counter = 0
        self.board = board
        self.posi1 = None
        self.posi2 = None
        # ////////////////////////////
        # Adding Top Menu
        self.menubar = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New Game", command=self.new_game)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        # Adding Frame
        self.btmfrm = tk.Frame(parent, height=64)
        self.info_label = tk.Label(self.btmfrm,
                                text="   White to Start the Game  ",
                                fg=self.color2)
        self.info_label.pack(side=tk.RIGHT, padx=8, pady=5)
        self.btmfrm.pack(fill="x", side=tk.BOTTOM)

        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = tk.Canvas(parent, width=canvas_width,
                               height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.square_clicked)

    def new_game(self):
        # print('ooo')
        # main_frame = Frame(self.parent,height=64)
        # main_frame.tkraise()
        self.chessboard.show(chessboard.START_PATTERN)
        self.draw_board()
        self.draw_pieces()
        self.info_label.config(text="   White to Start the Game  ", fg='red')

    def square_clicked(self, event=None,posi=None):
        if not posi:
            col_size = row_size = self.dim_square
            selected_column = int(event.x / col_size)
            selected_row = 7 - int(event.y / row_size)
        pos = posi or self.chessboard.alpha_notation((selected_row, selected_column))
        try:
            piece = self.chessboard[pos]
        except:
            pass
        if self.selected_piece:
            # //////////////////////////
            if self.play_mode == 'single_player' and self.counter == 2:
                self.counter = 0
            # //////////////////////////
            self.shift(self.selected_piece[1], pos)
            self.selected_piece = None
            self.focused = None
            self.pieces = {}
            self.draw_board()
            self.draw_pieces()
        self.focus(pos)
        self.draw_board()
        #////////////////////////////////////
        if self.chessboard.player_turn == "black" and self.play_mode == 'single_player':
            self.bot()
       #////////////////////////////////// 

    def shift(self, p1, p2):
        piece = self.chessboard[p1]
        try:
            dest_piece = self.chessboard[p2]
        except:
            dest_piece = None
        if dest_piece is None or dest_piece.color != piece.color:
            try:
                self.chessboard.shift(p1, p2)
            except chessboard.ChessError as error:
                self.info_label["text"] = error.__class__.__name__
            else:
                turn = ('white' if piece.color == 'black' else 'black')
                self.info_label[
                    "text"] = '' + piece.color.capitalize() + "  :  " + p1 + p2 + '    ' + turn.capitalize() + '\'s turn'
                # ////////////////////////////
                # if self.chessboard.player_turn == "white":
                if self.chessboard.player_turn == 'black':
                    move = p1[0].lower()
                    move += p1[1]
                    move += p2[0].lower()
                    move += p2[1]
                    self.board.push_san(move)
                # ///////////////////////////

    def focus(self, pos):
        try:
            piece = self.chessboard[pos]
        except:
            piece = None
        if piece is not None and (piece.color == self.chessboard.player_turn):
            self.selected_piece = (self.chessboard[pos], pos)
            self.focused = list(map(self.chessboard.num_notation,
                               (self.chessboard[pos].moves_available(pos))))

    def draw_board(self):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square)
                y1 = ((7 - row) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if (self.focused is not None and (row, col) in self.focused):
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=self.highlightcolor,
                                                 tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,
                                                 tags="area")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.pieces[name] = (self.pieces[name][0], self.pieces[name][1])
            x0 = (self.pieces[name][1] * self.dim_square) + int(
                self.dim_square / 2)
            y0 = ((7 - self.pieces[name][0]) * self.dim_square) + int(
                self.dim_square / 2)
            self.canvas.coords(name, x0, y0)
        self.canvas.tag_raise("occupied")
        self.canvas.tag_lower("area")

    def draw_pieces(self):
        self.canvas.delete("occupied")
        for coord, piece in self.chessboard.items():
            x, y = self.chessboard.num_notation(coord)
            if piece is not None:
                filename = "pieces_image/%s%s.png" % (
                piece.shortname.lower(), piece.color)
                piecename = "%s%s%s" % (piece.shortname, x, y)
                if filename not in self.images:
                    self.images[filename] = tk.PhotoImage(file=filename)
                self.canvas.create_image(0, 0, image=self.images[filename],
                                         tags=(piecename, "occupied"),
                                         anchor="c")
                x0 = (y * self.dim_square) + int(self.dim_square / 2)
                y0 = ((7 - x) * self.dim_square) + int(self.dim_square / 2)
                self.canvas.coords(piecename, x0, y0)
    # ///////////////////////////////////////////
    def bot(self):
        if self.counter == 0:
            move = bot_move(self.board,1)
            move = str(move)
            self.board.push_san(move)
            self.posi1 = move[0].upper()
            self.posi1 += move[1] 
            self.posi2 = move[2].upper()
            self.posi2 += move[3] 
            self.counter += 1
            self.square_clicked(None,self.posi1)
        elif self.counter == 1:
            self.counter += 1
            self.square_clicked(None,self.posi2)
    #//////////////////////////////////////////////////// 


def main(chessboard):

    board = chess.Board()
    root = tk.Tk()
    root.title("Chess")

    gui = GUI(root, chessboard,board)
    gui.draw_board()
    gui.draw_pieces()


    root.mainloop()
    
    


if __name__ == "__main__":
    game = chessboard.Board()
    # main(game)

    main_page = Tk()
    main_page.title("main page")
    main_page.geometry('400x300')

    f1 = Frame(main_page)
    f1.grid(row=0, column=0, sticky='news')
    def clicked():
        main_page.destroy()
        main(game)
    btn = Button(main_page, text="Click Me", command=clicked)
    btn.grid(column=1, row=0)

    main_page.mainloop()


    
