# Brainstorm

## parse filename

- index of 0 = m1 *figure out how to handle index not found*
- if m1+1 is 0-9 could be month.
- if index of 0 is null index of 1 = m1 *again crash-safe*
- if m1+1 is 0-2 could be month
- if filename[m1+2,m1+6] is within 5 years of current year could be date.
if filename[m1,m1+2] == filename[m1+9,m1+11] and filename[m1+4,m1+8] == filename[m1+13,m1+17] we can be pretty sure we're good.
  - This may be improved by a regex
- filename[m1,m1+2] -> report_month
- filename[m1+4,m1+8] -. report_year

## Feature thoughts / Roadmap

### First

- [ ] Ask for for folder
- [ ] Show all text files in a list
- [ ] Ask for start date
- [ ] Parse lines and display only

### Next

- [ ] Add full parsing
- [ ] Run full checks before showing the file list
- [ ] Write output to text file. Maybe CSV

### Later

- [ ] Keep a client list. Maybe as TOML?
- [ ] Somehow notify of missing clients
- [ ] Research SQL and datastructures and connections etc to write directly to the database. Likely need to store connection info in another TOML
- [ ] Options to write to screen, CSV, TSV, DB, other?

### Much Later

- [ ] Multi-select folders?
- [ ] Highlight missing client(s) within selection
