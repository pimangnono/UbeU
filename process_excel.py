import pandas as pd
import json

file_path = 'src/data/jobsandskills-skillsfuture-skills-framework-dataset.xlsx'

def clean_id(text):
    if not isinstance(text, str):
        return str(text)
    return text.lower().replace(' ', '-').replace('/', '-').replace('&', 'and').replace('---', '-').replace('--', '-')

try:
    xls = pd.ExcelFile(file_path)
    
    # Read Data
    df_roles = pd.read_excel(xls, 'Job Role_TCS_CCS')
    df_keys = pd.read_excel(xls, 'TSC_CCS_Key')
    
    # Clean column names
    df_roles.columns = df_roles.columns.str.strip()
    df_keys.columns = df_keys.columns.str.strip()
    
    print("Roles Columns:", df_roles.columns.tolist())
    print("Keys Columns:", df_keys.columns.tolist())
    
    # Create Description Map: TSC Code -> Description
    desc_map = dict(zip(df_keys['TSC Code'], df_keys['TSC_CCS Description']))
    
    # Filter for Critical Core Skills if needed. 
    # The user asked for "Critical Core Skills" from TSC_CCS Title.
    # Usually CCS are distinct from TSC. Let's check types.
    # For now, I will include ALL skills listed for the role, but I'll prioritize CCS if I can distinguish them.
    # Actually, the user said "Critical Core Skills from TSC_CCS Title". 
    # I will assume they want ALL items listed in that tab for the role.
    # But typically "Critical Core Skills" are a specific subset. 
    # Let's check if there is a 'ccs' type.
    # If 'TSC_CCS Type' has 'ccs', I might filter or group them. 
    # For this request, "make each of the Critical Core Skills a selection box", implies a list.
    # I will filter for Type == 'ccs' if it exists, otherwise I'll take all.
    
    # Check for 'ccs' type (case insensitive)
    # Check for 'ccs' type (case insensitive)
    # User reported missing elements. I will include ALL types (tsc and ccs).
    # if 'TSC_CCS Type' in df_roles.columns:
    #     has_ccs = 'ccs' in df_roles['TSC_CCS Type'].astype(str).str.lower().unique()
    #     if has_ccs:
    #          df_roles = df_roles[df_roles['TSC_CCS Type'].astype(str).str.lower() == 'ccs']
    
    # Sort by Proficiency Level
    # Assuming Proficiency Level is numeric or sortable string
    if 'Proficiency Level' in df_roles.columns:
        df_roles['Proficiency Level'] = pd.to_numeric(df_roles['Proficiency Level'], errors='coerce').fillna(0)
        df_roles = df_roles.sort_values(by=['Sector', 'Track', 'Job Role', 'Proficiency Level'])
    
    sectors_data = []
    
    for sector_name, sector_group in df_roles.groupby('Sector'):
        sector_obj = {
            'id': clean_id(sector_name),
            'label': sector_name,
            'tracks': []
        }
        
        for track_name, track_group in sector_group.groupby('Track'):
            track_obj = {
                'id': clean_id(track_name),
                'label': track_name,
                'roles': []
            }
            
            for role_name, role_group in track_group.groupby('Job Role'):
                skills = []
                for _, row in role_group.iterrows():
                    # Use TSC_CCS Code for roles dataframe
                    code = row['TSC_CCS Code']
                    title = row['TSC_CCS Title']
                    level = row['Proficiency Level']
                    # Use code to lookup description from desc_map (which uses TSC Code keys)
                    desc = desc_map.get(code, "No description available.")
                    
                    skills.append({
                        'id': code,
                        'label': title,
                        'description': desc,
                        'proficiencyLevel': level
                    })
                
                role_obj = {
                    'id': clean_id(role_name),
                    'label': role_name,
                    'skills': skills
                }
                track_obj['roles'].append(role_obj)
            
            sector_obj['tracks'].append(track_obj)
        
        sectors_data.append(sector_obj)

    # Output to TypeScript file
    output_file = 'src/data/sectorsData.ts'
    with open(output_file, 'w') as f:
        f.write("export const sectors = ")
        json.dump(sectors_data, f, indent=4)
        f.write(";\n")
    
    print(f"Successfully wrote data to {output_file}")

except Exception as e:
    print(f"Error: {e}")
