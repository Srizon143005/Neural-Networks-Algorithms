inputs = [[1,-1,1,-1,1,-1,1,-1],
          [1,1,1,1,-1,-1,-1,-1]]

tests = [[1,1,1,-1,1,-1,1,-1],
         [-1,1,1,1,-1,-1,-1,-1]]

input_lines = len(inputs[0])
# Training Phase
w = []
for i in range(input_lines):
    tmp = []
    for j in range(input_lines):
        tmp.append(0)
    w.append(tmp)

for i in range(input_lines):
    for j in range(input_lines):
        if i==j:
            continue
        for k in inputs:
            w[i][j] = w[i][j]+k[i]*k[j]

print(w)


# Testing Phase
f_h=0.4
c = 0
for u in tests:
    print(u)
    prev = u
    while(1):
        new = []
        for i in range(input_lines):
            tmp=0
            for j in range(input_lines):
                tmp=tmp+w[i][j]*prev[j]
            new.append(tmp)
        #print(new)
        for j in range(input_lines):
            if new[j]>0:
                new[j]=1
            else:
                new[j]=-1
        print(new)
        print()
        prev = new
        break