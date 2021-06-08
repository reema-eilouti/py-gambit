import chess
import chess.svg
import chess.polyglot



# Below are the two-dimentional arrays to guid the bot to choosing a proper move for each chess piece.

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


# To view the chess board.
# board = chess.Board()
# print(board)

movehistory = []

# Below are four functions used by the bot to evaluate and choose a proper move.
def evaluate_board(board):
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


def alphabeta(alpha, beta, depthleft, board):

    bestscore = -9999

    if( depthleft == 0 ):
        return quiesce( alpha, beta, board )

    for move in board.legal_moves:
        board.push(move)   
        score = -alphabeta( -beta, -alpha, depthleft - 1 , board)
        board.pop()

        if( score >= beta ):
            return score

        if( score > bestscore ):
            bestscore = score
            
        if( score > alpha ):
            alpha = score 

    return bestscore


def quiesce(alpha, beta, board):

    stand_pat = evaluate_board(board)

    if( stand_pat >= beta ):
        return beta

    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)        
            score = -quiesce( -beta, -alpha, board )
            board.pop()

            if( score >= beta ):
                return beta
                
            if( score > alpha ):
                alpha = score  
    return alpha


def selectmove(depth, board):
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
            boardValue = -alphabeta(-beta, -alpha, depth-1, board)

            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move

            if boardValue > alpha:
                alpha = boardValue

            board.pop()

        movehistory.append(bestMove)
        
        return bestMove


# Functions below are used to add extra properties for the user side of the game. 
def checking(board):
    """A function to check whether the game has stopping condition or not."""

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

def game_state(check, board):
    """A function to check whether the game has stopping condition or not."""

    if check == "Continue":

        print(board, '\n')
        
    elif check != "Continue":

        print(board, '\n')
        print(checking(board))
        print("Game Over.")       
        
        return "break"

def hints_for_attack():
    """ given a square, gets possible attack moves of a piece"""

    board = chess.Board()

    square_name = input("Enter square name: ").lower()
    
    square_number = chess.SQUARE_NAMES.index(square_name)

    squares = board.attacks(square_number)

    return chess.svg.board(board, squares=squares, size=350)

def is_piece_under_attack(board):
    """At a certain point player might want to know a piece of his is under attack by oppenent, 
    the user shall enter square name, then function would get the piece index and the color piece, 
    uses built-in method (is_under_attack) to check if any of his pieces is in danger and returns a boolean"""
    
  
    square = input('Enter square to test: ').lower()
    
    square_number = chess.SQUARE_NAMES.index(square)
  
    square_color = board.color_at(square_number)
   
    is_under_attack = board.is_attacked_by(not square_color, square_number)


    if is_under_attack == True:
        print(f'{square} is attacked!! Watch out!!!!')

        attackers_answer = input("Do you want to know which pieces are attacking you? (y/n) ")

        if attackers_answer == 'y':
            print(attackers(square, board))
         
    else:
        print(f'{square} is safe! :)')

def attackers(square, board):
    """At a certain point a player might want to know opponent's pieces that can attack of a piece of his, 
    the user shall enter square name, then function would get the piece index and the color piece, 
    uses built-in method (attackers) and returns a sqaure list"""

    square_number = chess.SQUARE_NAMES.index(square)

    square_color = board.color_at(square_number)

    attackers_list = board.attackers(not square_color, square_number)
    
    return attackers_list

def test_move(move, board):

    if move == 'hint':
        return True
    
    try:
        move_not_str = chess.Move.from_uci(move)

        if move_not_str in board.legal_moves:
            return True
        else:
            return False
    except:
        return False


# Functions below are to run the game in different modes.
def bot_vs_bot():
    """ Bot vs. Bot Mode for testing."""

    board = chess.Board()

    move = 'd2d4'

    board.push_san(move)

    for seq in range(2):
        
        bot1 = selectmove(3)

        board.push(bot1)

        print("Bot 1 move: ", bot1)

        bot2 = selectmove(3)

        board.push(bot2)

        print("Bot 2 move: ", bot2)

def user_vs_bot():
    """ User vs. Bot Mode."""
 
    board = chess.Board()

    first = input("Would you like to start? (y/n) ")

    if first == 'y':
        player_no = 'Player'
    else:
        player_no = 'Bot'

    mistakes = 0

    while True:

        if player_no == 'Player':

            print("If you want a hint on attacking input 'hint'.")

            move = input(f'{player_no} move: ')

            test = test_move(move, board)

            if test == True:

                if move == 'hint':

                    is_piece_under_attack(board)  

                else: 

                    board.push_san(move)

                    check = checking(board) 

                    game_state(check, board) 

                    player_no = "Bot"

                    if check != "Continue":
                        break

            else:
                mistakes += 1
                print("You have entered an invalid move, try again.")

                if mistakes >= 2:
                    legal_moves = []

                    for move in board.legal_moves:
                        legal_moves.append(str(move))

                    print("Valid moves: ", legal_moves)   

        elif player_no == 'Bot':

            bot_move = selectmove(3, board)

            board.push(bot_move)

            print("Bot move: ", bot_move)

            print(board, '\n')

            player_no = "Player"

def user_vs_user():
    """ User vs. User Mode."""

    board = chess.Board()

    player_no = 'Player #1'

    mistakes = 0

    while True:

        print("If you want a hint on attacking input 'hint'.")

        move = input(f'{player_no} move: ')

        test = test_move(move, board)

        if test == True:

            if move == 'hint':

                is_piece_under_attack(board)            

            else:
                board.push_san(move)

                check = checking(board) 

                game_state(check, board) 

                if player_no == "Player #1":
                    player_no = "Player #2"
                else:
                    player_no = "Player #1"

                if check != "Continue":
                    break

        else:
            mistakes += 1
            print("You have entered an invalid move, try again.")

            if mistakes >= 2:
                legal_moves = []

                for move in board.legal_moves:
                    legal_moves.append(str(move))

                print("Valid moves: ", legal_moves)


# Main function to run whole game.
def game():
    
    print("Welcome to Py Gambit!")

    mode = input("Which mode would you like to play? Against computer(1) or another player(2)? ")

    if mode == '1':
        user_vs_bot()
    
    if mode == '2':
        user_vs_user()

game() 