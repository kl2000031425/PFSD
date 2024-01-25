# Try This Python Code to get solution

print("Enter Maximum number of Integer given in question: ", end=' ')
h = int(input())
print("Enter number of times you can ask: ", end=' ')
n = int(input())
if h % 2 != 0:
    h = h + 1
mid = h / 2
j = h / 2
print("\nGuide:\nEnter 1 for largest and 0 for smallest :-)\n")
print("Ask:", mid)
for i in range(1, n):
    j = j / 2

    print("1 or 0 : ", end=' ')
    usr = input()

    if usr == '1':
        mid = mid + j
    elif usr == '0':
        mid = mid - j
    else:
        print("Input error!!\n")
        exit()
    print("Ask:", mid)
print("Congratulation!!!")