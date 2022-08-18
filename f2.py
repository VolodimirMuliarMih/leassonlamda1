#Function def with list & dict
list_old = [1,22,33,1,4,5,6,1,22,11,33] #

def dictcreater (*args):
        newdict = {}.fromkeys(list_old, 0)
        for a in list_old:
            newdict[a]+= 1
        print(newdict)
        return

dictcreater(list_old)