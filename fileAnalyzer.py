import json
import numpy
import pandas as pd
signsList = list()
file = open('file.txt')
for i in range(500):
    pageList = json.loads(file.readline())
    signsList.extend(pageList[1:])
file.close()

l = numpy.array(signsList)
df = pd.DataFrame(l,columns=['company','model','tream','kilometer','year','price'])

###### Q1
# new1 = df[df.company=="peugeot"]
# new2 = df[df.company=="hyundai"]
# print(set(new1['model']), set(new2['model']))

###### Q2
# q2_1_shamsi = df.loc[df['year']>1394]
# q2_2_shamsi = q2_1_shamsi.loc[q2_1_shamsi['year']<1402] #6916
# q2_1_miladi = df.loc[df['year']<2022]
# q2_2_miladi = q2_1_miladi.loc[q2_1_miladi['year']>2015] #2899
# print(len(q2_2_miladi), len(q2_2_shamsi))
# print(2899 + 6916)

##### Q3
# peguet206_SD_df = df[df['model']=='206sd']
# print(peguet206_SD_df.describe())
# print(set(peguet206_SD_df['tream']))

##### Q4
# print(df.max(axis=0)) # 930000 kilometer


##### Q5
# p = df.groupby('company')
# print((p['price'].mean().sort_values()))

###### Q6
# print(df.describe())

##### Q7
# car_206_df = df[df.model=='206']
# car_206_df_1 = car_206_df.loc[1384<car_206_df.year]
# car_206_df_1 = car_206_df_1.loc[car_206_df_1.year<1393]
# avrj_85_92 = car_206_df_1.mean().price
# print(avrj_85_92)
# car_206_df_new = car_206_df.loc[1392<car_206_df.year]
# car_206_df_new = car_206_df_new.loc[car_206_df_new.year<1401]
# avrj_93_01 = car_206_df_new.mean().price
# print(avrj_93_01)
# print(avrj_93_01 - avrj_85_92)
