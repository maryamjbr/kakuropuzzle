from operator import itemgetter
import time
width = 10
height = 10
t=time.time()
# matrix2 = [["*", "*", [20, "*"], [6, "*"]],
#            ["*", [14, 11], 0, 0],
#            [["*", 21], 0, 0, 0],
#            [["*", 8], 0, 0, "*"]]
# matrix2=[["*", "*", "*", [17,"*"], [28,"*"], "*", "*"],
#         ["*", "*", [27, 16], 0, 0, [17,"*"], [17,"*"]],
#         ["*", [11,27], 0, 0, 0, 0, 0],
#         [["*",3], 0, 0, [14,19], 0, 0, 0],
#         [["*",34], 0, 0, 0, 0, 0, [17,"*"]],  
#         ["*", ["*",30], 0, 0, 0, 0, 0],
#         ["*", ["*",3], 0, 0, ["*",16], 0, 0]]

matrix2=[["*", "*", "*", [17,"*"], [19,"*"], "*", "*",[7,"*"],[44,"*"],"*"],
        ["*",[3,"*"] , [37, 17], 0, 0,"*", ["*",10],0,0, [23,"*"]],
        [["*",20], 0, 0, 0, 0,[6,"*"],[3,15],0,0, 0],
        [["*",5], 0, 0 ,[3,25],0, 0,0,0,0, 0],
        ["*",["*",8] ,0,0,["*",3] ,0,0,[10,15],0,0],
        ["*", [13,3],0, 0, [7,"*"], [5,"*"],["*",17],0, 0,"*"],
        [["*",9] ,0,0, [10,3],0, 0, [16,6] ,0,0, [11,"*"]],
        [["*",38],0, 0,  0, 0,0, 0,[3,17],0,0],
        [["*",7] ,0,0,0,"*",["*",12] ,0,0,0,0],
        ["*", ["*",4]  , 0 , 0, "*",["*",3] , 0, 0,"*","*"]]

class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def printCell(self):
        print(self.x, self.y, self.value)


class Partition:
    def __init__(self, guide_num, cells: list, is_row: bool):
        self.guide_num = guide_num
        self.cells = cells
        self.is_row = is_row

    def add_cell(self, cell):
        self.cells.append(cell)

    def printPartition(self):
        print(self.guide_num)
        for i in self.cells:
            i.printCell()
        print(self.is_row)


def find_partition(m, w, h):
    partitionList = []
    cell_list = []
    for i in range(w):
        for j in range(h):
            if isinstance(m[i][j],list) and m[i][j][1] != "*":
                guideNum = m[i][j][1]
                j += 1
                p = Partition(guideNum, [], True)
                while (j < h and not isinstance(m[i][j],list) and m[i][j] != "*"):
                    c = Cell(i, j, m[i][j])
                    cell_list.append(c)
                    p.add_cell(c)
                    j += 1
                partitionList.append(p)
    for j in range(h):
        for i in range(w):
            if isinstance(m[i][j],list) and m[i][j][0] != "*":
                guideNum = m[i][j][0]
                p = Partition(guideNum, [], False)
                i += 1
                while (i < width and not isinstance(m[i][j],list) and m[i][j] != '*'):
                    c = Cell(i, j, m[i][j])
                    p.add_cell(c)
                    i += 1
                partitionList.append(p)
    return partitionList, cell_list


p, c = find_partition(matrix2, width, height)

cell_partition_dic = dict()
for cell in c:
    p_list = []
    for i in p:
        for j in i.cells:
            if cell.x == j.x and cell.y == j.y:
                p_list.append(i)
                break
        cell_partition_dic[cell] = p_list

c2 = sorted([(i, min(len(j.cells) for j in cell_partition_dic[i]), min(j.guide_num for j in cell_partition_dic[i]))
              for i in c], key=itemgetter(2, 1))

c3 = [i[0] for i in c2]
c=c3


def is_solved(cell):
    for i in cell_partition_dic[cell]:
        sum=0
        count=0
        for j in i.cells:
            if not(cell.x==j.x and cell.y==j.y):
                if cell.value == j.value:
                    return False
            if j.value!=0:
                sum+=j.value
            else:
                sum=sum+(9-count)
                count+=1
        if count!=0:
            if sum<i.guide_num:
                return False
        else:
            if sum!=i.guide_num:
                return False
    return True

def update_partition(cell, value):
    for i in cell_partition_dic[cell]:
        for j in i.cells:
            if cell.x == j.x and cell.y == j.y:
                j.value = value



def solve_puzzle(cell_number):
    if cell_number==len(c):
        return True
    for i in range(1,10):
        update_partition(c[cell_number],i)
        c[cell_number].value=i  
        if is_solved(c[cell_number]) and solve_puzzle(cell_number+1):
            return True
        update_partition(c[cell_number],0)   
        c[cell_number].value=0
    
    return False



def printKakuro(matrix):
    for i in range(width):
        for j in range(height):
            if matrix[i][j] == "*":
                print("■\t", end="")
            elif type(matrix[i][j]) == list:
                if matrix[i][j][0] == "*":
                    print("■" + "\\" + str(matrix[i][j][1]) + "\t", end="")
                elif matrix[i][j][1] == "*":
                    print(str(matrix[i][j][0]) + "\\" + "■" + "\t", end="")
                else:
                    print(str(matrix[i][j][0]) + "\\" + str(matrix[i][j][1]) + "\t", end="")
            else:
                for k in c:
                    if k.x == i and k.y == j:
                        print(k.value, end="\t")
                        break

        print()


if solve_puzzle(0):
    printKakuro(matrix2)
    print(time.time()-t)
else:
    print("no answer")