from list_compare import create_table
import pytest
import pandas as pd

def test_create_table():
    BomData = {
    "partno":['ABC','XYZ','UK','ABC','UK','XYZ','DEF'],
    "quantity":[2,1,1,1,1,2,2]
    }

    DistiData = {
        "partno":['XYZ','GEF','ABC','UK'],
        "quantity":[2,2,4,2]
    }
    combinedf = create_table(BomData,DistiData)

    bomtest_data = {
    "partno":['ABC','XYZ','UK','ABC','UK','XYZ','DEF','',''],
    "quantity":[2.0,1.0,1.0,1.0,1.0,2.0,2.0,'','']
    }

    distitest_data = {
        "partno":['ABC','XYZ','UK','ABC','UK','XYZ','','GEF','ABC'],
        "quantity":[2.0,1.0,1.0,1.0,1.0,1.0,'',2,1]
    }
    
    bomdf = pd.DataFrame(bomtest_data)
    Distidf = pd.DataFrame(distitest_data)
    test_combinedf = pd.concat([bomdf, Distidf],axis=1, keys = ['BomData', 'Distidf'])
    assert combinedf.equals(test_combinedf)==True  