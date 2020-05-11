from process import P, graph, report


def run(p):
    print('\n\n--------------------------------------------------------')
    print('EDF')
    EDF=[]
    print('\nTime\tProcess')
    i=0
    for t in range(0,p[0].d['burst']*50):
        #if t%p[i].d['period']==0 or True:
        if True:
            pid=p[i].d['pid']
            K1=10 #higher-EDF
            K2=0  #higher-more priority 
            K3=0  #Feedback-long process more importance
            K4=10  #Lesser - more context switch(-ve less context switch) +ve more context switch
            p.sort(key=lambda x: (  K1*(t//x.d['deadline'])*x.d['deadline']+x.d['deadline']-t)  + (K2)*x.d['priority'] + (K3)*(x.d['burst']-x.d['progress']) + K4*x.d['ContextSwitch'], reverse=True)  
            if pid!=p[i].d['pid']:
                p[i].contextSwitch()     
            print('---TQ---'+str(p[0].d['pid']))
        if p[i].d['progress']>=p[i].d['burst']:
            #print('popped: '+str(i))
            EDF.append(p[i])
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
    
    for i in EDF:
        i.calc_TAT()
    return EDF[:]    

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

