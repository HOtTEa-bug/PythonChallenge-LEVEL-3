#url: http://www.pythonchallenge.com/pc/def/equality.html

mess = open("3.text", "r")
t = mess.read() 
sol = "" #solution variable
last = True #The variable to detect uppercase letters before the first 3 bodyguards

'''My program finds 3 uppercase letters, then the fourth lowercase and last 3 uppercase and saves them all in the variable sol. Then it checks if the 8th letter is lowercase and prints the lowercase letter, resets and goes on.'''

for x in t:
    if x == "\n":
        continue
    if len(sol) in [0,1,2,4,5,6]:
        if x.islower():
            sol = ""
            last = True
        elif last:
            sol += x
    elif len(sol) == 3:
        
        if x.islower():
            sol += x
        else:
            sol = ""
            last = False
    elif len(sol) == 7:
        if x.islower():
            print(sol[3])
            sol = ""
        else:
            sol = ""