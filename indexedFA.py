import math
import pandas as pd
import re

blocks = int(input("Enter no of blocks: "))
block_size = 32  # 32 bytes
choice = 0
index = []
memory_block = ['empty'] * (blocks + 1)
file_allocation_table = {}
while choice != 4:
    print('1. Insert')
    print('2. Delete')
    print('3. Display result')
    print('4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        file_name = str(input("Enter file name: "))
        file_size = int(input("Enter size of the file: "))
        no_of_blocks = math.ceil(file_size / 32)
        empty_blocks = memory_block[:len(memory_block)-1].count("empty")
        count = 0
        index_count = 0
        if no_of_blocks < empty_blocks:
            for itr in range(len(memory_block)):
                if memory_block[itr] == 'empty' and index_count < 1:
                    index_loc = itr
                    memory_block[itr] = file_name+'_index'
                    index_count = index_count + 1
                if memory_block[itr] == 'empty' and count < no_of_blocks:
                    memory_block[itr] = file_name
                    count = count + 1
            for itr in range(len(memory_block)):
                if memory_block[itr] == file_name:
                    index.append(itr)
            memory_block[index_loc] = file_name+'_index: '+str(index)
            file_allocation_table.update({file_name+'_index': index_loc})
            index = []
        else:
            print("No space to allocate!!!")
    elif choice == 2:
        delete_file = str(input("Enter file to be deleted: "))
        del file_allocation_table[delete_file+'_index']
        for itr in range(len(memory_block)):
            if memory_block[itr] == delete_file:
                memory_block[itr] = 'empty'
            if re.match('('+delete_file + '_index).', memory_block[itr]):
                memory_block[itr] = 'empty'
    elif choice == 3:
        print("MEMORY BLOCKS")
        print(pd.DataFrame({'File Names': memory_block[:len(memory_block)-1]}))
        print("--------------------------------------------------------------")
        print("FILE ALLOCATION TABLE")
        print(file_allocation_table)
