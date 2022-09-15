def create_2D_matrix(file_name, operation):
    with open(file_name, operation) as f:
        data = f.read()
        data = data.splitlines()

        row, col = int(data[0]), int(data[1])

        adj_mat = []

        for i in data[2:]:
            adj_mat.append(i.split())

        return adj_mat, row, col

def count_alive(adj_mat):
    count = 0

    for i in range(len(adj_mat)):
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 'H':
                count += 1

    return count

def invade(adj_mat):
    time = 0
    while True:
        flag = False
        for i in range(0, len(adj_mat)):
            for j in range(0, len(adj_mat[i])):
                if adj_mat[i][j] == 'A' or adj_mat[i][j] == time:
                    #Checking Up
                    if i-1 < 0 or i-1 >= len(adj_mat) or j < 0 or j >= len(adj_mat[i]):
                        pass
                        # print("Entered")
                    else:
                        if adj_mat[i-1][j] == 'H':
                            flag = True
                            adj_mat[i-1][j] = time + 1
                    #Checking Down
                    if i+1 < 0 or i+1 >= len(adj_mat) or j < 0 or j >= len(adj_mat[i]):
                        pass
                        # print("Entered")
                    else:
                        if adj_mat[i+1][j] == 'H':
                            flag = True
                            adj_mat[i+1][j] = time + 1
                    #Checking Left
                    if i < 0 or i >= len(adj_mat) or j-1 < 0 or j-1 >= len(adj_mat[i]):
                        pass
                        # print("Entered")
                    else:
                        if adj_mat[i][j-1] == 'H':
                            flag = True
                            adj_mat[i][j-1] = time + 1
                    #Checking Right
                    if i < 0 or i >= len(adj_mat) or j+1 < 0 or j+1 >= len(adj_mat[i]):
                        pass
                        # print("Entered")
                    else:
                        if adj_mat[i][j+1] == 'H':
                            flag = True
                            adj_mat[i][j+1] = time + 1

        if flag:
            time += 1
        else:
            break

    return time, adj_mat               
            
adj_mat, row, col = create_2D_matrix("task2_input1.txt","r")
time, final_adj_mat = invade(adj_mat)
count = count_alive(final_adj_mat)

print(f"Time: {time} minutes")
if count == 0:
    print("No one survived")
else:
    print(f"{count} survived")