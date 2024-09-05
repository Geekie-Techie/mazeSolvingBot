import pyamaze as Maze
from queue import PriorityQueue


def aStar(m):
    start=(1,1)
    g={cell:float('inf') for cell in m.grid}
    g[start]=0
    f={cell:float('inf') for cell in m.grid}
    f[start]=h(start,(m.rows,m.cols))

    open=PriorityQueue()
    open.put((h(start,(m.rows,m.cols)),h(start,(m.rows,m.cols)),start))
    closed={}
    while not open.empty():
        cur=open.get()[2]
        if cur==(m.rows,m.cols):
            break
        for dir in 'ESNW':
            if m.maze_map[cur][dir]==True:
                if dir=='E':
                    child=(cur[0],cur[1]+1)
                if dir=='W':
                    child=(cur[0],cur[1]-1)
                if dir=='N':
                    child=(cur[0]-1,cur[1])
                if dir=='S':
                    child=(cur[0]+1,cur[1])

                temp_g=g[cur]+1
                temp_f=temp_g+h(child,(1,1))

                if temp_f < f[child]:
                    g[child]= temp_g
                    f[child]= temp_f
                    open.put((temp_f,h(child,(1,1)),child))
                    closed[child]=cur
    imgpath={}
    cell=(m.rows,m.cols)
    txtpath=[]
    while cell!=start:
        imgpath[closed[cell]]=cell
        txtpath.append(cell)
        cell=closed[cell]
    
    return imgpath,(txtpath+[start])[-1::-1]

def h(cur,goal):
    x1,y1=cur
    x2,y2=goal

    return abs(x1-x2) + abs(y1-y2)

def showPath(path):
    print("Path:")
    for x,y in path:
        print(f'\t{x}, {y}')


length,width = map(int,input('Enter maze size: ').split())
x0,y0 = 1,1

m=Maze.maze(length,width)
m.CreateMaze(length,width)
imgpath,txtpath=aStar(m)
showPath(txtpath)
a=Maze.agent(m,x0,y0,footprints=True,goal=(length,width))
m.tracePath({a:imgpath})
l=Maze.textLabel(m,'A* Path Length',len(txtpath))

m.run()