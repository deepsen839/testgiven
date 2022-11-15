from excel_json import excel_to_json
import json
import pytest
def test_excel_json():

    dictionary = json.dumps({'item': [{'LineNumber': '1.0', 'PartNumber': 'ABC', 'Description': 'Very Good', 'Price': '200.2'}, {'LineNumber': '2.0', 'PartNumber': 'DEF', 'Description': 'Not so good', 'Price': '100.1'}], 'Quote Number': '98765.0', 'Date': '43466.0', 'Ship To': 'USA'})
    excel_to_json1 = json.dumps(excel_to_json("Python_Skill_Test.xlsx"))
    assert dictionary==excel_to_json1