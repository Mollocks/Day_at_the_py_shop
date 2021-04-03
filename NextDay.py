
#%%
x = "passion fruit"
y = x.upper()
print(y)


# %%
age = 49
txt = "My name is Hubert, and I am {}"
print(txt.format(age))
"""
Apparently you can also concatenate data together by 
using the following method:
"""
age = 49
txt = "My name is Hubert, and I am" + str(age)
#%%

# %%
quantity = 5
itemno = 546
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
myorder2 = "I want " + str(quantity) + " pieces of item " + str (itemno) + " for " + str(price) + " dollars."
print(myorder2)
Amount = 3
Worth = 34.53
catalogueno = 354
myorder3 = "I want {} pieces of item number {} , which is about {} GBP."
print(myorder3.format(Amount, catalogueno, Worth))

#%%
#Escape characters allow for illegal moves such as the use of double quotes within double quotes. 
txt = "She stared into the distance, \"Just forget me!\" and with that she walked away."
print(txt)
#%%
#Escape characters - include \n for a new line:
txt2 = "Bonjour\nClaude"
print(txt2)
#%%
#Escape characters - There is carriage return...for a new line too
txt3 = "Bonjour\rClaude!"
print(txt3)
#This hasn't worked... Not sure why. 
#%%
#Escape characters - Tab space
txt4 = "Bonjour\tClaude" 
print (txt4)
#This seems of little impact or use, but who knows what the future holds.
#%%
#Escape characters - backspace, which will delete 1 character before the \b
txt5 = "Bonjour \bClaude!" #Space between the words, removed!
print(txt5)
txt6 = "pooh\b"
print(txt6)
#%%
#String methods now bitches
counts = txt.count(" ")
print (counts) #We counted the number of spaces in the sentence :)
split = txt.split(" ")
print(split) #Also useful, we split by space and each word was split out.
#%%
find = txt.find("she")
print(find) #case sensitive and only finds the first instance of whatever you're finding.
length = len(txt)
print(length)
#%%
rsplit = txt.rsplit(" ")
print(rsplit)
#join = rsplit.join("\n")
#print(join) #This is a Brownie test. It threw back an error of unhappiness. 
join = "\n".join(rsplit)
print(join)