from pprint import pprint
import numpy
import operator


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
    active_process = []
    total_process = len(process_list)
    time_chart = []
    time = 0
    while True:
        if total_process == len(active_process):
            break
        for items in process_list:
            if time == items['arrival']:
                active_process.append((items['burst'], items['PId'], items['arrival']))
                # process_list.remove(items)
        time = time + 1
    temp = active_process
    temp.sort(key=operator.itemgetter(2, 0))

    time = 0

    table = []
    turn_around_time = []
    waiting_time = []
    while len(temp) != 0:
        for items in temp:
            while time < items[2]:
                time_chart.append('idle')
                time = time + 1
            if time >= items[2]:
                time = time + items[0]
                table.append({'PID': items[1], 'AT': items[2], 'BT': items[0], 'CT': time, 'TAT': time - items[2],
                              'WT': time - items[0] - items[2]})
                turn_around_time.append(time - items[2])
                waiting_time.append(time - items[0] - items[2])
                for t in range(items[0]):
                    time_chart.append(items[1])
                temp.remove(items)
                break

    print(time_chart)
    print()
    pprint(table)
    print()
    print("average turn around time is", numpy.average(turn_around_time))
    print("average waiting time is", numpy.average(waiting_time))


input_info()
gantt_chart(process_list)
