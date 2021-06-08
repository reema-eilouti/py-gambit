import chessboard
from tkinter import *
import tkinter as tk
import chess
from bot import bot_move, checking
import tkinter.messagebox

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

    def __init__(self, parent, chessboard,board,root,player_mode = "single_player"):
        self.chessboard = chessboard
        self.parent = parent
        # /////////////////////////////////
        self.play_mode = player_mode
        self.counter = 0
        self.board = board
        self.posi1 = None
        self.posi2 = None
        self.root = root
        # ////////////////////////////
        # Adding Top Menu
        # self.menubar = tk.Menu(root)
        # self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.filemenu.add_command(label="New Game", command=self.new_game)
        # self.menubar.add_cascade(label="File", menu=self.filemenu)
        # self.root.config(menu=self.menubar)

        # Adding Frame
        self.btmfrm = tk.Frame(parent, height=64)
        self.info_label = tk.Label(self.btmfrm,text="   White to Start the Game  ",fg=self.color2)
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
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.board = chess.Board()
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
            # ///////////////////////////////////////////////
            check = checking(self.board)
            if check == 'White won' or check == "Black won":
                tkinter.messagebox.showinfo("winner",f"{check}")
                self.clicked_restart()
            # ////////////////////////////////////////////
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
                if self.chessboard.player_turn == 'black' and self.play_mode == "single_player":
                    move = p1[0].lower()
                    move += p1[1]
                    move += p2[0].lower()
                    move += p2[1]
                    self.board.push_san(move)
                if self.play_mode == "multi_player":
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

    def clicked_restart(self):
        self.new_game()

    def clicked_attack(self):
        pass

    #//////////////////////////////////////////////////// 


def main(chessboard):

    board = chess.Board()
    root = tk.Tk()
    root.title("Chess")
    root.geometry('250x600')
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    main_frame = Frame(root)
    main_frame.grid(row=0, column=0, sticky="nswe")
    chessframe = Frame(main_frame)
    chessframe.grid(row=0, column=0, sticky="nswe")
    game_option_frame = Frame(main_frame,background="bisque")
    game_option_frame.grid(row=0, column=1, sticky="nswe")
    player_option_frame = Frame(main_frame,background="bisque")
    player_option_frame.grid(row=0, column=3, sticky="nswe")

    def clicked_virual():
        pass

    def clicked_timer():
        pass

    def clicked_single():
        root.geometry('800x600')
        player_mode = "single_player"
        gui = GUI(chessframe, chessboard,board,root,player_mode)
        gui.draw_board()
        gui.draw_pieces()
        game_option_frame.destroy()
        lbl = Label(player_option_frame, text="                                                                                 ")
        lbl.grid(column=0, row=0)
        btn = Button(player_option_frame, text="restart game", command=gui.clicked_restart, bg="orange", fg="red",width=20,height=3)
        btn.grid(column=0, row=1)
        btn_2 = Button(player_option_frame, text="pieces under attack", command=gui.clicked_attack, bg="pink", fg="red",width=20,height=3)
        btn_2.grid(column=0, row=2)
        btn_3 = Button(player_option_frame, text="virual mouse", command=clicked_virual, bg="white", fg="red",width=20,height=3)
        btn_3.grid(column=0, row=3)

    def clicked_multi():
        root.geometry('800x600')
        player_mode = "multi_player"
        gui = GUI(chessframe, chessboard,board,root,player_mode)
        gui.draw_board()
        gui.draw_pieces()

        def clicked_draw():
            player = gui.chessboard.player_turn
            if player == 'white':
                winner = "black"
            else:
                winner = "white"
            tkinter.messagebox.showinfo("winner",f"the winner is {winner}")
            gui.clicked_restart()

        game_option_frame.destroy()
        lbl = Label(player_option_frame, text="                                                                                 ")
        lbl.grid(column=0, row=0)
        btn = Button(player_option_frame, text="draw", command=clicked_draw, bg="orange", fg="red",width=20,height=3)
        btn.grid(column=0, row=1)
        btn = Button(player_option_frame, text="show timer", command=clicked_timer, bg="orange", fg="red",width=20,height=3)
        btn.grid(column=0, row=2)
        btn_2 = Button(player_option_frame, text="pieces under attack", command=gui.clicked_attack, bg="pink", fg="red",width=20,height=3)
        btn_2.grid(column=0, row=3)
        btn_3 = Button(player_option_frame, text="virual mouse", command=clicked_virual, bg="white", fg="red",width=20,height=3)
        btn_3.grid(column=0, row=4)
    
    def clicked_rules():
        pass

    lbl = Label(game_option_frame, text="                                                                                 ")
    lbl.grid(column=0, row=0)
    btn = Button(game_option_frame, text="one player", command=clicked_single, bg="orange", fg="red",width=20,height=3)
    btn.grid(column=0, row=1)
    btn_2 = Button(game_option_frame, text="multi player", command=clicked_multi, bg="pink", fg="red",width=20,height=3)
    btn_2.grid(column=0, row=2)
    btn_3 = Button(game_option_frame, text="game rules", command=clicked_rules, bg="white", fg="red",width=20,height=3)
    btn_3.grid(column=0, row=3)
 
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    root.mainloop()
    
    


if __name__ == "__main__":
    game = chessboard.Board()
    main(game)



    
