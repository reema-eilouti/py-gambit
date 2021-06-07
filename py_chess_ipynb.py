import chess
import chess.svg
from IPython.display import SVG
import chess.polyglot
import os


pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]

board = chess.Board()
SVG(chess.svg.board(board = board, size = 400))

def evaluate_board():
    
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
            
    if board.is_stalemate():
        return 0

    if board.is_insufficient_material():
        return 0
    
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    
    material = 100*(wp-bp) + 320*(wn-bn) + 330*(wb-bb) + 500*(wr-br) + 900*(wq-bq)

    
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])


    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])


    bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])

    
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])


    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])


    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])
    

    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq

    if board.turn:
        return eval
    else:
        return -eval

def alphabeta( alpha, beta, depthleft ):

    bestscore = -9999

    if( depthleft == 0 ):
        return quiesce( alpha, beta )

    for move in board.legal_moves:
        board.push(move)   
        score = -alphabeta( -beta, -alpha, depthleft - 1 )
        board.pop()

        if( score >= beta ):
            return score

        if( score > bestscore ):
            bestscore = score
            
        if( score > alpha ):
            alpha = score 

    return bestscore

def quiesce( alpha, beta ):

    stand_pat = evaluate_board()

    if( stand_pat >= beta ):
        return beta

    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)        
            score = -quiesce( -beta, -alpha )
            board.pop()

            if( score >= beta ):
                return beta
                
            if( score > alpha ):
                alpha = score  
    return alpha

def selectmove(depth):
    try:
        move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(board).move()
        movehistory.append(move)
        return move

    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000

        for move in board.legal_moves:
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth-1)

            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move

            if boardValue > alpha:
                alpha = boardValue

            board.pop()

        movehistory.append(bestMove)
        
        return bestMove

def checking(board):

    if board.is_checkmate():
        
        if board.turn:
            return "Black won"
        else:
            return "White won"
            
    if board.is_stalemate():
        return "Draw"

    if board.is_insufficient_material():
        return "Draw"
        
    return "Continue"

""" User vs. Bot MODE"""
movehistory = []
board = chess.Board()
for seq in range(2):

    player1 = input('Your move :')
    board.push_san(player1)
    print("PLayer move ", player1)
    bot = selectmove(3)
    board.push(bot)
    print("Bot move: ", bot)


SVG(chess.svg.board(board=board,size=400))


""" Bot vs. Bot MODE"""
movehistory =[]
board = chess.Board()
move = 'd2d4'
board.push_san(move)
for seq in range(2):
    
    bot1= selectmove(1)
    board.push(bot1)
    print("Bot 1 move: ", bot1)
    bot2 = selectmove(3)
    board.push(bot2)
    print("Bot 2 move: ", bot2)


SVG(chess.svg.board(board=board,size=400))

def game_state(check):
    if check == "Continue":

        print(board)
        print(board.result())
        
    elif check != "Continue":

        print(board)
        print("Game over")
        print(checking(board))
        
        return "break"


def hints_for_attack():
    """ given a square, gets possible attack moves of a piece"""

    board = chess.Board()

    square_name = input("Enter square name: ").lower()
    
    square_number = chess.SQUARE_NAMES.index(square_name)

    squares = board.attacks(square_number)

    return chess.svg.board(board, squares=squares, size=350)



""" User vs. User MODE"""

movehistory_white = []
movehistory_black = []
board = chess.Board()
player_no = 'Player #1'

while True:

    move = input(f'{player_no} move: ')

    if move == 'h':

        hint = input('Would you like to know if a piece is under attack(tt) or attackers of your piece(att)?')

        if hint == 'tt':

            print(is_piece_under_attack())

        elif hint == 'att':
            
            print(attackers())

    else:
        board.push_san(move)

        print(f"{player_no} move ", move)

        check = checking(board) 

        game_state(check) 

        if player_no == "Player #1":
            player_no = "Player #2"
        else:
            player_no = "Player #1"

        if check != "Continue":
            break
     
  
    


SVG(chess.svg.board(board=board,size=400))



def is_piece_under_attack():
    """At a certain point player might want to know a piece of his is under attack by oppenent, 
    the user shall enter square name, then function would get the piece index and the color piece, 
    uses built-in method (is_under_attack) to check if any of his pieces is in danger and returns a boolean"""
    str_is_under_attack = ''
  
    square = input('Enter square 1111').lower()
    
    square_number = chess.SQUARE_NAMES.index(square)
  
    square_color = board.color_at(square_number)
   
    is_under_attack = board.is_attacked_by(not square_color, square_number)

    print(is_under_attack)

    if is_under_attack == True:
        str_is_under_attack = f'{square} is attacked!! Watch out!!!!'

    else:
        str_is_under_attack = f'{square} is safe! :)'

    return str_is_under_attack


def attackers():
    """At a certain point a player might want to know opponent's pieces that can attack of a piece of his, 
    the user shall enter square name, then function would get the piece index and the color piece, 
    uses built-in method (attackers) and returns a sqaure list"""
   
    square = input('Enter square').lower()

    square_number = chess.SQUARE_NAMES.index(square)

    square_color = board.color_at(square_number)

    attackers_list = board.attackers(not square_color, square_number)
    
    return attackers_list
  
