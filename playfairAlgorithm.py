import termcolor
import pyfiglet

def processingKey(key):  
    keyEdit=str(key).replace('i','j')
    keyEdit2=''.join(dict.fromkeys(keyEdit))
    return keyEdit2



def searchElement(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


def generateMaterix(Keyword):
    list1 = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'j', 'k',
             'l', 'm','n', 'o', 'p',
             'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']     
    key_letters = []
    for i in Keyword:
        if i not in key_letters:
            key_letters.append(i)
 
    
    for i in list1:
        if i!='i':
            if i not in key_letters:
                key_letters.append(i)
        else: continue
 
    matrix = []
    while key_letters != []:
        matrix.append(key_letters[:5])
        key_letters = key_letters[5:]
 
    return matrix





def PlainTextProcessing(Plaintext):
    Plaintext=str(Plaintext).replace('i','j')
    Plaintextedit=Plaintext
    newPlaText=''
    if len(Plaintext)%2==0:
        for teEven in range(0,len(Plaintext)-1):
            if Plaintext[teEven]==Plaintext[teEven+1]:
                newPlaText=Plaintextedit[0:teEven+1]+'x'+Plaintextedit[teEven+1:]
                Plaintextedit=newPlaText
            
        if Plaintext==Plaintextedit:
            return Plaintext
        else:
            if len(Plaintextedit)%2!=0:
                Plaintextedit+='x'
                return Plaintextedit        
    elif len(Plaintext)%2!=0:
        for teOdd in range(0,len(Plaintext)-1):
            if Plaintext[teOdd]==Plaintext[teOdd+1]:
                newPlaText=Plaintextedit[0:teOdd+1]+'x'+Plaintextedit[teOdd+1:]
                Plaintextedit=newPlaText
        if Plaintext==Plaintextedit and len(Plaintextedit)%2==0:
            return Plaintextedit
        else:
            if len(Plaintextedit)%2!=0:
                return Plaintextedit+'x'

def PlainTextencry(PlainPro,Matrax):
    Cipiertext=[]
    for i in range(0,len(PlainPro),2):

        elem1_x,elem1_y=searchElement(Matrax,PlainPro[i])
        elem2_x,elem2_y=searchElement(Matrax,PlainPro[i+1])
        if elem1_x==elem2_x:
            if elem1_y==4 and elem2_y!=4:
                Cipiertext.append(Matrax[elem1_x][elem1_y%4])
                Cipiertext.append(Matrax[elem2_x][elem2_y+1])
                
            elif elem2_y==4 and elem1_y!=4:
                Cipiertext.append(Matrax[elem1_x][elem1_y+1])
                Cipiertext.append(Matrax[elem2_x][elem2_y%4])
                
            else:
                Cipiertext.append(Matrax[elem1_x][elem1_y+1])
                Cipiertext.append(Matrax[elem2_x][elem2_y+1])
                
        elif elem1_y==elem2_y:
            if elem1_x==4 and elem2_x!=4:
                Cipiertext.append(Matrax[elem1_x%4][elem1_y])
                Cipiertext.append(Matrax[elem2_x+1][elem2_y])
                
            elif elem2_x==4 and elem1_x!=4:
                Cipiertext.append(Matrax[elem1_x+1][elem1_y])
                Cipiertext.append(Matrax[elem2_x%4][elem2_y])
                
            else:
                Cipiertext.append(Matrax[elem1_x+1][elem1_y])
                Cipiertext.append(Matrax[elem2_x+1][elem2_y])
                
        elif elem1_x!=elem2_x and elem1_y!= elem2_y:
            Cipiertext.append(Matrax[elem1_x][elem2_y])
            Cipiertext.append(Matrax[elem2_x][elem1_y])
            
    trans=''.join(Cipiertext)
    return trans

