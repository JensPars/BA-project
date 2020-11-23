def get_data(df,drop = [],split = False, dummies = []):
  '''
  Input:
  pandas.DataFrame 
  list of keys to be dropped
  boolean determining wether to split
  the keys of categorical features for onehot encoding
  Output:
  if split == True
    data cleaned and split into test and train
  if split == False
    the whole dataframe cleaned
  '''
  df = df.drop(drop,axis=1)
  if split == True:
    ## get dummies
    if dummies != []:
      df = pd.get_dummies(df,columns=dummies)
    ## else remove categorical features
    else:
      df = df.drop(['Continent'],axis=1)
    y = df['CO2 Emissions per Capita (metric tonnes)']
    X = df.drop(['CO2 Emissions per Capita (metric tonnes)'],axis=1)
    split = int(len(df)*0.75)
    X_train = X[:split]
    y_train = y[:split]
    X_test = X[split:]
    y_test = y[split:]
    return X_train,y_train,X_test,y_test
  else:
    return df
