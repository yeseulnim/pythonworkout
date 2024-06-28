# write a function (run_timing) that asks how long it took you to run 10km.
# the function continues to ask how long (in minutes) until user hits enter
# at that point the function exits -
# but only after calculating and displaying the average time that the 10km runs took
# note that the numeric inputs and outputs should be all floating-point values.

def run_timing():
    run_time_total = 0
    run_count = 0
    while run_time := input("Enter 10km run time (in minutes): "):
        try:
            run_time_total += int(run_time)
            run_count += 1
        except:
            break
    print(f"Average of {run_time_total/run_count:.2f}, over {run_count} runs.")

#run_timing()



# write a function that takes a float and two integers (before and after).
# the function should return a float consisting of before digits before the decimal point
# and after digits after.
# thus, if we call the function with 1234.5678, 2, 3
# the return value should be 34.567


def float_cut(f:float, before:int, after:int):
    #before
    num = f%(10**(before))
    #after
    num = num//(0.1**after)
    num = num/10**after
    return num

#print(float_cut(1234.5678,2,3))


# explore the decimal class, which has an alternative floating point representation
# that is as accurate as any decimal number can be.
# write a function that takes two strings from the user, turns them into decimal instances,
# and then prints the floating-point sum of the user's two inputs.
# in other words, make it possible for the user to enter 0.1 and 0.2 and for us to get 0.3 back.

from decimal import Decimal
def dec(a, b):
    a = str(a)
    b = str(b)
    a_b = Decimal(a)+Decimal(b)
    return float(a_b)

print(dec(0.1,0.2))


