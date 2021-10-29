def EuclidesSubstraction(a,b):
    if a == b:
        print(a)
        return a
    else:
        if a > b:
            a = a-b
        elif a < b:
            b = b-a
    return EuclidesSubstraction(a,b)


def EuclidesDivision(a,b):
    if a == b:
        print(a)
        return a
    else:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    return EuclidesSubstraction(a,b)

