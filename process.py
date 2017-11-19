import sys
import pandas as pd
import numpy as np

def make_rows(df, col):
    types = df[col].unique()
    for t in types:
        df[t] = df[col] == t

    del df[col]
    

def add_features(df):
    make_rows(df, 'property_type')
    make_rows(df, 'state_name')
#   make_rows(df, 'place_name')  


def reduce_cols(df):
    
    for col in df.columns[6:]:
        vc = df[col].value_counts()
        if True not in vc:
            continue
            
        if vc[True] < df.shape[0]/100:
            del df[col]


def delete_columns(df):

     del df['id']
     del df['operation']
     del df['country_name']
     del df['lat-lon']
     del df['created_on']
     del df['place_with_parent_names']
     del df['expenses']
     del df['description']
     del df['floor']

def run():
    df = pd.read_csv('data_gba_total.csv')
    delete_columns(df)
    add_features(df)


    properati = pd.read_csv('properati_dataset_testing_noprice.csv')
    properati.set_index('id')
    delete_columns(properati)
    add_features(properati)


    top_20 = properati['place_name'].value_counts()

    for i in top_20.index:
        df[i] = i == df['place_name']
        properati[i] = i == properati['place_name']

    del properati['place_name']
    del df['place_name']
    
    df.to_csv('data_gba_total_features.csv')    
    properati.to_csv('properati_features.csv')

if __name__ == '__main__':
    run()

