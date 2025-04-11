import pandas as pd
# TODO ASK 
# EDIT TO BE SETUP BASED ON THE QUALTRICS SURVEY!
# Category : Risky_Sexual_Activity: 02,03,04,05,06,09,10, 11, 12, 13, 14, 15, 16, 17
# Risky_Drugs : 19, 20, 21, 22, 23, 24
# Risky_alcohol: 25,26,27,28,29,30,31,32
# Safe_Sexual_Activity: 01,07
# 08 is not placed
# Access CSV file for CARE

# Just mean for now and we look at care later
def CARE_calculate_scores(df):
    """
    Calculate subscale scores for the CARE questionnaire based on categorized items from the Qualtrics survey.
    """

    # Convert all relevant columns to numeric
    item_nums = list(range(1, 33))  # CARE_01 to CARE_32
    for i in item_nums:
        col = f'CARE_{i:02d}'
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Define item categories
    risky_sexual_items = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    risky_drug_items = [19, 20, 21, 22, 23, 24]
    risky_alcohol_items = [25, 26, 27, 28, 29, 30, 31, 32]
    safe_sexual_items = [1, 7]

    # Compute subscale means
    df['CARE_Risky_Sexual_Activity'] = df[[f'CARE_{i:02d}' for i in risky_sexual_items]].mean(axis=1)
    df['CARE_Risky_Drugs'] = df[[f'CARE_{i:02d}' for i in risky_drug_items]].mean(axis=1)
    df['CARE_Risky_Alcohol'] = df[[f'CARE_{i:02d}' for i in risky_alcohol_items]].mean(axis=1)
    df['CARE_Safe_Sexual_Activity'] = df[[f'CARE_{i:02d}' for i in safe_sexual_items]].mean(axis=1)

    # Optionally: total CARE score as mean of all categories (excluding item 08)
    df['CARE_Total_Score'] = df[[
        'CARE_Risky_Sexual_Activity',
        'CARE_Risky_Drugs',
        'CARE_Risky_Alcohol',
        'CARE_Safe_Sexual_Activity'
    ]].mean(axis=1)

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

    means = df[subscales].mean()
    stds = df[subscales].std()

    print("\n📊 CARE Subscale Summary:")
    for sub in subscales:
        print(f"{sub}: Mean = {means[sub]:.2f}, Std = {stds[sub]:.2f}")

    return {f"Mean {sub}": means[sub] for sub in subscales}
def main(df):
    if df is not None:
        df = CARE_calculate_scores(df)
        _ = CARE_summarize_results(df)

        # Build summary output for pipeline
        summary_df = df[[
            'ResponseId',
            'CARE_Risky_Sexual_Activity',
            'CARE_Risky_Drugs',
            'CARE_Risky_Alcohol',
            'CARE_Safe_Sexual_Activity',
            'CARE_Total_Score'
        ]].copy()
        summary_df['Questionnaire'] = 'CARE'

        return df
    return None

