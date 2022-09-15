'''
  0 1 2 3 4 5 6
0 N N N Y Y N N
1 N Y N N Y Y N
2 Y Y N Y N N Y
3 N N N N N Y N
4 Y Y N N N N N
5 N N N Y N N N

1. First we will Iterate rowise
2. Check if current cell is 'Y'
    1. If yes, then we will check the 8 adjacent cells
        1. (row-1, col)
        2. (row+1, col)
        3. (row, col-1)
        4. (row, col+1)
        5. (row-1, col-1)
        6. (row-1, col+1)
        7. (row+1, col-1)
        8. (row+1, col+1)

        *Here basically what we will do is
        [Y] is in row, col. So, we will iterate till
        row-1, row+2 and col-1, col+2
        N  N  N
        N [Y] N
        Y  N  Y
        

        if any of the adjacent cell is 'Y', increment the count and make a recursive call
3. Then we will compare the highest of all the previous region and the current count
    1. update the one with maximum
'''

#This function is to convert input to a 2D Matrix
#This will return 2D ADJACENT MATRIX, number of ROWS and number of COLS
def create_2D_matrix(file_name, operation):
    with open(file_name, operation) as f:
        data = f.read()
        data = data.split('\n')

        rows = len(data)
        col = len(data[0].split()) 

        adj_mat = []
    
        for i in data:
            temp = i.split()
            adj_mat.append(temp)

        return adj_mat, rows, col

def count_cur_area_infected(adj_mat, row, col):
    if row<0 or row>=len(adj_mat) or col<0 or col>=len(adj_mat[row]):
        return 0

    if adj_mat[row][col] == 'N':
        return 0

    adj_mat[row][col] = 'N'
    count = 1
    
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            count += count_cur_area_infected(adj_mat, i, j)

    return count

def infection_tracker(adj_mat, row, col):
    max_infected_count = 0

    for i in range(row):
        for j in range(col):
            if adj_mat[i][j] == 'Y':
                
                find_cur_area_infected = count_cur_area_infected(adj_mat, i, j)

                if find_cur_area_infected > max_infected_count:
                    max_infected_count = find_cur_area_infected

    return max_infected_count


adj_mat, rows, col = create_2D_matrix('task1_input1.txt', 'r')
print(infection_tracker(adj_mat, rows, col))