# def TextValid(trueOrFulse):
# alphaUppper='ABCDEFGHIJKLMNOPQRSTUVXYZ'
# alphaLower='abcdefghijklmnopqrstuvxyz'
#     listTrues=[]
#     for f in trueOrFulse:
#         if alpha.find(f)==-1:
#             listTrues.append(False)
#         else: listTrues.append(True)
#     if all(listTrues):
#         return True
#     else: return False
########################################################




######################################
# ########## Encryption ############ #
######################################

import termcolor
import pyfiglet

def EncrLowerChr(chL,keylower):  
    ChTextLower=((ord(chL)+keylower-97)%26)+97
    return chr(ChTextLower)

    
def EncryptUpper(chU,keyUpper):
    ChtextUpper=(((ord(chU)+keyUpper)-65)%26)+65
    return chr(ChtextUpper)

        
#################################################
# ################ Decryption################## # 
#################################################   
def DecrLowerChr(DchL,Dekeylower):  
    ChTextLower=(((ord(DchL)-Dekeylower-97))%26)+97
    return chr(ChTextLower)  
    

def DecrUpperChr(DchU,Dekeyupper):  
    ChTextUpper=(((ord(DchU)-Dekeyupper-65))%26)+65
    return chr(ChTextUpper)  
    

def mainCesear():
    caesar=pyfiglet.figlet_format("Caesar : )")
    print(termcolor.colored(caesar,color='red'))
    choice=True
    while choice==True: 
        ChoiceDec=input('A-Encryption\nB-Decryption\nplease enter your choice A OR B: ').upper()  
        if ChoiceDec=='A':
            encryption=pyfiglet.figlet_format("Encryption")
            print(termcolor.colored(encryption,color='magenta'))
            text=input('please enter your text: ').replace(' ','')
            Key=input('enter your key: ')
            if  text.isalpha() and Key.isdigit():
                KeyValid=int(Key)
                texeEncr=[]
                for TE in text:
                    if TE.islower():
                        texeEncr.append(EncrLowerChr(TE,KeyValid))
                    elif TE.isupper():
                        texeEncr.append(EncryptUpper(TE,KeyValid))
                print('The encryption word: ',''.join(texeEncr))
            else : print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (number) with no symbols text: ({text}) , Key: ({Key})'.capitalize(),color='red'))
            choice=input(termcolor.colored('wold you want do try again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Caesar : (')
                print(termcolor.colored(End,color='red'))
                choice=False
                
        elif ChoiceDec=='B':
            decryption=pyfiglet.figlet_format("Decryption")
            print(termcolor.colored(decryption,color='cyan'))
            text=input('please enter your Encryption text: ').replace(' ','')
            Key=input('enter your key: ')
            if  text.isalpha() and Key.isdigit():
                KeyValid=int(Key)
                textdecr=[]
                for DeText in text:
                    if DeText.islower():
                        textdecr.append(DecrLowerChr(DeText,KeyValid))
                    elif DeText.isupper():
                        textdecr.append(DecrUpperChr(DeText,KeyValid))
                        
                print('the actual Text is: ',''.join(textdecr))
            else: print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (number) with no symbols text: ({text}) , Key: ({Key})'.capitalize(),color='red'))
            choice=input(termcolor.colored('wold you want do try again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Caesar : (')
                print(termcolor.colored(End,color='red'))
                choice=False
                
        else:
            print(termcolor.colored('worring choice'.upper(),color='red'))
            choice=input(termcolor.colored('This is not valid choice, wold you want do try again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End Caesar : (')
                print(termcolor.colored(End,color='red'))
                choice=False
        

