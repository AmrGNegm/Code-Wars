def disemvowel(string):
    for i in "aeoiuAEOIU":
        string = string.replace(i, "")
    
    return string
