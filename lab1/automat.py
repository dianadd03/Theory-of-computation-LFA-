states=[]
alpha=[]
rules=[]
q0=0
F=[]

def load_states(sts):
    sts=sts.split()
    for s in sts:
        s=s.split(",")
        if s[1]=="S":
            global q0
            q0=s[0]
        elif s[1]=="F":
            global F
            F.append(s[0])
        global states
        states.append(s[0])

def load_alphabet(alf):
    alf=alf.split()
    global alpha
    alpha=alf

def load_function(r):
    global rules
    for line in r:
        line=line.split()
        line=[x.split(",") if x!='-1' else [] for x in line]
        rules.append(line)

def load_input_file(filename):
    input_file = open(filename, 'r')
    lines=[line.strip("\n") for line in input_file]
    for i in range(0, len(lines)):
        if lines[i]=='STATES':
            load_states(lines[i+1])
        elif lines[i]=='ALPHABET':
            load_alphabet(lines[i+1])
        elif lines[i]=='FUNCTION':
            load_function(lines[i+1:i+1+len(states)])


load_input_file('FA.txt')
print(states)
print(alpha)
print(rules)
print(q0)
print(F)