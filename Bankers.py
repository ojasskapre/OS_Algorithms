import numpy as np

total_resources = int(input("Enter number of resources: "))
total_processes = int(input("Enter number of processes: "))

resource_vector = []
allocate_matrix = []
claim_matrix = []
templist = []
solution = []
print('Enter Resource Vector')
for itr in range(total_resources):
    resources = int(input('Enter amount of resources: '))
    resource_vector.append(resources)

for i in range(total_processes):
    for j in range(total_resources):
        claimed = int(input('Enter amount of resource' + str(j) + ' claimed by process' + str(i) + ' : '))
        templist.append(claimed)
    claim_matrix.append(templist)
    templist = []
claim_matrix = np.array(claim_matrix)
column_sum = claim_matrix.sum(axis=0)

for i in range(total_processes):
    for j in range(total_resources):
        if resource_vector[j] < claim_matrix[i][j]:
            exit(-1)

for i in range(total_processes):
    for j in range(total_resources):
        allocated = int(input('Enter amount of resource' + str(j) + ' claimed by process' + str(i) + ' : '))
        templist.append(allocated)
    allocate_matrix.append(templist)
    templist = []
allocate_matrix = np.array(allocate_matrix)

for i in range(total_processes):
    for j in range(total_resources):
        if allocate_matrix[i][j] > claim_matrix[i][j]:
            exit(-1)

need_matrix = np.subtract(claim_matrix, allocate_matrix)
column_sum = allocate_matrix.sum(axis=0)
available_vector = np.subtract(resource_vector, column_sum)


def display():
    print("Need Matrix")
    print(need_matrix)
    print("Available Vector")
    print(available_vector)


i = 0
while i < total_processes:
    for j in range(total_resources):
        if available_vector[j] >= need_matrix[i][j]:
            if j == total_resources -1:
                print('Process' + str(i) + ' is safe')
                solution.append('P' + str(i))
                display()
                for k in range(total_resources):
                    available_vector[k] = available_vector[k] + allocate_matrix[i][k]
                    allocate_matrix[i][k] = 999
                    need_matrix[i][k] = 999
                if i == total_processes - 1:
                    i = -1
                break  # restart for j loop and restart the process
            continue
        else:
            break
    i = i + 1

if len(solution) == total_processes:
    print("System is not in deadlock state")
else:
    print("System is not in deadlock state")

display()
print("Sequence in which process can be executed to avid deadlock is ")
print(solution)
