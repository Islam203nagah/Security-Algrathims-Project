import pyfiglet,termcolor
def EncryptionVigenere(word,key):
    cipherchar=[]
    if len(key)==len(word):
        for w in range(0,len(word)):
            c=ord(word[w])-97
            ke=ord(key[w])-97
            total=(c+ke)%26
            cipherchar.append(chr(total+97))
        final=''.join(cipherchar)
        return final
    else:
        if len(key)>len(word):
            newKey=list(key[0:len(word)])
        else:
            newKey=list(key)
        cipherchar=[]
        i=0#index char of key    
        for editk in range(len(word)-len(key)):
            newKey.append(key[i])
            i=(i+1)%len(key)   
        print("the edit key: ".capitalize()+''.join(newKey))
        for w in range(len(word)):
            c=ord(word[w])-97
            k=ord(newKey[w])-97
            total=(c+k)%26
            cipherchar.append(chr(total+97))
        final=''.join(cipherchar)
        return final

def DecryptionVigenere(cipword,key):
   
    Decrcipherchar=[]
    if len(key)==len(cipword):
        for w in range(0,len(cipword)):
            c=ord(cipword[w])-97
            k=ord(key[w])-97
            total=((c-k)+26)%26
            Decrcipherchar.append(chr(total+97))
        final=''.join(Decrcipherchar)
        return final
    else: 
        if len(key)>len(cipword):
            EditKey=list(key[0:len(cipword)])
        else:
            EditKey=list(key)
        i=0#index char of key    
        for editk in range(len(cipword)-len(key)):
            EditKey.append(key[i])
            i=(i+1)%len(key)  
        print("the orginal key : ".capitalize()+''.join(EditKey))
        for w in range(len(cipword)):
            c=ord(cipword[w])-97
            k=ord(EditKey[w])-97
            total=((c-k)+26)%26
            Decrcipherchar.append(chr(total+97))
        final=''.join(Decrcipherchar)
        return final
def mainVigenere():
    playfair=pyfiglet.figlet_format("PlayFair : )")
    print(termcolor.colored(playfair,color='yellow'))
    choice=True
    while choice==True:
        ChoiceDec=input('A-Encryption\nB-Decryption\nplease enter your choice A OR B: ').upper()  
        if ChoiceDec=='A':
            encryption=pyfiglet.figlet_format("Encryption")
            print(termcolor.colored(encryption,color='magenta'))
            text=input('please enter your text: ').lower().replace(' ','')
            Key=input('enter your key: ').lower()
            if text.isalpha() and Key.isalpha():
                Ctext=EncryptionVigenere(text,Key)
                print('the text encryption is: ',Ctext)
            else: print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (alphabet) with no symbols text: ({text}) , Key: ({Key})'.capitalize(),color="red"))
            choice=input(termcolor.colored('wold you want do try again Y/N : '.capitalize(),color="green")).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Vigenere : (')
                print(termcolor.colored(End,color='red'))
                choice=False
                
        elif ChoiceDec=='B':
            decryption=pyfiglet.figlet_format("Decryption")
            print(termcolor.colored(decryption,color='cyan'))
            ciptext=input('please enter your ciphertext: ').lower().replace(' ','')
            Key=input('enter your key: ').lower()
            if ciptext.isalpha() and Key.isalpha():
                plaintext=DecryptionVigenere(ciptext,Key)
                print("your plaintext is: ",plaintext)
            else:
                print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (alphabet) with no symbols text: ({text}) , Key: ({Key})'.capitalize(),color="red"))
            choice=input(termcolor.colored('wold you want do try again Y/N : '.capitalize(),color="green")).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Vigenere : (')
                print(termcolor.colored(End,color='red'))
                choice=False
                
        else:
            print(termcolor.colored('worring choice'.upper(),color="red"))
            choice=input(termcolor.colored('This is not valid choice, wold you want do try again Y/N : '.capitalize(),color="green")).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Vigenere : (')
                print(termcolor.colored(End,color='red'))
                choice=False


