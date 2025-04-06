states=[]
alpha=[]
stack=['$']
rules={}
q0=0
F=[]
error=0

def print_map_with_player(current_state, has_spoon=False):
    def mark(name, state):
        player = "🧍"
        spoon = "🥄" if has_spoon and current_state == state else " "
        return f"{name:^14}{player}{spoon}" if current_state == state else f"{name:^18}"

    print(f"""
                             +--------------------+
                             |{mark('SECRET ROOM', 'q3')}  |
                             +---------|----------+
                                      |
+--------------------+       +--------------------+       +--------------------+
|{mark('KITCHEN', 'q2')}  |-------|{mark('HALLWAY', 'q1')}  |-------|{mark('LIBRARY', 'q4')}  |
+--------------------+       +---------|----------+       +----------|---------+
                                       |                             |
                             +--------------------+        +--------------------+
                             |{mark('ENTRANCE', 'q0')}  |          |{mark('EXIT', 'q5')}|
                             +--------------------+        +--------------------+
""")



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
        # if line[0] not in states:
        #     print(f"Invalid state in function on line {i+1} from section \"Function\"")
        #     error=1
        # if line[1] not in alpha:
        #     print(f"Invalid symbol in function on line {i+1} from section \"Function\"")
        #     error=1
        # if line[2] not in states:
        #     print(f"Invalid state in function on line {i+1} from section \"Function\"")
        #     error=1

        if line[0] not in rules:
            rules[line[0]]=[]
        line[1]=line[1].split(',')
        rules[line[0]].append((line[1], line[2]))
    for state in rules:
        rules[state].sort(key=lambda x: x[0][0])

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
    if q not in rules:
        return -1
    dr=len(rules[q])-1
    while st<=dr:
        mij=(st+dr)//2
        if rules[q][mij][0][0]==x:
            return mij
        elif rules[q][mij][0][0]<x:
            st=mij+1
        else:
            dr=mij-1
    return -1

def solve():
    current_state=q0
    exit=0
    while exit==0:
        print_map_with_player(current_state, stack[-1]=='!')
        if current_state=='q0':
            room="ENTRANCE"
        elif current_state=='q1':
            room="HALLWAY"
        elif current_state=='q2':
            room="KITCHEN"
        elif current_state=='q3':
            room="SECRET ROOM"
        elif current_state=='q4':
            room="LIBRARY"
        else:
            room="EXIT"
        if(room=="KITCHEN" and stack[-1]!='!'):
            print(f'Your current state: {room}. You should pick the spoon 🥄 in order to win!(action=pick). Enter action:')
        else:
            print(f'Your current state: {room}. Enter action:')
        action=input()
        action=action.strip('\n')
        if action=='up':
            action='0'
        elif action=='down':
            action='1'
        elif action=='left':
            action='2'
        elif action=='right':
            action='3'
        elif action=='pick':
            action='4'
        else:
            print("Invalid action")
            continue

        noacc = 0
        poz = Binary_Search(action, current_state)
        # print(poz)
        if poz == -1:
            if current_state in rules:
                poz = Binary_Search('Îµ', current_state)
                current_state = rules[current_state][poz][1]
                continue
            else:
                noacc = 1
                break
        # print(current_state)
        rel = rules[current_state][poz][0]
        current_state=rules[current_state][poz][1]
        # print(rel)
        if rel[1] == 'Îµ':
            if rel[2] != 'Îµ':
                stack.append(rel[2])
        elif rel[1] == stack[-1]:
            trash = stack.pop()
            if rel[2] != 'Îµ':
                stack.append(rel[2])
        else:
            noacc = 1
            break
        # i += 1
        # print(ch, current_state)
        # print(stack)
        if current_state in F:
            break
    if len(stack)==1 and noacc==0:
        # exit=1
        print_map_with_player(current_state, True)
        print("!!WIN!!")
    else:
        print_map_with_player(current_state)
        print("You lost. You had to have the spoon hidden in the kitchen to win.")


load_input_file('config_pda.txt')
# print(states)
# print(alpha)
# print(rules)
# print(q0)
# print(F)
solve()
