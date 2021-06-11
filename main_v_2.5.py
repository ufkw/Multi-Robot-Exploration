#! python

#v.2.5

import pygame, random, math
from tkinter import *
import numpy as np


#globals
SIZE = 50

#globals for func Detect Deadlock

HistPoints = -1
H_Points = -1
 
#new_list_of_mds = []
#temp_list_of_mds = []

#classes
class Robot:
    def __init__(self, x, y):
      #  self.position = movement
        self.x = x
        self.y = y
        self.position = np.array([x,y])
        self.dir = 0

    def get_Coordinates(self):
        return self.position

    def set_direction(self, dir):
        self.dir = dir
    
    def get_direction(self):
        return self.dir

    def get_Coordinates(self):
        return self.position

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (str(self) == str(other))  

    def __ne__(self, other):
        return not(self == other)


class Graph:
    def __init__(self, cfg, cr):
        self.graph_1 = {}
        self.cr = cr
        for r in cfg:
            self.edge_list = []
            for index in range(len(cfg)):
                dist = math.dist(r.get_Coordinates(), cfg[index].get_Coordinates())
                if dist < cr and dist != 0:
                    #add edge to graph
                    self.edge_list.append(cfg[index])
            self.graph_1[r] = self.edge_list

    def printGraph(self):
        print(self.graph_1)

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.graph_1[node]:
                self.dfs(n, visited)
        return visited

    def checkConnected(self):
        try:
            graph_length = len(self.dfs(cfg[0], []))
            if graph_length != len(cfg):
                return False
            else:
                return True
        except:
            return False
        
        



class Container:
    def __init__(self, grid, cfg):
        self.grid = grid
        self.cfg = cfg


#global for detect deadlock
#list of mins and maxs
class Min_Max_Dict:
    def __init__(self):
        self.minx = 100
        self.miny = -100
        self.maxx = 100
        self.maxy = -100




#functions


def environment_1(grid):
    #take in grid, return grid
    #create obstacles
    #like ones in paper/unchanging
    row = 7
    l = 0
    cl = 0
    while l < 2:
        x = 0
        column = l * cl
        while x < 8:
            grid[row][column + x] = 3
            x = x + 1
        l = l + 1
        cl = x + 3
    column = 8*2-1
    row = 0
    am = 0
    while am < 2:
        for row in range(7):
            grid[row][column] = 3
        am = am + 1
        column = column + 10 + am
    row = 5
    for x in range(13):
        grid[row][int(SIZE/2 + SIZE/4)+ x] = 3
    row = row + 17
    for x in range(5,row-17+3):
        grid[x][int(SIZE/2 + SIZE/4)] = 3
    am = 1
    row = 0
    while am < 2:    
        for x in range(int(SIZE/2 - SIZE/4)):
            grid[int(SIZE/3) + row][x] = 3
        if am == 0:
            row = row + int(SIZE/6)
        elif am == 1:
            for x in range(5):
                grid[int(SIZE/3) + row][x + int(SIZE/10)] = 0
            row = row + int(SIZE/8)        
        am = am + 1
        column = int(SIZE/2) + 7
        for x in range(9):
            grid[25][column + x] = 3
    row = int(SIZE/3)
    for y in range(7):
        grid[row + y][int(SIZE/2 - SIZE/4)] = 3
    row = int(SIZE/3) + 7 + 5
    for y in range(8):
        grid[row + y][int(SIZE/2 - SIZE/4)] = 3
    for y in range(9):
        grid[SIZE - y - 1][int(SIZE/10)] = 3  
    for y in range(12):
        grid[SIZE - y - 1][int(SIZE/4) + 1] = 3
    for x in range(3):
        grid[SIZE - 15][x] = 3
    for x in range(8,14):
        grid[SIZE - 15][x] = 3
    for x in range(18,int(SIZE/4)+1):
        grid[SIZE - 15][x] = 3
    for y in range(int(SIZE/2 + SIZE/3), SIZE):
        grid[y][int(SIZE/2 + SIZE/4)] = 3
    for x in range(int(SIZE/2), int(SIZE/2)+10):
        grid[int(SIZE/2 + SIZE/5)][x] = 3
    for x in range(SIZE - 13, SIZE):
        grid[int(SIZE/2)+10][x] = 3       
    for y in range(int(SIZE/2)+10, int(SIZE/2)):
        grid[y][SIZE-13] = 3

    return grid


