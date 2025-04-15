import math
import threading
import time

def mul(mat,mat1,flag):
    start = time.time()
    gap = int(math.sqrt(len(mat))) 
    
    ranges_mat = []
    for j in range(0,len(mat[0]),gap):
        ranges_mat.append((j,min(j+gap,len(mat[0]))))

    fans = [[0]*len(mat) for i in range(len(mat[0]))]

    threads = []
    gap1 = int(math.sqrt(len(mat1[0])))

    lock = threading.Lock()

    def small_range(i,j,start,end):
        val = 0
        for k in range(start,end):
            val += mat[i][k]*mat1[k][j]

        with lock:
            fans[i][j] += val

        return

    def broad_range(start,end,index):
        for i in range(start,end):
            for start_small,end_small in ranges_mat:
                t = threading.Thread(target=small_range,args=(index,i,start_small,end_small))
                t.start()
                threads.append(t)
        return
    
    for i in range(len(mat)):
        for j in range(0,len(mat1[0]),gap1):
            t = threading.Thread(target=broad_range,args=(j,min(j+gap1,len(mat[0])),i))
            t.start()
            threads.append(t)
    
    for t in threads:
        t.join()

    # for i in fans:
    #     print(*i)
    if flag:
        return fans
    else:
        return time.time()-start

# mul([[1,2,3],[4,5,6],[7,8,9]],[[2,3,4],[6,5,4],[9,2,1]])