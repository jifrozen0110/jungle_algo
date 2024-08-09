def solve(a: list) -> int:
    sum=0
    for num in a:
        sum+=num
    return sum

def main():
    print(solve([1,2,3]))

if __name__=="__main__":
    main()