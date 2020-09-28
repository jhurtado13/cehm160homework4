##my attempt at  war, i'm aware that it is by far not the most efficient way
## of programming this function, but I gave it my best effort, knowing that I am clearly
## missing the key to making this much more simple.

## also not 100% it even functions correctly

from cards import *
ntrials = 10000
p1cards=0
p2cards=0
ties=[]
winsby0=0
wby2=[]
winsby2=0
wby4=[]
winsby4=0
wby6=[]
winsby6=0
wby8=[]
winsby8=0
wby10=[]
winsby10=0
wby12=[]
winsby12=0
wby14=[]
winsby14=0
wby16=[]
winsby16=0
wby18=[]
winsby18=0
wby20=[]
winsby20=0
wby22=[]
winsby22=0
wby24=[]
winsby24=0
wby26=[]
winsby26=0
wby28=[]
winsby28=0
wby30=[]
winsby30=0
wby32=[]
winsby32=0
wby34=[]
winsby34=0
wby36=[]
winsby36=0
wby38=[]
winsby38=0
wby40=[]
winsby40=0
wby42=[]
winsby42=0
wby44=[]
winsby44=0
wby46=[]
winsby46=0
wby48=[]
winsby48=0
wby50=[]
winsby50=0
wby52=[]
winsby52=0
for i in range (ntrials):
    p1deck=deck()
    p2deck=deck()
    p1deck.shuffle()
    p2deck.shuffle()
    while p1deck.cardsleft and p2deck.cardsleft() >0:
        p1card=p1deck.dealcard()
        p2card=p2deck.dealcard()
        if p1card.value()>p2card.value():
            p1cards+=2
        if p1card.value()<p2card.value():
            p2cards+=2
        else:
            p1cards+=1
            p2cards+=1
    if p1cards-p2cards==0 or p2cards-p1cards==0:
        winsby0+=1
        ties.append(winsby0/ntrials)
        maxties=max(ties)
    if p1cards-p2cards==2 or p2cards-p1cards==2:
        winsby2+=1
        wby2.append(winsby2/ntrials)
        mwb2=max(wby2)
    if p1cards-p2cards==4 or p2cards-p1cards==4:
        winsby4+=1
        wby4.append(winsby4/ntrials)
        mwb4=max(wby4)
    if p1cards-p2cards==6 or p2cards-p1cards==6:
        winsby6+=1
        wby6.append(winsby6/ntrials)
        mwb6=max(wby6)
    if p1cards-p2cards==8 or p2cards-p1cards==8:
        winsby8+=1
        wby8.append(winsby8/ntrials)
        mwb8=max(wby8)
    if p1cards-p2cards==10 or p2cards-p1cards==10:
        winsby10+=1
        wby10.append(winsby10/ntrials)
        mwb10=max(wby10)
    if p1cards-p2cards==12 or p2cards-p1cards==12:
        winsby12+=1
        wby12.append(winsby12/ntrials)
        mwb12=max(wby12)
    if p1cards-p2cards==14 or p2cards-p1cards==14:
        winsby14+=1
        wby14.append(winsby14/ntrials)
        mwb14=max(wby14)
    if p1cards-p2cards==16 or p2cards-p1cards==16:
        winsby16+=1
        wby16.append(winsby16/ntrials)
        mwb16=max(wby16)
    if p1cards-p2cards==18 or p2cards-p1cards==18:
        winsby18+=1
        wby18.append(winsby18/ntrials)
        mwb18=max(wby18)
    if p1cards-p2cards==20 or p2cards-p1cards==20:
        winsby20+=1
        wby20.append(winsby20/ntrials)
        mwb20=max(wby20)
    if p1cards-p2cards==22 or p2cards-p1cards==22:
        winsby22+=1
        wby22.append(winsby22/ntrials)
        mwb22=max(wby22)
    if p1cards-p2cards==24 or p2cards-p1cards==24:
        winsby24+=1
        wby24.append(winsby24/ntrials)
        mwb24=max(wby24)
    if p1cards-p2cards==26 or p2cards-p1cards==26:
        winsby26+=1
        wby26.append(winsby26/ntrials)
        mwb26=max(wby26)
    if p1cards-p2cards==228 or p2cards-p1cards==28:
        winsby28+=1
        wby28.append(winsby28/ntrials)
        mwb28=max(wby28)
    if p1cards-p2cards==30 or p2cards-p1cards==30:
        winsby30+=1
        wby30.append(winsby30/ntrials)
        mwb30=max(wby30)
    if p1cards-p2cards==32 or p2cards-p1cards==32:
        winsby32+=1
        wby32.append(winsby32/ntrials)
        mwb32=max(wby32)
    if p1cards-p2cards==34 or p2cards-p1cards==34:
        winsby34+=1
        wby34.append(winsby34/ntrials)
        mwb34=max(wby34)
    if p1cards-p2cards==36 or p2cards-p1cards==36:
        winsby36+=1
        wby36.append(winsby36/ntrials)
        mwb36=max(wby36)
    if p1cards-p2cards==38 or p2cards-p1cards==38:
        winsby38+=1
        wby38.append(winsby6/ntrials)
        mwb38=max(wby38)
    if p1cards-p2cards==40 or p2cards-p1cards==40:
        winsby40+=1
        wby40.append(winsby40/ntrials)
        mwb40=max(wby40)
    if p1cards-p2cards==42 or p2cards-p1cards==42:
        winsby42+=1
        wby42.append(winsby42/ntrials)
        mwb42=max(wby42)
    if p1cards-p2cards==44 or p2cards-p1cards==44:
        winsby44+=1
        wby44.append(winsby44/ntrials)
        mwb44=max(wby44)
    if p1cards-p2cards==46 or p2cards-p1cards==46:
        winsby46+=1
        wby46.append(winsby46/ntrials)
        mwb46=max(wby46)
    if p1cards-p2cards==48 or p2cards-p1cards==48:
        winsby48+=1
        wby48.append(winsby48/ntrials)
        mwb48=max(wby48)
    if p1cards-p2cards==50 or p2cards-p1cards==50:
        winsby50+=1
        wby50.append(winsby50/ntrials)
        mwb50=max(wby50)
    if p1cards-p2cards==52 or p2cards-p1cards==52:
        winsby52+=1
        wby52.append(winsby52/ntrials)
        mwb52=max(wby52)
        
    



print("0",maxties*100)
print("2",mwb2)
print("4",mwb4)
print("6",mwb6)
print("8",mwb8)
print("10",mwb10)
print("12",mwb12)
print("14",mwb14)
print("16",mwb16)
print("18",mwb18)
print("20",mwb20)
print("22",mwb22)
print("24",mwb24)
print("26",mwb26)
print("28",mwb28)
print("30",mwb30)
print("32",mwb32)
print("34",mwb34)
print("36",mwb36)
print("38",mwb38)
print("40",mwb40)
print("42",mwb42)
print("44",mwb44)
print("46",mwb46)
print("48",mwb48)
print("50",mwb50)
print("52",mwb52)

        
        
    

    
            
            
        
    
