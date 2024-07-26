import os   # based | telechargée avec python
fileList = os.listdir("C:\\Users\\School.LAPTOP-GN5E6HKO\\Downloads\\") #store all file 
for i in fileList :
    #print (i)
    
    scrap = i.split(".")    #split
    print (scrap)
    if len(scrap) >= 2 : 
        print(scrap[-1])    #take last digit | prend le dernier element de la liste
    else :
        print("folder",i)

