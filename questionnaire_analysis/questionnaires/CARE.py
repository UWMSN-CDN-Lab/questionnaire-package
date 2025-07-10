import pandas as pd

def CARE_calculate_scores(df):
    """
    Calculate subscale scores for the CARE questionnaire based on categorized items from the Qualtrics survey.
    
    Scoring Guidelines:
    - Risky_Sexual_Activity: 02,03,04,05,06,09,10,11,12,13,14,15,16,17
    - Risky_Drugs: 19,20,21,22,23,24
    - Risky_alcohol: 25,26,27,28,29,30,31,32
    - Safe_Sexual_Activity: 01,07
    - 08 is not placed
    """
    
    # Convert all relevant columns to numeric (ignoring errors)
    for col in df.columns:
        if col.startswith('CARE_'):
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Define item categories according to the guidelines
    risky_sexual_items = ['CARE_02', 'CARE_03', 'CARE_04', 'CARE_05', 'CARE_06', 'CARE_09', 
                         'CARE_10', 'CARE_11', 'CARE_12', 'CARE_13', 'CARE_14', 'CARE_15', 
                         'CARE_16', 'CARE_17']
    risky_drug_items = ['CARE_19', 'CARE_20', 'CARE_21', 'CARE_22', 'CARE_23', 'CARE_24']
    risky_alcohol_items = ['CARE_25', 'CARE_26', 'CARE_27', 'CARE_28', 'CARE_29', 'CARE_30', 
                          'CARE_31', 'CARE_32']
    safe_sexual_items = ['CARE_01', 'CARE_07']

    # Create a dictionary of the new columns with their calculations
    new_columns = {
        'CARE_Risky_Sexual_Activity': df[risky_sexual_items].mean(axis=1),
        'CARE_Risky_Drugs': df[risky_drug_items].mean(axis=1),
        'CARE_Risky_Alcohol': df[risky_alcohol_items].mean(axis=1),
        'CARE_Safe_Sexual_Activity': df[safe_sexual_items].mean(axis=1)
    }

    # Concatenate the new columns at once
    df = pd.concat([df, pd.DataFrame(new_columns)], axis=1)

    # Calculate total CARE score as mean of all categories (excluding item 08)
    df['CARE_Total_Score'] = df[['CARE_Risky_Sexual_Activity', 'CARE_Risky_Drugs', 
                                 'CARE_Risky_Alcohol', 'CARE_Safe_Sexual_Activity']].mean(axis=1)

    return df

def CARE_summarize_results(df):
    """
    Summarize CARE scores by calculating mean and standard deviation.
    """
    subscales = [
        'CARE_Risky_Sexual_Activity',
        'CARE_Risky_Drugs',
        'CARE_Risky_Alcohol',
        'CARE_Safe_Sexual_Activity',
        'CARE_Total_Score'
    ]

    mean_scores = df[subscales].mean()
    std_scores = df[subscales].std()

    print("\n📊 CARE Subscale Summary:")
    print(df[subscales])
    
    for sub in subscales:
        print(f"{sub}: Mean = {mean_scores[sub]:.3f}, Std = {std_scores[sub]:.3f}")

    return {f"Mean {sub}": mean_scores[sub] for sub in subscales}

def main(df):
    if df is not None:
        # Step 1: Calculate scores
        df = CARE_calculate_scores(df)

        # Step 2: Optional summary logging
        _ = CARE_summarize_results(df)

        # Only return the summary columns for concatenation
        summary_columns = [
            'CARE_Risky_Sexual_Activity',
            'CARE_Risky_Drugs',
            'CARE_Risky_Alcohol',
            'CARE_Safe_Sexual_Activity',
            'CARE_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

