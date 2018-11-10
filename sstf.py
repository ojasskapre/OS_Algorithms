from operator import itemgetter
import pandas as pd


def min_distance(queue):
    queue = sorted(queue, key=itemgetter('head_distance'))
    # print(queue)
    return queue


tracks = int(input("Enter no of tracks: "))
head = int(input("Enter initial head position: "))
blocks = int(input("Enter total no of blocks in queue: "))
queue = []
solution = []
for itr in range(blocks):
    n = int(input("Enter block number: "))
    queue.append({'block': n, 'head_distance': abs(n - head)})

i = 0
total_distance = 0
while i < blocks:
    queue = min_distance(queue)
    head = queue[0]['block']
    total_distance = total_distance + queue[0]['head_distance']
    solution.append({'block_accessed': queue[0]['block'], 'tracks_traversed': queue[0]['head_distance']})
    del queue[0]
    for items in queue:
        items['head_distance'] = abs(head - items['block'])
    i = i + 1

print(pd.DataFrame(solution))
print("total seek distance:", total_distance)
