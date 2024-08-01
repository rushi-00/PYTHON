# -*- coding: utf-8 -*-
"""
1.Write a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

"""

def check_vowel(letter):
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("letter is a vowel.")
    elif letter.lower() == 'y':
        print("Sometimes 'y' is a vowel, and sometimes 'y' is a consonant.")
    else:
        print("letter is a consonant.")

def main():
    letter = input("Enter a letter of the alphabet: ")
    if len(letter) == 1 and letter.isalpha():
        check_vowel(letter)
    else:
        print("Please enter a single letter of the alphabet.")

if __name__ == "__main__":
    main()
    


"""
2. Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""
def main():
  
    shape_names = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon",10: "decagon"}

    num_sides = int(input("Enter the number of sides from 3 to 10: "))
    if 3 <= num_sides <= 10:
     
        shape_name = shape_names[num_sides]
        print(f"A shape with {num_sides} sides is called a {shape_name}.")
    else:
        print("Error: Number of sides must be between 3 and 10.")

if __name__ == "__main__":
    main()


"""
4. A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.

"""
def triangle_type(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def main():
    a = float(input("Enter the length of the first side of the triangle: "))
    b = float(input("Enter the length of the second side of the triangle: "))
    c = float(input("Enter the length of the third side of the triangle: "))

    if a + b > c and a + c > b and b + c > a:
        triangle = triangle_type(a, b, c)
        print(f"The triangle with side lengths {a}, {b}, and {c} is {triangle}.")
    else:
        print("The given side lengths do not form a valid triangle.")

if __name__ == "__main__":
    main()
    
"""
5. The year is divided into three seasons: summer, rainy and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, Write a program to display the season if date is given.

"""
def get_season(month, day):
    
    if (month == 3 and day >= 20) or (month == 4) or (month == 5) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day < 23):
        return "Summer"
    elif (month == 9 and day >= 23) or (month == 10) or (month == 11) or (month == 12 and day < 21):
        return "Autumn"
    else:
        return "Winter"

def main():
    
    month = int(input("Enter the month : "))
    day = int(input("Enter the day : "))

    
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid date.")
        return

    season = get_season(month, day)
    print(f"The season for {month}/{day} is {season}.")

if __name__ == "__main__":
    main()
    
