import csv
a = []

print("The given training data set is : ")

with open("enjoysport.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)

num_attributes = len(a[0]) - 1

print("The initial value of hypothesis is ")

S = ['0'] * num_attributes
G = ['?'] * num_attributes

print("The most specific hypothesis is : " , S)
print("The most generic hypothesis is : ", G)


#Comparing with fist training example
for j in range(0,num_attributes):
    S[j] = a[0][j]


#Comparing with remaining training examples
print("Candidate Elimnation Algorithm for Hypothesis Version Space Computation ")

temp = []

for i in range(0,len(a)):
    
    print("-----------------------")
    if a[i][num_attributes] == "Yes":
        
        for j in range(0,num_attributes):
            if a[i][j]!=S[j]:
                S[j] = '?'
        
        for k in range(1,len(temp)):
            for j in range(0,num_attributes):
                if temp[k][j]!='?' and temp[k][j]!=S[j]:
                    del temp[k]
                    
        """
        for j in range(0,num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j] != '?' and temp[k][j] != S[j]:
                    del temp[k]
                    """
        
        print("For training example no {} the hypothesis is S{} ".format(i+1,S))
        
        if len(temp)==0:
            print("For training example No : {} , the hypothesis is G: {}".format(i+1,G))
        else:
            print("For training example No {} , the hypothesis is G: {}".format(i+1,temp))


    if a[i][num_attributes] == "No":
        
        for j in range(0,num_attributes):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j] = S[j]
                temp.append(G)
                G = ['?'] * num_attributes
                

        print("For training example no {} , the hypothesis is S : {}".format(i+1,S))
        print("For training example No. {} , the example hypothesis is G : {}".format(i+1,temp))







