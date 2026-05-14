actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

tp,tn,fp,fn = 0 ,0,0,0

for i in range(len(actual)):
    if(actual[i]==1 and predicted[i]==1):
        tp = tp +1
    elif(actual[i]==0 and predicted[i]==0):
        tn = tn +1
    elif(actual[i]==1 and predicted[i]==0):
        fn = fn + 1
    else:
        fp = fp+1

print(f"True Positive  =  {tp}\nTrue Negative  =  {tn}\nFalse Positive  =  {fp}\nFalse Negative  =  {fn}")