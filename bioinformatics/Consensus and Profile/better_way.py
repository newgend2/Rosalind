import pandas as pd
import numpy as np


def consensus(input_file):
    df = pd.DataFrame(open(input_file)).transpose()
    DNA = df[1].str.extractall('(.)').unstack().droplevel(0, axis=1)
    profile_df = DNA.apply(pd.Series.value_counts).fillna(value=0).astype(int)
    consensus = profile_df.idxmax().to_list()

    profile_df.index = profile_df.index + ':'
    profile = profile_df.reset_index().to_string(index=False, header=False).replace('  ', ' ')
    profile = profile.lstrip()
    profile = profile.replace('\n ', '\n')
    consensus = ''.join(consensus)
    print('{}\n{}'.format(consensus, profile))


consensus('../fasta_test.txt')
