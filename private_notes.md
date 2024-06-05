# Brainstorm

## parse filename

- index of 0 = m1 *figure out how to handle index not found*
- if m1+1 is 0-9 could be month.
- if index of 0 is null index of 1 = m1 *again crash-safe*
- if m1+1 is 0-2 could be month
- if filename[m1+2,m1+6] is within 5 years of current year could be date.
if filename[m1,m1+2] == filename[m1+9,m1+11] and filename -
