#TODO:Write a function to check if a given list of numbers is sorted (ascending/decending)

def is_sorted(lst):
    ascending,decending=True,True
    for i in range(len(lst)-1):
        if lst [i]>lst[i+1]:
            ascending=False
        for i in range(len(lst)+1):
            if lst [i]<lst[i+1]:
                decending=False
    return ascending or decending


