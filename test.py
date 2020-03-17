import csv

cwb_filename = '107061210.csv'

data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)

    def summation(Input) :
        Output = 0

        if Input == '-99.000' or '-999.000' :
            Output = 0
        else :    
            Output += float(Input)

        return Output 

    for i in range(5) :
        sum[i] = 0
        out[i] = ['', 0]

    for row in data :
        if row['station_id'] == 'C0A880':
            sum[0] += summation(row['HUMD'])
    out[0] = ['C0A880', sum[0]]        

    for row in data :
        if row['station_id'] == 'C0F9A0':
            sum[1] += summation(row['HUMD'])
    out[1] = ['C0F9A0', sum[1]]

    for row in data :
        if row['station_id'] == 'C0G640':
            sum[2] += summation(row['HUMD'])
    out[2] = ['C0G640', sum[2]]

    for row in data :
        if row['station_id'] == 'C0R190':
            sum[3] += summation(row['HUMD'])
    out[3] = ['C0R190', sum[3]]

    for row in data :
        if row['station_id'] == 'C0X260':
            sum[4] += summation(row['HUMD'])
    out[4] = ['C0X260', sum[4]]

    for i in range(5) :
        if sum[i] == 0 :
            print('None')
        else :
            print(out[i])

