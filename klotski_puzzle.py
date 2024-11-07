import collections


# 1448
# 1448
# 2559
# 2679
# 3..0

def printMat(cur):
   print("------BEGIN-MATRIX------")
   for i in range(5):
      for j in range(4):
         ch = cur[i*4+j]
         if ch=='4': print('■', end='')
         elif ch=='1' or ch=='2' or ch=='8' or ch=='9': print('|', end='')
         elif ch == '5': print('-', end='')
         elif ch == '3' or ch == '6' or ch == '7' or ch == '0': print('o', end='')
         else: print('.', end='')
      print()
   print("------END-MATRIX------")

begin ='1448'\
       '1448'\
       '2559'\
       '2679'\
       '3..0'
# a[x][y] = begin[4*y+x]
vis =dict()

printMat(begin)

st =collections.deque()
st.append(begin)
vis[begin] = 1

def printVictory(endState):
   printMat(endState)
   cur = vis[endState]
   iterz=0
   while cur != begin and cur != 1 and iterz<200:
      print("iter: {}".format(iterz))
      iterz+=1
      printMat(cur)
      cur = vis[cur]

iters = 0
while st:
   viselement =[0 ] *11
   cur = st.popleft()
   # movenumber = vis[cur]
   iters += 1
   if iters % 10000 == 0:
      # printMat(cur)
      print('visited = {}'.format(len(vis)))
   for x in range(4):
      for y in range(5):
         idx = 4* y + x
         if cur[idx] == '.' or viselement[int(cur[idx])]:
            continue
         curl = list(cur)
         elnum = int(cur[idx])
         elch = cur[idx]
         viselement[elnum] = True
         # add neighbours
         # small element
         for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if x + dx < 0 or x + dx >= 4 or y + dy < 0 or y + dy >= 5:
               continue
            if elnum == 3 or elnum == 0 or elnum == 6 or elnum == 7:
               if curl[4 * (y + dy) + x + dx] == '.':
                  curl[4 * (y + dy) + x + dx] = elch
                  curl[4 * y + x] = '.'
                  newcur = ''.join(curl)
                  if not newcur in vis:
                     st.append(newcur)
                     vis[newcur] = cur
                  curl[4 * y + x] = elch
                  curl[4 * (y + dy) + x + dx] = '.'
            if elnum == 1 or elnum == 9 or elnum == 8 or elnum == 2:  # |
               if dx == -1:  # left
                  if curl[4 * y + x - 1] == '.' and curl[4 * (y + 1) + x - 1] == '.':
                     curl[4 * y + x - 1] = elch
                     curl[4 * (y + 1) + x - 1] = elch
                     curl[4 * y + x] = '.'
                     curl[4 * (y + 1) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * y + x - 1] = '.'
                     curl[4 * (y + 1) + x - 1] = '.'
                     curl[4 * y + x] = elch
                     curl[4 * (y + 1) + x] = elch
               if dx == 1:  # right
                  if curl[4 * y + x + 1] == '.' and curl[4 * (y + 1) + x + 1] == '.':
                     curl[4 * y + x + 1] = elch
                     curl[4 * (y + 1) + x + 1] = elch
                     curl[4 * y + x] = '.'
                     curl[4 * (y + 1) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * y + x + 1] = '.'
                     curl[4 * (y + 1) + x + 1] = '.'
                     curl[4 * y + x] = elch
                     curl[4 * (y + 1) + x] = elch
               if dy == -1:  # up
                  if curl[4 * (y - 1) + x] == '.':
                     curl[4 * (y - 1) + x] = elch
                     curl[4 * (y + 1) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * (y - 1) + x] = '.'
                     curl[4 * (y + 1) + x] = elch
               if dy == 1 and y + 2 < 5:  # down
                  if curl[4 * (y + 2) + x] == '.':
                     curl[4 * (y + 2) + x] = elch
                     curl[4 * (y) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * (y + 2) + x] = '.'
                     curl[4 * (y) + x] = elch
               # todo handle different cases for up down left right |
            if elnum == 5:  # -
               if dx == -1:  # left
                  if curl[4 * (y) + x - 1] == '.':
                     curl[4 * (y) + x - 1] = elch
                     curl[4 * (y) + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * (y) + x - 1] = '.'
                     curl[4 * (y) + x + 1] = elch
               if dx == 1 and x + 2 < 4:  # right
                  if curl[4 * (y) + x + 2] == '.':
                     curl[4 * (y) + x + 2] = elch
                     curl[4 * (y) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * y + x + 2] = '.'
                     curl[4 * (y) + x] = elch
               if dy == -1:  # up
                  if curl[4 * (y - 1) + x] == '.' and curl[4 * (y - 1) + x + 1] == '.':
                     curl[4 * (y - 1) + x + 1] = elch
                     curl[4 * (y - 1) + x] = elch
                     curl[4 * y + x] = '.'
                     curl[4 * y + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * (y - 1) + x + 1] = '.'
                     curl[4 * (y - 1) + x] = '.'
                     curl[4 * y + x] = elch
                     curl[4 * y + x + 1] = elch
               if dy == 1 < 5:  # down
                  if curl[4 * (y + 1) + x] == '.' and curl[4 * (y + 1) + x + 1] == '.':
                     curl[4 * (y + 1) + x + 1] = elch
                     curl[4 * (y + 1) + x] = elch
                     curl[4 * y + x] = '.'
                     curl[4 * y + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     curl[4 * (y + 1) + x + 1] = '.'
                     curl[4 * (y + 1) + x] = '.'
                     curl[4 * y + x] = elch
                     curl[4 * y + x + 1] = elch
               # again handle up down left right -
            if elnum == 4:  # ■
               if dx == -1:  # left check 2
                  if curl[4 * y + x - 1] == '.' and curl[4 * (y + 1) + x - 1] == '.':
                     curl[4 * y + x - 1] = elch
                     curl[4 * (y + 1) + x - 1] = elch
                     curl[4 * y + x + 1] = '.'
                     curl[4 * (y + 1) + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     if curl[4*4+1] == '4' and curl[4*4+2] == '4':
                        print('WIN')
                        printVictory(newcur)
                        # printMat(newcur)
                        exit(0)
                     
                     curl[4 * y + x - 1] = '.'
                     curl[4 * (y + 1) + x - 1] = '.'
                     curl[4 * y + x + 1] = elch
                     curl[4 * (y + 1) + x + 1] = elch
               if dx == 1 and x + 2 < 4:  # right check 2
                  if curl[4 * y + x + 2] == '.' and curl[4 * (y + 1) + x + 2] == '.':
                     curl[4 * y + x + 2] = elch
                     curl[4 * (y + 1) + x + 2] = elch
                     curl[4 * y + x] = '.'
                     curl[4 * (y + 1) + x] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     if curl[4*4+1] == '4' and curl[4*4+2] == '4':
                        print('WIN')
                        printVictory(newcur)
                        # printMat(newcur)
                        exit(0)
                     
                     curl[4 * y + x + 2] = '.'
                     curl[4 * (y + 1) + x + 2] = '.'
                     curl[4 * y + x] = elch
                     curl[4 * (y + 1) + x] = elch
               if dy == -1:  # up check 2
                  if curl[4 * (y - 1) + x] == '.' and curl[4 * (y - 1) + x + 1] == '.':
                     curl[4 * (y - 1) + x] = elch
                     curl[4 * (y - 1) + x + 1] = elch
                     curl[4 * (y + 1) + x] = '.'
                     curl[4 * (y + 1) + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     if curl[4*4+1] == '4' and curl[4*4+2] == '4':
                        print('WIN')
                        printVictory(newcur)
                        # printMat(newcur)
                        exit(0)
                     curl[4 * (y + 1) + x + 1] = '.'
                     curl[4 * (y + 1) + x] = '.'
                     curl[4 * (y - 1) + x + 1] = elch
                     curl[4 * (y - 1) + x] = elch
               if dy == 1 and y + 2 < 5:  # down check 2 on all
                  if curl[4 * (y + 2) + x] == '.' and curl[4 * (y + 2) + x + 1] == '.':
                     curl[4 * (y + 2) + x] = elch
                     curl[4 * (y + 2) + x + 1] = elch
                     curl[4 * (y) + x] = '.'
                     curl[4 * (y) + x + 1] = '.'
                     newcur = ''.join(curl)
                     if not newcur in vis:
                        st.append(newcur)
                        vis[newcur] = cur
                     if curl[4*4+1] == '4' and curl[4*4+2] == '4':
                        print('WIN')
                        printVictory(newcur)
                        # printMat(newcur)
                        exit(0)
                     
                     curl[4 * (y + 2) + x + 1] = '.'
                     curl[4 * (y + 2) + x] = '.'
                     curl[4 * (y) + x + 1] = elch
                     curl[4 * (y) + x] = elch
               # handle up left right down ■

'''
visited = 10585657
WIN
------BEGIN-MATRIX------
||||
||||
oo--
.■■o
.■■o
------END-MATRIX------
iter: 0
------BEGIN-MATRIX------
||||
||||
oo--
■■.o
■■.o
------END-MATRIX------
iter: 1
------BEGIN-MATRIX------
||||
||||
oo--
■■o.
■■.o
------END-MATRIX------
iter: 2
------BEGIN-MATRIX------
||||
||||
oo--
■■..
■■oo
------END-MATRIX------
iter: 3
------BEGIN-MATRIX------
||||
||||
oo..
■■--
■■oo
------END-MATRIX------
iter: 4
------BEGIN-MATRIX------
||||
||||
o.o.
■■--
■■oo
------END-MATRIX------
iter: 5
------BEGIN-MATRIX------
||||
||||
o..o
■■--
■■oo
------END-MATRIX------
iter: 6
------BEGIN-MATRIX------
||||
||||
.o.o
■■--
■■oo
------END-MATRIX------
iter: 7
------BEGIN-MATRIX------
||||
||||
..oo
■■--
■■oo
------END-MATRIX------
iter: 8
------BEGIN-MATRIX------
||||
||||
■■oo
■■--
..oo
------END-MATRIX------
iter: 9
------BEGIN-MATRIX------
||||
||||
■■oo
■■--
.o.o
------END-MATRIX------
iter: 10
------BEGIN-MATRIX------
||||
||||
■■oo
■■--
.oo.
------END-MATRIX------
iter: 11
------BEGIN-MATRIX------
||||
||||
■■oo
■■--
o.o.
------END-MATRIX------
iter: 12
------BEGIN-MATRIX------
||||
||||
■■oo
■■--
oo..
------END-MATRIX------
iter: 13
------BEGIN-MATRIX------
||||
||||
■■oo
■■..
oo--
------END-MATRIX------
iter: 14
------BEGIN-MATRIX------
||||
||||
■■o.
■■.o
oo--
------END-MATRIX------
iter: 15
------BEGIN-MATRIX------
||||
||||
■■.o
■■.o
oo--
------END-MATRIX------
iter: 16
------BEGIN-MATRIX------
||||
||||
.■■o
.■■o
oo--
------END-MATRIX------
iter: 17
------BEGIN-MATRIX------
.|||
||||
|■■o
.■■o
oo--
------END-MATRIX------
iter: 18
------BEGIN-MATRIX------
.|||
.|||
|■■o
|■■o
oo--
------END-MATRIX------
iter: 19
------BEGIN-MATRIX------
|.||
|.||
|■■o
|■■o
oo--
------END-MATRIX------
iter: 20
------BEGIN-MATRIX------
||.|
||.|
|■■o
|■■o
oo--
------END-MATRIX------
iter: 21
------BEGIN-MATRIX------
|||.
|||.
|■■o
|■■o
oo--
------END-MATRIX------
iter: 22
------BEGIN-MATRIX------
|||.
|||o
|■■.
|■■o
oo--
------END-MATRIX------
iter: 23
------BEGIN-MATRIX------
|||.
|||o
|■■o
|■■.
oo--
------END-MATRIX------
iter: 24
------BEGIN-MATRIX------
|||o
|||.
|■■o
|■■.
oo--
------END-MATRIX------
iter: 25
------BEGIN-MATRIX------
|||o
|||o
|■■.
|■■.
oo--
------END-MATRIX------
iter: 26
------BEGIN-MATRIX------
|||o
|||o
|.■■
|.■■
oo--
------END-MATRIX------
iter: 27
------BEGIN-MATRIX------
|.|o
|||o
||■■
|.■■
oo--
------END-MATRIX------
iter: 28
------BEGIN-MATRIX------
|.|o
|.|o
||■■
||■■
oo--
------END-MATRIX------
iter: 29
------BEGIN-MATRIX------
||.o
||.o
||■■
||■■
oo--
------END-MATRIX------
iter: 30
------BEGIN-MATRIX------
||.o
||o.
||■■
||■■
oo--
------END-MATRIX------
iter: 31
------BEGIN-MATRIX------
||oo
||..
||■■
||■■
oo--
------END-MATRIX------
iter: 32
------BEGIN-MATRIX------
||oo
||■■
||■■
||..
oo--
------END-MATRIX------
iter: 33
------BEGIN-MATRIX------
||oo
||■■
||■■
||--
oo..
------END-MATRIX------
iter: 34
------BEGIN-MATRIX------
||oo
||■■
||■■
||--
o.o.
------END-MATRIX------
iter: 35
------BEGIN-MATRIX------
||oo
||■■
||■■
||--
o..o
------END-MATRIX------
iter: 36
------BEGIN-MATRIX------
||oo
||■■
||■■
||--
.o.o
------END-MATRIX------
iter: 37
------BEGIN-MATRIX------
||oo
||■■
||■■
||--
..oo
------END-MATRIX------
iter: 38
------BEGIN-MATRIX------
||oo
||■■
|.■■
||--
.|oo
------END-MATRIX------
iter: 39
------BEGIN-MATRIX------
|.oo
||■■
||■■
||--
.|oo
------END-MATRIX------
iter: 40
------BEGIN-MATRIX------
|o.o
||■■
||■■
||--
.|oo
------END-MATRIX------
iter: 41
------BEGIN-MATRIX------
|oo.
||■■
||■■
||--
.|oo
------END-MATRIX------
iter: 42
------BEGIN-MATRIX------
|oo.
||■■
.|■■
||--
||oo
------END-MATRIX------
iter: 43
------BEGIN-MATRIX------
.oo.
||■■
||■■
||--
||oo
------END-MATRIX------
iter: 44
------BEGIN-MATRIX------
o.o.
||■■
||■■
||--
||oo
------END-MATRIX------
iter: 45
------BEGIN-MATRIX------
oo..
||■■
||■■
||--
||oo
------END-MATRIX------
iter: 46
------BEGIN-MATRIX------
oo■■
||■■
||..
||--
||oo
------END-MATRIX------
iter: 47
------BEGIN-MATRIX------
oo■■
||■■
||--
||..
||oo
------END-MATRIX------
iter: 48
------BEGIN-MATRIX------
oo■■
||■■
||--
||o.
||.o
------END-MATRIX------
iter: 49
------BEGIN-MATRIX------
oo■■
||■■
||--
||.o
||.o
------END-MATRIX------
iter: 50
------BEGIN-MATRIX------
oo■■
||■■
||--
|.|o
|.|o
------END-MATRIX------
iter: 51
------BEGIN-MATRIX------
oo■■
|.■■
||--
|||o
|.|o
------END-MATRIX------
iter: 52
------BEGIN-MATRIX------
oo■■
|.■■
|.--
|||o
|||o
------END-MATRIX------
iter: 53
------BEGIN-MATRIX------
oo■■
|.■■
|--.
|||o
|||o
------END-MATRIX------
iter: 54
------BEGIN-MATRIX------
o.■■
|o■■
|--.
|||o
|||o
------END-MATRIX------
iter: 55
------BEGIN-MATRIX------
.o■■
|o■■
|--.
|||o
|||o
------END-MATRIX------
iter: 56
------BEGIN-MATRIX------
|o■■
|o■■
.--.
|||o
|||o
------END-MATRIX------
iter: 57
------BEGIN-MATRIX------
|o■■
|o■■
--..
|||o
|||o
------END-MATRIX------
iter: 58
------BEGIN-MATRIX------
|o■■
|o■■
--|.
|||o
||.o
------END-MATRIX------
iter: 59
------BEGIN-MATRIX------
|o■■
|o■■
--|.
|||o
||o.
------END-MATRIX------
iter: 60
------BEGIN-MATRIX------
|o■■
|o■■
--|.
|||.
||oo
------END-MATRIX------
iter: 61
------BEGIN-MATRIX------
|o■■
|o■■
--.|
||.|
||oo
------END-MATRIX------
iter: 62
------BEGIN-MATRIX------
|o■■
|o■■
--.|
||o|
||.o
------END-MATRIX------
iter: 63
------BEGIN-MATRIX------
|o■■
|o■■
--.|
||o|
||o.
------END-MATRIX------
iter: 64
------BEGIN-MATRIX------
|o■■
|o■■
--..
||o|
||o|
------END-MATRIX------
iter: 65
------BEGIN-MATRIX------
|o■■
|o■■
.--.
||o|
||o|
------END-MATRIX------
iter: 66
------BEGIN-MATRIX------
|o■■
|o■■
..--
||o|
||o|
------END-MATRIX------
iter: 67
------BEGIN-MATRIX------
|o■■
|.■■
.o--
||o|
||o|
------END-MATRIX------
iter: 68
------BEGIN-MATRIX------
|o■■
|.■■
o.--
||o|
||o|
------END-MATRIX------
iter: 69
------BEGIN-MATRIX------
|o■■
|.■■
o|--
||o|
|.o|
------END-MATRIX------
iter: 70
------BEGIN-MATRIX------
|o■■
||■■
o|--
|.o|
|.o|
------END-MATRIX------
iter: 71
------BEGIN-MATRIX------
|o■■
||■■
o|--
.|o|
.|o|
------END-MATRIX------
iter: 72
------BEGIN-MATRIX------
|o■■
||■■
.|--
o|o|
.|o|
------END-MATRIX------
iter: 73
------BEGIN-MATRIX------
.o■■
||■■
||--
o|o|
.|o|
------END-MATRIX------
iter: 74
------BEGIN-MATRIX------
o.■■
||■■
||--
o|o|
.|o|
------END-MATRIX------
iter: 75
------BEGIN-MATRIX------
o|■■
||■■
|.--
o|o|
.|o|
------END-MATRIX------
iter: 76
------BEGIN-MATRIX------
o|■■
||■■
||--
o|o|
..o|
------END-MATRIX------
iter: 77
------BEGIN-MATRIX------
o|■■
||■■
||--
o|o|
.o.|
------END-MATRIX------
iter: 78
------BEGIN-MATRIX------
o|■■
||■■
||--
o|o|
o..|
------END-MATRIX------
iter: 79
------BEGIN-MATRIX------
o|■■
||■■
|.--
o|o|
o|.|
------END-MATRIX------
iter: 80
------BEGIN-MATRIX------
o|■■
||■■
|--.
o|o|
o|.|
------END-MATRIX------
iter: 81
------BEGIN-MATRIX------
o|■■
||■■
|--|
o|o|
o|..
------END-MATRIX------
iter: 82
------BEGIN-MATRIX------
o|■■
||■■
|--|
o|.|
o|o.
------END-MATRIX------
iter: 83
------BEGIN-MATRIX------
o|■■
||■■
|--|
o|.|
o|.o
------END-MATRIX------
iter: 84
------BEGIN-MATRIX------
o|■■
||■■
|--|
o.||
o.|o
------END-MATRIX------
iter: 85
------BEGIN-MATRIX------
o|■■
||■■
|--|
o.||
.o|o
------END-MATRIX------
iter: 86
------BEGIN-MATRIX------
o|■■
||■■
|--|
.o||
.o|o
------END-MATRIX------
iter: 87
------BEGIN-MATRIX------
o|■■
.|■■
|--|
|o||
.o|o
------END-MATRIX------
iter: 88
------BEGIN-MATRIX------
o|■■
.|■■
.--|
|o||
|o|o
------END-MATRIX------
iter: 89
------BEGIN-MATRIX------
.|■■
o|■■
.--|
|o||
|o|o
------END-MATRIX------
iter: 90
------BEGIN-MATRIX------
.|■■
.|■■
o--|
|o||
|o|o
------END-MATRIX------
iter: 91
------BEGIN-MATRIX------
|.■■
|.■■
o--|
|o||
|o|o
------END-MATRIX------
iter: 92
------BEGIN-MATRIX------
|■■.
|■■.
o--|
|o||
|o|o
------END-MATRIX------
iter: 93
------BEGIN-MATRIX------
|■■.
|■■|
o--|
|o|.
|o|o
------END-MATRIX------
iter: 94
------BEGIN-MATRIX------
|■■.
|■■|
o--|
|o|o
|o|.
------END-MATRIX------
iter: 95
------BEGIN-MATRIX------
|■■|
|■■|
o--.
|o|o
|o|.
------END-MATRIX------
iter: 96
------BEGIN-MATRIX------
|■■|
|■■|
o.--
|o|o
|o|.
------END-MATRIX------
iter: 97
------BEGIN-MATRIX------
|■■|
|■■|
.o--
|o|o
|o|.
------END-MATRIX------
iter: 98
------BEGIN-MATRIX------
|■■|
|■■|
|o--
|o|o
.o|.
------END-MATRIX------
iter: 99
------BEGIN-MATRIX------
|■■|
|■■|
|o--
|o|o
o.|.
------END-MATRIX------
iter: 100
------BEGIN-MATRIX------
|■■|
|■■|
|o--
|.|o
oo|.
------END-MATRIX------
iter: 101
------BEGIN-MATRIX------
|■■|
|■■|
|.--
|o|o
oo|.
------END-MATRIX------
iter: 102
------BEGIN-MATRIX------
|■■|
|■■|
|--.
|o|o
oo|.
------END-MATRIX------
iter: 103
------BEGIN-MATRIX------
|■■|
|■■|
|--o
|o|.
oo|.
------END-MATRIX------
iter: 104
------BEGIN-MATRIX------
|■■|
|■■|
|--o
|o.|
oo.|
------END-MATRIX------
iter: 105
------BEGIN-MATRIX------
|■■|
|■■|
|--o
|o.|
o.o|
------END-MATRIX------
iter: 106
------BEGIN-MATRIX------
|■■|
|■■|
|--o
|o.|
.oo|
------END-MATRIX------
iter: 107
------BEGIN-MATRIX------
|■■|
|■■|
.--o
|o.|
|oo|
------END-MATRIX------
iter: 108
------BEGIN-MATRIX------
|■■|
|■■|
--.o
|o.|
|oo|
------END-MATRIX------
iter: 109
------BEGIN-MATRIX------
|■■|
|■■|
--o.
|o.|
|oo|
------END-MATRIX------
iter: 110
------BEGIN-MATRIX------
|■■|
|■■|
--o|
|o.|
|oo.
------END-MATRIX------
iter: 111
------BEGIN-MATRIX------
|■■|
|■■|
--o|
|o.|
|o.o
------END-MATRIX------
iter: 112
------BEGIN-MATRIX------
|■■|
|■■|
--.|
|oo|
|o.o
------END-MATRIX------
iter: 113
------BEGIN-MATRIX------
|■■|
|■■|
.--|
|oo|
|o.o
------END-MATRIX------
iter: 114
------BEGIN-MATRIX------
|■■|
|■■|
|--|
|oo|
.o.o
------END-MATRIX------
iter: 115
------BEGIN-MATRIX------
|■■|
|■■|
|--|
|oo|
o..o
------END-MATRIX------
'''
