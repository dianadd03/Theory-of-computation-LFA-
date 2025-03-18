states=[]
alpha=[]
rules={}
q0=0
F=[]
error=0

def load_states(sts):
    global q0
    global F
    sts=sts.split()
    for s in sts:
        s=s.split(",")
        if len(s)==2:
            if s[1]=="S":
                q0=s[0]
            elif s[1]=="F":
                F.append(s[0])
        if len(s)==3:
            q0=s[0]
            F.append(s[0])
        global states
        states.append(s[0])

def load_alphabet(alf):
    alf=alf.split()
    global alpha
    alpha=alf

def load_function(r):
    global rules
    global states
    global alpha
    global error
    for i, line in enumerate(r):
        line=line.split()
        if line[0] not in states:
            print(f"Invalid start state in function on line {i+1} from section \"Function\"")
            error=1
        if line[1] not in alpha:
            print(f"Invalid symbol in function on line {i+1} from section \"Function\"")
            error=1
        if line[2] not in states:
            print(f"Invalid final state in function on line {i+1} from section \"Function\"")
            error=1
        if line[0] not in rules:
            rules[line[0]]={}
        if line[1] not in rules[line[0]]:
            rules[line[0]][line[1]]=[]
        rules[line[0]][line[1]].append(line[2])

def load_input_file(filename):
    input_file = open(filename, 'r')
    lines=[line.strip("\n") for line in input_file]
    for i in range(0, len(lines)):
        if lines[i]=='STATES':
            load_states(lines[i+1])
        elif lines[i]=='ALPHABET':
            load_alphabet(lines[i+1])
        elif lines[i]=='FUNCTION':
            mat=[]
            for line in lines[i+1:]:
                if line[0]=="#":
                    break
                mat.append(line)
            load_function(mat)

def Binary_Search(x, q):
    st=0
    dr=len(rules[q])-1
    while st<=dr:
        mij=(st+dr)//2
        if rules[q][mij][0]==x:
            return mij
        elif rules[q][mij][0]<x:
            st=mij+1
        else:
            dr=mij-1

def solve(input):
    current_states={q0}
    for ch in input:
        next_states=set()
        for state in current_states:
            if state in rules and ch in rules[state]:
                if ch == 'ε':
                    for symbol in rules[rules[state][ch]]:
                        next_states.update(symbol)
                else:
                    next_states.update(rules[state][ch])
        current_states=next_states

    return any(state in F for state in current_states)


load_input_file('NFA_last3rdpos0.txt')
# print(states)
# print(alpha)
# print(rules)
# print(q0)
# print(F)
if error==0:
    print("Enter input(please insert blank spaces between symbols):")
    input=input()
    input=input.split()
    if solve(input):
        print("Accepted!")
    else:
        print("Not accepted!")
