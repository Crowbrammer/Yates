from math import log

treatment_results_in_Yates_order = [3,5,4,7, 8,10,5,6, 12,11,5,7, 3,5,9,13]

# What appears to cause the issue:
num_columns = int(log(len(treatment_results_in_Yates_order),2))
cols = []
col = treatment_results_in_Yates_order
cols.append(col)
# print("cols:", cols) # Shows the same result as cols for the working code.
# End of perceived issue area.

ctr = 0

for col_num in range(num_columns):
    col = []
    # This doesn't stop at or after 16.
    while ctr < len(treatment_results_in_Yates_order):
            summed_pair = cols[0][ctr + 1] + cols[0][ctr]
            col.append(summed_pair)
            ctr += 2

# Why does ctr not stop at 16 for this code... but does for the other, "working"
# code?

The absence of col
