l=[]
n=int(input("enter the numbers :"))
print("enter the alphabets :")
for i in range(15):
    ele=str(input())
    l.append(ele)
print('list of alphabets',l)

vowels=[]
consonants=[]

for j in l:
    if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
        vowels.append(j)
    else:
        consonants.append(j)

print(vowels)
print(consonants)
