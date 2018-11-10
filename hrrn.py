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


def gantt_chart(process_list):
    # Inserting active processes in a list
    active_process = []
    total_process = len(process_list)
    end = 0
    time = 0
    waiting_time = 0
    turnaround_time = 0
    table = []
    while len(active_process) > 0 or len(process_list) > 0:
        j = 0
        while j < len(process_list):
            if time == process_list[j]['arrival']:
                active_process.append({'PId': process_list[j]['PId'], 'at': process_list[j]['arrival'], 'bt': process_list[j]['burst'], 'ratio': 0})
                del process_list[j]
                j = j - 1
            j = j + 1

        if time >= end and len(active_process) > 0:
            for items in active_process:
                items['ratio'] = ((time - items['at'])+items['bt']) / items['bt']
            hrrn = active_process[0]['ratio']
            position = 0
            for itr in range(len(active_process)):
                if active_process[itr]['ratio'] > hrrn:
                    hrrn = active_process[itr]['ratio']
                    position = itr
                elif active_process[itr]['ratio'] == hrrn:
                    if active_process[itr]['at'] < active_process[position]['at']:
                        position = itr
            end = time + active_process[position]['bt']
            table.append({'PID': active_process[position]['PId'], 'AT': active_process[position]['at'], 'BT': active_process[position]['bt'], 'ST': time, 'ET': end, 'TAT': end - active_process[position]['at'], 'WT': time - active_process[position]['at']})
            waiting_time = waiting_time + time - active_process[position]['at']
            turnaround_time = turnaround_time + end - active_process[position]['at']
            del active_process[position]
        time = time + 1
    pprint(table)
    print('Average Turn Around Time:', turnaround_time / total_process)
    print('Average Waiting Time:', waiting_time / total_process)


input_info()
gantt_chart(process_list)
