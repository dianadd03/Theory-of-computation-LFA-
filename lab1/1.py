def is_matrix(m):
    n=len(m[0])
    for line in m:
        if n != len(line):
            return False
    return True

def save_matrix(m, fn):
    output_file=open(fn,'w')
    comm=[]
    m_without_comms=[]
    for line in m:
        if str(line[0]).isalpha():
            comm.append(line)
        else:
            m_without_comms.append(line)
    if is_matrix(m_without_comms):
        for line in m_without_comms:
            line=[str(x) for x in line]
            output_file.write(" ".join(line))
            output_file.write("\n")

def load_matrix(fn):
    input_file=open(fn,'r')
    m=[]
    comm=[]
    for line in input_file.readlines():
        if str(line[0]).isalpha():
            comm.append(line)
        else:
            l=[int(x) for x in line.split()]
            m.append(l)
    if is_matrix(m):
        return m, comm
    else:
        return "Invalid matrix"

m, c=load_matrix('date.txt')
print("COMENTARII:", *c)
if str(m[0]).isalpha():
    print(m)
else:
    for line in m: 
        print(*line)

m2=[[1, 2, 3], "coM",[4, 5, 6], [7, 8, 9]]
save_matrix(m2,'date2.txt')