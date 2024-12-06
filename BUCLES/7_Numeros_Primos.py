for num in range(2, 51):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=", " if num < 47 else "\n")
