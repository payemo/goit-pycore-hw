import random

MIN_VALUE = 1
MAX_VALUE = 1000

def get_random_ticket_numbers(min_value:int, max_value:int, quantity:int)->list[int]:
    """Returns a sorted list of randomly generated numbers.
    
    Random numbers must be generated according to the input
    parameter which shoud follow the statement: min_value <= quantity <= max_value.

    Output list of randomly gnerated numbers must contain only unique elements.

    Parameters
    ----------
    min_value : int
        Minimum generated value.
    max_value :
        Maximum generated value.
    quanity:
        Amount of elements that must be generated.

    Returns
    -------
    ticket_numbers : list[int]
        Sorted list of randomly generated numbers.

    Raises
    ------
    ValueError
        - { 'min_value' < 1 | 'max_value' > 1000 }
        - If the sample size (max_value - min_value) is larger than the population size (quantity).
    """

    if min_value < MIN_VALUE or max_value > MAX_VALUE:
        raise ValueError(f"Min: {min_value} > {MIN_VALUE} | Max: {max_value} > {MAX_VALUE}")
    if(quantity < 0 or quantity > (max_value - min_value + 1)):
        raise ValueError(f"Input parameters are invalid: {min_value} <= {quantity} <= {max_value}")

    # Generate a sequence of range [min_value, max_value] and
    # returns a sorted list of k-th random samples.
    return sorted(random.sample(range(min_value, max_value + 1), quantity))

print(get_random_ticket_numbers(1, 49, 6))
#print(get_random_ticket_numbers(49, 1, 3)) # raises exception
#print(get_random_ticket_numbers(-1, 1000, 10)) # raises exception