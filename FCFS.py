from process import *

def run(p):
    FCFS=[]
    print('\n\n--------------------------------------------------------')
    print('FCFS')
    i=0
    p.sort(key=lambda x: x.d['AT'], reverse=False)
    print('Time\tProcess')
    for t in range(1,p[0].d['burst']*50):
        if p[i].d['progress']>=p[i].d['burst']:
            pid=p[i].d['pid']
            FCFS.append(p[i])
            if i+1>=len(p):
                break
            i+=1
            print('list index out of range: ',i,'len of p ',len(p))
            if pid!=p[i].d['pid']:
                p[i].contextSwitch()
        for o in p:
            if o.d['pid']!=p[i].d['pid']:
                p[i].wait()
            else:
                p[i].execute(t)
        print('{0}\t{1}'.format(t,p[i].d['pid']))    
    for i in FCFS:
        i.calc_TAT()
    report(FCFS)
    return FCFS[:]

if __name__=='__main__':

    p=[]
    nProcesses=4
    for i in range(1,nProcesses+1):
        p.append(P())

    report(p)
    FCFS=run(p)
    report(FCFS)
    graph(FCFS)