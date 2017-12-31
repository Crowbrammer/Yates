from Yates import deployYatesOrder
# from BuildDerivativeBlock import mod2Multiply

def buildBlock(confounded_effects, treatment_list):

    ctr = 0
    block = []

    assert type(confounded_effects) == list

    for treatment in treatment_list:
        for confounded_effect in confounded_effects:
            add_treat = True
            for letterT in treatment:
                for letterC in confounded_effect:
                    if letterT.lower() == letterC.lower():
                        ctr += 1
            if ctr % 2 != 0:
                add_treat = False
                break
        if add_treat == True:
            block.append(treatment)
        ctr = 0

    return block

def buildPrincipleFromPrinciple(arg):
    pass
# for each in buildBlock(["ABCE", "ABDF", "CDEF"], deployYatesOrder(6)):
#     print(each)
