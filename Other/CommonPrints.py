

def shortDottedLine():
    return "- - - - - - - - - - - - - - - - - -"

def shortLine():
    return "-----------------------------------"

def fullLine():
    return "------------------------------------------------------------------------------------"

def fullDottedLine():
    return "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

def fullHashLine():
    return "####################################################################################"

def exitString():
    rtn = fullHashLine()
    for i in range(4):
        rtn += "\n" + fullHashLine()
    rtn += "\n                            EXITING PROCESS STRUCTURE\n"
    for i in range(5):
        rtn += f"{fullHashLine()}\n"
    return rtn


