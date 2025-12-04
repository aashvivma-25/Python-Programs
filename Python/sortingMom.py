# ---------------------------------------------
# Create two parallel lists:
# Childname  -> list of names
# ChildAge   -> list of ages (same index as names)
# ---------------------------------------------
Childname = ["daria", "aashvi", "saanvi", "janet", "aadhira", "nikitha"]
ChildAge  = [150, 14, 110, 12, 50, 2]

# ---------------------------------------------
# SORTING THE TWO PARALLEL LISTS
# Using a simple nested loop (like bubble sort)
# Outer loop goes through each index (counter1)
# Inner loop compares with the remaining items (counter2)
# If a smaller age is found, swap both age AND name
# ---------------------------------------------
for counter1 in range(len(ChildAge)):          # Loop through each element
    for counter2 in range(counter1, len(ChildAge)):   # Compare with all elements after it
        
        # If the current age is greater than the compared age, swap them
        if ChildAge[counter1] > ChildAge[counter2]:

            # Swap ages
            tempAge = ChildAge[counter1]
            ChildAge[counter1] = ChildAge[counter2]
            ChildAge[counter2] = tempAge

            # Swap corresponding names to match sorted ages
            tempName = Childname[counter1]
            Childname[counter1] = Childname[counter2]
            Childname[counter2] = tempName

# ---------------------------------------------
# PRINT the final sorted output
# ---------------------------------------------
for n in range(len(Childname)):
    print(Childname[n] + " : " + str(ChildAge[n]))
