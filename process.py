from random import randint
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class P:
    def __init__(self,title="Title"):
        self.d={}
        self.d['pid']=randint(100,999)
        self.d['AT']=0
        self.d['burst']=randint(1,100)
        self.d['deadline']=randint(1,7)
        self.d['period']=randint(1,3)
        self.d['priority']=randint(1,5)
        self.d['progress']=0
        self.d['WT']=0
        self.d['TAT']=0
        self.d['ContextSwitch']=0
        self.d['RT']=0
    
    def execute(self,t):
        if self.d['progress']==0:
            self.d['RT']=t-self.d['AT']
        self.d['progress']+=1

    def contextSwitch(self):
        self.d['ContextSwitch']+=1

    def wait(self):
        self.d['WT']+=1
    
    def calc_TAT(self):
        self.d['TAT']=self.d['WT']+self.d['burst']

    def details(self):
        print('PID:'+str(self.d['pid']))
        print('AT:'+str(self.d['AT']))
        print('Burst:'+str(self.d['burst']))
        print('Deadline:'+str(self.d['deadline']))
        print('Period:'+str(self.d['period']))
        print('Progress:'+str(self.d['progress']))
        print('Wait:'+str(self.d['WT']))
        print('CntxtSwtch:'+str(self.d['ContextSwitch']))

    def avg(self,p):
        self.d['pid']=999
        self.d['WT']=0
        self.d['TAT']=0
        self.d['ContextSwitch']=0
        self.d['RT']=0
        for i in p:
            self.d['WT']+=i.d['WT']
            self.d['TAT']+=i.d['TAT']
            self.d['ContextSwitch']+=i.d['ContextSwitch']
            self.d['RT']+=i.d['RT']
        self.d['WT']/=len(p)
        self.d['TAT']/=len(p)
        self.d['ContextSwitch']/=len(p)
        self.d['RT']/=len(p)   

    
def report(p):
    l=list(p[0].d.keys())
    #print(*l, sep='\t')
    p.sort(key=lambda x: x.d['pid'], reverse=False)
    print()
    for j in l:
        print("\n"+"{: <10}:".format(j.upper()),end='')
        for i in p:
            print('{: >0}'.format(i.d[j]), end = '\t')
    print()

def graph(p,title="Title"):
    global ax
    avgP = P()
    avgP.avg(p)
    p.append(avgP)
    p.sort(key=lambda x: x.d['pid'], reverse=False)
    labels = [x.d['pid'] for x in p]
    

    WT = [x.d['WT'] for x in p]
    TAT = [x.d['TAT'] for x in p]
    context_switch = [x.d['ContextSwitch'] for x in p]
    responseTime = [x.d['RT'] for x in p]


    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars

    fig, ax = plt.subplots()
    fig.canvas.set_window_title(title)
    rects1 = ax.bar(x + width, WT, width, label='WT')
    rects2 = ax.bar(x + 2*width, TAT, width, label='TAT')
    rects3 = ax.bar(x + 3*width, context_switch, width, label='no. of Context Switch')
    rects3 = ax.bar(x + 4*width, responseTime, width, label='Response Time')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title(title+'\nScores by WT and TAT')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    plt.show(block=False)


def autolabel(rects):
    global ax
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x(), height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


