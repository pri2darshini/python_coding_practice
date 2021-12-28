# This is the input
zoo = ["fox","bug","chicken","grass","sheep"]

foodChain = {
    "antelope":["grass"],
    "big-fish":["little-fish"],
    "bug":["leaves"],
    "bear":["big-fish","bug","chicken","cow","leaves","sheep"],
    "chicken":["bug"],
    "cow":["grass"],
    "fox":["chicken","sheep"],
    "giraffe":["leaves"],
    "lion":["antelope","cow"],
    "panda":["leaves"],
    "sheep":["grass"]
}

i=0

solution = []

line=""
for i in range(len(zoo)-1):
    line+=str(zoo[i])+","
line+=zoo[len(zoo)-1]
solution.append(line)

i=0
while(i<len(zoo)):
    
    if zoo[i] not in foodChain.keys():
        i = i+1
        continue

    if(i-1)>=0:
        for j in foodChain[zoo[i]]:
            if(zoo[i-1]==j):
                solution.append(str(zoo[i])+" eats "+str(j))
                zoo.remove(j)
                i=0
                continue
    
    if(i+1<len(zoo)):
        for j in foodChain[zoo[i]]:
            if(zoo[i+1]==j):
                solution.append(str(zoo[i])+" eats "+str(j))
                zoo.remove(j)
                i=0
                continue
    i = i+1

line=""
for i in range(len(zoo)-1):
    line+=str(zoo[i])+","
line+=zoo[len(zoo)-1]
solution.append(line)

print(solution)



