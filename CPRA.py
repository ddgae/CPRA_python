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


def createlist(alist):
    a=[]
    for i in alist:
        if i[0:2] in 'A:':
            i = i.strip('A:')
            i = i.strip('\n')
            i = i.split(',')
            for j in range(len(i)):
                a.append(i[j])
    a.sort()
    b=[]
    for i in alist:
        if i[0:2] in 'B:':
            i = i.strip('B:')
            i = i.strip('\n')
            i = i.split(',')
            for j in range(len(i)):
                b.append(i[j])
    b.sort()
    c = []
    for i in alist:
        if i[0:2] in 'C:':
            i = i.strip('C:')
            i = i.strip('\n')
            i = i.split(',')
            for j in range(len(i)):
                c.append(i[j])
    c.sort()
    dr = []
    for i in alist:
        if i[0:3] in 'DR:':
            i = i.strip('DR:')
            i = i.strip('\n')
            i = i.split(',')
            for j in range(len(i)):
                dr.append(i[j])
    dr.sort()
    dq=[]
    for i in alist:
        if i[0:3] in 'DQ:':
            i = i.strip('DQ:')
            i = i.strip('\n')
            i = i.split(',')
            for j in range(len(i)):
                dq.append(i[j])
    dq.sort()
    cnt =-1
    if a and b:
        listAB1 = pd.DataFrame(np.zeros(((652,1))))
        for k in range(len(a)):
            for m in range(len(b)):
                    #print aa1
                    #print k,m
                    cnt = cnt+1
                    aa1 = [a[k], b[m]]
                    listAB1.iloc[cnt] = ' '.join(aa1)
    listAB1 = list(listAB1.values.flatten())
    #print listAB1[0]
    #print listAB1[1]
    cnt = -1
    if a and c:
        listAC1 = pd.DataFrame(np.zeros(((316, 1))))
        for k in range(len(a)):
            for m in range(len(c)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [a[k], c[m]]
                listAC1.iloc[cnt] = ' '.join(aa1)
    listAC1 = list(listAC1.values.flatten())
    # print listAB1[0]
    #print listAC1
    cnt = -1
    if a and dr:
        listADR1 = pd.DataFrame(np.zeros(((332, 1))))
        for k in range(len(a)):
            for m in range(len(dr)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [a[k], dr[m]]
                listADR1.iloc[cnt] = ' '.join(aa1)
    listADR1 = list(listADR1.values.flatten())
    cnt = -1
    if a and dq:
        listADQ1 = pd.DataFrame(np.zeros(((194, 1))))
        for k in range(len(a)):
            for m in range(len(dq)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [a[k], dq[m]]
                listADQ1.iloc[cnt] = ' '.join(aa1)
    listADQ1 = list(listADQ1.values.flatten())
    cnt = -1
    if b and c:
        listBC1 = pd.DataFrame(np.zeros(((528, 1))))
        for k in range(len(b)):
            for m in range(len(c)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [b[k], c[m]]
                listBC1.iloc[cnt] = ' '.join(aa1)
    listBC1 = list(listBC1.values.flatten())
    cnt = -1
    if b and dr:
        listBDR1 = pd.DataFrame(np.zeros(((573, 1))))
        for k in range(len(b)):
            for m in range(len(dr)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [b[k], dr[m]]
                listBDR1.iloc[cnt] = ' '.join(aa1)
    listBDR1 = list(listBDR1.values.flatten())
    cnt = -1
    if b and dq:
        listBDQ1 = pd.DataFrame(np.zeros(((380, 1))))
        for k in range(len(b)):
            for m in range(len(dq)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [b[k], dq[m]]
                listBDQ1.iloc[cnt] = ' '.join(aa1)
    listBDQ1 = list(listBDQ1.values.flatten())
    cnt = -1
    if dr and c:
        listDRC1 = pd.DataFrame(np.zeros(((257, 1))))
        for k in range(len(dr)):
            for m in range(len(c)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [dr[k], c[m]]
                listDRC1.iloc[cnt] = ' '.join(aa1)
    listDRC1 = list(listDRC1.values.flatten())
    cnt = -1
    if dq and c:
        listDQC1 = pd.DataFrame(np.zeros(((143, 1))))
        for k in range(len(dq)):
            for m in range(len(c)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [dq[k], c[m]]
                listDQC1.iloc[cnt] = ' '.join(aa1)
    listDQC1 = list(listDQC1.values.flatten())
    cnt = -1
    if dr and dq:
        listDRDQ1 = pd.DataFrame(np.zeros(((149, 1))))
        for k in range(len(dr)):
            for m in range(len(dq)):
                # print aa1
                # print k,m
                cnt = cnt + 1
                aa1 = [dr[k], dq[m]]
                listDRDQ1.iloc[cnt] = ' '.join(aa1)
    listDRDQ1 = list(listDRDQ1.values.flatten())
    cnt = -1
    if a and b and c:
        listABC1 = pd.DataFrame(np.zeros(((2630, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k],b[m],c[z]]
                    listABC1.iloc[cnt] = ' '.join(aa1)
    listABC1 = list(listABC1.values.flatten())
    #print listABC1
    cnt = -1
    if a and b and dr:
        listABDR1 = pd.DataFrame(np.zeros(((2988, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dr)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k],b[m],dr[z]]
                    listABDR1.iloc[cnt] = ' '.join(aa1)
    listABDR1 = list(listABDR1.values.flatten())
    cnt = -1
    if a and b and dq:
        listABDQ1 = pd.DataFrame(np.zeros(((2501, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dq)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k], b[m], dq[z]]
                    listABDQ1.iloc[cnt] = ' '.join(aa1)
    listABDQ1 = list(listABDQ1.values.flatten())
    cnt = -1
    if a and dr and c:
        listADRC1 = pd.DataFrame(np.zeros(((2132, 1))))
        for k in range(len(a)):
            for m in range(len(dr)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k], dr[m], c[z]]
                    listADRC1.iloc[cnt] = ' '.join(aa1)
    listADRC1 = list(listADRC1.values.flatten())
    cnt = -1
    if a and dq and c:
        listADQC1 = pd.DataFrame(np.zeros(((1599, 1))))
        for k in range(len(a)):
            for m in range(len(dq)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k], dq[m], c[z]]
                    listADQC1.iloc[cnt] = ' '.join(aa1)
    listADQC1 = list(listADQC1.values.flatten())
    cnt = -1
    if a and dr and dq:
        listADRDQ1 = pd.DataFrame(np.zeros(((1339, 1))))
        for k in range(len(a)):
            for m in range(len(dr)):
                for z in range(len(dq)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [a[k], dr[m], dq[z]]
                    listADRDQ1.iloc[cnt] = ' '.join(aa1)
    listADRDQ1 = list(listADRDQ1.values.flatten())
    cnt = -1
    if b and dr and c:
        listBDRC1 = pd.DataFrame(np.zeros(((2540, 1))))
        for k in range(len(b)):
            for m in range(len(dr)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [b[k], dr[m], c[z]]
                    listBDRC1.iloc[cnt] = ' '.join(aa1)
    listBDRC1 = list(listBDRC1.values.flatten())
    cnt = -1
    if b and dq and c:
        listBDQC1 = pd.DataFrame(np.zeros(((2089, 1))))
        for k in range(len(b)):
            for m in range(len(dq)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [b[k], dq[m], c[z]]
                    listBDQC1.iloc[cnt] = ' '.join(aa1)
    listBDQC1 = list(listBDQC1.values.flatten())
    cnt = -1
    if b and dr and dq:
        listBDRDQ1 = pd.DataFrame(np.zeros(((1933, 1))))
        for k in range(len(b)):
            for m in range(len(dr)):
                for z in range(len(dq)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [b[k], dr[m], dq[z]]
                    listBDRDQ1.iloc[cnt] = ' '.join(aa1)
    listBDRDQ1 = list(listBDRDQ1.values.flatten())
    cnt = -1
    if dr and dq and c:
        listDRDQC1 = pd.DataFrame(np.zeros(((1252, 1))))
        for k in range(len(dr)):
            for m in range(len(dq)):
                for z in range(len(c)):
                    # print aa1
                    # print k,m,z
                    cnt = cnt + 1
                    aa1 = [dr[k], dq[m], c[z]]
                    listDRDQC1.iloc[cnt] = ' '.join(aa1)
    listDRDQC1 = list(listDRDQC1.values.flatten())
    cnt = -1
    if a and b and dr and c:
        listABDRC1 = pd.DataFrame(np.zeros(((5725, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dr)):
                    for q in range(len(c)):
                        # print aa1
                        # print k,m,z
                        cnt = cnt + 1
                        aa1 = [a[k], b[m], dr[z], c[q]]
                        listABDRC1.iloc[cnt] = ' '.join(aa1)
    listABDRC1 = list(listABDRC1.values.flatten())
    cnt = -1
    if a and b and dq and c:
        listABDQC1 = pd.DataFrame(np.zeros(((5391, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dq)):
                    for q in range(len(c)):
                        # print aa1
                        # print k,m,z
                        cnt = cnt + 1
                        aa1 = [a[k], b[m], dq[z], c[q]]
                        listABDQC1.iloc[cnt] = ' '.join(aa1)
    listABDQC1 = list(listABDQC1.values.flatten())
    cnt = -1
    if a and b and dr and dq:
        listABDRDQ1 = pd.DataFrame(np.zeros(((5138, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dr)):
                    for q in range(len(dq)):
                        # print aa1
                        # print k,m,z
                        cnt = cnt + 1
                        aa1 = [a[k], b[m], dr[z], dq[q]]
                        listABDRDQ1.iloc[cnt] = ' '.join(aa1)
    listABDRDQ1 = list(listABDRDQ1.values.flatten())
    cnt = -1
    if a and dr and dq and c:
        listADRDQC1 = pd.DataFrame(np.zeros(((4343, 1))))
        for k in range(len(a)):
            for m in range(len(dr)):
                for z in range(len(dq)):
                    for q in range(len(c)):
                        # print aa1
                        # print k,m,z
                        cnt = cnt + 1
                        aa1 = [a[k], dr[m], dq[z], c[q]]
                        listADRDQC1.iloc[cnt] = ' '.join(aa1)
    listADRDQC1 = list(listADRDQC1.values.flatten())
    cnt = -1
    if b and dr and dq and c:
        listBDRDQC1 = pd.DataFrame(np.zeros(((4592, 1))))
        for k in range(len(b)):
            for m in range(len(dr)):
                for z in range(len(dq)):
                    for q in range(len(c)):
                        # print aa1
                        # print k,m,z
                        cnt = cnt + 1
                        aa1 = [b[k], dr[m], dq[z], c[q]]
                        listBDRDQC1.iloc[cnt] = ' '.join(aa1)
    listBDRDQC1 = list(listBDRDQC1.values.flatten())
    cnt = -1
    if (a and b and dr and dq and c):
        listABDRDQC1 = pd.DataFrame(np.zeros(((7265, 1))))
        for k in range(len(a)):
            for m in range(len(b)):
                for z in range(len(dr)):
                    for q in range(len(dq)):
                        for f in range(len(c)):
                            # print aa1
                            # print k,m,z
                            cnt = cnt + 1
                            aa1 = [a[k], b[m], dr[z], dq[q], c[f]]
                            listABDRDQC1.iloc[cnt] = ' '.join(aa1)
    listABDRDQC1 = list(listABDRDQC1.values.flatten())
    #print listABDRDQC1
    return a,b,c,dr,dq,listAB1,listAC1,listADR1,listADQ1,listBC1,listBDR1,listBDQ1,listDRC1,listDQC1,listDRDQ1,listABC1,listABDR1,listABDQ1,listADRC1,listADQC1,listADRDQ1,listBDRC1,listBDQC1,listBDRDQ1,listDRDQC1,listABDRC1,listABDQC1,listABDRDQ1,listADRDQC1,listBDRDQC1,listABDRDQC1

if __name__ == '__main__':
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

# equivalence of antigen types is listed below but decided not to include in the code because was not in the paper.
# so if the answer you can get from OPTN vs mine is different then I didnt include this in the code.
eqDR51 = [ 'DR2','DR15','DR16','DR51']
eqDR52 = [ 'DR3','DR5','DR6','DR11','DR12','DR13','DR14','DR17','DR18']
eqDR53 = [ 'DR4','DR7','DR9']
eqBw4  = ['B4','B5','B13','B17','B27','B37','B38','B44','B47','B49','B51','B52','B53','B57','B58','B59','B63','B77']
eqBW6 = ['B6','B7','B8','B14','B18','B22','B2708','B35','B39','B40','B41','B42','B45','B48','B50','B4005','B54','B55','B56','B60','B61','B62','B64','B65','B67','B70','B71','B72','B75','B76','B78','B81','B82']
eqCw = ['Cw3','Cw9','Cw10']

# define dictionary
dflistA, dflistB, dflistC, dflistDR, dflistDQ, dflistAB1, dflistAC1, dflistADR1, dflistADQ1, dflistBC1, dflistBDR1, dflistBDQ1, dflistDRC1, dflistDQC1, dflistDRDQ1, dflistABC1, dflistABDR1, dflistABDQ1, dflistADRC1, dflistADQC1, dflistADRDQ1, dflistBDRC1, dflistBDQC1, dflistBDRDQ1, dflistDRDQC1, dflistABDRC1, dflistABDQC1, dflistABDRDQ1, dflistADRDQC1, dflistBDRDQC1, dflistABDRDQC1 = dic.dic()

input_fn = sys.argv[1]
f = open(input_fn,'r')
lines = f.readlines()
f.close()
clist = createlist(lines)

# one locus
# index A
S1a = 0
S1b = 0
S1c = 0
S1d = 0
S2a = 0
S2b = 0
S2c = 0
S2d = 0
S3a = 0
S3b = 0
S3c = 0
S3d = 0
S4a = 0
S4b = 0
S4c = 0
S4d = 0
S5a = 0
S5b = 0
S5c = 0
S5d = 0
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
i = 0
if not clist[0] == ['']:
    for cnt in range((len(clist[0]) - (clist[0].count(0)))):
    #for cnt in xrange((len(clist[0])-(clist[0].count(0)))): python3 version change
            # index position in dflist
            # if listA[cnt-1] == []:
            #        listA.remove([])
            # else:
            #print cnt
            cnt1 = dflistA.index(clist[0][cnt])
            #print cnt1
            S1a += np.sum(A.iloc[cnt1, 1])
            S1b += np.sum(A.iloc[cnt1, 2])
            S1c += np.sum(A.iloc[cnt1, 3])
            S1d += np.sum(A.iloc[cnt1, 4])

if not clist[1] == ['']:
    for cnt in range((len(clist[1])-(clist[1].count(0)))):
    #for cnt in xrange((len(clist[1])-(clist[1].count(0)))): python3 version change
            # index position in dflist
            cnt1 = dflistB.index(clist[1][cnt])
            # print cnt1
            S1a += np.sum(B.iloc[cnt1, 1])
            S1b += np.sum(B.iloc[cnt1, 2])
            S1c += np.sum(B.iloc[cnt1, 3])
            S1d += np.sum(B.iloc[cnt1, 4])
            # print S1a

if not clist[2] == ['']:
    for cnt in range((len(clist[2])-(clist[2].count(0)))):
    #for cnt in xrange((len(clist[2])-(clist[2].count(0)))): python3 version change
            # index position in dflist
            cnt1 = dflistC.index(clist[2][cnt])
            # print cnt1
            S1a += np.sum(C.iloc[cnt1, 1])
            S1b += np.sum(C.iloc[cnt1, 2])
            S1c += np.sum(C.iloc[cnt1, 3])
            S1d += np.sum(C.iloc[cnt1, 4])
            # print S1a

if not clist[3] == ['']:
    for cnt in range((len(clist[3]) - (clist[3].count(0)))):
    #for cnt in xrange((len(clist[3])-(clist[3].count(0)))): python3 version change
            # index position in dflist
            cnt1 = dflistDR.index(clist[3][cnt])
            #print cnt
            #print cnt1
            S1a += np.sum(DR.iloc[cnt1, 1])
            S1b += np.sum(DR.iloc[cnt1, 2])
            S1c += np.sum(DR.iloc[cnt1, 3])
            S1d += np.sum(DR.iloc[cnt1, 4])
            # print S1a

if not clist[4] == ['']:
    for cnt in range((len(clist[4]) - (clist[4].count(0)))):
    #for cnt in xrange((len(clist[4])-(clist[4].count(0)))): python3 version change
            # index position in dflist
            cnt1 = dflistDQ.index(clist[4][cnt])
            # print cnt1
            S1a += np.sum(DQ.iloc[cnt1, 1])
            S1b += np.sum(DQ.iloc[cnt1, 2])
            S1c += np.sum(DQ.iloc[cnt1, 3])
            S1d += np.sum(DQ.iloc[cnt1, 4])
            # print S1a


# two locus
# AB
if not clist[5] == ['']:
    for cnt2 in range((len(clist[5]) - (clist[5].count(0)))):
    #for cnt2 in xrange((len(clist[5])-(clist[5].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistAB1.index(clist[5][cnt2])
            # col1.append(int(column))
            S2a += np.sum(AB.iloc[column, 2])
            S2b += np.sum(AB.iloc[column, 3])
            S2c += np.sum(AB.iloc[column, 4])
            S2d += np.sum(AB.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue
        #print dflistAB1.index(clist[5][cnt2])
        #print clist[5]

# AC
if not clist[6] == ['']:
    for cnt2 in range((len(clist[6]) - (clist[6].count(0)))):
    #for cnt2 in xrange((len(clist[6]) - (clist[6].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistAC1.index(clist[6][cnt2])
            # col1.append(int(column))
            S2a += np.sum(AC.iloc[column, 2])
            S2b += np.sum(AC.iloc[column, 3])
            S2c += np.sum(AC.iloc[column, 4])
            S2d += np.sum(AC.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# ADR
if not clist[7] == ['']:
    for cnt2 in range((len(clist[7]) - (clist[7].count(0)))):
    #for cnt2 in xrange((len(clist[7]) - (clist[7].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistADR1.index(clist[7][cnt2])
            # col1.append(int(column))
            S2a += np.sum(ADR.iloc[column, 2])
            S2b += np.sum(ADR.iloc[column, 3])
            S2c += np.sum(ADR.iloc[column, 4])
            S2d += np.sum(ADR.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# ADQ
if not clist[8] == ['']:
    for cnt2 in range((len(clist[8]) - (clist[8].count(0)))):
    #for cnt2 in xrange((len(clist[8]) - (clist[8].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistADQ1.index(clist[8][cnt2])
            # col1.append(int(column))
            S2a += np.sum(ADQ.iloc[column, 2])
            S2b += np.sum(ADQ.iloc[column, 3])
            S2c += np.sum(ADQ.iloc[column, 4])
            S2d += np.sum(ADQ.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# BC
if not clist[9] == ['']:
    for cnt2 in range((len(clist[9]) - (clist[9].count(0)))):
    #for cnt2 in xrange((len(clist[9]) - (clist[9].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistBC1.index(clist[9][cnt2])
            # col1.append(int(column))
            S2a += np.sum(BC.iloc[column, 2])
            S2b += np.sum(BC.iloc[column, 3])
            S2c += np.sum(BC.iloc[column, 4])
            S2d += np.sum(BC.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# BDR
if not clist[10] == ['']:
    for cnt2 in range((len(clist[10]) - (clist[10].count(0)))):
    #for cnt2 in xrange((len(clist[10]) - (clist[10].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistBDR1.index(clist[10][cnt2])
            # col1.append(int(column))
            S2a += np.sum(BDR.iloc[column, 2])
            S2b += np.sum(BDR.iloc[column, 3])
            S2c += np.sum(BDR.iloc[column, 4])
            S2d += np.sum(BDR.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# BDQ
if not clist[11] == ['']:
    for cnt2 in range((len(clist[10]) - (clist[10].count(0)))):
    #for cnt2 in xrange((len(clist[11]) - (clist[11].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistBDQ1.index(clist[11][cnt2])
            # col1.append(int(column))
            S2a += np.sum(BDQ.iloc[column, 2])
            S2b += np.sum(BDQ.iloc[column, 3])
            S2c += np.sum(BDQ.iloc[column, 4])
            S2d += np.sum(BDQ.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# DRC
if not clist[12] == ['']:
    for cnt2 in range((len(clist[12]) - (clist[12].count(0)))):
    #for cnt2 in xrange((len(clist[12]) - (clist[12].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistDRC1.index(clist[12][cnt2])
            # col1.append(int(column))
            S2a += np.sum(DRC.iloc[column, 2])
            S2b += np.sum(DRC.iloc[column, 3])
            S2c += np.sum(DRC.iloc[column, 4])
            S2d += np.sum(DRC.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# DQC
if not clist[13] == ['']:
    for cnt2 in range((len(clist[13]) - (clist[13].count(0)))):
    #for cnt2 in xrange((len(clist[13]) - (clist[13].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistDQC1.index(clist[13][cnt2])
            # col1.append(int(column))
            S2a += np.sum(DQC.iloc[column, 2])
            S2b += np.sum(DQC.iloc[column, 3])
            S2c += np.sum(DQC.iloc[column, 4])
            S2d += np.sum(DQC.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

# DRDQ
if not clist[14] == ['']:
    for cnt2 in range((len(clist[14]) - (clist[14].count(0)))):
    #for cnt2 in xrange((len(clist[14]) - (clist[14].count(0)))): python3 version change
        # index position in dflist
        try:
            column = dflistDRDQ1.index(clist[14][cnt2])
            # col1.append(int(column))
            S2a += np.sum(DRDQ.iloc[column, 2])
            S2b += np.sum(DRDQ.iloc[column, 3])
            S2c += np.sum(DRDQ.iloc[column, 4])
            S2d += np.sum(DRDQ.iloc[column, 5])
            # print S2a
            # print column
        except ValueError:
            continue

#three
# ABC
if not clist[15] == ['']:
    for cnt3 in range((len(clist[15]) - (clist[15].count(0)))):
    #for cnt3 in xrange((len(clist[15]) - (clist[15].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistABC1.index(clist[15][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ABC.iloc[column2, 3])
            S3b += np.sum(ABC.iloc[column2, 4])
            S3c += np.sum(ABC.iloc[column2, 5])
            S3d += np.sum(ABC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# ABDR
if not clist[16] == ['']:
    for cnt3 in range((len(clist[16]) - (clist[16].count(0)))):
    #for cnt3 in xrange((len(clist[16]) - (clist[16].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistABDR1.index(clist[16][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ABDR.iloc[column2, 3])
            S3b += np.sum(ABDR.iloc[column2, 4])
            S3c += np.sum(ABDR.iloc[column2, 5])
            S3d += np.sum(ABDR.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# ABDQ
if not clist[17] == ['']:
    for cnt3 in range((len(clist[17]) - (clist[17].count(0)))):
    #for cnt3 in xrange((len(clist[17]) - (clist[17].count(0)))): python3 version change
    # index position in dflist
        try:
            column2 = dflistABDQ1.index(clist[17][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ABDQ.iloc[column2, 3])
            S3b += np.sum(ABDQ.iloc[column2, 4])
            S3c += np.sum(ABDQ.iloc[column2, 5])
            S3d += np.sum(ABDQ.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# ADRC
if not clist[18] == ['']:
    for cnt3 in range((len(clist[18]) - (clist[18].count(0)))):
    #for cnt3 in xrange((len(clist[18]) - (clist[18].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistADRC1.index(clist[18][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ADRC.iloc[column2, 3])
            S3b += np.sum(ADRC.iloc[column2, 4])
            S3c += np.sum(ADRC.iloc[column2, 5])
            S3d += np.sum(ADRC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# ADQC
if not clist[19] == ['']:
    for cnt3 in range((len(clist[19]) - (clist[19].count(0)))):
    #for cnt3 in xrange((len(clist[19]) - (clist[19].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistADQC1.index(clist[19][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ADQC.iloc[column2, 3])
            S3b += np.sum(ADQC.iloc[column2, 4])
            S3c += np.sum(ADQC.iloc[column2, 5])
            S3d += np.sum(ADQC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# ADRDQ
if not clist[20] == ['']:
    for cnt3 in range((len(clist[20]) - (clist[20].count(0)))):
    #for cnt3 in xrange((len(clist[20]) - (clist[20].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistADRDQ1.index(clist[20][cnt3])
            # col1.append(int(column))
            S3a += np.sum(ADRDQ.iloc[column2, 3])
            S3b += np.sum(ADRDQ.iloc[column2, 4])
            S3c += np.sum(ADRDQ.iloc[column2, 5])
            S3d += np.sum(ADRDQ.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# BDRC
if not clist[21] == ['']:
    for cnt3 in range((len(clist[21]) - (clist[21].count(0)))):
    #for cnt3 in xrange((len(clist[21]) - (clist[21].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistBDRC1.index(clist[21][cnt3])
            # col1.append(int(column))
            S3a += np.sum(BDRC.iloc[column2, 3])
            S3b += np.sum(BDRC.iloc[column2, 4])
            S3c += np.sum(BDRC.iloc[column2, 5])
            S3d += np.sum(BDRC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# BDQC
if not clist[22] == ['']:
    for cnt3 in range((len(clist[22]) - (clist[22].count(0)))):
    #for cnt3 in xrange((len(clist[22]) - (clist[22].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistBDQC1.index(clist[22][cnt3])
            # col1.append(int(column))
            S3a += np.sum(BDQC.iloc[column2, 3])
            S3b += np.sum(BDQC.iloc[column2, 4])
            S3c += np.sum(BDQC.iloc[column2, 5])
            S3d += np.sum(BDQC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# BDRDQ
if not clist[23] == ['']:
    for cnt3 in range((len(clist[23]) - (clist[23].count(0)))):
    #for cnt3 in xrange((len(clist[23]) - (clist[23].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistBDRDQ1.index(clist[23][cnt3])
            # col1.append(int(column))
            S3a += np.sum(BDRDQ.iloc[column2, 3])
            S3b += np.sum(BDRDQ.iloc[column2, 4])
            S3c += np.sum(BDRDQ.iloc[column2, 5])
            S3d += np.sum(BDRDQ.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# DRDQC
if not clist[24] == ['']:
    for cnt3 in range((len(clist[24]) - (clist[24].count(0)))):
    #for cnt3 in xrange((len(clist[24]) - (clist[24].count(0)))): python3 version change
        # index position in dflist
        try:
            column2 = dflistDRDQC1.index(clist[24][cnt3])
            # col1.append(int(column))
            S3a += np.sum(DRDQC.iloc[column2, 3])
            S3b += np.sum(DRDQC.iloc[column2, 4])
            S3c += np.sum(DRDQC.iloc[column2, 5])
            S3d += np.sum(DRDQC.iloc[column2, 6])
            # print S2a
            # print column
        except ValueError:
            continue

# 4 locus
# ABDRC
if not clist[25] == ['']:
    for cnt4 in range((len(clist[25]) - (clist[25].count(0)))):
    #for cnt4 in xrange((len(clist[25]) - (clist[25].count(0)))): python3 version change
        # index position in dflist
        try:
            column3 = dflistABDRC1.index(clist[25][cnt4])
            # col1.append(int(column))
            S4a += np.sum(ABDRC.iloc[column3, 4])
            S4b += np.sum(ABDRC.iloc[column3, 5])
            S4c += np.sum(ABDRC.iloc[column3, 6])
            S4d += np.sum(ABDRC.iloc[column3, 7])
            # print S2a
            # print column
        except ValueError:
            continue

# ABDQC
if not clist[26] == ['']:
    for cnt4 in range((len(clist[26]) - (clist[26].count(0)))):
    #for cnt4 in xrange((len(clist[26]) - (clist[26].count(0)))): python3 version change
        # index position in dflist
        try:
            column3 = dflistABDQC1.index(clist[26][cnt4])
            # col1.append(int(column))
            S4a += np.sum(ABDQC.iloc[column3, 4])
            S4b += np.sum(ABDQC.iloc[column3, 5])
            S4c += np.sum(ABDQC.iloc[column3, 6])
            S4d += np.sum(ABDQC.iloc[column3, 7])
            # print S2a
            # print column
        except ValueError:
            continue

# ABDRDQ
if not clist[27] == ['']:
    for cnt4 in range((len(clist[27]) - (clist[27].count(0)))):
    #for cnt4 in xrange((len(clist[27]) - (clist[27].count(0)))): python3 version change
        # index position in dflist
        try:
            column3 = dflistABDRDQ1.index(clist[27][cnt4])
            # col1.append(int(column))
            S4a += np.sum(ABDRDQ.iloc[column3, 4])
            S4b += np.sum(ABDRDQ.iloc[column3, 5])
            S4c += np.sum(ABDRDQ.iloc[column3, 6])
            S4d += np.sum(ABDRDQ.iloc[column3, 7])
            # print S2a
            # print column
        except ValueError:
            continue

# ADRDQC
if not clist[28] == ['']:
    for cnt4 in range((len(clist[28]) - (clist[28].count(0)))):
    #for cnt4 in xrange((len(clist[28]) - (clist[28].count(0)))): python3 version change
        # index position in dflist
        try:
            column3 = dflistADRDQC1.index(clist[28][cnt4])
            # col1.append(int(column))
            S4a += np.sum(ADRDQC.iloc[column3, 4])
            S4b += np.sum(ADRDQC.iloc[column3, 5])
            S4c += np.sum(ADRDQC.iloc[column3, 6])
            S4d += np.sum(ADRDQC.iloc[column3, 7])
            #print S4a
            # print column
        except ValueError:
            continue

# BDRDQC
if not clist[29] == ['']:
    for cnt4 in range((len(clist[29]) - (clist[29].count(0)))):
    #for cnt4 in xrange((len(clist[29]) - (clist[29].count(0)))): python3 version change
        # index position in dflist
        try:
            column3 = dflistBDRDQC1.index(clist[29][cnt4])
            # col1.append(int(column))
            S4a += np.sum(BDRDQC.iloc[column3, 4])
            S4b += np.sum(BDRDQC.iloc[column3, 5])
            S4c += np.sum(BDRDQC.iloc[column3, 6])
            S4d += np.sum(BDRDQC.iloc[column3, 7])
            # print S2a
            # print column
        except ValueError:
            continue

# 5 locus
# ABDRDQC
if not clist[30] == ['']:
    for cnt5 in range((len(clist[30]) - (clist[30].count(0)))):
    #for cnt5 in xrange((len(clist[30]) - (clist[30].count(0)))): python3 version change
        # index position in dflist
        try:
            column4 = dflistABDRDQC1.index(clist[30][cnt5])
            # col1.append(int(column))
            S5a += np.sum(ABDRDQC.iloc[column4, 4])
            S5b += np.sum(ABDRDQC.iloc[column4, 5])
            S5c += np.sum(ABDRDQC.iloc[column4, 6])
            S5d += np.sum(ABDRDQC.iloc[column4, 7])
            # print S2a
            # print column
        except ValueError:
            continue

pos = 1 - (1 - S1a + S2a - S3a + S4a - S5a) ** 2
pos1 = 1 - (1 - S1b + S2b - S3b + S4b - S5b) ** 2
pos2 = 1 - (1 - S1c + S2c - S3c + S4c - S5c) ** 2
pos3 = 1 - (1 - S1d + S1d - S3d + S4d - S5d) ** 2
CPRA = (pos * 0.687 + pos1 * 0.147 + pos2 * 0.143 + pos3 * 0.023) * 100
print(CPRA)

