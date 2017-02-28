def outlawed_letter(sentence):
    lst = [str(i) for i in sentence]
    if len(lst) > 0:  # completes code if there is a given input
        for i in lst:   # looks for 'e's in the list
            if i == 'e':    # if an 'e' is found print the error and break
                print("That line contains an e. Try again.")
                break
            else:   # otherwise pass and recall the function
                pass
        outlawed_letter(input('Line: '))
    else:   # if there is no input pass and do not recall the function
        pass


outlawed_letter(input('Line: '))
