import math
import random
from textblob import TextBlob
from colorama import Fore
from getkey import getkey, key
from replit import audio
import time

name = "Stranger"

open=[
  "Good day mate! What's up?",
  'Hi, how are you today?',
  "Yo what's up bro?",
  'Hello, how is everything going?',
]
bro=['bro', 'mate', 'my friend',]
gadj=['epic', 'cool', 'cool', 'cute', 'sweet']
blank=[' ', '!', '?']
vowels=['a', 'e', 'i', 'o', 'u']
good = ['n amazing', ' great', 'n awesome', ' good', ' fine']

b=Fore.BLUE
w=Fore.WHITE
r=Fore.RED
lg=Fore.LIGHTGREEN_EX
lr=Fore.LIGHTMAGENTA_EX  

#---------------------------Loading------------------------------

print(lr + 'Loading...')
source = audio.play_tone(1, 600, 1)
time.sleep(3)
print(lr + "\nLoaded")
source = audio.play_tone(0.25, 1500, 1)
time.sleep(1)
print('\n')

#---------------------------Opening-------------------------------

while True:
  print(b + random.choice(open), (lr + " (Type 'skip' to skip greeting)") )
  openans = TextBlob((input(w)).lower())
  if ('hi' in openans and 'nothing' not in openans) or 'hello' in openans or 'hey' in openans:
    continue
  else:
    break

openansblob = openans.polarity

if openans.lower() == 'skip':
  solve = 'yes'
  pass
else:
  if ' and you' in openans or 'about you' in openans or 'you?' in openans or 'are you' in openans or 'hbu' in openans or 'wbu' in openans:
    print(b + "Oh, I am having a" + random.choice(good) + " day so far! Thank you for asking!\n\nSo, what's your name?")
  elif openansblob > 0:
    print(b+"\nThat's amazing", random.choice(bro), "\b! \nSo What's your name?")
  elif openansblob == 0:
    print(b+"\nNice, anyways.\nWhat's your name", random.choice(bro), "\b?")
  else:
    print(b+"\nOh, that's fine, don't worry, you'll feel much better soon since you are chating with me heheeh, anyways.")
    print("So what's your name my friend?")

  name = (input(w)).lower()

  if "my name is " in name or "i'm " in name or "i am " in name:
    name = name.replace('my name is ', '')
    name = name.replace("i'm ", '')
    name = name.replace("i am ", '')
  
  while True:
    if "don't" in name or "no" in name or "not" in name:
      print(b + "Oh, that's fine, I'm sorry for any offense, I swear didn't mean that \U0001F622")
      name = 'no'
      break
    if len(name.split()) > 1:
      print(b + "\nWow, I'm sorry but I am really bad at memorising, your name is sooooo long \U0001F635. Just give me your first name please =.=")
      name = input(w)
      if len(name.split()) == 1:
        break
    if len(name.split()) < 1:
      print(b + "Oh come on, don't kill our chat 🥹")
      print(b + "What's your first name?")
      name = input(w)
      if len(name.split()) == 1:
        break
    else:
      break
      
  for x in blank:
    if x in name:
      name = name.replace(x, '')
  
  name = name.capitalize()
  bro.append(name)
  bro=random.choice(bro)
  #------------------------Intro + Choose---------------------------
  gadj=random.choice(gadj)
  
  if gadj[0] == 'a' or gadj[0] == 'e' or gadj[0] == 'i' or gadj[0] == 'o' or gadj[0] == 'u':
    gadj = 'n ' + gadj
  else:
    gadj = ' ' + gadj

  if name.lower() == 'no':
    pass
  else:
    name = name.capitalize()
    print(b + 'Awww', name, "That's such a"+gadj, "name! ☆*:.o(≧▽≦)o.:*☆")
    
  print(b + "\nAnyways, I am Cici, a math problem solving robot. \nDo you know why I'm called Cici?")
  ans=input(w)
  
  davinci="y name actually came from the last syllable of Da Vinci! \nThis is because the person who created me admires Da Vinci a lot as he is good at nearly everything. Therefore, she wishes I can be similar minded to him as I was created to solve math problems, so she named me Cici. \nAnyways, so do you have any mathematical questions for me?"
  
  if 'da vinci' in ans.lower():
    print(b+f"Oh my god! \n\nYes you are right, m{davinci}")
  elif ans.lower() == 'yes':
    print(b+"Wow, tell me your thought!")
    ans = input(w)
    if 'da vinci' in ans.lower():
      print(b+f"Oh my god! \n\nYes you are right, m{davinci}")
    else:
      print(b+f"Haha, good guess! But nah, I know it's hard to guess. \n\nM{davinci}")
  else:
    print(b+f"Haha, I know it's hard to guess. \nM{davinci}")
  solve=input(w)

#--------------------Choose question type-------------------------

p1='1. Arithmetic & Geometric Sequences - Finding numbers, Sums and Terms in sequences'
p2='2. Simple calculations - Additions, Subtractions, Multiplications, Divisions, Exponentials, Logarithms...'
p3='3. Complex Number - Additions, Subtractions, Multiplications, Divisions...'
p4='4. Geometry - Finding Areas, Volumes, Perimeters, Surface Areas...'
p5='5. Trigonometry - Sin, Cos, Tan...'
p6='6. Pythagoras - Finding lengths of sides of right triangles'
problemtypes=[p1, p2, p3, p4, p5,p6]


