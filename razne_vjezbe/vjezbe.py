'''
def is_greater(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(is_greater(4,21,24,))

'''
''''---------------------------------------------------------------------------'''
'''
num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter a second number: "))

def calculator(num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        print("Invalid operator")

print(calculator(num1,num2,op))
'''
''''-----------------------------------------------------------------------------'''
#Dictonary
'''
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(monthConversions["Jan"])

ili mozemo ovako

print(monthConversions.get("Jan"))

ako nije unesena vrijednost koju imamo u rijecniku onda se moze i ovako napraviti

print(monthConversions.get("Luv","Not a correct value"))
'''''''-------------------------------------------------------------------------------------------'''
'''while loop

i = 1
while i <= 100:
    print(i)
    i += 1

print("Done with loop")
'''
'''-----------------------------------------------------------------------------------------'''

#Guessing game
'''
secret_word = "Lopta"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Guess a word: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You have no more guesses left!")
else:
    print("You win!")
'''
#FOR LOOP
'''
friends =["Jim","Kareen","Kevin"]
for friend in friends:
    print(friend)
'''
#EXPONENT FUNCTION

'''def raise_to_power(base, exp):
    result = 1
    for index in range(exp):
        result = result * base
    return result

print(raise_to_power(2, 4))'''

#2D List & Nested Loops
#2D List
'''number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
'''
'''print(number_grid[1][1])'''

#Nested Loops

'''for row in number_grid:
    for col in row:
        print(col)
'''
#Building a translator

'''def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))'''

#Try Except





















