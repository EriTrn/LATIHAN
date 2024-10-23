def print_pattern(x):
    alphabet = "ABCDE"
    for i in range(1, x+1):
        print(alphabet[:i] + alphabet[:i-1][::-1])
def main():
    print_pattern(5)
if __name__ == '__main__':
    main()