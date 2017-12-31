from math import log

treatment_results_in_Yates_order = [3,5,4,7, 8,10,5,6, 12,11,5,7, 3,5,9,13]

# New format that stops the issue:
num_columns_needed = int(log(len(treatment_results_in_Yates_order), 2))
cols = [treatment_results_in_Yates_order]
print("cols:", cols) # Shows the same result as cols for the broken code.
# End of perceived "fix".

ctr = 0

for col_num in range(num_columns_needed):
    col = []
    # This does stop at 16.
    while ctr < len(treatment_results_in_Yates_order):
            summed_pair = cols[0][ctr + 1] + cols[0][ctr]
            col.append(summed_pair)
            ctr += 2
