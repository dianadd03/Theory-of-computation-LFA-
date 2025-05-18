states=[]
alpha=[]
rules={}
q0=0
F=[]
error=0
tape=''

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
        line=line.split('>')
        sts=line[0].split()
        stf=line[1].split()
        if sts[0] not in rules:
            rules[sts[0]]={}
        rules[sts[0]][sts[1]]=stf

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
        elif lines[i]=='TAPE':
            global tape
            tape=lines[i+1]

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

def solve(tape):
    tape=[x for x in tape]
    print(*tape)
    current_state=q0
    i=0
    while i<len(tape):
        print(current_state, i)
        if current_state in rules and tape[i] in rules[current_state]:
            # print(rules[current_state][tape[i]])
            old=rules[current_state][tape[i]]
            next_state=rules[current_state][tape[i]][0]
            tape[i]=rules[current_state][tape[i]][1]
            if next_state in F:
                return tape
            if(old[2]=='L'):
                i-=1
            else:

                i+=1
            current_state=next_state

    return tape


# load_input_file('gpt_copy_bits.txt')
# load_input_file('config_tape$.txt')
# load_input_file('config_concat.txt')
load_input_file('add_binary.txt')
# load_input_file("add_nocarry.txt")
# print(states)
# print(alpha)
# print(rules)
# print(q0)
# print(F)
print(*solve(tape))
