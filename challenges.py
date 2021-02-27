class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            elif strA[i - 1] == strB[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]+1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
    
    return dp_table[rows-1][cols-1]


def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity == 0:
        return 0
 
    item_value = items[0][2]
    item_weight = items[0][1]

    if capacity >= item_weight:
        value_with = item_value + knapsack(items[1:], capacity - item_weight)
    else:
        value_with = 0

    value_without = knapsack(items[1:], capacity)
    # first_item = items[0]
    # value_with = first_item[2] + knapsack(items[1:], capacity - item_weight)
    # value_without = (items[1:], capacity)
          
    return max(value_with, value_without)


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for col in range(cols)] for irow in range(rows)]
    

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows - 1):
        for col in range(cols - 1):
            item_value = items[row-1][2]
            item_weight = items[row-1][1]
            
            if row == 0 or col == 0:
                dp_table[row][col] = 0
            # if the item fits in the knapsack
            current_capacity = col
            if current_capacity - item_weight >= 0:
                # include it
                    # two table lookups
                    # check what is above it in the col
                    # either change the value to the number above it 
                    # or subtract the weight from the capacity and 
                    # check the resutlting capacity column for the value 
                    # pick the max value of the two
            # if it doesn't fit in the knapsack
            else:
                # 
                # don't include it
                    # one table lookup
                    # check the number in in the row above (same column)
                    # set value to that number

                
                
            if dp_table[row - 1][col] or dp_table[row][col -1] > 0
            

            return dp_table[rows-1][cols-1]
    
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if not str1 and not str2:
        return 0
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
        
    # If last characters match
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])

    # If last characters are not identical, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(edit_distance(str1, str2[:-1]),      # Insert
                   edit_distance(str1[:-1], str2),       # Remove
                   edit_distance(str1[:-1], str2[:-1])   # Replace
                )


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    if len(str1) == 0 and len(str2) == 0:
        return 0
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # If last characters match
    if str1[:-1] == str2[:]:
        return edit_distance_dp(str1[:-1], str2[:-1])
 
    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(edit_distance_dp(str1, str2[:-1]),   # Insert
                   edit_distance_dp(str1[:-1], str2),   # Remove
                   edit_distance_dp(str1[:-1], str2[:-1])   # Replace
                )

    return dp_table[rows-1][cols-1]