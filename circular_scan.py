import pandas as pd

print('Assumed direction right!!!')
tracks = int(input("Enter no of tracks: "))
start = 0
end = tracks - 1
head = int(input("Enter initial head position: "))
blocks = int(input("Enter total no of blocks in queue: "))
queue = []
solution = []
direction = 'right'
for itr in range(blocks):
    n = int(input("Enter block number: "))
    queue.append({'block': n, 'head_distance': 0})

total_distance = 0

while len(queue) != 0:
    for items in queue:
        if head == items['block'] and direction == 'right':
            solution.append({'block_accessed': head, 'total_tracks_traversed': total_distance})
            queue.remove(items)
    if head == end:
        direction = 'left'
        total_distance = total_distance + 1
    if head == start:
        direction = 'right'
        total_distance = total_distance + 1
    if direction == 'right':
        head = head + 1
    else:
        head = head - 1
    total_distance = total_distance + 1

print(pd.DataFrame(solution))
print("total seek distance:", total_distance-1)
