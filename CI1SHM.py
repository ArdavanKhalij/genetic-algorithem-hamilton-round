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
def DeleteRP(Paths):
    i=0
    k2=len(Paths)
    while i < k2:
        if len(Repeat(Paths[i])) > 0:
            kk=Paths[i]
            Paths.remove(kk)
            k2=k2-1
            i=i-1
        i = i + 1
    return Paths
def EvaluationAllThePath(Paths):
    values = []
    i=0
    k2=len(Paths)
    for j in range(0, k2):
        values.append(EvaluationThePath(Paths[j]))
    return values
############### Evaluation Function ###############
##################### Mating ######################
def Mating(Mom, Dad):
    ml=[]
    for i in range(0, len(Mom)):
        ml.append(i)
    k1 = random.choice(ml)
    ml.remove(k1)
    k2 = random.choice(ml)
    ml.clear()
    ml.append(k1)
    ml.append(k2)
    p1=[]
    p2=[]
    if k1>k2:
        s=k2
        k2=k1
        k1=s
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
NumberToDelete = 0
while(GenerationCounter <= 100):
    if GenerationCounter == 1:
        sum=0
        poss.clear()
        pp = []
        PrimaryPopulation2 = DeleteRP(PrimaryPopulation)
        for i in range(0, len(PrimaryPopulation2)):
            pp.append(PrimaryPopulation2[i])
        PrimaryPopulation.clear()
        for i in range(0, len(pp)):
            PrimaryPopulation.append(pp[i])
        print(PrimaryPopulation)
        print(PrimaryPopulation2)
        values = EvaluationAllThePath(PrimaryPopulation)
        for i in range(0, len(values)):
            sum = sum + values[i]
        for i in range(0, len(values)):
            poss.append((values[i])/sum)
        x1=0.0
        for i in range(0, len(poss)-1):
            x1 = x1 + poss[i]
        x2 = len(poss)
        LastOne = poss[x2-1]
        poss[x2-1] = 1-x1
        q = []
        for j in range(0, len(PrimaryPopulation)):
            q.append(j)
        for i in range(0, len(poss)):
            draw = choice(q, 1, p = poss)
            ChoosingParents.append(PrimaryPopulation[draw[0]])
        i=0
        while i < len(ChoosingParents):
            TwoChildren = Mating(ChoosingParents[i], ChoosingParents[i+1])
            Children.append(TwoChildren[0])
            Children.append(TwoChildren[1])
            TwoChildren.clear()
            i=i+2
        i=0
        NumberToDelete = len(PrimaryPopulation)
        for i in range(0, len(Children)):
            PrimaryPopulation.append(Children[i])
    else:
        sum=0
        poss.clear()
        values.clear()
        pp = []
        PrimaryPopulation2 = DeleteRP(PrimaryPopulation)
        for i in range(0, len(PrimaryPopulation2)):
            pp.append(PrimaryPopulation2[i])
        PrimaryPopulation.clear()
        for i in range(0, len(pp)):
            PrimaryPopulation.append(pp[i])
        print(PrimaryPopulation)
        print(PrimaryPopulation2)
        values = EvaluationAllThePath(PrimaryPopulation)
        for i in range(0, len(values)):
            sum = sum + values[i]
        for i in range(0, len(values)):
            poss.append((values[i])/sum)
        x1=0.0
        for i in range(0, len(poss)-1):
            x1 = x1 + poss[i]
        x2 = len(poss)
        LastOne = poss[x2-1]
        poss[x2-1] = 1-x1
        q = []
        for j in range(0, len(PrimaryPopulation)):
            q.append(j)
        for i in range(0, len(poss)):
            draw = choice(q, 1, p = poss)
            ChoosingParents.append(PrimaryPopulation[draw[0]])
        i=0
        while i < len(ChoosingParents):
            TwoChildren = Mating(ChoosingParents[i], ChoosingParents[i+1])
            Children.append(TwoChildren[0])
            Children.append(TwoChildren[1])
            TwoChildren.clear()
            i=i+2
        i=0
        NumberToDelete2 = len(PrimaryPopulation)
        while i<NumberToDelete:
            del PrimaryPopulation[0]
            i=i+1
        i=0
        NumberToDelete = NumberToDelete2
        for j in range(0, len(Children)):
            PrimaryPopulation.append(Children[j])
    print("________________________________")
    print(len(PrimaryPopulation))
    print("________________________________")
    GenerationCounter = GenerationCounter + 1