amount = int(input("enter amount "))
n500 = amount // 500 
amount-=n500 * 500
n100 = amount // 100
amount-=n100 * 100
n50 = amount // 50
amount-=n50 * 50
n20 = amount//20
amount-=n20 * 20
n10 = amount//10
amount-=n10*10
n5 = amount//5
amount -= n5*5
n1 = amount // 1
print("No of 500 notes : ", n500)
print("No of 100 notes :", n100)
print("No of 50 notes :", n50)
print("No of 20 notes :", n20)
print("No of 10 notes :", n10)
print("No of 5 notes : ", n5)
print("No of 1 notes :", n1)





''' another method to calculate no of notes'''
print("-----------------------another method------------------------")

amount = int(input("enter amount "))
n500 = amount // 500 
amount = amount%500
n100 = amount // 100
amount = amount%100
n50 = amount // 50
amount = amount%50
n20 = amount//20
amount = amount%20
n10 = amount//10
amount%=10
n5 = amount//5
amount %=5
n1 = amount//1
print("No of 500 notes : ", n500)
print("No of 100 notes :", n100)
print("No of 50 notes :", n50)
print("No of 20 notes :", n20)
print("No of 10 notes :", n10)
print("No of 5 notes : ", n5)
print("No of 1 notes :", n1)

