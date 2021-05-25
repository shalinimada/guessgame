#while loop
i=1
while i<=20 and i!= 16:
    print(i)
    i+=1

print("reached number 16")

#guessing game

secret_word="shalini"
guess=""
guess_count=0
outofguesses=False
print("Hint: It's a name\nyou have three guesses.\nBegin")
while guess!=secret_word and not(outofguesses):
    if guess_count<3 :

        guess=input("guess please:")
        guess_count += 1
    else:
        outofguesses=True

if outofguesses:
    print("you loose!Try Again.")
else:
    print("you guessed right!you win")