import math
import threading
import time
# def mul1(mat,mat1,flag):
#     start = time.time()
#     gap = int(math.sqrt(len(mat))) 
    
#     ranges_mat = []
#     for j in range(0,len(mat[0]),gap):
#         ranges_mat.append((j,min(j+gap,len(mat[0]))))

#     fans = [[0]*len(mat1[0]) for i in range(len(mat))]

#     threads = []
#     gap1 = int(math.sqrt(len(mat1[0])))

#     lock = threading.Lock()

#     def small_range(i,j,start,end):
#         val = 0
#         for k in range(start,end):
#             val += mat[i][k]*mat1[k][j]

#         with lock:
#             fans[i][j] += val

#         return

#     def broad_range(start,end,index):
#         for i in range(start,end):
#             for start_small,end_small in ranges_mat:
#                 t = threading.Thread(target=small_range,args=(index,i,start_small,end_small))
#                 t.start()
#                 threads.append(t)
#         return
    
#     for i in range(len(mat)):
#         for j in range(0,len(mat1[0]),gap1):
#             t = threading.Thread(target=broad_range,args=(j,min(j+gap1,len(mat[0])),i))
#             t.start()
#             threads.append(t)
    
#     for t in threads:
#         t.join()

#     # for i in fans:
#     #     print(*i)
#     if flag:
#         return fans
#     else:
#         return time.time()-start

def mul(mat,mat1,flag,n=-1):
    start = time.time()

    if n==-1:
        n1 = math.ceil(math.sqrt(len(mat)))
        n = len(mat)
    else:
        n1 = n
        n = len(mat)
        
    sqrt_n = n1
    sqrt_n1 = n1

    ans = [[0] * len(mat1[0]) for _ in range(len(mat))]
    threads = []
    row_block = math.ceil(n/sqrt_n)
    col_block = math.ceil(n/sqrt_n1)

    def multiply_block(mat, mat1, ans, row_start, row_end, col_start, col_end, n):
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                total = 0
                for k in range(n):
                    total += mat[i][k]*mat1[k][j]
                ans[i][j] = total

    for i in range(sqrt_n):
        for j in range(sqrt_n1):
            row_start = i*row_block
            row_end = min((i+1)*row_block,len(mat))
            col_start = j*col_block
            col_end = min((j+1)*col_block,len(mat1[0]))
            t = threading.Thread(target=multiply_block,args=(mat, mat1, ans, row_start, row_end, col_start, col_end, len(mat1)))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    if flag:
        return ans
    else:
        return time.time()-start
