def palindrome(kelime):
    
    return kelime == kelime[::-1]#tersi ile esitse true 

kelime = input("Kelime giriniz: ").lower()

if palindrome(kelime): 
    print("Palindromdur")
else:
    print("Palindrom değildir")