def environment_2(grid):
    #return a grid

    for y in range(int(SIZE/2 + SIZE/5), SIZE):
        grid[y][int(SIZE/2)] = 3
        grid[SIZE-20][y] = 3
        grid[y][9] = 3
    for x in range(int(SIZE/2), int(SIZE/2)+5):
        grid[int(SIZE/2 + SIZE/3 + 3)][x] = 3
    for y in range(int(SIZE/2 + SIZE/5), SIZE):
        grid[y][int(SIZE/3)] = 3
    for x in range(int(SIZE/2), int(SIZE/2)+5):
        grid[int(SIZE/2 + SIZE/3)][10+x] = 3
    for x in range(int(SIZE/2 - 4), int(SIZE/2)+9):
        grid[int(SIZE/2 + SIZE/4)][15+x] = 3
    for x in range(int(SIZE/3), int(SIZE/3)+9):
        grid[int(SIZE/2 + SIZE/4)][4+x] = 3
    for x in range(20):
    #    grid[int(SIZE/3)+x][int(SIZE/3)+x] = 3
    #    grid[int(SIZE/3)+x][int(SIZE/3)+x+1] = 3
        grid[x][10] = 3
        grid[int(SIZE/2)][x] = 3
    for x in range(10):
        grid[int(SIZE/2)-x][int(SIZE/2) + x] = 3
        grid[int(SIZE/2)-x][int(SIZE/2) + x+1] = 3
        grid[int(SIZE/3)-x][int(SIZE/3)+5 + x] = 3
        grid[int(SIZE/3)-x][int(SIZE/3)+5 + x+1] = 3
        grid[x][SIZE-15] = 3
    for x in range(5):
        grid[20][SIZE-15+x] = 3
        grid[10][SIZE-10+x] = 3

    return grid


def selectMovement(robot):
    #randomly select movement and add it to current robot
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
 #   x = -1
  #  y = 0

    #if out of bounds just return robot
    if(robot.x + x < 0 or robot.x + x > SIZE - 1 or robot.y + y < 0 or robot.y + y > SIZE - 1):
        return robot

    if(x == -1):
        if(y == -1):
            dir = 12
        elif(y == 1):
            dir = 13
        elif(y == 0):
            dir = 8
    elif(x == 1):
        if(y == -1):
            dir = 11
        elif(y == 1):
            dir = 10
        elif(y == 0):
            dir = 9
    elif(x == 0):
        if(y == 1):
            dir = 6
        elif(y == -1):
            dir = 7
        elif(y == 0):
            dir = 0  

    new_x = robot.x + x
    new_y = robot.y + y
    new_robot = Robot(new_x, new_y)
    new_robot.set_direction(dir)

    return new_robot


def md(px,py,dx,dy):
    #euclidean distance
    p = [px,py]
    d = [dx,dy]
    ed = math.dist(p,d)
    return int(ed)
    #r_md = abs(px - dx) + abs(py - dy)
    #return r_md
    


#utility function passes in a configuration and returns an int
def utilityFunction(list_of_mds, cfg_t, row, column, t, have_range):
 
    #for each movement, compare to every other part of confg
#    print("In utility function:")
    A_CONST = SIZE * 3      #arbitrary constant

    #we will be summing over this utility
    utility = 0
    temp_cfg_pos = [] #full of coordinate arrays to check robots are not going to same space
    row_size = len(row)
    i = 0 #index
    
    found = False
    for p in cfg_t:
    
        #if out of range
        #find distance between all robots
        if have_range:
            graph_r = Graph(cfg_t, cr)
            
            if not graph_r.checkConnected():
                utility = utility - A_CONST


      

        

        #2)two robots in same space
        #need to check if coordinates are unique
        temp_pos = p.get_Coordinates()
        temp_cfg_pos.append(temp_pos)
        #1)out of bounds
        if(p.x < 0 or p.x > SIZE - 1 or p.y < 0 or p.y > SIZE - 1):
            #this never happens
            utility = utility - A_CONST
        elif(grid[p.x][p.y] == 3):        #3)hitting black obstacle
            utility = utility - A_CONST

        else:
            #4)frontier. brute force

            #go through every element of the frontier and calculate the md between that point and p.x, p.y
            #crashing here
            min_md = A_CONST
            
            for k in range(row_size):
                x = row[k]
                y = column[k]
                md_1 = md(x,y,p.x,p.y)
                if(md_1 < min_md):
                    min_md = md_1
                
                if(min_md == 0):
                    break
                
            utility = utility - (min_md  - list_of_mds[i])                  
        
        
        i = i + 1 
        

    
    arr, uniq_c = np.unique(temp_cfg_pos, axis = 0, return_counts = True)
    uniq_arr = arr[uniq_c == 1]

    flag = 0
    # to check all unique list elements for #2
    size_list = len(temp_cfg_pos)
    size_n_list = len(uniq_arr)
    flag = size_list != size_n_list  
    # result 
    if(flag): 
        #impossible position
        utility = utility - A_CONST

