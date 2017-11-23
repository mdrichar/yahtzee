from functools import reduce
import itertools
import operator

#for i in itertools.product(range(3),range(3)):
#    print(i)

class Action:
    def __init__(self,held,rerolled):
        print("Action: ", held,"Rerolled:",rerolled)
        self.held = held
        self.rerolled = rerolled
        self.destinations = {}
        for roll, prob in items[rerolled].items():
            assert len(roll)==len(held)
            #z = zip(held,roll)
            #print("Roll: ",roll,"Prob:",prob, z)
            #print("Roll: ",roll,"Prob:",prob, "Zip: ", zip(held,roll), "Sum: ", sum(zip(held,roll)))
            dest = tuple(map(sum,zip(held,roll)))
            print("   Dest: ",dest)
            self.destinations[dest] = prob


    

items = [{} for i in range(6)]
#items.append({})
items[0][(0,0,0,0,0,0)] = 1

base = [(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),(0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1)]

for i in range(1,len(items)):
    for j in range(6):
        #zlist = [0] * 6
        #zlist[j] = 1
        
        for key,val in items[i-1].items():
            t = tuple(map(sum,zip(key,base[j])))
            if t in items[i]:
                items[i][t] += val
            else: 
                items[i][t] = val

#print(items)
#for i in range(len(items)):
#    print("I: ",i,"Size:",len(items[i]))
#    isize = 0
#    for k,v in items[i].items():
#        isize += v
#        print(k,v)
#
#    print("Total: ",isize)


def yahtzee(t):
    assert(len(t) == 6)
    if sum(t) == max(t) and max(t) == 5:
        return 50
    return 0

def large_straight(t):
    if sum(t) == 5 and max(t) == 1 and (t[0]+t[5]==1):
        return 40
    return 0
    
def has1(t):
    return t[0] > 0
def has2(t):
    return t[1] > 0
def has3(t):
    return t[2] > 0
def has4(t):
    return t[3] > 0
def has5(t):
    return t[4] > 0
def has6(t):
    return t[5] > 0

def small_straight(t):
    if not has3(t) or not has4(t):
        return 0
    if (has2(t) and has5(t)) or (has1(t) and has2(t)) or (has5(t) and has6(t)):
        return 30
    return 0

def prod(factors):
    return(reduce(operator.mul, factors, 1))

def chance(t):
    #return sum(map(prod(zip(t,(1,2,3,4,5,6)))))
    return sum(p*q for p,q in zip(t,(1,2,3,4,5,6)))

def three_of_a_kind(t):
    if max(t) < 3:
        return 0
    return chance(t)

def four_of_a_kind(t):
    if max(t) < 4:
        return 0
    return chance(t)

def full_house(t):
    if yahtzee(t) or (2 in t and 3 in t):
        return 25
    return 0

def ones(t):
    return t[0]
def twos(t):
    return 2*t[1]
def threes(t):
    return 3*t[2]
def fours(t):
    return 4*t[3]
def fives(t):
    return 5*t[4]
def sixes(t):
    return 6*t[5]

def scores(t):
    return (ones(t),twos(t),threes(t),fours(t),fives(t),sixes(t),three_of_a_kind(t),four_of_a_kind(t),full_house(t),small_straight(t),large_straight(t),yahtzee(t),chance(t))

#print(yahtzee((1,0,0,0,3,1)))
#print(yahtzee((5,0,0,0,0,0)))
#print(large_straight((5,0,0,0,0,0)))
#print(large_straight((1,1,1,1,1,0)))
#print(large_straight((0,1,1,1,1,1)))
#print(large_straight((0,0,2,1,1,1)))
#print(small_straight((5,0,0,0,0,0)))
#print(small_straight((1,1,1,1,0,2)))
#print(small_straight((1,1,0,1,0,2)))
#print(small_straight((1,1,1,1,1,0)))
#print(small_straight((0,1,1,1,1,1)))
#print(small_straight((0,0,2,1,1,1)))
#print(small_straight((1,1,1,1,0,1)))
#print(small_straight((1,1,0,1,0,2)))
#
#print("Chance")
#print(chance((5,0,0,0,0,0)))
#print(chance((1,1,1,1,1,0)))
#print(chance((0,1,1,1,1,1)))
#print(chance((0,0,2,1,1,1)))
#print(chance((5,0,0,0,0,0)))
#print(chance((1,1,1,1,0,2)))
#print(chance((1,1,0,1,0,2)))
#print(chance((1,1,1,1,1,0)))
#print(chance((0,1,1,1,1,1)))
#print(chance((0,0,2,1,1,1)))
#print(chance((0,2,0,0,0,3)))
#print(chance((1,1,1,0,0,2)))
#
#print("Full House")
#print(full_house((5,0,0,0,0,0)))
#print(full_house((1,1,1,1,1,0)))
#print(full_house((0,1,1,1,1,1)))
#print(full_house((0,0,2,1,1,1)))
#print(full_house((5,0,0,0,0,0)))
#print(full_house((1,1,1,1,0,2)))
#print(full_house((1,1,0,1,0,2)))
#print(full_house((1,1,1,1,1,0)))
#print(full_house((0,1,1,1,1,1)))
#print(full_house((0,0,2,1,1,1)))
#print(full_house((0,2,0,0,0,3)))
#print(full_house((1,1,1,0,0,2)))

#print (scores((1,1,1,2,0,0)))

for t in items[5]:
    print("Roll: ",t,"Scores: ",scores(t))


actionSets = {}
transitions = 0
actionCnt = 0
for t in items[5]:
    print("Tuple: ",t)
    for action in itertools.product(range(t[0]+1),range(t[1]+1),range(t[2]+1),range(t[3]+1),range(t[4]+1),range(t[5]+1)):
        actionCnt += 1
        #print("Action: ", action, 5-sum(action))
        actionItem = Action(action,5-sum(action))
        transitions += len(actionItem.destinations)
        #print("Action:",actionItem)
print(actionCnt)
print(transitions)
print(len(items[5]))
	
