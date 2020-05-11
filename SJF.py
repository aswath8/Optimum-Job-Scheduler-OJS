from process import P, graph, report


def run(p):
    print('\n\n--------------------------------------------------------')
    print('SJF')
    SJF=[]
    print('\nTime\tProcess')
    i=0
    p.sort(key=lambda x: x.d['burst'], reverse=True)  
    for t in range(0,p[0].d['burst']*50):
        if p[i].d['progress']>=p[i].d['burst']:
            #print('popped: '+str(i))
            SJF.append(p[i])
            p.pop(i)
        if len(p)==0:
            break
        for o in p:
            if o.d['pid']!=p[i].d['pid']:
                p[i].wait()
            else:
                p[i].execute(t)
        #print('{0}\t{1}'.format(t,p[i].pid))
        print(p[i].d['pid'],end='|')
    
    for i in SJF:
        i.calc_TAT()
    return SJF[:]    

if __name__=='__main__':
    p=[]
    nProcesses=4
    for i in range(1,nProcesses+1):
        p.append(P())
    print('No. of processes: '+str(len(p)))
    TQ=5


    report(p)
        

    for i in p:
        print('\nProcess:'+str(i.d['pid'])+' ',end=' ')
        for t in range(1,100):
            c='*' if t%i.d['deadline']==0 else '-'
            print(c,end='')
        


    EDF=run(p)

    report(EDF)
    graph(EDF)

