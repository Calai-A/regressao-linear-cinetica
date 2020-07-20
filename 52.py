lc = lc.pop
    abs_conc = []
    for i in range(len(lc)):
        abs_conc.append(lc)
    for i in abs_conc:
        abs_conc[i] = ((abs_conc[i] - abs_conc[0]) / (abs_conc[-1] - abs_conc[0])*c0)
        return abs_conc


c0 = float(input('Insira o dado da concentração inicial do reagente'))
    lc = espec_to_conc(lc,c0)
