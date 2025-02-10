# Here is what should be in the final submission file
# This is NOT the answer key
from random import randint

# Tell the users what their options are

# Prompt partner A for their strategy choice
# Check that partner A is within 1-3 and re-prompt if not

# Prompt partner B for their strategy choice
# Check that partner B is within 1-3 and re-prompt if not


# Prompt for number of trials to be ran
# Check that number of trials is within 10-500 and reprompt if not

# Init 0 years in jail before trials are ran
partnerACount = 0
partnerBCount = 0

for x in range(trials):
    # If statements for partnerAStrategy to assign their choice
    # If statements for partnerBStrategy to assign their choice


    # If statements for partnerAChoice and partnerBChoice
        # Increment each partner's count as needed


# Now we are outside of the for loop
partnerAAverage = partnerACount / trials
partnerBAverage = partnerBCount / trials

print("Partner A spent an average of", partnerAAverage, "years in jail.")
print("Partner B spent an average of", partnerBAverage, "years in jail.")

