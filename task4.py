#--- import modules
import numpy as np

#--- input params. ( forget to record... )
N, S =
board =

#--- define method
def search_five_lineup_xy(board=[], b=0):
    def xy(board=board, b=b, xy='x'):
        flag_list = []
        if xy == 'y': board = board.T
        for raw_num, raw_list in enumerate(board, start=1):
            flag_list.extend(
                [list(raw_list[i:i+N_game]) == [b] * N_game
                     for i in range(N - N_game + 1)]
                )

        return any(flag_list)

    return xy(board=board, b=b, xy='x') | xy(board=board, b=b, xy='y')

def search_five_lineup_diag(board=[], b=0):
    def diag(board=board, b=b, direction='rd'):
        flag_list = []
        if direction == 'ld':
            board = np.array([board.copy()[i][::-1] for i in range(N)]).reshape(N, N).T
        # diagonal
        diag_list = np.diag(board)
        flag_list.extend(
            [list(diag_list[i:i+N_game]) == [b] * N_game
                 for i in range(N - N_game + 1)]
            )
        # column
        for i in range(1, N - 4):
            diag_list = [board[j][i+j] for j in range(N - i)]
            flag_list.extend(
                [diag_list[j:j+N_game] == [b] * N_game
                     for j in range(N - N_game + 1 - i)]
                )
        # raw
        for i in range(1, N - 4):
            diag_list = [board[:, j][i+j] for j in range(N - i)]
            flag_list.extend(
                [diag_list[j:j+N_game] == [b] * N_game
                     for j in range(N - N_game + 1 - i)]
                )

        return any(flag_list)

    return diag(board=board, b=b, direction='rd') | diag(board=board, b=b, direction='ld')

def search_reach_coor(board=[], b=0):
    coor = []
    ind_empty = np.where(board==-1)
    for ind_raw, ind_col in zip(ind_empty[0], ind_empty[1]):
        board_rep = board.copy()
        board_rep[ind_raw][ind_col] = b
        if search_five_lineup_xy(board_rep, b) | search_five_lineup_diag(board_rep, b):
            coor.append('{0} {1}\n'.format(ind_col+1, ind_raw+1))

    return coor

#--- main
ans = search_reach_coor(board, S)
if len(ans) != 0: print(ans[0])
elif len(ans) == 0:
    ans = search_reach_coor(board, not(S))
    if len(ans) == 0: print('{} {}\n'.format(np.where(board==-1)[1][0] + 1, np.where(board==-1)[0][0] + 1))
    elif len(ans) == 1: print(ans[0])
    elif len(ans) >= 2: print('LOSE\n')
