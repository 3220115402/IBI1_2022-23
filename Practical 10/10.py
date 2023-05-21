# Mortgage	affordability calculator
def can_buy_house(value, salary):
    """
    Determines whether an individual can buy a specific house based on the total value of the house and the purchaser's annual salary.
    """
    max_value = 5 * salary
    if value <= max_value:
        return "Yes"
    else:
        return "No"
    
# Example usage
print(can_buy_house(180000, 35000)) # Should print "Yes"



# Triathlon	times database
class Triathlon:
    """
    Contains information about individual athletes and their competitions.
    """
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time
    
    def print_details(self):
        """
        Prints all the details of the triathlete in a single line.
        """
        print(f"{self.first_name} {self.last_name} competed in {self.location} with swim time {self.swim_time}, cycle time {self.cycle_time}, run time {self.run_time}, and total time {self.total_time}.")

# Example usage
triathlete = Triathlon("John", "Doe", "London", 10, 20, 30)
triathlete.print_details() # Should print "John Doe competed in London with swim time 10, cycle time 20, run time 30, and total time 60."



# Protein-coding capability	calculator
def protein_coding(sequence):
    """
    Determines whether a given DNA sequence is likely to be protein-coding or not based on the distance between an opening 'ATG' codon and a final stop 'TGA' codon.
    """
    sequence = sequence.upper()
    start = sequence.find('ATG')
    stop = sequence.rfind('TGA')
    if start == -1 or stop == -1:
        return "unclear", 0
    coding = sequence[start:stop+3]
    coding_percentage = len(coding) / len(sequence)
    if coding_percentage > 0.5:
        return "protein-coding", coding_percentage
    elif coding_percentage < 0.1:
        return "non-coding", coding_percentage
    else:
        return "unclear", coding_percentage
    
# Example usage
print(protein_coding("ATGCGCGCGTGA")) # Should print ("protein-coding", 1.0)