#    print("returned utility is ", utility)
    return utility


def detect_Deadlock(cfg, grid, S):
    #return a bool
    #cfg: list of robots
    #grid: entire grid before updating the robots move

    #S  #number of steps before stored positions are compared
    ep = 4 #distance that indicates limited movement

    global HistPoints
    
    index = 0   #index used to get 
    #check for every robot
    for robe in cfg:
        #if a robot hits a frontier then reset the deadlock detection
        if grid[robe.x][robe.y] == 2:       #check that these are correct x y order
            list_of_min_maxs[index].minx = robe.x
            list_of_min_maxs[index].maxx = robe.x
            list_of_min_maxs[index].miny = robe.y
            list_of_min_maxs[index].maxy = robe.y
            HistPoints = 0
            return False
        else:
            #update changes in x and y

            if robe.x < list_of_min_maxs[index].minx:
                list_of_min_maxs[index].minx = robe.x
            if robe.y < list_of_min_maxs[index].miny:
                list_of_min_maxs[index].miny = robe.y
            if robe.x > list_of_min_maxs[index].maxx:
                list_of_min_maxs[index].maxx = robe.x
            if robe.y > list_of_min_maxs[index].maxy:
                list_of_min_maxs[index].maxy = robe.y
            
            #check whether last frontier visit is older than S steps
            if HistPoints > S:
                #if no progress is made
                if ((list_of_min_maxs[index].maxx - list_of_min_maxs[index].minx) < ep) and ((list_of_min_maxs[index].maxy - list_of_min_maxs[index].miny) < ep):
                    #notify that deadlock occured
                    return True
                else:
                    #otherwise reset the deadlock detection
                    list_of_min_maxs[index].minx = robe.x
                    list_of_min_maxs[index].maxx = robe.x
                    list_of_min_maxs[index].miny = robe.y
                    list_of_min_maxs[index].maxy = robe.y
                    HistPoints = 0
            
        index = index + 1
    #changed algorithm to count steps (HistPoints) as t        
    HistPoints = HistPoints + 1

    return False



