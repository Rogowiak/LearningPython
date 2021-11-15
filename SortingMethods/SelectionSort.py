def FindIndex(tab, StartIndex):
    d = len(tab)
    MinIndex = StartIndex
    MinValue = tab[StartIndex]
    for i in range(StartIndex, d):
        if tab[i] < MinValue:
            MinIndex = i
    return MinIndex


def SelectionSort(tab):
    d = len(tab)
    for i in range(d):
        index = FindIndex(tab,i)
        if index != i:
            tmp = tab[i]
            tab[i] = tab[index]
            tab[index] = tmp
    PrintArray(tab)
    

def PrintArray(tab):
    d = len(tab)
    for i in range(d):
        print(tab[i])




