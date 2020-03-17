#mbed_hw1_107061210_楊皓淯

import csv                                                         # import module

cwb_filename = '107061210.csv'                                     # the target csv document

data = []
header = []
with open(cwb_filename) as csvfile:                                # read the data
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)                                           # data[] store the 107061210.csv data

    sum = list(range(5))    
    out = list(range(5))
    station = list(range(5))

    station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']   # the appointed output

    for i in range(5):                                             # find the sum in station[]
        sum[i] = 0
        for row in data :
            if row['station_id'] == station[i]:                    # determine the sum
                if row['HUMD'] == '-99.000' :
                    sum[i] = 0
                elif row['HUMD'] == '-999.000':
                    sum[i] = 0
                else :    
                    sum[i] += float(row['HUMD'])
        if sum[i] == 0 :      
            out[i] = [station[i], 'None']                         # sum == 0 mean its data was deleted
        else :
            out[i] = [station[i], sum[i]]

    out.sort()                                                    # sort the output list to make it in the lexicographical order 

    print(out)