def deadlock_Recovery(cfg, grid, cr):
    #return container class with new cfg and grid
    #cfg: cfg of robots
    #cr: communication range
    #grid that comes in has not been updated
    #print("Deadlock recovery")
    #randomly select a robot as meeting point
    robot_rand = random.choice(cfg)
    
    #set meeting point
    meet_x = robot_rand.x
    meet_y = robot_rand.y

    temp_cfg_f = []
    continuing = True
    double_dead = False
    locals = 0
    locals1 = 0
    global HistPoints
    HistPoints = locals
    tester = 0
    r_dist = int(math.sqrt(2*cr*cr) / 2)
    while continuing:
        #move every robot closer to the meeting point using MD path planning
        changed = False
        num = 0 #keeps track of how many robots are in the radius of the random robot
        tester = tester + 1
        for robe in cfg:
            new_x = 0
            new_y = 0
            if (robe.x < meet_x + r_dist) and (robe.x > meet_x - r_dist) and (robe.y < meet_y + r_dist) and (robe.y > meet_y - r_dist): 
                num = num - 1
                temp_cfg_f.append(robe)
              #  grid[robe.x][robe.y] = 1
            else:
                changed = True
                min_md = 1000
                listq = [-1, 0, 1]
                for q in listq:
                    for p in listq:
                        #check bounds
                        if(robe.x + q > -1 and robe.x + q < SIZE and robe.y + p > -1 and robe.y + p < SIZE and (q != 0 or p != 0)):
                            if grid[robe.x + q][robe.y + p] != 3:
                                if grid[robe.x + q][robe.y + p] != 4:
                                    md_1 = md(meet_x, meet_y, robe.x + q, robe.y + p)
                                    if md_1 < min_md:
                                        min_md = md_1
                                        new_x = q
                                        new_y = p

                new_robot = Robot(robe.x + new_x, robe.y + new_y)
                temp_cfg_f.append(new_robot)
                
                #execute min_md
                #move robe one step towards meeting place
                for q in listq:
                    for p in listq:
                        #check bounds
                        if(robe.x+q > -1 and robe.x+q < SIZE and robe.y+p > -1 and robe.y+p < SIZE):
                            if(grid[robe.x + q][robe.y + p] == 0):
                                grid[robe.x + q][robe.y + p] = 2

                        elif(robe.x+q + new_x > -1 and robe.x+q + new_x < SIZE and robe.y+p+ new_y > -1 and robe.y+p+ new_y < SIZE):
                            if(grid[robe.x + new_x + q][robe.y + new_y + p] == 0):
                                grid[robe.x + new_x + q][robe.y + new_y + p] = 2
            
            grid[robe.x][robe.y] = 1
            grid[robe.x + new_x][robe.y + new_y] = 4
        
        #for r in temp_cfg_f:
        #    grid[r.x][r.y] = 4

        
        if detect_Deadlock(temp_cfg_f, grid, 8):
            container_f = Container(grid, temp_cfg_f)
            return container_f
                            

        c = 0
        #print robots cfgs
        frontier_size = 0
        for x in range(SIZE):
            for y in range(SIZE):
                color = WHITE

                if(grid[x][y] == 0):
                    color = WHITE
                elif(grid[x][y] == 1):
                    color = GREEN
                elif(grid[x][y] == 2):
                    color = YELLOW
                    frontier_size = frontier_size + 1
                elif(grid[x][y] == 3):
                    color = BLACK
                elif(grid[x][y] == 4):
                    color = RED
                    c = c + 1


                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * y + MARGIN,
                            (MARGIN + HEIGHT) * x + MARGIN, WIDTH, HEIGHT])
    
        
        pygame.display.flip()


        if num == -len(cfg):       
           continuing = False            
        
    #    if changed:
      #      for r in temp_cfg_f:
      #          grid[r.x][r.y] = 1
        cfg = []
        cfg = temp_cfg_f.copy()
        temp_cfg_f.clear()
        
 
    container_f = Container(grid, cfg)
    return container_f




def deadlock_Reset(cfg, grid):
    #return container of grid and cfg
   
    move_count = 5
    index = 0
    listq = [-1, 0, 1]
    list_of_nums = []
    temp_cfg_f = []
    changed = False
    while index < move_count:
        i = 0
        for robe in cfg:            
            if index == 0:
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
                while x == 0 and y == 0:
                    x = random.randint(-1, 1)
                    y = random.randint(-1, 1)
                list_x_y = [x, y]
                list_of_nums.append(list_x_y)
            else:
                x = list_of_nums[i][0]
                y = list_of_nums[i][1]
            #check bounds
            if(robe.x + x > -1 and robe.x + x < SIZE and robe.y + y > -1 and robe.y + y < SIZE):
                #check not hitting obstacle or other robot
                if(grid[robe.x + x][robe.y + y] != 3 and grid[robe.x + x][robe.y + y] != 4):
                    changed = True

                    
                    for q in listq:
                        for p in listq:
                            #check bounds
                    #        if(robe.x + q > -1 and robe.x + q < SIZE - 1 and robe.y + p > -1 and robe.y + p < SIZE - 1):
                        #           if(grid[robe.x + q][robe.y + p] == 0):
                        #               grid[robe.x + q][robe.y + p] = 2

                            if(robe.x + x + q > -1 and robe.x + x + q < SIZE and robe.y + y + p > -1 and robe.y + y + p < SIZE):
                                if(grid[robe.x + x + q][robe.y + y + p] == 0):
                                    grid[robe.x + x + q][robe.y + y + p] = 2

                    grid[robe.x][robe.y] = 1
                    grid[robe.x+x][robe.y+y] = 4  #set new location to robot 

                    n_robot = Robot(robe.x + x, robe.y + y)
                    temp_cfg_f.append(n_robot)
                else:
                    temp_cfg_f.append(robe)
            else:
                temp_cfg_f.append(robe)
            
            i = i + 1

  

        index = index + 1
        
        
        c = 0
        #print robots cfgs
        frontier_size = 0
        for x in range(SIZE):
            for y in range(SIZE):
                color = WHITE

                if(grid[x][y] == 0):
                    color = WHITE
                elif(grid[x][y] == 1):
                    color = GREEN
                elif(grid[x][y] == 2):
                    color = YELLOW
                    frontier_size = frontier_size + 1
                elif(grid[x][y] == 3):
                    color = BLACK
                elif(grid[x][y] == 4):
                    color = RED
                    c = c + 1


                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * y + MARGIN,
                            (MARGIN + HEIGHT) * x + MARGIN, WIDTH, HEIGHT])
        pygame.display.flip()




        if changed:
            cfg = []
            cfg = temp_cfg_f.copy()
            temp_cfg_f.clear()




    
    container_f = Container(grid, cfg)
    return container_f






