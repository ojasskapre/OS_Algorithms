# Ojas Kapre 1611022 A2
from pprint import pprint


def input_info():
    global process_list
    process_list = []
    while True:
        enter = input('Do you want to enter other entry Enter "no" to exit: ').lower()
        if enter == 'no':
            break
        process_id = input('Enter process id: ')
        arrival_time = int(input('Enter arrival time: '))
        burst_time = int(input('Enter burst time: '))
        process_info = {'PId': process_id, 'arrival': arrival_time, 'burst': burst_time}
        process_list.append(process_info)
    # print(process_list)


def gantt_chart(process_list):
    # Inserting active processes in a list
    active_process = []
    gc = []
    total_process = len(process_list)
    time = 0
    end = 0
    waiting_time = 0
    turnaround_time = 0
    table = []
    while len(active_process) > 0 or len(process_list) > 0:
        j = 0
        while j < len(process_list):
            if time == process_list[j]['arrival']:
                active_process.append({'PId': process_list[j]['PId'], 'at': process_list[j]['arrival'], 'bt': process_list[j]['burst'], 'rt': process_list[j]['burst']})
                del process_list[j]
                j = j - 1
            j = j + 1

        if len(active_process) == 0:
            gc.append('i')

        if time >= end and len(active_process) > 0:
            rt = active_process[0]['rt']
            position = 0
            for itr in range(len(active_process)):
                if active_process[itr]['at'] <= time:
                    if active_process[itr]['rt'] < rt:
                        rt = active_process[itr]['rt']
                        position = itr
                    elif active_process[itr]['rt'] == rt:
                        if active_process[itr]['at'] < active_process[position]['at']:
                            position = itr
            active_process[position]['rt'] = active_process[position]['rt'] - 1
            gc.append(active_process[position]['PId'])
            end = time + 1
            if active_process[position]['rt'] == 0:
                table.append({'PID': active_process[position]['PId'], 'AT': active_process[position]['at'],
                              'BT': active_process[position]['bt'], 'CT': end,
                              'TAT': end - active_process[position]['at'], 'WT': end - active_process[position]['at'] - active_process[position]['bt']})
                waiting_time = waiting_time + end - active_process[position]['at'] - active_process[position]['bt']
                turnaround_time = turnaround_time + end - active_process[position]['at']
                del active_process[position]
        time = time + 1
    for itr in range(end):
        print(str(itr)+'\t|\t', end='')
    print()
    for items in gc:
        print(items+'\t|\t', end='')
    print()
    pprint(table)
    print('Average Turn Around Time:', turnaround_time / total_process)
    print('Average Waiting Time:', waiting_time / total_process)


input_info()
gantt_chart(process_list)
