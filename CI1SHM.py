import random
from numpy.random import choice
#################### Get Input ####################
with open('input.txt', 'r') as f:
    NumberOfNodes = int(f.readline())
    MatrixOfDistances = [[0 for x in range(NumberOfNodes)] for y in range(NumberOfNodes)]
    for i in range(0, NumberOfNodes):
        x = (f.readline()).split(" ")
        for j in range(0, NumberOfNodes):
            MatrixOfDistances[i][j] = int(x[j])
        if i==j and MatrixOfDistances[i][j]!=0:
            print("Input is incorrect.")
            exit()
#################### Get Input ####################
######## Make the random first population #########
    PrimaryPopulationNumber = int(f.readline())
f.close()
ChooseRandomFromThisArray = []
for i in range(2,NumberOfNodes+1):
    ChooseRandomFromThisArray.append(i)
PrimaryPopulation = []
for i in range(0, PrimaryPopulationNumber):
    PrimaryPopulation.append([])
    for j in range(1, NumberOfNodes):
        k = random.choice(ChooseRandomFromThisArray)
        PrimaryPopulation[i].append(k)
        ChooseRandomFromThisArray.remove(k)
    for i in range(2,NumberOfNodes+1):
        ChooseRandomFromThisArray.append(i)
######## Make the random first population #########
############### Evaluation Function ###############
def EvaluationThePath(Path):
    cost = 0.0
    for i in range(0, len(Path)-1):
        cost = cost + MatrixOfDistances[Path[i]-1][Path[i+1]-1]
    cost = cost + MatrixOfDistances[0][Path[0]-1]
    x = len(Path) - 1
    cost = cost + MatrixOfDistances[Path[x]-1][0]
    return cost
def Repeat(Path):
    _size = len(Path)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if Path[i] == Path[j] and Path[i] not in repeated:
                repeated.append(Path[i])
    return repeated
def EvaluationAllThePath(Paths):
    values = []
    i=0
    k2=len(Paths)
    while i < k2:
        if len(Repeat(Paths[i])) > 0:
            kk=Paths[i]
            Paths.remove(kk)
            k2 = k2 - 1
        i = i + 1
    for j in range(0, k2):
        values.append({"person": j, "mark": EvaluationThePath(Paths[j])})
    values2 = sorted(values, key = lambda i: i['mark'], reverse=True)
    return values2
############### Evaluation Function ###############
##################### Mating ######################
def Mating(Mom, Dad):
    ml=[]
    for i in range(0, len(PrimaryPopulation)-1):
        ml.append(i)
    k1 = random.choice(ml)
    ml.remove(k1)
    k2 = random.choice(ml)
    ml.clear()
    ml.append(k1)
    ml.append(k2)
    p1=[]
    p2=[]
    for i in range(0, k1+1):
        p1.append(Mom[i])
        p2.append(Dad[i])
    for i in range(k1+1, k2+1):
        p1.append(Dad[i])
        p2.append(Mom[i])
    for i in range(k2+1, len(Mom)):
        p1.append(Mom[i])
        p2.append(Dad[i])
    l=[]
    l.append(p1)
    l.append(p2)
    return l
##################### Mating ######################
################ Choosing parents #################
GenerationCounter = 1
sum = 0.0
ChoosingParents = []
poss=[]
Children = []
while(GenerationCounter <= 1):
    if GenerationCounter == 1:
        sum=0
        poss.clear()
        print(PrimaryPopulation)
        values = EvaluationAllThePath(PrimaryPopulation)
        print(values)
        for i in range(0, len(values)):
            sum = sum + values[i]['mark']
        for i in range(0, len(values)):
            poss.append((values[i]['mark'])/sum)
        x1=0.0
        for i in range(0, len(poss)-1):
            x1 = x1 + poss[i]
        x2 = len(poss)
        LastOne = poss[x2-1]
        poss[x2-1] = 1-x1
        for i in range(0, len(poss)):
            draw = choice(values, 1, p = poss)
            ChoosingParents.append(draw[0])
            print(ChoosingParents)
        i=0
        while i < len(ChoosingParents):

            TwoChildren = Mating(PrimaryPopulation[ChoosingParents[i]['person']], PrimaryPopulation[ChoosingParents[i+1]['person']])
            print(TwoChildren)
            Children.append(TwoChildren[0])
            Children.append(TwoChildren[1])
            i=i+2
        i=0
        evalChildren = EvaluationAllThePath(Children)
        print(Children)
        print(evalChildren)
#     else:
#         sum=0
# #         poss.clear()
#         values = EvaluationAllThePath(PrimaryPopulation)
#         for i in range(0, len(values)):
#             sum = sum + ChoosingParents[i]['mark']
#         for i in range(0, len(values)):
#             poss.append((ChoosingParents[i]['mark'])/sum)
#         x1=0.0
#         for i in range(0, len(poss)-1):
#             x1 = x1 + poss[i]
#         x2 = len(poss)
#         LastOne = poss[x2-1]
#         poss[x2-1] = 1-x1
#         for i in range(0, len(poss)):
#             draw = choice(values, 1, p = poss)
#             print(draw)
#             ChoosingParents.append(draw[0])

################ Choosing parents #################

    GenerationCounter = GenerationCounter +1
