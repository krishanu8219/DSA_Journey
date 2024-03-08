def sum_of_digits(a,b):
    return a +b

def main():
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum_of_digits(a,b))

main()