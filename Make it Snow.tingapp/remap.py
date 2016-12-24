def remap(oldValue, oldMin, oldMax, newMin, newMax):
    oldValue = float(oldValue)
    oldMin = float(oldMin)
    oldMax = float(oldMax)
    newMin = float(newMin)
    newMax = float(newMax)

    oldRange =  oldMax - oldMin 

    if oldRange == 0:
        newValue = newMin
    else:
        newRange = newMax - newMin
        newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin
    return newValue