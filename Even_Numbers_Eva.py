#Function has to be defined, vals is a freely chosen word
def count_even(vals):
    """Returns the amount of even numbers."""
    #counting variable defined
    c=0
    #loop, v is a freely chosen variable
    for v in vals:
        #% is modulus
        if (v % 2) == 0:
            # counting variable
            c=c+1
    return c
#list
x = [-2, -4, 3, 6, 88, 76, -7]
#only
y=count_even(x)

print("The list {} contains {} even numbers.".format(x,y))
