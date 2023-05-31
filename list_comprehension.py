

## List comprehension syntax with one value and one for loop:-
#* Adding the numbers into the list by normal approach:-
l=[]
for i in range(1,11):
    l.append(i)
print(l)





#* Adding the numbers into the list by List comprehension:-
l=[i for i in range(1,11)]
print(l)





#* Adding the squares numbers into the list by List comprehension:-
l=[i**2 for i in range(1,11)]
l=[i*i for i in range(1,11)]
print(l)





## List comprehension syntax with one value and one for loop and one if condition:-
#* Adding the even numbers into the list by normal approach:-
l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)






#* Adding the even numbers into the list by List comprehension-
l=[i for i in range(1,11) if i%2==0]
print(l)





## List comprehension syntax with one value and one for loop and multiple if condition:-
#* from the given tuple add only even numbers which are greater than 50 into the list in normal approach:-
t=(11,78,34,23,67,90,70)
l=[]
for i in t:
    if i%2==0 and i>50:
        l.append(i)
print(l)






#* from the given tuple add only even numbers which are greater than 50 into the list in List comprehension:-
t=(11,78,34,23,67,90,70)
l=[i for i in t if i%2==0 and i>50]
print(l)





#* from the given tuple add even numbers and odd numbers which are greater than 30 in List comprehension:-
t=(11,78,34,23,67,90,70)
l=[i for i in t if i%2==0 or i>30]
print(l)






## List comprehension syntax with one value and one for loop and one if-else condition:-
#* Adding 1 in even position and 0 in odd position
t=(11,22,100,23,44,60)
l=[ 1 if i%2==0 else 0 for i in t]
print(l)






#* if it is non-negetive and more than 5:-
l=[1,2,3,-99,55,66,-100,5]
l1=[i for i in l if i>0 and i>5]
print(l1)






## List comprehension syntax with one value and multiple for loop and one if condition:-

#* O/P:- [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]]
#~ Method-1
l=[]
for i in range(1,11):
    l.append([i]*3)
print(l)






#~ Method-2
l=[]
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if i==j==k:
                l.append([i,j,k])
print(l)






#^ using list comprehension
#~ Method-1
l=[[i,j,k] for i in range(1,11) for j in range(1,11) for k in range(1,11) if i==j==k]
print(l)





#~ Method-2
l=[[i]*3 for i in range(1,11)]
print(l)
