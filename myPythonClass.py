import string
from myPythonHelperModule import *

## Part 1: The Message object ##
# Queston 1.
# Create a class called Message. 
class Message():
    def __init__(self, text):
        self.msg_txt=text
        self.accepted_words=extract_words("words.txt")
# Create the init function with self and text arguments to initialize the Message object. 
# The text argument is a string and it is the text of the message to encrypt. 
# The attributes of the Message object are msg_txt (a string) and accepted_words (a list coming from the extract_words function from the helper module.)
    
    
# Question 2: 
# Create a method called get_message_text with the to access the self.msg_txt outside of the class, return a string of the shifted 
    def get_message_text(self):
        return self.msg_txt
    
# Question 3: 
# Create a method called get_accepted_words to  access a COPY of the list accepted_words outside of the class
    def get_accepted_words(self):
        copy_words=self.accepted_words
        return copy_words
# Question 4:
# Create a method called make_shift_dict that takes the shift as an input. 
    def make_shift_dict(self,shift):

         def shifting(list,shift):
             
             newlist=[]
             for i in range(0,26):
                 if(i<26-shift):
                     newlist+=list[shift+i]
                 else:
                     newlist+=list[i-26+shift]
             mydict= {list[n]: newlist[n] for n in range(len(list))}
             return mydict
         dict=shifting(string.ascii_lowercase,shift)
         dict.update(shifting(string.ascii_uppercase,shift))
         return dict
     
    def apply_shift(self,shift):
        shift_dict=self.make_shift_dict(shift)
       # print(shift_dict)
        text=self.msg_txt
        #print(text)
        #text=text.split(" ")
        text=list(text)
        for i in range(0,len(text)):
            if(text[i] in string.ascii_letters):
                # print(text[i])
                # print(shift_dict[text[i]])
                text[i]=shift_dict[text[i]]
            # #print(text)
        return "".join(text)
            
#k=Message("Alc hmh xli glmgoir gvsww xli vseh? Tpexs: Jsv xli kviexiv kssh. Oevp Qevb: Mx aew e lmwxsvmgep mrizmxefmpmxc. Rmixdwgli: Figeywi mj csy kedi xss psrk egvsww xli Vseh, xli Vseh kediw epws egvsww csy.")
# print(k.make_shift_dict(22))
#print(k.apply_shift(22))



# This method applies a shift to all the lowercase and uppercase letters and saves the results in a dictionary.
# Note that shift is an integer and cannot be less than 0 or larger than 26. 
# For example: 
'''
print(a.make_shift_dict(2))
Output: 
{'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 
'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 
'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 
'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 
'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 
'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 
'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 
'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}
For each alphabet letter saved as a key, it associates its shifted letter based on the shift input you give.
If the shift was 4, this dictionary wouldv'e been {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', ...., 'X': 'B', 'Y': 'C', 'Z': 'D'}
etc.
Hint: In this function, you may use the string module's ascii_lowercase and ascii_uppercase letters.
'''

# Question 5: 
'''
Create a method called apply_shift that takes the shift integer as an input. 
Given a Message object or its children, this method applies the shift given to it as input to that object and return a string of the encrypted final value. 
Note that shift is an integer and cannot be less than 0 or larger than 26. 
Example:
# a = Message("Hello")
# print(a.apply_shift(2))
Output: 
"Jgnnq"
Hint: In this function, you may use the output of the make_shift_dict function.
'''

## Part 2: AnytextMessage Inherited class ##

# Question 6: 
'''
Create a child class of Message called: AnytextMessage.
In the init function: 
Initialize the AnytextMessage object with a text, which is a string and a shift, which is an integer. 
An AnytextMessage object inherits from the Message class and has five attributes:
msg_txt, accepted_words, shift, encr_shift_dict [the dictionary of the shifted letters], enc_msg_txt (the final encrypted text saved as a string)
'''
class AnytextMessage(Message):
    def __init__(self,text,shift):
        self.msg_txt=text
      #  Message.__init__(self,text)
       # super().__init__(text)
        self.shift=shift
        self.encr_shift_dict=Message.make_shift_dict(self,shift)
        self.enc_msg_txt=Message.apply_shift(self,shift)
        self.accepted_words=extract_words("words.txt")
    def get_shift(self):
        return self.shift
    
    def get_encr_dict(self):
        copy_encr=self.encr_shift_dict
        return copy_encr
    def get_encr_msg(self):
        return self.enc_msg_txt
    def change_shift(self,newshift):
        self.shift=newshift 
        pass
        

# print(a.apply_shift(2))
# print(a.get_shift())
# print(a.get_encr_dict())
# print(a.get_encr_msg())
# a.change_shift(3)
# print(a.get_shift())

    
# Question 7:
'''
Create a function called get_shift that will return the shift given to an AnytextMessage object. 
'''

# Question 8: 
'''
Create a function called get_encr_dict that will return a copy of the dictionary of the encrypted letters.
'''

# Question 9: 
'''
Create a function called get_encr_msg that will return the string of the encrypted message. 
'''

# Question 10:
'''
Create a function called change_shift that takes a shift value as an input and changes the shift value of an existing AnytextMessage object. This method returns nothing.
'''

## Part 3: CaesarsDecoder ### 

# Question 11 
'''
Create a child class of Message called CaesarsDecoder. 
In the init function, initialize a CaesarsDecoder object with text which is a string. 
Let msg_txt and accepted words be the attributes of this class. 
'''
class CeasarsDecoder(Message):
    def __init__(self,text):
        self.msg_txt=text
        self.accepted=extract_words("words.txt")
    def decrypt_message(self):
        txt=self.msg_txt
        msg=Message(txt)
        #print(msg.apply_shift(0))
        countlist=[]
        for i in range(0,26):
            bestmsg=msg.apply_shift(i)
            bestmsg=bestmsg.split(" ")
            count=0
            for word in bestmsg:
                
                if(is_word(self.accepted,word)):
                    count+=1
            countlist.append(count)
        k=max(countlist)
        for i in range(0,len(countlist)):
            if(countlist[i]==k):
                return(i, msg.apply_shift(i))
        
msg=CeasarsDecoder("Alc hmh xli glmgoir gvsww xli vseh? Tpexs: Jsv xli kviexiv kssh. Oevp Qevb: Mx aew e lmwxsvmgep mrizmxefmpmxc. Rmixdwgli: Figeywi mj csy kedi xss psrk egvsww xli Vseh, xli Vseh kediw epws egvsww csy.")
print(msg.decrypt_message())
# Question 12: 
'''
Create a method called decrypt_message.
In this method, decrypt the msg_txt by trying every possible shift value 
and find the "best" one. 
We will define "best" as the shift that creates the maximum number of real words when we use apply_shift(shift) on the message text. 
If s is the original shift value used to encrypt the message, then we would expect 26 - s to be the best shift value for decrypting it.
This method returns a tuple of the best shift value used to decrypt the message and the decrypted message text using that shift value
'''
