
import pandas as pd
from aux_funcs import train_test_df

def main():
# Load data
    data = pd.read_csv("newspaper_titles.tsv", sep="\t")

# Divide into train and test sets
    train, test = train_test_df(data,0.5)
    print(train.head())

if __name__ == "__main__":
    main()
