def calculate(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
        else:
            pass
    print("No. of Upper-case characters:",upper_case)
    print("No. of Lower-case characters:",lower_case)

calculate('The quick Brow Fox')