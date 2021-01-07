def containsWord(s, w):
    for KEY in w:
        if f' {KEY} ' in f' {s} ':
            return True
    return False