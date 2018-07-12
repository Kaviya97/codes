# To check whether the character is a vowel or a consonant
while True:
    a=input(">")
    if(64<ord(a)<91)or(95<ord(a)<123):
        if a in 'aeiou':
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("invalid")
    

        
    
