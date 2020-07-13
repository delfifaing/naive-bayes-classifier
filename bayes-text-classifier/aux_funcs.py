def train_test_df(data, train_size):
    ''' Divide into training set and testing set.
    data: is a pandas dataframe.
    train_size: the proportion of the dataset to include in the train_set. Between 0-1.
    The test_size will be 1-train_size.
    '''
    train_data = data.sample(frac = train_size, replace = False)
    test_data  = data.drop(train_data.index).reset_index(drop = True)

    train_data = train_data.reset_index(drop = True)
    return train_data,  test_data