x=0
y=0
m=5
n=3
print("Initial state = (0,0)")
print("Capacities = (5,3)")
print("Goal State = (x,y)")
while x!=4:
    r = int(input("Enter the rule number:"))
    if r==1:
        x=m
    elif r==2:
        x=0
    elif r==3:
        y=n
    elif r==4:
        y=0
    elif r==5:
        x+=y
        y=0
    elif r==6:
        y+=x
        x=0
    elif r==7:
        t=m-x
        x=m
        y-=t
    elif r==8:
        t=n-y
        x-=t
        y=n
        
    print('(',x,',',y,')')
    
if x==4:
    print("Goal Reached")
    
    
        