def PlainTextDecryp(PlainPro,Matrax):
    Cipiertext=[]
    for i in range(0,len(PlainPro),2):

        elem1_x,elem1_y=searchElement(Matrax,PlainPro[i])
        elem2_x,elem2_y=searchElement(Matrax,PlainPro[i+1])
        if elem1_x==elem2_x:
            if elem1_y==0 and elem2_y!=0:
                Cipiertext.append(Matrax[elem1_x][elem1_y+4])
                Cipiertext.append(Matrax[elem2_x][elem2_y-1])
                
            elif elem2_y==0 and elem1_y!=0:
                Cipiertext.append(Matrax[elem1_x][elem1_y-1])
                Cipiertext.append(Matrax[elem2_x][elem2_y+4])
                
            else:
                Cipiertext.append(Matrax[elem1_x][elem1_y-1])
                Cipiertext.append(Matrax[elem2_x][elem2_y-1])
                
        elif elem1_y==elem2_y:
            if elem1_x==0 and elem2_x!=0:
                Cipiertext.append(Matrax[elem1_x+4][elem1_y])
                Cipiertext.append(Matrax[elem2_x-1][elem2_y])
                
            elif elem2_x==0 and elem1_x!=0:
                Cipiertext.append(Matrax[elem1_x-1][elem1_y])
                Cipiertext.append(Matrax[elem2_x+4][elem2_y])
                
            else:
                Cipiertext.append(Matrax[elem1_x-1][elem1_y])
                Cipiertext.append(Matrax[elem2_x-1][elem2_y])
                
        elif elem1_x!=elem2_x and elem1_y!= elem2_y:
            Cipiertext.append(Matrax[elem1_x][elem2_y])
            Cipiertext.append(Matrax[elem2_x][elem1_y])
            
    Decry=''.join(Cipiertext)
    return Decry

def mainPlayFair():
    playfair=pyfiglet.figlet_format("PlayFair : )")
    print(termcolor.colored(playfair,color='blue'))
    choice=True
    while choice==True:
        ChoiceDec=input('A-Encryption\nB-Decryption\nplease enter your choice A OR B: ').upper()  
        if ChoiceDec=='A':
            encryption=pyfiglet.figlet_format("Encryption")
            print(termcolor.colored(encryption,color='magenta'))
            text=input('please enter your text: ').replace(' ','').lower()
            Key=input('enter your key: ').lower()
            if text.isalpha() and Key.isalpha():
                EditText=PlainTextProcessing(text)
                EditKey=processingKey(Key)
                endMatrix=generateMaterix(EditKey)
                for mat in endMatrix:
                    print(mat)
                print(EditText)
                textencr=PlainTextencry(EditText,endMatrix)
                print(f'your encryption text is : {textencr}')
            else:
                print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (alpabet) with no symbols text: ({text}) , Key:({Key})'.capitalize(),color='red'))
            choice=input(termcolor.colored('wold you want do Choice again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End PlayFair : (')
                print(termcolor.colored(End,color='red'))
                choice=False
        elif ChoiceDec=='B':
            decryption=pyfiglet.figlet_format("Decryption")
            print(termcolor.colored(decryption,color='cyan'))
            text=input('please enter your Cipher: ').replace(' ','').lower()
            Key=input('enter your key: ').lower()
            if text.isalpha() and Key.isalpha():
                EditKey=processingKey(Key)
                endMatrix=generateMaterix(EditKey)
                for mat in endMatrix:
                    print(mat)
                print(text)
                actualText=PlainTextDecryp(text,endMatrix)
                print('your actual Text: ',actualText)
            else: print(termcolor.colored(f'please enter a valid text: (alphabet)/Key: (alpabet) with no symbols text: ({text}) , Key:({Key})'.capitalize(),color='red'))
            choice=input(termcolor.colored('wold you want do try again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                End=pyfiglet.figlet_format('End PlayFair : (')
                print(termcolor.colored(End,color='red'))
                choice=False

        else:
            print(termcolor.colored('worring choice'.upper(),color='red'))
            choice=input(termcolor.colored('This is not valid choice, wold you want do try again Y/N : '.capitalize(),color='green')).upper()
            if choice=='Y':
                    choice=True
            else:
                
                End=pyfiglet.figlet_format('End PlayFair : (')
                print(termcolor.colored(End,color='red'))
                choice=False









