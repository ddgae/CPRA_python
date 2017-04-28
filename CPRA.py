""" copyright 2017 David Gae
    University of California, San Francisco
    usage: python CPRA.py test.txt
"""
#!/opt/local/bin/python
import sys,os
import numpy as np
import pandas as pd
import dictionary as dic
#define frequency arrays
A  = pd.read_csv('./FREQ/A.csv')
B  = pd.read_csv('./FREQ/B.csv')
C  = pd.read_csv('./FREQ/C.csv')
DR = pd.read_csv('./FREQ/DR.csv')
DQ = pd.read_csv('./FREQ/DQ.csv')
#two
AB = pd.read_csv('./FREQ/AB.csv')
AC = pd.read_csv('./FREQ/AC.csv')
ADR= pd.read_csv('./FREQ/ADR.csv')
ADQ= pd.read_csv('./FREQ/ADQ.csv')
BC = pd.read_csv('./FREQ/BC.csv')
BDR= pd.read_csv('./FREQ/BDR.csv')
BDQ= pd.read_csv('./FREQ/BDQ.csv')
DRC= pd.read_csv('./FREQ/DRC.csv')
DQC= pd.read_csv('./FREQ/DQC.csv')
DRDQ= pd.read_csv('./FREQ/DRDQ.csv')
#three
ABC = pd.read_csv('./FREQ/ABC.csv')
ABDR = pd.read_csv('./FREQ/ABDR.csv')
ABDQ = pd.read_csv('./FREQ/ABDQ.csv')
ADRC = pd.read_csv('./FREQ/ADQC.csv')
ADQC = pd.read_csv('./FREQ/ADRC.csv')
ADRDQ = pd.read_csv('./FREQ/ADRDQ.csv')
BDRC = pd.read_csv('./FREQ/BDRC.csv')
BDQC = pd.read_csv('./FREQ/BDQC.csv')
BDRDQ = pd.read_csv('./FREQ/BDRDQ.csv')
DRDQC = pd.read_csv('./FREQ/DRDQC.csv')
#four
ABDRC= pd.read_csv('./FREQ/ABDRC.csv')
ABDQC= pd.read_csv('./FREQ/ABDQC.csv')
ABDRDQ= pd.read_csv('./FREQ/ABDRDQ.csv')
ADRDQC= pd.read_csv('./FREQ/ADRDQC.csv')
BDRDQC= pd.read_csv('./FREQ/BDRDQC.csv')

#five
ABDRDQC = pd.read_csv('./FREQ/ABDRDQC.csv')


eqDR51 = [ 'DR2','DR15','DR16','DR51']
eqDR52 = [ 'DR3','DR5','DR6','DR11','DR12','DR13','DR14','DR17','DR18']
eqDR53 = [ 'DR4','DR7','DR9']
eqBw4  = ['B4','B5','B13','B17','B27','B37','B38','B44','B47','B49','B51','B52','B53','B57','B58','B59','B63','B77']
eqBW6 = ['B6','B7','B8','B14','B18','B22','B2708','B35','B39','B40','B41','B42','B45','B48','B50','B4005','B54','B55','B56','B60','B61','B62','B64','B65','B67','B70','B71','B72','B75','B76','B78','B81','B82']
eqCw = ['Cw3','Cw9','Cw10']

#define dictionary
dflistA,dflistB,dflistC,dflistDR,dflistDQ,dflistAB1,dflistAC1,dflistADR1,dflistADQ1,dflistBC1,dflistBDR1,dflistBDQ1, dflistDRC1, dflistDQC1,dflistDRDQ1,dflistABC1,dflistABDR1, dflistABDQ1, dflistADRC1,dflistADQC1,dflistADRDQ1,dflistBDRC1,dflistBDQC1,dflistBDRDQ1,dflistDRDQC1,dflistABDRC1,dflistABDQC1,dflistABDRDQ1,dflistADRDQC1,dflistBDRDQC1,dflistABDRDQC1 = dic.dic()


#input_fn =sys.argv[1]
input_fn = sys.argv[1]
f = open(input_fn,'r')
lines = f.readlines()
f.close()

#empty string
listA = []
listB = []
listC = []
listDR = []
listDQ = []
listAB1 = []
listAC1 = []
listADR1= []
listADQ1= []
listBC1 = []
listBDR1= []
listBDQ1= []
listDRC1= []
listDQC1= []
listDRDQ1= []
listABC1 = []
listABDR1 = []
listABDQ1 = []
listADRC1 = []
listADQC1 = []
listADRDQ1 = []
listBDRC1 = []
listBDQC1 = []
listBDRDQ1 = []
listDRDQC1 = []
listABDRC1 = []
listABDQC1= []
listABDRDQ1= []
listADRDQC1= []
listBDRDQC1= []
listABDRDQC1 =[]

