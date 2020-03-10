# Given a string that may or may not contain a letter of interest. 
# Print the index location of the first and last appearance of f.
# If the letter f occurs only once,then output its index.
#  If the letter f does not occur, then do not print anything.
# Don't use loops in this task.


def stroka():
    s=input("Введите  :")
    fir=s.index('f')
    sec=s[::-1]
    thir=sec.index('f')
    # print("первый индекс: " , fir)
    # print("с конца индекс: " , thir)
    return('первый индекс: %s,с конца индекс %s'%(fir,thir))
print(stroka())

#Eldiyar

# word = input()
# if "f" in word:
#     if word.count("f") > 1:
#         print(word.find("f"))
#         print(word.rfind("f"))
#     else:
#         print(word.find("f"))