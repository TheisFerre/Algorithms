import string
import numpy as np
import pandas as pd

def full_absorb(df):
    '''
    Recursive Helper-function.
    absorbs redundant columns in Dataframe
    '''
    # Go through every column and check for redundancy
    for left_col_idx in range(len(list(df))):
        for right_col_idx in range(len(list(df))):
            if left_col_idx < right_col_idx:
                col_dif = np.array(df.iloc[:, right_col_idx]) - \
                          np.array(df.iloc[:, left_col_idx])
                # If information in the left-column
                # is fully explained in the right-column
                # then remove the right-column,
                # and recursively call full_absorb
                if 1 not in col_dif:
                    df.drop(df.columns[right_col_idx],
                            axis=1, inplace=True)
                    return(full_absorb(df)) 
    # Base call of recursive function
    return df

def insert_absorb(index, true_list):
    '''
    Insert-Absorb Algorithm for Compact Letter Display (CLD)
    of significances between Treatments
    The problem of CLD is a NP-hard problem..
    The Insert-Absorb is a heuristic algorithm
    that does not guarantee the optimal solution.
    Furthermore, one could implement 'Sweeping'.
    Sweeping is used to reduce redundant letters,
    although this does not change the final conclusion of the algorithm.
    Source:
    http://www.akt.tu-berlin.de/fileadmin/
    fg34/publications-akt/letter-displays-csda06.pdf
    '''
    # Initialize empty Dataframe
    algo_df = pd.DataFrame(index=index)
    algo_df['0'] = np.ones(len(algo_df), dtype=int)
    

    # Find index for every significant treatment
    for count, tup in enumerate(true_list):

        idx1 = algo_df.index.get_loc(tup[0])
        idx2 = algo_df.index.get_loc(tup[1])

        # Go through Dataframe and add new column if
        # current a column contains '1' for both indices
        col = 0
        while col < len(list(algo_df)):
            if algo_df.iloc[idx1, col] == 1 and \
               algo_df.iloc[idx2, col] == 1:

                algo_df.insert(col+1,
                               str(count)+'_'+str(col),
                               np.array(algo_df.iloc[:, col]),
                               allow_duplicates=False)
                algo_df.iloc[idx1, col] = 0
                algo_df.iloc[idx2, col+1] = 0

                # Absorb redundant columns
                algo_df = full_absorb(algo_df)
            col += 1

    return algo_df


def compact_letter_report(significant_list, sorted_groups):
    insert_absorb_df = insert_absorb(sorted_groups, significant_list)
    
    # Horinzontally flip the Dataframe and absorb redundant columns the last time
    flipped = np.fliplr(insert_absorb_df.values)
    flipped_df = full_absorb(pd.DataFrame(flipped))
    flipped_values = flipped_df.values

    alphabet = string.ascii_uppercase
    cols = [alphabet[i] for i in range(flipped_values.shape[1])]
    Letter_report = pd.DataFrame(data=flipped_values,
                                index=insert_absorb_df.index,
                                columns=cols)

    # Change '1' to the column Letter and '0' to emptry string
    for column in range(len(list(Letter_report))):
        col_letter = list(Letter_report)[column]
        for row in range(len(Letter_report)):
            if Letter_report.iloc[row, column] == 1:
                Letter_report.iloc[row, column] = col_letter
            else:
                Letter_report.iloc[row, column] = ''
    
    
    return Letter_report

# Define significant groups and how they should be sorted to test algorithm
"""
significants = [('T1', 'T3'), ('T1','T3'), 
                ('T1', 'T4'), ('T1','T5'), 
                ('T2','T4'), ('T2', 'T5'), 
                ('T3','T5')]
sorted_groups = ['T1','T2','T3', 'T4', 'T5']
compact_letter_report(significants, sorted_groups)
"""