for i in lines:
    if i[0:2] == 'A:':
	i = i.strip('A:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listA.append(i[j])
    if i[0:2] == 'B:':
	i = i.strip('B:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listB.append(i[j])
    if i[0:2] == 'C:':
	i = i.strip('C:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listC.append(i[j])
    if i[0:3] == 'DR:':
	i = i.strip('DR:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDR.append(i[j])
    if i[0:3] == 'DQ:':
	i = i.strip('DQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDQ.append(i[j])
    if i[0:3] == 'AB:':
	i = i.strip('AB:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listAB1.append(i[j])
    if i[0:3] == 'AC:':
	i = i.strip('AC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listAC1.append(i[j])
    if i[0:4] == 'ADR:':
	i = i.strip('ADR:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADR1.append(i[j])
    if i[0:4] == 'ADQ:':
	i = i.strip('ADQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADQ1.append(i[j])
    if i[0:4] == 'BC:':
	i = i.strip('BC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBC1.append(i[j])
    if i[0:4] == 'BDR:':
	i = i.strip('BDR:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDR1.append(i[j])
    if i[0:4] == 'BDQ:':
	i = i.strip('BDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDQ1.append(i[j])
    if i[0:4] == 'DRC:':
	i = i.strip('DRC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDRC1.append(i[j])
    if i[0:4] == 'DQC:':
	i = i.strip('DQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDQC1.append(i[j])
    if i[0:5] == 'DRDQ:':
	i = i.strip('DRDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDRDQ1.append(i[j])
    if i[0:4] == 'ABC:':
	i = i.strip('ABC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABC1.append(i[j])
    if i[0:5] == 'ABDR:':
	i = i.strip('ABDR:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDR1.append(i[j])
    if i[0:5] == 'ABDQ:':
	i = i.strip('ABDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDQ1.append(i[j])
    if i[0:5] == 'ADRC:':
	i = i.strip('ADRC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADRC1.append(i[j])
    if i[0:5] == 'ADQC:':
	i = i.strip('ADQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADQC1.append(i[j])
    if i[0:6] == 'ADRDQ:':
	i = i.strip('ADRDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADRDQ1.append(i[j])
    if i[0:5] == 'BDRC:':
	i = i.strip('BDRC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDRC1.append(i[j])
    if i[0:5] == 'BDQC:':
	i = i.strip('BDQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDQC1.append(i[j])
    if i[0:6] == 'BDRDQ:':
	i = i.strip('BDRDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDRDQ1.append(i[j])
    if i[0:6] == 'DRDQC:':
	i = i.strip('DRDQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listDRDQC1.append(i[j])
    if i[0:6] == 'ABDRC:':
	i = i.strip('ABDRC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDRC1.append(i[j])
    if i[0:6] == 'ABDQC:':
	i = i.strip('ABDQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDQC1.append(i[j])
    if i[0:7] == 'ABDRDQ:':
	i = i.strip('ABDRDQ:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDRDQ1.append(i[j])
    if i[0:7] == 'ADRDQC:':
	i = i.strip('ADRDQC1:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listADRDQC1.append(i[j])
    if i[0:7] == 'BDRDQC:':
	i = i.strip('BDRDQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listBDRDQC1.append(i[j])
    if i[0:7] == 'ABDRDQC:':
	i = i.strip('ABDRDQC:')
        i = i.strip('\n')
        i = i.split(',')
	for j in range(len(i)):
           listABDRDQC1.append(i[j])

listA.sort()
listB.sort()
listC.sort()
listDR.sort()
listDQ.sort()
listAB1.sort()
listAC1.sort()
listADR1.sort()
listADQ1.sort()
listBC1.sort()
listBDR1.sort()
listBDQ1.sort()
listDRC1.sort()
listDQC1.sort()
listDRDQ1.sort()
listABC1.sort()
listABDR1.sort()
listABDQ1.sort()
listADRC1.sort()
listADQC1.sort()
listADRDQ1.sort()
listBDRC1.sort()
listBDQC1.sort()
listBDRDQ1.sort()
listDRDQC1.sort()
listABDRC1.sort()
listABDQC1.sort()
listABDRDQ1.sort()
listADRDQC1.sort()
listBDRDQC1.sort()
listABDRDQC1.sort()

# one locus
#index A
S1a=0
S1b=0
S1c=0
S1d=0
S2a=0
S2b=0
S2c=0
S2d=0
S3a=0
S3b=0
S3c=0
S3d=0
S4a=0
S4b=0
S4c=0
S4d=0
S5a=0
S5b=0
S5c=0
S5d=0
cnt=0
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
i=0
for cnt in xrange(len(listA)):
    #index position in dflist
    #if listA[cnt-1] == []:
    #        listA.remove([])
    #else:
    cnt1 = dflistA.index(listA[cnt-1])
    #print cnt1
    S1a += np.sum(A.iloc[cnt1,1])
    S1b += np.sum(A.iloc[cnt1,2])
    S1c += np.sum(A.iloc[cnt1,3])
    S1d += np.sum(A.iloc[cnt1,4])
    #print S1a


#index B
for cnt in xrange(len(listB)):
    #index position in dflist
    cnt1 = dflistB.index(listB[cnt-1])
    #print cnt1
    S1a += np.sum(B.iloc[cnt1,1])
    S1b += np.sum(B.iloc[cnt1,2])
    S1c += np.sum(B.iloc[cnt1,3])
    S1d += np.sum(B.iloc[cnt1,4])
    #print S1a


#index C
for cnt in xrange(len(listC)):
    #index position in dflist
    cnt1 = dflistC.index(listC[cnt-1])
    #print cnt1
    S1a += np.sum(C.iloc[cnt1,1])
    S1b += np.sum(C.iloc[cnt1,2])
    S1c += np.sum(C.iloc[cnt1,3])
    S1d += np.sum(C.iloc[cnt1,4])
    #print S1a


#index DR
for cnt in xrange(len(listDR)):
    #index position in dflist
    cnt1 = dflistDR.index(listDR[cnt-1])
    #print cnt1
    S1a += np.sum(DR.iloc[cnt1,1])
    S1b += np.sum(DR.iloc[cnt1,2])
    S1c += np.sum(DR.iloc[cnt1,3])
    S1d += np.sum(DR.iloc[cnt1,4])
    #print S1a
 

#index DQ
for cnt in xrange(len(listDQ)):
    #index position in dflist
    cnt1 = dflistDQ.index(listDQ[cnt-1])
    #print cnt1
    S1a += np.sum(DQ.iloc[cnt1,1])
    S1b += np.sum(DQ.iloc[cnt1,2])
    S1c += np.sum(DQ.iloc[cnt1,3])
    S1d += np.sum(DQ.iloc[cnt1,4])
    #print S1a



#two locus
#AB
for cnt2, i in enumerate(listAB1):
    #index position in dflist
	try:
	  column = dflistAB1.index(listAB1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(AB.iloc[column,2])
	  S2b += np.sum(AB.iloc[column,3])
	  S2c += np.sum(AB.iloc[column,4])
	  S2d += np.sum(AB.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue

#AC
for cnt2, i in enumerate(listAC1):
    #index position in dflist
	try:
	  column = dflistAC1.index(listAC1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(AC.iloc[column,2])
	  S2b += np.sum(AC.iloc[column,3])
	  S2c += np.sum(AC.iloc[column,4])
	  S2d += np.sum(AC.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue
#ADR
for cnt2, i in enumerate(listADR1):
    #index position in dflist
	try:
	  column = dflistADR1.index(listADR1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(ADR.iloc[column,2])
	  S2b += np.sum(ADR.iloc[column,3])
	  S2c += np.sum(ADR.iloc[column,4])
	  S2d += np.sum(ADR.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue
#ADQ
for cnt2, i in enumerate(listADQ1):
    #index position in dflist
	try:
	  column = dflistADQ1.index(listADQ1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(ADQ.iloc[column,2])
	  S2b += np.sum(ADQ.iloc[column,3])
	  S2c += np.sum(ADQ.iloc[column,4])
	  S2d += np.sum(ADQ.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue
#BC
for cnt2, i in enumerate(listBC1):
    #index position in dflist
	try:
	  column = dflistBC1.index(listBC1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(BC.iloc[column,2])
	  S2b += np.sum(BC.iloc[column,3])
	  S2c += np.sum(BC.iloc[column,4])
	  S2d += np.sum(BC.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue
#BDR
for cnt2, i in enumerate(listBDR1):
    #index position in dflist
	try:
	  column = dflistBDR1.index(listBDR1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(BDR.iloc[column,2])
	  S2b += np.sum(BDR.iloc[column,3])
	  S2c += np.sum(BDR.iloc[column,4])
	  S2d += np.sum(BDR.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue

#BDQ
for cnt2, i in enumerate(listBDQ1):
    #index position in dflist
	try:
	  column = dflistBDQ1.index(listBDQ1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(BDQ.iloc[column,2])
	  S2b += np.sum(BDQ.iloc[column,3])
	  S2c += np.sum(BDQ.iloc[column,4])
	  S2d += np.sum(BDQ.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue

#DRC
for cnt2, i in enumerate(listDRC1):
    #index position in dflist
	try:
	  column = dflistDRC1.index(listDRC1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(DRC.iloc[column,2])
	  S2b += np.sum(DRC.iloc[column,3])
	  S2c += np.sum(DRC.iloc[column,4])
	  S2d += np.sum(DRC.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue


#DQC
for cnt2, i in enumerate(listDQC1):
    #index position in dflist
	try:
	  column = dflistDQC1.index(listDQC1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(DQC.iloc[column,2])
	  S2b += np.sum(DQC.iloc[column,3])
	  S2c += np.sum(DQC.iloc[column,4])
	  S2d += np.sum(DQC.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue


#DRDQ
for cnt2, i in enumerate(listDRDQ1):
    #index position in dflist
	try:
	  column = dflistDQC1.index(listDRDQ1[cnt2])
	  #col1.append(int(column))
	  S2a += np.sum(DRDQ.iloc[column,2])
	  S2b += np.sum(DRDQ.iloc[column,3])
	  S2c += np.sum(DRDQ.iloc[column,4])
	  S2d += np.sum(DRDQ.iloc[column,5])
	  #print S2a
	  #print column 
	except ValueError:
		continue


#ABC
for cnt3, i in enumerate(listABC1):
    #index position in dflist
	try:
	  column2 = dflistABC1.index(listABC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ABC.iloc[column2,3])
	  S3b += np.sum(ABC.iloc[column2,4])
	  S3c += np.sum(ABC.iloc[column2,5])
	  S3d += np.sum(ABC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue

#ABDR
for cnt3, i in enumerate(listABDR1):
    #index position in dflist
	try:
	  column2 = dflistABDR1.index(listABDR1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ABDR.iloc[column2,3])
	  S3b += np.sum(ABDR.iloc[column2,4])
	  S3c += np.sum(ABDR.iloc[column2,5])
	  S3d += np.sum(ABDR.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#ABDQ
for cnt3, i in enumerate(listABDQ1):
    #index position in dflist
	try:
	  column2 = dflistABDQ1.index(listABDQ1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ABDQ.iloc[column2,3])
	  S3b += np.sum(ABDQ.iloc[column2,4])
	  S3c += np.sum(ABDQ.iloc[column2,5])
	  S3d += np.sum(ABDQ.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue



#ADRC
for cnt3, i in enumerate(listADRC1):
    #index position in dflist
	try:
	  column2 = dflistADRC1.index(listADRC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ADRC.iloc[column2,3])
	  S3b += np.sum(ADRC.iloc[column2,4])
	  S3c += np.sum(ADRC.iloc[column2,5])
	  S3d += np.sum(ADRC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#ADQC
for cnt3, i in enumerate(listADQC1):
    #index position in dflist
	try:
	  column2 = dflistADQC1.index(listADQC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ADQC.iloc[column2,3])
	  S3b += np.sum(ADQC.iloc[column2,4])
	  S3c += np.sum(ADQC.iloc[column2,5])
	  S3d += np.sum(ADQC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#ADRDQ
for cnt3, i in enumerate(listADRDQ1):
    #index position in dflist
	try:
	  column2 = dflistADRDQ1.index(listADRDQ1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(ADRDQ.iloc[column2,3])
	  S3b += np.sum(ADRDQ.iloc[column2,4])
	  S3c += np.sum(ADRDQ.iloc[column2,5])
	  S3d += np.sum(ADRDQ.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#BDRC
for cnt3, i in enumerate(listBDRC1):
    #index position in dflist
	try:
	  column2 = dflistBDRC1.index(listBDRC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(BDRC.iloc[column2,3])
	  S3b += np.sum(BDRC.iloc[column2,4])
	  S3c += np.sum(BDRC.iloc[column2,5])
	  S3d += np.sum(BDRC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#BDQC
for cnt3, i in enumerate(listBDQC1):
    #index position in dflist
	try:
	  column2 = dflistBDQC1.index(listBDQC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(BDQC.iloc[column2,3])
	  S3b += np.sum(BDQC.iloc[column2,4])
	  S3c += np.sum(BDQC.iloc[column2,5])
	  S3d += np.sum(BDQC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#BDRDQ
for cnt3, i in enumerate(listBDRDQ1):
    #index position in dflist
	try:
	  column2 = dflistBDRDQ1.index(listBDRDQ1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(BDRDQ.iloc[column2,3])
	  S3b += np.sum(BDRDQ.iloc[column2,4])
	  S3c += np.sum(BDRDQ.iloc[column2,5])
	  S3d += np.sum(BDRDQ.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue



#DRDQC
for cnt3, i in enumerate(listDRDQC1):
    #index position in dflist
	try:
	  column2 = dflistDRDQC1.index(listDRDQC1[cnt3])
	  #col1.append(int(column))
	  S3a += np.sum(DRDQC.iloc[column2,3])
	  S3b += np.sum(DRDQC.iloc[column2,4])
	  S3c += np.sum(DRDQC.iloc[column2,5])
	  S3d += np.sum(DRDQC.iloc[column2,6])
	  #print S2a
	  #print column
	except ValueError:
		continue


#4 locus
#ABDRC
for cnt4, i in enumerate(listABDRC1):
    #index position in dflist
	try:
	  column3 = dflistABDRC1.index(listABDRC1[cnt4])
	  #col1.append(int(column))
	  S4a += np.sum(ABDRC.iloc[column3,4])
	  S4b += np.sum(ABDRC.iloc[column3,5])
	  S4c += np.sum(ABDRC.iloc[column3,6])
	  S4d += np.sum(ABDRC.iloc[column3,7])
	  #print S2a
	  #print column
	except ValueError:
		continue


#ABDQC
for cnt4, i in enumerate(listABDQC1):
    #index position in dflist
	try:
	  column3 = dflistABDQC1.index(listABDQC1[cnt4])
	  #col1.append(int(column))
	  S4a += np.sum(ABDQC.iloc[column3,4])
	  S4b += np.sum(ABDQC.iloc[column3,5])
	  S4c += np.sum(ABDQC.iloc[column3,6])
	  S4d += np.sum(ABDQC.iloc[column3,7])
	  #print S2a
	  #print column
	except ValueError:
		continue



#ABDRDQ
for cnt4, i in enumerate(listABDRDQ1):
    #index position in dflist
	try:
	  column3 = dflistABDRDQ1.index(listABDRDQ1[cnt4])
	  #col1.append(int(column))
	  S4a += np.sum(ABDRDQ.iloc[column3,4])
	  S4b += np.sum(ABDRDQ.iloc[column3,5])
	  S4c += np.sum(ABDRDQ.iloc[column3,6])
	  S4d += np.sum(ABDRDQ.iloc[column3,7])
	  #print S2a
	  #print column
	except ValueError:
		continue



#ADRDQC
for cnt4, i in enumerate(listADRDQC1):
    #index position in dflist
	try:
	  column3 = dflistADRDQC1.index(listADRDQC1[cnt4])
	  #col1.append(int(column))
	  S4a += np.sum(ADRDQC.iloc[column3,4])
	  S4b += np.sum(ADRDQC.iloc[column3,5])
	  S4c += np.sum(ADRDQC.iloc[column3,6])
	  S4d += np.sum(ADRDQC.iloc[column3,7])
	  #print S2a
	  #print column
	except ValueError:
		continue



#BDRDQC
for cnt4, i in enumerate(listBDRDQC1):
    #index position in dflist
	try:
	  column3 = dflistBDRDQC1.index(listBDRDQC1[cnt4])
	  #col1.append(int(column))
	  S4a += np.sum(BDRDQC.iloc[column3,4])
	  S4b += np.sum(BDRDQC.iloc[column3,5])
	  S4c += np.sum(BDRDQC.iloc[column3,6])
	  S4d += np.sum(BDRDQC.iloc[column3,7])
	  #print S2a
	  #print column
	except ValueError:
		continue


#5 locus
#ABDRDQC
for cnt5, i in enumerate(listABDRDQC1):
    #index position in dflist
	try:
	  column4 = dflistABDRDQC1.index(listABDRDQC1[cnt5])
	  #col1.append(int(column))
	  S5a += np.sum(ABDRDQC.iloc[column4,4])
	  S5b += np.sum(ABDRDQC.iloc[column4,5])
	  S5c += np.sum(ABDRDQC.iloc[column4,6])
	  S5d += np.sum(ABDRDQC.iloc[column4,7])
	  #print S2a
	  #print column
	except ValueError:
		continue

pos = 1 -(1-S1a+S2a-S3a+S4a-S5a)**2
pos1 = 1 - (1-S1b+S2b-S3b+S4b-S5b)**2
pos2 = 1 -(1-S1c+S2c-S3c+S4c-S5c)**2
pos3 = 1 - (1-S1d+S1d-S3d+S4d-S5d)**2
CPRA = (pos*0.687 + pos1*0.147 + pos2*0.143 + pos3*0.023)*100
print CPRA
