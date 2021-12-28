import re
from day4data import test_called_nums, test_boards_str, boards_str, called_nums


# Classes
class BingoBoard():
    def __init__(self, board):
        if isinstance(board, list): self.board = board
        self.marks = [] # List of vals called already (row, col in matrix)
        self.adj_list = {}
        self.called_nums = []

    @property
    def bingo(self):
        '''
        Determines if board has bingo
        Bingo is 5 in a row horizontal or vertical
        '''
        if self._check_rows_for_bingo():
            return True
        elif self._check_cols_for_bingo():
            return True
        else: return False
        
    def _check_rows_for_bingo(self):
        for row in range(len(self.board)):
            called = 0
            for col in range(len(self.board[row])):
                if self.board[row][col] in self.called_nums:
                    #print(f'{self.board[row][col]} is in the called nums.')
                    called += 1
            if called == 5:
                return True
        return False

    def _check_cols_for_bingo(self):
        for col in range(len(self.board[0])):
            called = 0
            for row in range(len(self.board)):
                if self.board[row][col] in self.called_nums:
                    called += 1
            if called == 5:
                return True
        return False
    
    def sum_unmarked_vals(self):
        sum = 0
        for row in self.board:
            for col in row:
                if col not in self.called_nums:
                    sum += col
        return sum

    def mark_val(self):
        pass
    
    def get_val(self, pos):
        pass

    def get_space(self, val):
        pass

    # Didn't use
    def _build_adj_list(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                val = self.board[row][col]
                adjs = []
                if not row == 0:
                    up = self.board[row-1][col]
                    adjs.append(up)
                if not col == 0:
                    left = self.board[row][col-1]
                    adjs.append(left)
                if not row >= len(self.board)-1:
                    down = self.board[row+1][col]
                    adjs.append(down)
                if not col >= len(self.board[row])-1:
                    right = self.board[row][col+1]
                    adjs.append(right)
                self.adj_list[val] = adjs




# Helper functions
def format_board_data(board_str):
    # Roughly cut the multiline str into a list of board strings
    board_rough_list = board_str.split('\n\n')
    boards = []
    # Split each board into a list of rows
    for board in board_rough_list:
        new_board = []
        board = board.split('\n')
        # For each row in each board, strip whitespace
        # Change rows from str to list
        for row in board:
            row = row.strip()
            row = re.sub('  ', ' ', row)
            vals = row.split(' ')
            # Convert each value in the 2d matrix into int
            for i in range(len(vals)):
                vals[i] = int(vals[i])
            # Add the row list to the board
            new_board.append(vals)
        # Add the board to the board list
        boards.append(new_board)
    return boards

# Test driver code
def test(test_boards_str, test_called_nums):
    test_boards = format_board_data(test_boards_str)
    board_objs = []
    for board in test_boards:
        test_board = BingoBoard(board)
        board_objs.append(test_board)
    bingo = False
    for num in test_called_nums:
        if not bingo:
            for test_board in board_objs:
                test_board.called_nums.append(num)
                if test_board.bingo:
                    # print(f'Winning board: {test_board.board}')
                    unmarked_sum = test_board.sum_unmarked_vals()
                    last_num_called = test_board.called_nums[-1]
                    test_answer = unmarked_sum * last_num_called
                    # print(f'{unmarked_sum} x {last_num_called} = {test_answer}')
                    bingo = True
        else: break
    assert test_answer == 4512
    return test_answer

def test2(test_boards_str, test_called_nums):
    boards = format_board_data(test_boards_str)
    board_objs = []
    for board in boards:
        board = BingoBoard(board)
        board_objs.append(board)
    last_bingo = False
    for num in test_called_nums:
        print(f'Calling {num}!')
        if not last_bingo:
            for board in board_objs:
                board.called_nums.append(num)
                if board.bingo:
                    print(f'Bingo! Board: {board.board}')
                    if len(board_objs) > 1:
                        board_objs.remove(board)
                    else:
                        print(f'Last winning board: {board.board}')
                        unmarked_sum = board.sum_unmarked_vals()
                        last_num_called = board.called_nums[-1]
                        print(f'called: {board.called_nums}')
                        answer = unmarked_sum * last_num_called
                        print(f'{unmarked_sum} x {last_num_called} = {answer}')
                        last_bingo = True
        else: break
    print(answer)
    assert answer == 1924
    return answer

# Puzzle driver code
def part1(boards_str, called_nums):
    boards = format_board_data(boards_str)
    board_objs = []
    for board in boards:
        board = BingoBoard(board)
        board_objs.append(board)
    bingo = False
    for num in called_nums:
        if not bingo:
            for board in board_objs:
                board.called_nums.append(num)
                if board.bingo:
                    # print(f'Winning board: {board.board}')
                    unmarked_sum = board.sum_unmarked_vals()
                    last_num_called = board.called_nums[-1]
                    answer = unmarked_sum * last_num_called
                    bingo = True
        else: break
    return answer

def part2(boards_str, called_nums):
    boards = format_board_data(boards_str)
    board_objs = []
    for board in boards:
        board = BingoBoard(board)
        board_objs.append(board)
    last_bingo = False
    for num in called_nums:
        if not last_bingo:
            for board in board_objs:
                board.called_nums.append(num)
                if board.bingo:
                    if len(board_objs) > 1:
                        board_objs.remove(board)
                    else:
                        print(f'Last winning board: {board.board}')
                        unmarked_sum = board.sum_unmarked_vals()
                        last_num_called = board.called_nums[-1]
                        answer = unmarked_sum * last_num_called
                        last_bingo = True
        else: break
    print(answer)
    return answer

if __name__ == '__main__':
   # test(test_boards_str, test_called_nums)
   # part1_ans = part1(boards_str, called_nums)
   # print(f'Part 1 answer: {part1_ans}')
    test2(test_boards_str, test_called_nums)