# To check whether the number is even or odd or invalid
def main():
    while True:
        a=int(input("<"))
        if(a%2==0):
            print("Even")
        elif(a%2!=0):
            print("Odd")
        else:
            print("Invalid")
if __name__=='__main__':
    main()