while True:
  solve=solve.lower()
  if 'ye' in solve or 'yes' in solve or 'yea' in solve or 'yup' in solve or 'sure' in solve:
    print(b+"\nThat's great! Solving more questions helps my developer to improve me.")
    print(b+"Which type of question would you like me to solve for you? \nAs I am still a developing program and my developer is only in Year 10, I can only solve the following types of problems:")
    for y in problemtypes:
      print(lg + y)
    print(b+'\nPlease type down the number of choice you want to choose and we can start solving your question!')
  else:
      if openansblob < 0:
        print(b+f"\nAlright then, it looks like you don't really need me right now. \nI guess I'll just leave for now and wish we can talk in the fulture. Also, Hope you'll feel better, {name}. Cya~")
        source = audio.play_file('bgm.mp3')
        time.sleep(9)
        print(Fore.RED + "\nCici left the chat..."+w)
        break
      else:
        print(b+f"Alright then, I wish we can talk again in the future, {name}. Cya~")
        source = audio.play_file('bgm.mp3')
        time.sleep(9)
        print(Fore.RED + "\nCici left the chat..." +w)
        break

  
  #====================== Problem Solving!!! =======================
  
  
  gadj=['epic', 'cool', 'cool', 'cute', 'sweet']
  gadj=random.choice(gadj)
  
  p1ty = ['1. Arithmetic Sequences', '2. Geometric Sequences']
  p11 = ['1. Finding the nth term (tn)', '2. Finding the first term and difference (a and d)', '3. Finding the sum of the nth term (Sn)']
  p12 = ['1. Finding the nth term (tn)', '2. Finding the first term and common ratio (a and d)', '3. Finding the sum of the nth term (Sn)', '4. Finding the sum to infinity']

  p2ty = ['1. Additions', '2. Subtractions', '3. Multiplications', '4. Divisions', '5. Exponentials', '6. Logarithms', '7. Square Root', '8. Root of x']

  p3ty = ['1. Additions', '2. Subtractions', '3. Multiplications', '4. Divisions']

  p4ty = ['1. Finding Area', '2. Finding Volume', '3. Finding Perimeters & Circumferences', '4. Surface Areas']
  p41 = ['1. Circles', '2. Quadrilaterals', '3. Squares', '4. Triangles']
  p42 = ['1. Spheres', '2. Rectangular Prisms', '3. Cubes', '4. Pyramids', '5. Triangular Pyramids', '6. Cylinders', '7. Cones']
  p43 = ['1. Circles', '2. Polygons']
  p44 = ['1. Spheres', '2. Rectangular Prisms', '3. Cubes', '4. Pyramids', '5. Cylinders', '6. Cones']

  p5ty = ['1. Finding Angles', '2. Finding Side Lengths']
  p5dr = ['1. Degrees', '2. Radians']
  p51 = ['1. Opposite & Hypotenuse Given (Sin)', '2. Adjacent & Hypotenuse Given (Cos)', '3. Opposite & Adjacent Given (Tan)']
  p52 = ['1. Finding Opposite', '2. Finding Adjacent', '3. Finding Hypotenuse']

  p6ty = ['1. Finding The Length of the Hypotenuse side', '2. Finding the Length of a side that is not hypotenuse']
  
  num= Fore.YELLOW + "\u26A0" + Fore.RED+" Number Error: 1) Please just insert the NUMBER of the type of question you want to solve. 2) Please just type the NUMBER required in the question."
  unit = "(Don't type the unit)"
  comnum = Fore.RED + "Please just insert the complex number ONLY, make sure you typed in an actual COMPLEX NUMBER with the right format."
  
  while True:
    try:
      ans=input(w)
      ans=int(ans)
      break
    except:
      print(num)
      
  #================ 1. Arithmetic & Geometric Sequences =============
  
  if ans == 1:
    print("\n\n")
    print(lr + p1)
    print(b+gadj.capitalize(), "\b! Let's start from Arithmetic and Geometric Sequences first then!")
    print(b+'So whcih sequence are we particularly looking at?')
    for y in p1ty:
      print(lg+y)
      
    while True:
      try: 
        p1ty1ans=int(input(w))
        if p1ty1ans > 2 or p1ty1ans <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if p1ty1ans <= 2 and p1ty1ans > 0:
            break
        else:
          break
      except:
        print(num)
          
    #--------------------1.1. Arithmetic Sequences------------------
    
    if p1ty1ans == 1:
      print(b+"And what are we finding?")
      for x in p11:
        print(lg+x)
      while True:
        try: 
          p1ty1ans1=int(input(w))
          if p1ty1ans1 > 3 or p1ty1ans1 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p1ty1ans1 <= 3 and p1ty1ans1 > 0:
              break
          else:
            break
        except:
          print(num)
      #--------------------1.1.1. nth term (tn)----------------------
      if p1ty1ans1 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the value of the first term?')
            a=float(input(w+'a = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'What is the difference between terms?')
            d=float(input(w+'d = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'Finally, what is the number of term we looking for?')
            n=float(input(w+'tn = '))
            break
          except:
            print(num)
            
        tn = lr + str(a+((n-1)*d))
        rule = lr + str(f"tn = {a} + ((n - 1) * {d})")
        print(b+"The number of the", n, "\bth term in this arithmetic sequence is:", tn)
        print(b+"The rule for this arithmetic sequence is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #--------1.1.2. first term and difference (a and d)------------
      if p1ty1ans1 == 2:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the value of the smaller term given?')
            s=float(input(w+'s = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And which number of term is this number?')
            ts=float(input(w+'ts = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'What is the value of the lareger term given?')
            l=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And finally, which number of term is this larger number?')
            tl=float(input(w+'tl = '))
            break
          except:
            print(num)

        if (tl-ts) == 0:
          d = lr + 'Undefined'
          a = lr + 'Undefined'
          rule = lr + 'Undefined'
        else:
          d = (l-s)/(tl-ts)
          a = lr + str(s-((ts-1)*d))
          d = lr + str(d)
          rule = lr + str(f'tn = {a} + (n - 1) * {d}')
        print(b+"The first term for this arithmetic sequence is:", a)
        print(b+'The difference between terms in this arithmetic sequence is:', d)
        print(b+'The rule for this arithmetic sequence is:', rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #---------------1.1.3 sum of the nth term (Sn)-----------------
      if p1ty1ans1 == 3:
        while True:
          try:
            print(b+'What is the first term of the range in the sequence?')
            a=float(input(w+'a = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'What is the number of the last term of the range in the sequence?')
            n=float(input(w+'n = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'Finally, what is the difference between the terms in the sequence?')
            d=float(input(w+'d = '))
            break
          except:
            print(num)

        Sn = lr + str((n/2)*(2*a+(n-1)*d))
        rule = lr + str(f'Sn = ({n} * ((2 * {a}) + (n - 1) * {d})) / 2')
        print(b+'The sum of this range in this arithmetic sequence is', Sn)
        print(b+'The rule for this arithmetic sequence is: ', rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)

    #--------------------1.2. Geometric Sequences--------------------
    
    if p1ty1ans == 2:
      print(b+"And what are we finding?")
      for x in p12:
        print(lg + x)
      while True:
        try: 
          p1ty1ans2=int(input(w))
          if p1ty1ans2 > 4 or p1ty1ans2 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p1ty1ans2 <= 4 and p1ty1ans2 > 0:
              break
          else:
            break
        except:
          print(num)
      #---------------------1.2.1. nth term (tn)---------------------
      if p1ty1ans2 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the first term?')
            a=float(input(w+'a = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'What is the common ratio between terms?')
            ratio=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'Finally, what number of term are we looking for?')
            n=float(input(w+'tn = '))
            break
          except:
            print(num)
            
        p11ans = lr + str(a*pow(ratio,(n-1)))
        rule = lr + str(f'tn = {a} * {ratio}^(n-1)')
        print(b+"The number of the", n, "\bth term in this geometric sequence is:", p11ans)
        print(b+"The rule for this geometric sequence is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #---------1.2.2. first term and difference (a and r)-----------
      if p1ty1ans2 == 2:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the value of the smaller term given? (smaller term)')
            s=float(input(w+'s = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And which number of term is this number?')
            ts=float(input(w+'ts = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'What is the second term given? (larger term)')
            l=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And finally, which number of term is this second number?')
            tl=float(input(w+'tl = '))
            break
          except:
            print(num)

        if (tl-ts) == 0:
          d = lr + 'Undefined'
          a = lr + 'Undefined'
          rule = lr + 'Undefined'
        else:
          r = lr + str(pow(l/s, 1/(tl-ts)))
          a = lr + str(pow(s, 1/ts))
          rule = lr + str(f'tn = {a} + {r} ^ (n-1)')
        print(b+"The first term for this geometric sequence is:", a)
        print(b+'The the common ratio of this geometric sequence is:', r)
        print(b+'The rule for this geometric sequence is:', rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------1.2.3. sum of the nth term (Sn)-------------------
      if p1ty1ans2 == 3:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the value of the first term?')
            a=float(input(w+'a = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the common ratio of this geometric sequence?')
            ratio=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And finally, what is the number of the last number of this sequence?')
            n=float(input(w+'n = '))
            break
          except:
            print(num)

        if (r-1) == 0:
          Sn = lr + 'Undefined'
          rule = lr + 'Undefined'
        else:
          Sn = lr + str((a*(pow(ratio,n)-1))/(r-1))
          rule = lr + str(f'({a} * (({r} ^ n) - 1))/({ratio} - 1)')
          
        print(b+"The sum of this geometric sequence is:", Sn)
        print(b+'The rule for this geometric sequence is:', rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------1.2.4. sum to infinity(Si)------------------
      if p1ty1ans2 == 4:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the value of the first term?')
            a=float(input(w+'a = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the common ratio of this geometric sequence?')
            ratio=float(input(w+'r = '))
            break
          except:
            print(num)

        if abs(r) > 1:
          Sn = lr + 'Undefined. To calculate the sum to infinity, the absolute value of the geometric sequence can ONLY be LESS than 0!'
          rule = lr + 'Undefined'
        elif (1-r) == 0:
          Sn = lr + 'Undefined'
          rule = lr + 'Undefined'
        else:
          Sn = lr + str(a/(1-ratio))
          rule = lr + str(f'Si = {a} / (1 - {ratio})')
          
        print(b+"The sum to infinity for this geometric sequence is:", Sn)
        print(b+'The rule for this geometric sequence is:', rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
  
  #==================== 2. Simple Calculations ======================

  if ans == 2:
    print("\n\n")
    print(lr + p2)
    print(b+gadj.capitalize(), "\b! Let's start from Simple Calculations then!")
    print(b+'So which type of calculation are we particularly looking at?')
    for y in p2ty:
      print(lg+y)
      
    while True:
      try: 
        simpcal=int(input(w))
        if simpcal > 8 or simpcal <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if simpcal <= 8 and simpcal > 0:
            break
        else:
          break
      except:
        print(num)
    #------------------------2.1. Additions--------------------------
    if simpcal == 1:
      sum = 0
      print(b+"Great! Let's start then!")
      print(b+'Insert all the addends in the question. (Press Enter once to insert one value, press Enter three times to end)', unit)
      while True:
        try:
          x=float(input(w))
          sum += x
        except:
          entkey = getkey(x)
          if entkey == key.ENTER:
            sum = lr + str(sum)
            break
          else:
            print(num)
      
      print(Fore.BLUE+"Sum:", sum)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.2. Subtractions-------------------------
    if simpcal == 2:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the minuend?')
          a=float(input(w))
          break
        except:
          print(num)
          
      while True:
        try:
          print(b+'What is the first subtrahend?')
          d=float(input(w+f'{a} - '))
          break
        except:
          print(num)
          
      c=a-d
    
      while True:
        print(b + 'Is there any more subtrahend?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other subtrahend?")
            x=float(input(w + f"{c} - "))
            c -= x
          except:
            print(num)
        else:
          difference=lr + str(c)
          break
      
      print(Fore.BLUE+"Difference:", difference)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.3. Multiplications----------------------
    if simpcal == 3:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the first multiplier?')
          a=float(input(w))
          break
        except:
          print(num)
      while True:
        try:
          print(b+'What is the second multiplier?')
          d=float(input(w+f'{a} * '))
          break
        except:
          print(num)
          
      c=a*d
    
      while True:
        print(b + 'Is there any more multipliers?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other multipliers?")
            x=float(input(w + f"{c} * "))
            c *= x
          except:
            print(num)
        else:
          product=lr + str(c)
          break
      
      print(Fore.BLUE+"Product:", product)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #------------------------2.4. Division---------------------------
    if simpcal == 4:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the dividend?')
          a=float(input(w))
          break
        except:
          print(num)
      while True:
        try:
          print(b+'What is the first divisor?')
          d=float(input(w+f'{a} / '))
          break
        except:
          print(num)
          
      c=a/d
    
      while True:
        print(b + 'Is there any more divisors?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other divisors?")
            x=float(input(w + f"{c} / "))
            c /= x
          except:
            print(num)
        else:
          quotient=lr + str(c)
          break
      
      print(Fore.BLUE+"Quotient:", quotient)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.5. Exponentials-------------------------
    if simpcal == 5:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the base?')
          a=float(input(w + 'Base = '))
          break
        except:
          print(num)
      while True:
        try:
          print(b+'What is the exponent of power?')
          d=float(input(w + 'Exponent of power = '))
          break
        except:
          print(num)
          
      res=lr + str(pow(a,d))
      
      print(Fore.BLUE+f"{a} ^ {d}:", res)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.6. Logarithms-------------------------
    if simpcal == 6:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the base?')
          a=float(input(w + 'Base = '))
          break
        except:
          print(num)
      while True:
        try:
          print(b+'And...')
          d=float(input(w + f'log {a} to '))
          break
        except:
          print(num)

      if abs(a) != a or abs(d) != d:
        res = lr + 'Undefined'
      elif a == 10:
        res=lr + str(math.log10(d))
      else:
        res=lr + str(math.log(d,a))

      print(Fore.BLUE+f"log {a} to {d}:", res)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.7. Square Root--------------------------
    if simpcal == 7:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+"What number's square root are we looking for?")
          a=float(input(w + 'Square root of '))
          break
        except:
          print(num)

      res = lr + str(math.sqrt(a))
      
      print(Fore.BLUE+f"Square root of {a} is:", res)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------2.8. Cube Root--------------------------
    if simpcal == 8:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+"What is the root number?")
          a=float(input(w))
          break
        except:
          print(num)
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+f"What number is in {a} root?")
          d=float(input(w+f"{a} root of "))
          break
        except:
          print(num)

      res = lr + str(pow(a,1/d))
      
      print(Fore.BLUE+f"{a} root of {d} is:", res)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
  
  #===================== 3. Complex Numbers =========================

  if ans == 3:
    com = b + "(Please insert the imaginary as 'j', without spaces!)"
    print("\n\n")
    print(lr + p3)
    print(b+gadj.capitalize(), "\b! Let's start from complex numbers then!")
    print(b+'So which type of complex number calculation are we particularly looking at?')
    for y in p3ty:
      print(lg+y)
      
    while True:
      try: 
        compcal=int(input(w))
        if compcal > 4 or compcal <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if compcal <= 4 and compcal > 0:
            break
        else:
          break
      except:
        print(num)
    #------------------------3.1. Additions--------------------------
    if compcal == 1:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+"What is the first complex number that needs to be added?", com)
          a=complex(input(w))
          break
        except:
          print(comnum)
      while True:
        try:
          print(b+"What is the second complex number that needs to be added?", com)
          d=complex(input(w+f'{a} + '))
          break
        except:
          print(comnum)
          
      c=d+a    
    
      while True:
        print(b + 'Is there any more addends?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other addends?", com)
            x=complex(input(w + f"{c} + "))
            c += x
          except:
            print(comnum)
        else:
          sum=lr + str(c)
          break
      
      print(Fore.BLUE+"Sum:", sum)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------3.2. Subtractions-------------------------
    if compcal == 2:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the minuend?', com)
          a=complex(input(w))
          break
        except:
          print(comnum)
      while True:
        try:
          print(b+'What is the first subtrahend?', com)
          d=complex(input(w+f'{a} - '))
          break
        except:
          print(comnum)
          
      c=a-d
    
      while True:
        print(b + 'Is there any more subtrahend?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other subtrahend?", com)
            x=complex(input(w + f"{c} - "))
            c -= x
          except:
            print(comnum)
        else:
          difference=lr + str(c)
          break
      
      print(Fore.BLUE+"Difference:", difference)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #----------------------3.3. Multiplications----------------------
    if compcal == 3:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the first multiplier?', com)
          a=complex(input(w))
          break
        except:
          print(comnum)
      while True:
        try:
          print(b+'What is the second multiplier?', com)
          d=complex(input(w+f'{a} * '))
          break
        except:
          print(comnum)
          
      c=a*d
    
      while True:
        print(b + 'Is there any more multipliers?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other multipliers?", com)
            x=complex(input(w + f"{c} * "))
            c *= x
          except:
            print(comnum)
        else:
          product=lr + str(c)
          break
      
      print(Fore.BLUE+"Product:", product)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)
    #------------------------2.4. Division---------------------------
    if compcal == 4:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the dividend?', com)
          a=complex(input(w))
          break
        except:
          print(comnum)
      while True:
        try:
          print(b+'What is the first divisor?', com)
          d=complex(input(w+f'{a} / '))
          break
        except:
          print(comnum)
          
      c=a/d
    
      while True:
        print(b + 'Is there any more divisors?')
        add=input(w)
        if 'yes' in add or 'ye' in add or 'sure' in add or 'yea' in add or 'yup' in add:
          try:
            print(b+"Other divisors?", com)
            x=complex(input(w + f"{c} / "))
            c /= x
          except:
            print(comnum)
        else:
          quotient=lr + str(c)
          break
        
      print(Fore.BLUE+"Quotient:", quotient)
      
      print(Fore.BLUE+"\nDo you have any more questions?")
      solve = input(w)

  #========================= 4. Geometry ============================

  if ans == 4:
    print("\n\n")
    print(lr + p4)
    print(b+gadj.capitalize(), "\b! Let's start from Simple Calculations then!")
    print(b+'So which part of geometry are we particularly looking at?')
    for y in p4ty:
      print(lg+y)
      
    while True:
      try: 
        p4ty1ans=int(input(w))
        if p4ty1ans > 4 or p4ty1ans <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if p4ty1ans <= 4 and p4ty1ans > 0:
            break
        else:
          break
      except:
        print(num)

    #-------------------------4.1. Areas-----------------------------
    
    if p4ty1ans == 1:
      print(b+"And what are we finding?")
      for x in p41:
        print(lg+x)
      while True:
        try: 
          p4ty1ans1=int(input(w))
          if p4ty1ans1 > 4 or p4ty1ans1 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p4ty1ans1 <= 4 and p4ty1ans1 > 0:
              break
          else:
            break
        except:
          print(num)
      #----------------------4.1.1. Circles--------------------------
      if p4ty1ans1 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the radius of the circle? (If the diameter is given then divide it by 2)')
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
            
        area = lr + str(math.pi*radius**2)
        rule = lr + str(f"A = ({radius}^2) * \u03C0")
        print(b+"The area of this circle is:", area, "unit^2")
        print(b+"The equation for finding this circle's area is:", rule)
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #---------------------4.1.2. Quadrilaterals--------------------
      if p4ty1ans1 == 2:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the base given?", unit)
            base=float(input(w+'b = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        area = lr + str(base*height)
        rule = lr + str(f'A = {base} * {height}')
        print(b+"The area of this quadrilateral is:", area, "unit^2")
        print(b+"The equation for finding this quadrilateral's area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-------------------------4.1.3. Squares-----------------------
      if p4ty1ans1 == 3:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length of one side of the squre?", unit)
            side=float(input(w+'s = '))
            break
          except:
            print(num)

        area = lr + str(side**2)
        rule = lr + str(f'A = {side}^2')
        print(b+"The area of this squre is:", area, "unit^2")
        print(b+"The equation for finding this quadrilateral's area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-----------------------4.1.4. Triangles-----------------------
      if p4ty1ans1 == 4:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the base given?", unit)
            base=float(input(w+'b = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        area = lr + str(base*height/2)
        rule = lr + str(f'A = {base} * {height} / 2')
        print(b+"The area of this triangle is:", area, "unit^2")
        print(b+"The equation for finding this quadrilateral's area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)

    #------------------------4.2. Volume-----------------------------
    
    if p4ty1ans == 2:
      print(b+"And what are we finding?")
      for x in p42:
        print(lg+x)
      while True:
        try: 
          p4ty1ans1=int(input(w))
          if p4ty1ans1 > 7 or p4ty1ans1 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p4ty1ans1 <= 7 and p4ty1ans1 > 0:
              break
          else:
            break
        except:
          print(num)
      #----------------------4.2.1. Spheres--------------------------
      if p4ty1ans1 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the radius of the sphere? (If the diameter is given then divide it by 2)', unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
            
        volume = lr + str((4/3)*math.pi*radius**3)
        rule = lr + str(f"V = (4/3) * ({radius}^3) * \u03C0")
        print(b+"The volume of this sphere is:", volume, "unit^3")
        print(b+"The equation for finding this sphere's volume is:", rule)
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #---------------------4.2.2. Quadril Prisms--------------------
      if p4ty1ans1 == 2:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the width given?', unit)
            width=float(input(w+'w = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        volume = lr + str(length*width*height)
        rule = lr + str(f'V = {length} * {width} * {height}')
        print(b+"The volume of this quadrilateral prism is:", volume, "unit^3")
        print(b+"The equation for finding this rectangular prism's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------------------4.2.3. Cubes--------------------------
      if p4ty1ans1 == 3:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length of one side of the cube given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        
        volume = lr + str(length**3)
        rule = lr + str(f'V = {length}^3')
        print(b+"The volume of this cube is:", volume, "unit^3")
        print(b+"The equation for finding this cube's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-----------------------4.2.4. Pyramids------------------------
      if p4ty1ans1 == 4:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the base length given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the base width given?', unit)
            width=float(input(w+'w = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        volume = lr + str(length*width*height/3)
        rule = lr + str(f'V = ({length} * {width} * {height}) / 3')
        print(b+"The volume of this pyramid is:", volume, "unit^3")
        print(b+"The equation for finding this pyramid's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------------4.2.5. Triangular Pyramids------------------
      if p4ty1ans1 == 5:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length of the base's base given?", unit)
            base=float(input(w+'bb = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+"And what is the base's height given?", unit)
            baseheight=float(input(w+'bh = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height of this triangular based pyramid given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        volume = lr + str(((base*baseheight)/2*height)/3)
        rule = lr + str(f'V = (({base} * {baseheight}) / 2 * {height}) / 3')
        print(b+"The volume of this triangular based pyramid is:", volume, "unit^3")
        print(b+"The equation for finding this triangle based pyramid's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-----------------------4.2.6. Cylinders-----------------------
      if p4ty1ans1 == 6:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the radius of the circle base of the cylinder? (If the diameter is given then divide it by 2)", unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height of the cylinder given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        volume = lr + str(math.pi*height*radius**2)
        rule = lr + str(f'V = ({radius}^2) * \u03C0 * {height}')
        print(b+"The volume of this cylinder is:", volume, "unit^3")
        print(b+"The equation for finding this cylinder's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------------------4.2.7. Cones--------------------------
      if p4ty1ans1 == 7:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the radius of the circle base of this cone? (If the diameter is given then divide it by 2)", unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height of this cone given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        volume = lr + str((math.pi*height*radius**2)/3)
        rule = lr + str(f'V = (\u03C0 * {height} * {radius}^2) / 3')
        print(b+"The volume of this cone is:", volume, "unit^3")
        print(b+"The equation for finding this cone's volume is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)

    #----------------4.3. Perimeters & Circumefrences----------------
    
    if p4ty1ans == 3:
      print(b+"And what are we finding?")
      for x in p43:
        print(lg+x)
      while True:
        try: 
          p4ty1ans1=int(input(w))
          if p4ty1ans1 > 2 or p4ty1ans1 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p4ty1ans1 <= 2 and p4ty1ans1 > 0:
              break
          else:
            break
        except:
          print(num)
      #----------------------4.3.1. Circles--------------------------
      if p4ty1ans1 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the radius of the circle? (If the diameter is given then divide it by 2)', unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
            
        ccf = lr + str(2*radius*math.pi)
        rule = lr + str(f"V = 2 * {radius} * \u03C0")
        print(b+"The circumference of this circle is:", ccf, "unit")
        print(b+"The equation for finding this circle's circumference is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #----------------------4.3.2. Polygon--------------------------
      if p4ty1ans1 == 2:
        perimeter = 0
        print(b+'Insert lengths of all the sides of this polygon. (Press Enter once to insert one value, press Enter three times to end)', unit)
        while True:
          try:
            x=float(input(w))
            perimeter += x
          except:
            entkey = getkey(x)
            if entkey == key.ENTER:
              perimeter = lr + str(perimeter)
              break
            else:
              print(num)
        print(b+"The perimeter of this polygon is:", perimeter, "unit")
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)

    #-----------------------4.4. Surface Areas-----------------------
    
    if p4ty1ans == 4:
      print(b+"And what are we finding?")
      for x in p44:
        print(lg+x)
      while True:
        try: 
          p4ty1ans1=int(input(w))
          if p4ty1ans1 > 7 or p4ty1ans1 <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p4ty1ans1 <= 7 and p4ty1ans1 > 0:
              break
          else:
            break
        except:
          print(num)

      #----------------------4.4.1. Spheres--------------------------
      if p4ty1ans1 == 1:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+'What is the radius of the sphere? (If the diameter is given then divide it by 2)', unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
            
        sa = lr + str(4*math.pi*radius**2)
        rule = lr + str(f"SA = 4 * ({radius}^2) * \u03C0")
        print(b+"The surface area of this sphere is:", sa, "unit^2")
        print(b+"The equation for finding this sphere's surface area is:", rule)
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #---------------------4.4.2. Quadril Prisms--------------------
      if p4ty1ans1 == 2:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the width given?', unit)
            width=float(input(w+'w = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        sa = lr + str(2*(length*width+length*height+width*height))
        rule = lr + str(f'SA = 2 * ({length} * {width} + {length} * {height} + {width} * {height })')
        print(b+"The surface area of this quadrilateral prism is:", sa, "unit^2")
        print(b+"The equation for finding this rectangular prism's surface area is:", rule)
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------------------4.4.3. Cubes--------------------------
      if p4ty1ans1 == 3:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the length of one side of the cube given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        
        sa = lr + str(6*length**2)
        rule = lr + str(f'SA = 6 * {length}^2')
        print(b+"The surface area of this cube is:", sa, "unit^2")
        print(b+"The equation for finding this cube's surface area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-----------------------4.4.4. Pyramids------------------------
      if p4ty1ans1 == 4:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the base length given?", unit)
            length=float(input(w+'l = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the base width given?', unit)
            width=float(input(w+'w = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        sa = lr + str(length*width + length*math.sqrt(pow(width/2,2) + height**2) + width*math.sqrt(pow(length/2, 2) + height**2))
        rule = lr + str(f'SA = {length} * {width} + {length} * (({width}/2)^2 + {height}^2) ^ (1/2) + {width} * (({length}/2)^2 + {height}^2) ^ (1/2)')
        print(b+"The surface area of this pyramid is:", sa, "unit^2")
        print(b+"The equation for finding this pyramid's surface area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #-----------------------4.4.5. Cylinders-----------------------
      if p4ty1ans1 == 5:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the radius of the circle base of the cylinder? (If the diameter is given then divide it by 2)", unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height of the cylinder given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        sa = lr + str(2*math.pi*radius*height + 2*math.pi*radius**2)
        rule = lr + str(f'SA = (2 * \u03C0 * {radius} * {height}) + (2 * \u03C0 * {radius}^2)')
        print(b+"The surface area of this cylinder is:", sa, "unit^2")
        print(b+"The equation for finding this cylinder's surface area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)
      #------------------------4.4.7. Cones--------------------------
      if p4ty1ans1 == 7:
        while True:
          print(b+"Great! Let's start then!")
          try:
            print(b+"What is the radius of the circle base of this cone? (If the diameter is given then divide it by 2)", unit)
            radius=float(input(w+'r = '))
            break
          except:
            print(num)
        while True:
          try:
            print(b+'And what is the height of this cone given?', unit)
            height=float(input(w+'h = '))
            break
          except:
            print(num)

        sa = lr + str(math.pi*radius*(radius+math.sqrt(pow(height,2)+pow(radius,2))))
        rule = lr + str(f'V = \u03C0 * {radius} * {radius} + (({height}^2) + ({radius}^2)) ^ (1/2)')
        print(b+"The surface area of this cone is:", sa, "unit^3")
        print(b+"The equation for finding this cone's surface area is:", rule)
        
        print(b+"\nDo you have any more questions?")
        solve = input(w)

  #====================== 5. Trigonometry ===========================

  if ans == 5:
    print("\n\n")
    print(lr + p5)
    print(b+gadj.capitalize(), "\b! Let's start from Trigonometry then!")
    print(b+'So which part of trigonometry are we particularly looking at?')
    
    for y in p5ty:
      print(lg+y)
    while True:
      try: 
        p5ty1ans=int(input(w))
        if p5ty1ans > 6 or p5ty1ans <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if p5ty1ans <= 6 and p5ty1ans > 0:
            break
        else:
          break
      except:
        print(num)

    #-------------------------5.1. Angles-------------------------------
    
    if p5ty1ans == 1:
      print(b+"And what are we finding?")
      for x in p51:
        print(lg+x)
      while True:
        try: 
          p5ty1ans=int(input(w))
          if p5ty1ans > 3 or p5ty1ans <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p5ty1ans <= 3 and p5ty1ans > 0:
              break
          else:
            break
        except:
          print(num)

      print(b+"And are we finding the answer in degrees or radians?")
      for x in p5dr:
        print(lg+x)
      while True:
        try: 
          dr=int(input(w))
          if dr > 2 or dr <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if dr <= 2 and dr > 0:
              break
          else:
            break
        except:
          print(num)

      if p5ty1ans == 1:
        x,xs,y,ys='opposite','O','hypotenuse','H'
      if p5ty1ans == 2:
        x,xs,y,ys='adjacent','A','hypotenuse','H'
      if p5ty1ans == 3:
        x,xs,y,ys='opposite','O','adjacent','A'
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+f'What is the length of the side {x} given to the angle we are finding?', unit)
          x=float(input(w+f'{xs} = '))
          break
        except:
          print(num)
      while True:
        try:
          print(b+f'And what is the length of the {y} side given?', unit)
          y=float(input(w+f'{ys} = '))
          if x > y:
            if p5ty1ans == 3:
              break
            else:
              print(r + "This triangle is impossible! (note the hypotenuse is always the longest side of a right traingle) Try again.")
          else:
            break
        except:
          print(num)

      if p5ty1ans == 1:
        rule = lr + str(f"\u03B8 = arcsin({x} / {y})")
        theta = lr + str(math.degrees(math.asin(x/y))) if dr == 2 else lr + str(math.asin(x/y))
      if p5ty1ans == 2:
        rule = lr + str(f"\u03B8 = arccos({x} / {y})")
        theta = lr + str(math.degrees(math.acos(x/y))) if dr == 2 else lr + str(math.acos(x/y))
      if p5ty1ans == 3:
        rule = lr + str(f"\u03B8 = arctan({x} / {y})")
        theta = lr + str(math.degrees(math.atan(x/y))) if dr == 2 else lr + str(math.atan(x/y))
      if p5dr == 1:
        print(b+"\u03B8:", theta, "\b\u00B0")
      else:
        print(b+"\u03B8:", theta)
      print(b+"The equation for finding this angle of this triangle is:", rule)
      print(b+"\nDo you have any more questions?")
      solve = input(w)

    #-----------------------5.2. Side Length---------------------------
    
    if p5ty1ans == 2:
      print(b+"And what are we finding?")
      for x in p52:
        print(lg+x)
      while True:
        try: 
          p5ty1ans=int(input(w))
          if p5ty1ans > 3 or p5ty1ans <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if p5ty1ans <= 3 and p5ty1ans > 0:
              break
          else:
            break
        except:
          print(num)

      if p5ty1ans == 1:
        x,xs,y,ys='adjacent','A','hypotenuse','H'
      if p5ty1ans == 2:
        x,xs,y,ys='opposite','A','hypotenuse','H'
      if p5ty1ans == 3:
        x,xs,y,ys='opposite','O','adjacent','A'

      print(b+'Great! So which side is given?')
      print(lg+f"1. {x}" + "\n" + f"2. {y}")
      while True:
        try: 
          side=int(input(w))
          if side > 2 or side <= 0:
            print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
            if side <= 2 and side > 0:
              break
          else:
            break
        except:
          print(num)
          
      known=xs if side == 1 else ys
      knownf=x if side == 1 else y
      unknown=ys if side == 1 else xs
      unknownf=y if side == 1 else x
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+f'What is the length of the {knownf}?', unit)
          knownnum=float(input(w+f'{known} = '))
          break
        except:
          print(num)
      while True:
        try:
          print(b+'And angle given? (please give your answer in degrees', unit)
          theta=float(input(w+'\u03B8 = '))
          break
        except:
          print(num,'3) Please give your answer in DEGREES')

      theta = math.radians(theta)
      if p5ty1ans == 1:
        
        answer = lr + str(knownnum*math.tan(theta)) if side == 1 else lr + str(knownnum*math.sin(theta))
      if p5ty1ans == 2:
        answer = lr + str(knownnum/math.tan(theta)) if side == 1 else lr + str(knownnum*math.cos(theta))
      if p5ty1ans == 3:
        answer = lr + str(knownnum/math.sin(theta)) if side == 1 else lr + str(knownnum/math.cos(theta))

      thetaword = str(math.degrees(theta)) + '\u00B0'
      if p5ty1ans == 1:
        rule = lr + str(f"{unknown} = {knownnum} * tan({thetaword})") if side == 1 else lr + str(f"{unknown} = {knownnum} * sin({thetaword})")  
      if p5ty1ans == 2:
        rule = lr + str(f"{unknown} = {knownnum} / tan({thetaword})") if side == 1 else lr + str(f"{unknown} = {knownnum} * cos({thetaword})")
      if p5ty1ans == 3:
        rule = lr + str(f"{unknown} = {knownnum} / sin({thetaword})") if side == 1 else lr + str(f"{unknown} = {knownnum} * cos({thetaword})")

      print(b+f"The length of {unknownf} is:", answer, 'unit')
      print(b+"The equation for finding the length of this side is:", rule)
      
      print(b+"\nDo you have any more questions?")
      solve = input(w)

  #========================= 6. Pythagoras ==========================

  if ans == 6:
    print("\n\n")
    print(lr + p6)
    print(b+gadj.capitalize(), "\b! Let's start from Pythagoras then!")
    print(b+'So which side of the right triangle are we finding?')
    for y in p6ty:
      print(lg+y)
    while True:
      try: 
        p6ty1ans=int(input(w))
        if p6ty1ans > 2 or p6ty1ans <= 0:
          print(r+"I'm afraid there's not such an option. Please check the list and let's choose again!")
          if p6ty1ans <= 2 and p6ty1ans > 0:
            break
        else:
          break
      except:
        print(num)
        
    #-----------------------6.1. Find Hypotenuse-----------------------
    
    if p6ty1ans == 1:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the length of the first known side given?', unit)
          aside=float(input(w+'a = '))
          break
        except:
          print(num)

      while True:
        try:
          print(b+'And what is the length of the second known side given?', unit)
          bside=float(input(w+'b='))
          break
        except:
          print(num)
      c=lr + str(math.sqrt((aside**2)+(bside**2)))
      rule=lr + f'(({aside}^2) + ({bside}^2))^(1/2) = {c}'
      print(b+'The length of the hypotenuse is:', c, 'unit')
      print(b+'The equation for finding the hypothenuse is:', rule)

      print(b+"\nDo you have any more questions?")
      solve = input(w)
      
    #---------------------6.2. Find Non-hypotenuse---------------------
    
    if p6ty1ans == 2:
      while True:
        print(b+"Great! Let's start then!")
        try:
          print(b+'What is the length of the known non-hypotenuse side given?', unit)
          bside=float(input(w+'b = '))
          break
        except:
          print(num)

      while True:
        try:
          print(b+'And what is the length of the second known side given?', unit)
          cside=float(input(w+'c='))
          break
        except:
          print(num)
      a=lr + str(math.sqrt((cside**2)-(bside**2)))
      rule=lr + f'(({cside}^2) - ({bside}^2))^(1/2) = {a}'
      print(b+'The length of the unknown side is:', a, 'unit')
      print(b+'The equation for finding this unknown side is:', rule)

      print(b+"\nDo you have any more questions?")
      solve = input(w)
