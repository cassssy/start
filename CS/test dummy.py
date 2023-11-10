N = int(input())
i= 0

while i < N:
    if i < 3:
        xy_values = input()

        xy_list = xy_values.split(" ")


        p = [int(num) for num in xy_list]

        x1 = int(p[0])
        y1 = int(p[1])
        x2 = int(p[2])
        y2 = int(p[3])
        x3 = int(p[4])
        y3 = int(p[5])
        x4 = int(p[6])
        y4 = int(p[7])



    else:
        xy_values = input()

        xy_list = xy_values.split(" ")


        p = [int(num) for num in xy_list]

        x1 = int(p[0])
        y1 = int(p[1])
        x2 = int(p[2])
        y2 = int(p[3])
        x3 = int(p[4])
        y3 = int(p[5])
        x4 = int(p[6])
        y4 = int(p[7])
        print (x1, y1, x2, y2, x3, y3, x4, y4)
    
    
    i = i + 1
    
    
6
4 1 -2 4 1 0 3 4
0 3 -2 4 1 0 3 4
1 0 3 4 2 0 4 4
-1 6 3 6 1 3 1 7
-1 6 3 6 2 6 5 6
1 0 1 0 0 1 -1 0

2 2
do not intersect
do not intersect
1 6
invalid input
invalid input