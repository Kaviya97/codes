# To check whether the number is even or odd or invalid
def main():
    while True:
        a=int(input("<"))
        if(a%2==0):
            print("even")
        elif(a%2!=0):
            print("odd")
        else:
            print("ïnvalid")
if __name__=='__main__':
    main()
