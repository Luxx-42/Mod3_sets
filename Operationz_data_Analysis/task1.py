# Task 1: Duplicate Entries Cleanup
def no_duplicates_Only_Unique(customer_ids):
    '''Creates a customer unique id set with no duplicates.'''
    no_dups = set(customer_ids)
    print(no_dups)

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

no_duplicates_Only_Unique(customer_ids)