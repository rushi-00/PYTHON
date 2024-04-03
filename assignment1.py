"""ASSIGNMENT NO 1
1 ) Write a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user."""

name = "Rushikesh"
address = "Jai janardhan hostel,Near sanjivani petrol pump."
city = "Kopargaon"
pin_code = "423603"
state = "Maharashtra"

print(name)
print(address)
print(city + ", " + state + "-" + pin_code)


"""2 )Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with."""

length=float(input("enter the length of the room  :"))
print(length)

width=float(input("enter the width of the room  :"))
print(width)

area=length*width
print(area, "feet")

"""3)Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre."""


length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

area_feet = length*width
area_acres = area_feet / 43560
print(area_acres,"acres")

"""4)In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

small_deposit = 0.10
large_deposit = 0.25

num_small = int(input("Enter the number of containers holding one liter or less: "))
num_large = int(input("Enter the number of containers holding more than one liter: "))
s=num_small*small_deposit
r=num_large*large_deposit
t=r+s
print(f"Refund from small drink container is: {s}$ : ")
print(f"Refund from large drink container is :{r}$ ")
print(f"Total Refund drink container is : {t}$")



"""5)The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places."""

meal = int(input("Enter the cost of the meal: $"))
tax = int(input("Enter the tax rate : "))

tax_amount = (tax/meal)*100
tip_amount = (18/meal)*100
total_cost = meal + tax_amount + tip_amount

print("Tax amount: $",tax_amount)
print("Tip amount: $",tip_amount)
print("Grand total: $",total_cost)


"""6)Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters."""

feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches:"))

total_inches = feet * 12 + inches
centimeters = total_inches * 2.54  #1 inch is 2.54cms
height_centimeters=centimeters 

print("The height in centimeters is " ,centimeters)


