def sucet(zoznam1, zoznam2):
    vysl = []
    ix = min(len(zoznam1), len(zoznam2))
    for i in range(ix):
        vysl.append(zoznam1[i] + zoznam2[i])
    return vysl + zoznam1[ix:] + zoznam2[ix:]

sucet(['1.', '2.', '3.', '4.'], list('python'))
