def deployYatesOrder(num_letters=3, alphabet="abcdefghijklmnopqrstuvwxyz"):
    yates_ordered_list = [""]
    factors = [factor for factor in alphabet[0:num_letters]]
    for letter in factors:
        effect_list = []
        for factor in yates_ordered_list:
            effect_list.append(factor + letter)
        yates_ordered_list += effect_list
    return yates_ordered_list

def deployYatesMemoryError(num_letters=3, alphabet="abcdefghijklmnopqrstuvwxyz"):
    yates_ordered_list = [""]
    factors = [factor for factor in alphabet[0:num_letters]]
    for letter in factors:
        for factor in yates_ordered_list:
            yates_ordered_list.append(factor + letter)
    return yates_ordered_list

def deployYatesForward(treatment_results_in_Yates_order, all_cols=False):
    """
    Have the treatment results in Yates order
    In order, add the even items to the odd items directly before each, and append
    each to the next column.
    In order, subtract the even items from the odd items directly before each, and append
    each to the same next column.
    Repeat steps two and three with the most recent column
    Repeat step four until there are a total of k new columns, aside from the
    original Yates order
    Divide the first by len(column) and append it to a results column
    Divide the rest by len(column)/2 and append it to the same results column

    Note, write a book about reframing problems to focus on the extraction of
    their benefits. (Keep a log of how I*'ve done this: Baby, workouts, PUBG, missed
    deadlines, confusion, reading, money, experiment design.) Also, write a book
    about DVORAK typing, why I* find programming exciting, and why I* use the * in every

    """
    assert type(treatment_results_in_Yates_order) == list

    from math import log

    num_columns_needed = int(log(len(treatment_results_in_Yates_order),2))
    cols = [treatment_results_in_Yates_order]

    for col_num in range(num_columns_needed):
        ctr = 0
        # Add phase
        col = []
        while ctr < len(treatment_results_in_Yates_order):
            summed_pair = cols[col_num][ctr + 1] + cols[col_num][ctr]
            col.append(summed_pair)
            ctr += 2
        # Subtract phase
        ctr = 0
        while ctr < len(treatment_results_in_Yates_order):
            differed_pair = cols[col_num][ctr + 1] - cols[col_num][ctr]
            col.append(summed_pair)
            ctr += 2
        cols.append(col) # cols[0] = col


    result_col = []
    start = True
    for value in cols[-1]:
        if start:
            result_col.append(value/len(cols[-1]))
            start = False
        else:
            result_col.append(value/(len(cols[-1])/2))

    cols.append(result_col)
    if all_cols == True:
        return cols
    else:
        return result_col

# How do I make a statement conditional on being imported. file != "__main__"?
# print("Yates imported...\n")

treatments = [3,5,4,7, 8,10,5,6, 12,11,5,7, 3,5,9,13]
print(deployYatesForward(treatments, all_cols=True))
