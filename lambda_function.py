import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [27,25], 'col2': [23,24]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
