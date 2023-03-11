import cesearAlgorithm , playfairAlgorithm , AutoKeyAlgorithm , VigenereCipherAlgorithm,termcolor,pyfiglet


Ciphertext=pyfiglet.figlet_format("Ciphertext : )")
print(termcolor.colored(Ciphertext,color='green'))
stopPro=True
while stopPro:
    print("1-Cesear\n2-Playfair\n3-Auto Key\n4-Vigenere Cipher")
    AlgoChoice=input("please choice number of algorithm: ".capitalize())
    if AlgoChoice=='1':
        cesearAlgorithm.mainCesear()
        anotherAlg=input(termcolor.colored('do you want choice another algorithm y/n: '.capitalize(),color="green")).upper()
        if anotherAlg=="Y":
            stopPro=True  
        else :
            End=pyfiglet.figlet_format('End Program : (')
            print(termcolor.colored(End,color='red'))
            stopPro=False

    elif AlgoChoice=='2':
        playfairAlgorithm.mainPlayFair()
        anotherAlg=input(termcolor.colored('do you want choice another algorithm y/n: '.capitalize(),color="green")).upper()
        if anotherAlg=="Y":
            stopPro=True  
        else :           
            End=pyfiglet.figlet_format('End Program : (')
            print(termcolor.colored(End,color='red'))
            stopPro=False
    elif AlgoChoice=='3':
        AutoKeyAlgorithm.mainAutoKey()
        anotherAlg=input(termcolor.colored('do you want choice another algorithm y/n: '.capitalize(),color="green")).upper()
        if anotherAlg=="Y":
            stopPro=True  
        else :           
            End=pyfiglet.figlet_format('End Program : (')
            print(termcolor.colored(End,color='red'))
            stopPro=False
    elif AlgoChoice=='4':
        VigenereCipherAlgorithm.mainVigenere()
        anotherAlg=input(termcolor.colored('do you want choice another algorithm y/n: '.capitalize(),color="green")).upper()
        if anotherAlg=="Y":
            stopPro=True  
        else :           
            End=pyfiglet.figlet_format('End Program : (')
            print(termcolor.colored(End,color='red'))
            stopPro=False
    else: 
        print(termcolor.colored('woring choice please enter valide choice'.upper(),color='red'))
        Woringchoic=input(termcolor.colored('This is not valid choice, wold you want do try again Y/N : '.capitalize(),color='green')).upper()
        if Woringchoic=='Y':
            stopPro=True
        else:
            End=pyfiglet.figlet_format('End Program : (')
            print(termcolor.colored(End,color='red'))
            stopPro=False

