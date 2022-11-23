# EXERCISE 13 FALLING DISTANCE PROGRAM

GRAVITY = 9.8

def main():

    iterator = 10

    print("Time \tDistance")
    print("-------------------")

    for checker in range(iterator):
        checker += 1

        falling_distance(checker)

        print(checker, "\t", format(falling_distance(checker=checker),
                                      ',.2f'), "m", sep='')

def falling_distance(checker):
    distance = 0.5 * GRAVITY * checker**2
    return distance
    

main()
