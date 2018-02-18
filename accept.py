def acceptor(nameIn , nameOut):
    inDict = open(nameIn, 'r', encoding = 'utf-8')
    outDict = open(nameOut , 'w',encoding = 'utf-8')
    words = inDict.readlines()
    cnt=0

    for word in words:
        if (cnt==0):
            cnt+=2
        else:
            i=0
            outDict.write('0 '+str(cnt)+' '+word[i]+'\n')
            cnt+=1
            
            for i in range(1,len(word)-2):
                outDict.write(str(cnt-1)+' '+str(cnt)+' '+word[i]+'\n')
                cnt+=1
            outDict.write(str(cnt-1)+' '+str(1)+' '+word[i+1]+'\n')
    
    outDict.write(str(1)+'\n')
    inDict.close()
    outDict.close()
    return
### Part - 5 
acceptor('el_caps_noaccent.dict' , 'gr_accept.txt')

### Part - 6
acceptor('en_caps_noaccent.dict' , 'en_accept.txt')
