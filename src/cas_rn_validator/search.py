import os
import pandas as pd
import cas_rn_validator.validator as v


'''
Function to search ChemicalFormula With CAS NUMBER
'''
def getChemicalFormulaWithCAS(input_str):
    # validating cas registry number
    if v.validateCAS_RN(input_str) == True:
        # reading csv and getting data
        dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
        df = pd.read_csv(dataset_path)

        df = df[df['CAS_Number'] == input_str]
        return df['Chemicalformula'].tolist()[0]

    else:
        return None


'''
Function to search Synonyms With CAS NUMBER
'''
def getSynonymsWithCAS(input_str):
    # validating cas registry number
    if v.validateCAS_RN(input_str) == True:
        # reading csv and getting data
        dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
        df = pd.read_csv(dataset_path)

        df = df[df['CAS_Number'] == input_str]
        return df['Synonyms'].tolist()[0]

    else:
        return None      


'''
Function to search CASNumber With Synonyms
'''
def getCASNumberWithSynonyms(input_str):
    # reading csv and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)
    # Convert input string to lowercase for case insensitivity
    input_str_lower = input_str.lower()
    # Convert 'Synonyms' column to lowercase for case insensitivity
    df['Synonyms'] = df['Synonyms'].str.lower()
    df_filtered = df[df['Synonyms'] == input_str_lower]
    if not df_filtered.empty:
        return df_filtered['CAS_Number'].iloc[0]
    else:
        return None


'''
Function to search ChemicalFormula With Synonyms
'''
def getChemicalFormulaWithSynonyms(input_str):
    # reading csv and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)
    # Convert input string to lowercase for case insensitivity
    input_str_lower = input_str.lower()
    # Convert 'Synonyms' column to lowercase for case insensitivity
    df['Synonyms'] = df['Synonyms'].str.lower()
    df_filtered = df[df['Synonyms'] == input_str_lower]
    if not df_filtered.empty:
        return df_filtered['Chemicalformula'].iloc[0]
    else:
        return None




'''
Function to search CASNumber With ChemicalFormula
'''
def getCASNumberWithChemicalFormula(input_str):
    # reading csv and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)
    # Convert input string to lowercase for case insensitivity
    input_str_lower = input_str.lower()
    # Convert 'Synonyms' column to lowercase for case insensitivity
    df['Chemicalformula'] = df['Chemicalformula'].str.lower()
    df_filtered = df[df['Chemicalformula'] == input_str_lower]
    if not df_filtered.empty:
        return df_filtered['CAS_Number'].iloc[0]
    else:
        return None


'''
Function to search Synonyms With ChemicalFormula
'''
def getSynonymsWithChemicalFormula(input_str):
    # reading csv and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)
    # Convert input string to lowercase for case insensitivity
    input_str_lower = input_str.lower()
    # Convert 'Synonyms' column to lowercase for case insensitivity
    df['Chemicalformula'] = df['Chemicalformula'].str.lower()
    df_filtered = df[df['Chemicalformula'] == input_str_lower]
    if not df_filtered.empty:
        return df_filtered['Synonyms'].iloc[0]
    else:
        return None


'''
Function to search Chemicalformula by CAS Number
'''
def searchChemicalFormulaWithCAS(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert CAS numbers to lowercase for case-insensitive comparison
    df['CAS_Number'] = df['CAS_Number'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['CAS_Number'].str.contains(input_str_lower, regex=False, case=False)]['Chemicalformula'].values.tolist()
    dfstartsWithList = df[df['CAS_Number'].str.startswith(input_str_lower)]['Chemicalformula'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None

'''
Function to search Synonyms by CAS Number
'''
def searchSynonymsWithCAS(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert CAS numbers to lowercase for case-insensitive comparison
    df['CAS_Number'] = df['CAS_Number'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['CAS_Number'].str.contains(input_str_lower, regex=False, case=False)]['Synonyms'].values.tolist()
    dfstartsWithList = df[df['CAS_Number'].str.startswith(input_str_lower)]['Synonyms'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None






'''
Function to search CAS Number by Synonyms
'''
def searchCASNumberWithSynonyms(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert synonyms to lowercase for case-insensitive comparison
    df['Synonyms'] = df['Synonyms'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['Synonyms'].str.contains(input_str_lower, regex=False, case=False)]['CAS_Number'].values.tolist()
    dfstartsWithList = df[df['Synonyms'].str.startswith(input_str_lower)]['CAS_Number'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None


'''
Function to search ChemicalFormula by Synonyms
'''
def searchChemicalFormulaWithSynonyms(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert synonyms to lowercase for case-insensitive comparison
    df['Synonyms'] = df['Synonyms'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['Synonyms'].str.contains(input_str_lower, regex=False, case=False)]['Chemicalformula'].values.tolist()
    dfstartsWithList = df[df['Synonyms'].str.startswith(input_str_lower)]['Chemicalformula'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None


'''
Function to search CASNumber by ChemicalFormula 
'''
def searchCASNumberWithChemicalFormula(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert chemical formulas to lowercase for case-insensitive comparison
    df['Chemicalformula'] = df['Chemicalformula'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['Chemicalformula'].str.contains(input_str_lower, regex=False, case=False)]['CAS_Number'].values.tolist()
    dfstartsWithList = df[df['Chemicalformula'].str.startswith(input_str_lower)]['CAS_Number'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None


'''
Function to search Synonyms by ChemicalFormula
'''
def searchSynonymsWithChemicalFormula(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert chemical formulas to lowercase for case-insensitive comparison
    df['Chemicalformula'] = df['Chemicalformula'].str.lower()

    # Perform case-insensitive search
    dfContainsWithList = df[df['Chemicalformula'].str.contains(input_str_lower, regex=False, case=False)]['Synonyms'].values.tolist()
    dfstartsWithList = df[df['Chemicalformula'].str.startswith(input_str_lower)]['Synonyms'].values.tolist()

    if len(dfContainsWithList) > 0 and len(dfstartsWithList) > 0:
        dfstartsWithList.extend(list(set(dfContainsWithList) - set(dfstartsWithList)))
        return dfstartsWithList
    elif len(dfContainsWithList) > 0 and len(dfstartsWithList) == 0:
        return dfContainsWithList
    else:
        return None

'''
Function to search by CAS NUMBER
'''
def searchByCasNumber(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert CAS numbers to lowercase for case-insensitive comparison
    df['CAS_Number'] = df['CAS_Number'].str.lower()

    # Perform case-insensitive search
    df = df[df['CAS_Number'].str.contains(input_str_lower, regex=False)]

    if len(df) > 0:
        return df.values.tolist()
    else:
        return None


'''
Function to search by Synonyms
'''
def searchBySynonyms(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert synonyms to lowercase for case-insensitive comparison
    df['Synonyms'] = df['Synonyms'].str.lower()

    # Perform case-insensitive search
    df = df[df['Synonyms'].str.contains(input_str_lower, regex=False)]

    if len(df) > 0:
        return df.values.tolist()
    else:
        return None


'''
Function to search by Chemicalformula
'''
def searchByChemicalformula(input_str):
    # Reading CSV and getting data
    dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'cas_rn_dataset.csv')
    df = pd.read_csv(dataset_path)

    # Convert input string to lowercase for case-insensitive search
    input_str_lower = input_str.lower()

    # Convert synonyms to lowercase for case-insensitive comparison
    df['Chemicalformula'] = df['Chemicalformula'].str.lower()

    # Perform case-insensitive search
    df = df[df['Chemicalformula'].str.contains(input_str_lower, regex=False)]

    if len(df) > 0:
        return df.values.tolist()
    else:
        return None




