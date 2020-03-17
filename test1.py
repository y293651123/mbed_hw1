import csv

cwb_filename = '107061210.csv'

data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)

    sum1 = 0
    for row in data :
        if row['station_id'] == 'C0A880':
            if row['HUMD'] == '-99.000' :
                sum1 = 0
            elif row['HUMD'] == '-999.000':
                sum1 = 0
            else :    
                sum1 += float(row['HUMD'])
    out1 = ['C0A880', sum1]

    sum2 = 0
    for row in data :
        if row['station_id'] == 'C0F9A0':
            if row['HUMD'] == '-99.000' :
                sum2 = 0
            elif row['HUMD'] == '-999.000':
                sum2 = 0
            else :    
                sum2 += float(row['HUMD'])
    out2 = ['C0F9A0', sum2]
    
    sum3 = 0
    for row in data :
        if row['station_id'] == 'C0G640':
            if row['HUMD'] == '-99.000' :
                sum3 = 0
            elif row['HUMD'] == '-999.000':
                sum3 = 0
            else :    
                sum3 += float(row['HUMD'])
    out3 = ['C0G640', sum3]

    sum4 = 0
    for row in data :
        if row['station_id'] == 'C0R190' :
            if row['HUMD'] == '-99.000' :
                sum4 = 0
            elif row['HUMD'] == '-999.000':
                sum4 = 0
            else :    
                sum4 += float(row['HUMD'])
    out4 = ['C0R190', sum4]

    sum5 = 0
    for row in data :
        if row['station_id'] == 'C0X260' :
            if row['HUMD'] == '-99.000' :
                sum5 = 0
            elif row['HUMD'] == '-999.000':
                sum5 = 0
            else :    
                sum5 += float(row['HUMD'])
    out5 = ['C0X260', sum5]

    print( out1,"\n",out2,"\n",out3,"\n",out4,"\n",out5,"\n")


