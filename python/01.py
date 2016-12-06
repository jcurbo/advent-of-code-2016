# Advent of Code 2016 Day 1
# James Curbo

# Step one is converting the input to a form where each line is an
# instruction. This was done via a simple sed command:
# sed -e 's/, /\n/g'

# Next we set up some variables.  I am going to track the direction as a
# compass heading, and the location as blocks on an x-y grid with 0,0 being
# the starting point.

from collections import defaultdict

# direction
dir = 0
# current position
x = 0
y = 0
# position tracking
count = defaultdict()
count[(0,0)] = 1

with open('01.input') as lines:
    for line in lines:
        print("current direction: {} current position: {},{}".format(dir,x,y))
        x1 = x
        y1 = y

        if line[0] == 'L':
            print("turning left")
            dir -= 90
            if dir < 0:
                dir += 360
        elif line[0] == 'R':
            print("turning right")
            dir = (dir + 90) % 360
            
        dist = int(line[1:])
        if dir == 0:
            print("moving {} blocks N".format(dist))
            y += dist
            for i in range(y1+1, y+1):
                if (x,i) in count:
                    count[(x,i)] += 1
                else:
                    count[(x,i)] = 1
                print("visiting {},{} count: {}".format(x,i, count[(x,i)]))

        elif dir == 90:
            print("moving {} blocks E".format(dist))
            x += dist
            for i in range(x1+1,x+1):
                if (i,y) in count:
                    count[(i,y)] += 1
                else:
                    count[(i,y)] = 1
                print("visiting {},{} count: {}".format(i,y, count[(i,y)]))

        elif dir == 180:
            print("moving {} blocks S".format(dist))
            y -= dist
            for i in range(y1-1,y-1,-1):
                if (x,i) in count:
                    count[(x,i)] += 1
                else:
                    count[(x,i)] = 1
                print("visiting {},{} count: {}".format(x,i, count[(x,i)]))

        elif dir == 270:
            print("moving {} blocks W".format(dist))
            x -= dist
            for i in range(x1-1,x-1,-1):
                if (i,y) in count:
                    count[(i,y)] += 1
                else:
                    count[(i,y)] = 1
                print("visiting {},{} count: {}".format(i,y, count[(i,y)]))

        for key in count:
            if count[key] == 2:
                print("visited twice: {}, dist {}".format(key, abs(key[0])+abs(key[1])))

print("Final position: {},{}".format(x,y))
total = abs(x) + abs(y)
print(total)


