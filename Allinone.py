import EDF
import FCFS
import RoundRobin
import SJF
import OJS
from process import *
import matplotlib.pyplot as plt
import copy
import pickle


p=[]
'''
nProcesses=4
for i in range(1,nProcesses+1):
    p.append(P())

with open('process', 'wb') as config_dictionary_file:
  pickle.dump(p, config_dictionary_file)
'''
with open('process', 'rb') as config_dictionary_file:
     p = pickle.load(config_dictionary_file)
     print("Loaded File ",p)

pFCFS=copy.deepcopy(p)
pRR=copy.deepcopy(p)
pEDF=copy.deepcopy(p)
pSJF=copy.deepcopy(p)
pOJS=copy.deepcopy(p)

pFCFS=FCFS.run(pFCFS)
report(pFCFS)
graph(pFCFS,"FCFS")

pRR=RoundRobin.run(pRR)
report(pRR)
graph(pRR,"RR")

pEDF=EDF.run(pEDF)
report(pEDF)
graph(pEDF,"EDF")

pSJF=SJF.run(pSJF)
report(pSJF)
graph(pSJF,"SJF")

pOJS=OJS.run(pOJS)
report(pOJS)
graph(pOJS,"OJS")

plt.show()