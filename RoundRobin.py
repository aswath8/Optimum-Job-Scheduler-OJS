from process import *

def run(p):
    print('\n\n--------------------------------------------------------')
    print('RR')
    i=0
    TQ=5
    print('Time\tProcess')
    RoundRobin=[]
    for t in range(0,p[0].d['burst']*50):
        if len(p)==0:
            break
        if p[i].d['progress']>=p[i].d['burst']:
            print('popped: '+str(i))
            RoundRobin.append(p[i])
            p.pop(i)
            i=i-1 if i>len(p)-1 else i
            #print(i,end='P ')
            #print(len(p))
            continue 
        
        if t%TQ==0:
            pid=p[i].d['pid']
            i+=1
            i=i%(len(p))
            if pid!=p[i].d['pid']:
                p[i].contextSwitch()
            print('---TQ---'+str(i))
        for o in p:
            if o.d['pid']!=p[i].d['pid']:
                p[i].wait()
            else:
                p[i].execute(t)
        print('{0}\t{1}'.format(t,p[i].d['pid']))

    for i in RoundRobin:
        i.calc_TAT()
    report(RoundRobin)
    return RoundRobin[:]

if __name__=='__main__':

    p=[]
    nProcesses=4
    for i in range(1,nProcesses+1):
        p.append(P())

    report(p)

    RR=run(p)
    report(RR)
    graph(RR)
