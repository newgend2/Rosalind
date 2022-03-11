# My first method
def shift_adult(adult_list, newborn_num):
    if len(adult_list) >= 1:
        for z in range(len(adult_list)):
            if z == 0:
                adult_list_new = []
                adult_list_new.append(newborn_num)
            else:
                adult_list_new.append(adult_list[z - 1])

    return adult_list_new


# print(shift_adult([1], 5))


def fib_mort2(n, m):
    if m == 1:
        if n == 1:
            return 1
        elif n > 1 or n < 1:
            return 0
    elif m == 2:
        return 1
    elif m < 1:
        return 0
    else:

        # create genration cycle list
        gen_list = [0] * m
        gen_list[0] = 1  # set 1 newborn pair in newborn index
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:

            for i in range(1, n):
                newborn_number = gen_list[0]
                adult = gen_list[1:-1]

                newborn_adult_contrib = sum(adult)  # all adults reproduce a pair.
                newborn_old_contrib = gen_list[-1]  # olds get converted into newborns on next iteration

                adult_new = shift_adult(adult, newborn_number)
                old_new = adult[-1]

                gen_list = [newborn_adult_contrib + newborn_old_contrib] + adult_new + [old_new]

            return sum(gen_list)


# print(fib_mort2(99, 19))
# __________________________________________

# SOLUTION METHOD 1
# CATEGORIZE ALL RABIT AGE GROUPS IN A LIST.
# WITH THE 0'TH ELEMENT BEING THE NUMBER OF NEWOBORNS, THE LAST ELEMENT BEING THE # OF RABBITS ON DEATH ROW,
# AND EVERYTHING IN BETWEEN BEING ADULTS WHO WILL LIVE ON TO THE NEXT CYCLE.
# WITH THIS FORMAT THE LIST HAS TO BE THE SAME LENGTH AS THE INPUT VARIABLE M DENOTING THE LIFESPAN OF EACH RABBIT IN
# MONTHS BECAUSE RABBIT AGE CAN VARY FROM 1 MONTH TO THE GIVEN INPUT AGE.


def fib(n, m):
    ages = [1] + [0] * (m - 1)
    for i in range(n - 1):
        # sum(ages[1:]) gets the newborn number and places it in he newborn age slot
        # ages [:-1] shifts the age numbers 1 to the right and gets rid of the last age slot which die
        # this function solves the problem using the same approach as my method except updates the generation list
        # using more efficient array slicing... very cool.
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


print(fib(7, 3))
# with m = 3 sequence goes [1,1,2,2,3,4,5]




# SOLUTION USING RECURSION




