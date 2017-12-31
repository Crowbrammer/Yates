from BuildPrincipleBlock import buildBlock
from Yates import deployYatesOrder

def mod2Multiply(effect1, effect2):
    """
    I don't know if the core algorithm could work or not for three effects.
    """
    mod_2_product = ""
    for letter1 in effect1:
        if letter1.lower() not in effect2.lower():
            mod_2_product += letter1
    for letter2 in effect2:
        if letter2.lower() not in effect1.lower():
            mod_2_product += letter2

    return mod_2_product

principle_block = buildBlock(["ABCE", "BCDF", "ADEF"], deployYatesOrder(6))
principle_block2 = buildBlock(["ABF", "CDE", "ABCDEF"], deployYatesOrder(6))

def discoverAndShowAliasRelations(identity_effects, all_effects):
    """
    Inputs:
    Identity effects
    List of effects(?)

    Outputs:
    LoL's of paired effects

    degrees of freedom:
    Two variables = 2 (Not 1?)

    Note: Alphabetize before appending. Delete duplicates.
    """
    LoL = []
    for any_effect in all_effects:
        # degree of freedom 1
        L = [any_effect]
        # degree of freedom 2
        for id_effect in identity_effects:
            print("{} == {}:".format(any_effect, id_effect), any_effect == id_effect)
            if any_effect == id_effect:
                # make sure this works.
                continue
            L.append(''.join(sorted(mod2Multiply(id_effect, any_effect))))
        LoL.append(L)
    return LoL

all_effects = [effect.upper() for effect in deployYatesOrder(6)][1:]
for L in discoverAndShowAliasRelations(["ABCE", "BCDF", "ADEF"], all_effects):
    if "AB" in L:
        print(L)

def printStuff():


    # p2 = principle_block2
    # p1 = principle_block
    # Need to alphabetize it.
    p = ["", "abce", "bcdf", "adef"]
    bc = buildDerivativeBlock("bc", p)
    abd = buildDerivativeBlock("abd", p)
    cef = buildDerivativeBlock("cef", p)
    all_blocks = [p, bc, abd, cef]
    for x in range(100):
        print()
    print(principle_block)
    for block in all_blocks:
        print(block)


    # for each in all_blocks:
    #     for each in each:
    #         if each in p1:
    #             print(each)


def buildDerivativeBlock(effect_not_in_principle, principle_block):
    derivative_block = []
    for principle_treatment in principle_block:
        derivative_block.append(mod2Multiply(effect_not_in_principle, principle_treatment))
    return derivative_block

# printStuff()
