print("Welcome to my Basic College Quiz game")

Name=(input("Enter your name: "))
print('Best luck',Name)

Reaction=input("Are u ready? ")

if Reaction.lower() != "yes":
    quit()

print("Here comes the first question")

point=0

answer=(input("What is the full form of CPU? "))
if answer.lower()=='central processing unit':
    print("Correct :)")
    print("You Earned one point")
    point+=1
else:
    print("Incorrect :(")        

answer=(input("What is the full form of GPU? "))
if answer.lower()=='graphical processing unit':
    print("Correct :)")
    print("You Earned one point")
    point+=1
else:
    print("Incorrect :(")        

answer=(input("What is the full form of IEDC? "))
if answer.lower()=='innovation and enterpreneurship development center':
    print("Correct :)")
    print("You Earned one point")
    point+=1
else:
    print("Incorrect :(")        

answer=(input("What is the full form of ED? "))
if answer.lower()=='enterpreneurship development':
    print("Correct :)")
    print("You Earned one point")
    point+=1
else:
    print("Incorrect :(")        

answer=(input("What is the full form of DS? "))
if answer.lower()=='data structures':
    print("Correct :)")
    print("You Earned one point")
    point+=1
else:
    print("Incorrect :(")        

print("u got  " + point + " out of 5")
