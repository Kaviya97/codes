# To check whether the character is a vowel or a consonant
while True:
    a=input(">")
    if(64<ord(a)<90)or(95<ord(a)<122):
        if a in 'aeiou':
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("invalid")
    

        
    