#grid
BLACK = (0,0,0)
GREEN = (0, 255, 0)
#YELLOW = (255, 255, 0)
YELLOW = (0,100,255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH = 10
HEIGHT = 10
MARGIN = 1

#grid is 2d array
global grid
grid = np.zeros((SIZE, SIZE))


#get user input to decide environment

root = Tk()
var = IntVar()
label = Label(text = "Choose environment and close window to run.")
label.pack()
R1 = Radiobutton(root, text="Empty", variable=var, value=1)#, command = sel())#,  command = root.destroy)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Obstacle 1", variable=var, value=2)#, command = sel())#,  command = root.destroy)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Obstacle 2", variable=var, value=3)#, command = sel()) #, command = root.destroy)
R3.pack( anchor = W)


root.mainloop()
selection = var.get()

if selection == 1:
    #grid is empty, we do not change it
    grid
elif selection == 2:
    grid = environment_1(grid)
elif selection == 3:
    grid = environment_2(grid)


#get user input to decide number of robots

root = Tk()
var = IntVar()
label = Label(text = "Choose number of robots and close window to run.")
label.pack()
R1 = Radiobutton(root, text="3", variable=var, value=3)#, command = sel())#,  command = root.destroy)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="4", variable=var, value=4)#, command = sel())#,  command = root.destroy)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="5", variable=var, value=5)#, command = sel()) #, command = root.destroy)
R3.pack( anchor = W)


root.mainloop()
n = var.get()





#pygame
pygame.init()

#display
WINDOW_SIZE = [550, 550]
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Let's go exploring!")
clock = pygame.time.Clock()



past_deadlock = False

#k < 9^n
k = 40


#create list of minmaxs for algorithm 3 detect deadlock
list_of_min_maxs = []
index = 0
for index in range(n):
    m = Min_Max_Dict()
    list_of_min_maxs.append(m)


frontier_size = n + 4

#putting all the robots next to eachother in a corner
#all adjacent squares are frontier
pcfg = []

for column in range(n):
    r = Robot(SIZE-1, int(SIZE/3 + SIZE/4) + column)
    pcfg.append(r)
    grid[SIZE-1][int(SIZE/3 + SIZE/4) + column] = 4
    grid[SIZE-2][int(SIZE/3 + SIZE/4) + column] = 2

    if column == 0:
        grid[SIZE-1][int(SIZE/3 + SIZE/4) + column - 1] = 2
        grid[SIZE-2][int(SIZE/3 + SIZE/4) + column - 1] = 2


grid[SIZE-1][int(SIZE/3 + SIZE/4) + n] = 2
grid[SIZE-2][int(SIZE/3 + SIZE/4) + n] = 2





# algorithm 1 #
t = 0

#run for T steps
T = 45000
temp_t = -T -2
#set communication range
cr = 15

have_range = True
reset_counter = 17


#### drawing program ####       currently not running
done = False
clock.tick(60)
#while not done:


#drawing grid
screen.fill(BLACK)
cfg_max_val = -100 #makes first move always move
counter = 0
while t < T and frontier_size != 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#done = True
#      
    #generate a population
    popu = []
    popu.clear()

    for i in  range(k):
        #generate a configuration change
        cfg = [] #a list of robots (potential places)
        cfg.clear()
    
        for j in pcfg:
            #j is a Robot
            #select a random movement
            cfg_1 = selectMovement(j)   #applying a random movement on one of the robots
            cfg.append(cfg_1)

        #should now have a list of movements for each of the n robots in a list
        #add this cfg list to popu(lation)
        popu.append(cfg)

        temp_cfg = pcfg.copy()



    #compute fitness find maximum
    cfg_max = pcfg.copy()      #make if none of the new configurations are better than where they already are, dont move
    changed = False
    z = 0

    #find frontier
    
    two = [2]
    mask = np.isin(grid, two)
    frontier_coord = np.nonzero(mask)
    row = frontier_coord[0]
    column = frontier_coord[1]

    A_CONST = 2*SIZE
    list_of_mds = []
    for element in pcfg:
        min_md = A_CONST
        for p in range(len(row)):
            x = row[p]
            y = column[p]
            md_1 = md(x,y,element.x, element.y)
            if(md_1 < min_md):
                min_md = md_1
        list_of_mds.append(min_md)



    for h in popu:
        #utility function

        z = z + 1

        ut_of_cfg = utilityFunction(list_of_mds, h, row, column, t, have_range)
        

        if(ut_of_cfg >= cfg_max_val):
            cfg_max = h.copy()
            cfg_max_val = ut_of_cfg
            changed = True




    #executing
        
    if(changed):
        index = 0

        #move the robots to the positions with the maximum fitness
        #execute cfg_max
        for el in temp_cfg:
            grid[el.x][el.y] = 1

        for m in cfg_max:
   
            #go through coordinates and adjust grid accordingly
            
            #go through all adjacent squares and adjust
            
            #if 1, skip
            #if 2, skip
            #if 4, change to 1
            #if 3, skip
            #if 0, change to 2           
            
            listq = [-1, 0, 1]

            for q in listq:
                for p in listq:
                    #check bounds
                    if(m.x+q > -1 and m.x+q < SIZE and m.y+p > -1 and m.y+p < SIZE):
                        if(grid[m.x+q][m.y+p] == 0):
                            grid[m.x+q][m.y+p] = 2


            grid[m.x][m.y] = 4  #set new location to robot
            index = index + 1
    
        c = 0 
        #print robots cfgs
        frontier_size = 0
        for x in range(SIZE):
            for y in range(SIZE):
                color = WHITE

                if(grid[x][y] == 0):
                    color = WHITE
                elif(grid[x][y] == 1):
                    color = GREEN
                elif(grid[x][y] == 2):
                    color = YELLOW
                    frontier_size = frontier_size + 1
                elif(grid[x][y] == 3):
                    color = BLACK
                elif(grid[x][y] == 4):
                    color = RED
                    c = c + 1


                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * y + MARGIN,
                            (MARGIN + HEIGHT) * x + MARGIN, WIDTH, HEIGHT])
    
            
            pygame.display.flip()

            counter = 0
            pcfg.clear()
            pcfg = cfg_max.copy()
    



    
    else:
        counter = counter + 1
        if counter >= 2:
            cfg_max_val = -100
        






    #check for deadlock
    #algorithm 2 goes here
    #   noDL = True
    S = n * 30
    if detect_Deadlock(cfg_max, grid, S):

        
        #recover from deadlock
        
        if temp_t + S + 5 >= t:
            container_returned = deadlock_Reset(cfg_max, grid)
            have_range = False
            reset_counter = 0
            
        else:

            container_returned = deadlock_Recovery(cfg_max, grid, cr)
  
        temp_t = t
        cfg_returned = container_returned.cfg
        grid = container_returned.grid.copy()
        pcfg.clear()
        pcfg = cfg_returned.copy()
        HistPoints = 0

    elif reset_counter == 15:
        have_range = True
        container_returned = deadlock_Recovery(cfg_max, grid, cr)
        temp_t = t
        cfg_returned = container_returned.cfg
        grid = container_returned.grid.copy()
        pcfg.clear()
        pcfg = cfg_returned.copy()
        HistPoints = 0
    
    t = t+1
    reset_counter = reset_counter + 1



pygame.quit()
