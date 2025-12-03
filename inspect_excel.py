import pandas as pd

file_path = 'src/data/jobsandskills-skillsfuture-skills-framework-dataset.xlsx'

try:
    # Read the Excel file
    xls = pd.ExcelFile(file_path)
    print("Sheet names:", xls.sheet_names)

    # Inspect 'Job Role_TCS_CCS'
    if 'Job Role_TCS_CCS' in xls.sheet_names:
        df_roles = pd.read_excel(xls, 'Job Role_TCS_CCS', nrows=5)
        print("\n--- Job Role_TCS_CCS Headers ---")
        print(df_roles.columns.tolist())
        print("\n--- Job Role_TCS_CCS Sample Data ---")
        print(df_roles.head(2).to_string())

    # Inspect 'TSC_CCS_Key'
    if 'TSC_CCS_Key' in xls.sheet_names:
        df_keys = pd.read_excel(xls, 'TSC_CCS_Key', nrows=5)
        print("\n--- TSC_CCS_Key Headers ---")
        print(df_keys.columns.tolist())
        print("\n--- TSC_CCS_Key Sample Data ---")
        print(df_keys.head(2).to_string())

except Exception as e:
    print(f"Error reading excel file: {e}")
