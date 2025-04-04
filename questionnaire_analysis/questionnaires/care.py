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

def CARE_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculating total and subscale scores
def CARE_calculate_scores(df):
    """
    Calculate the subscale scores for the CARE questionnaire.
    Subscales include:
    - Past Frequency
    - Expected Involvement
    - Expected Benefits
    - Expected Risks
    """
    # Example calculation (based on the format in the provided PDF):
    df['CARE_Past_Frequency'] = df[['CARE_01', 'CARE_02', 'CARE_03']].mean(axis=1)  # Summing the frequency
    df['CARE_Expected_Involvement'] = df[['EI_1', 'EI_2', 'EI_3']].mean(axis=1)
    df['CARE_Expected_Benefits'] = df[['EB_1', 'EB_2', 'EB_3']].mean(axis=1)
    df['CARE_Expected_Risks'] = df[['ER_1', 'ER_2', 'ER_3']].mean(axis=1)
    
    df['CARE_Total_Score'] = df[['CARE_Past_Frequency', 'CARE_Expected_Involvement', 'CARE_Expected_Benefits', 'CARE_Expected_Risks']].sum(axis=1)
    
    return df

# Summarize results
def CARE_summarize_results(df):
    """
    Summarize CARE scores by calculating mean and standard deviation.
    """
    mean_scores = df[['CARE_Past_Frequency', 'CARE_Expected_Involvement', 'CARE_Expected_Benefits', 'CARE_Expected_Risks']].mean()
    std_scores = df[['CARE_Past_Frequency', 'CARE_Expected_Involvement', 'CARE_Expected_Benefits', 'CARE_Expected_Risks']].std()

    print("\nSummary of CARE Scores:")
    print(df[['CARE_Past_Frequency', 'CARE_Expected_Involvement', 'CARE_Expected_Benefits', 'CARE_Expected_Risks']])
    
    return {
        'Mean CARE Past Frequency': mean_scores['CARE_Past_Frequency'],
        'Mean CARE Expected Involvement': mean_scores['CARE_Expected_Involvement'],
        'Mean CARE Expected Benefits': mean_scores['CARE_Expected_Benefits'],
        'Mean CARE Expected Risks': mean_scores['CARE_Expected_Risks'],
        'Std Dev CARE Past Frequency': std_scores['CARE_Past_Frequency'],
        'Std Dev CARE Expected Involvement': std_scores['CARE_Expected_Involvement'],
        'Std Dev CARE Expected Benefits': std_scores['CARE_Expected_Benefits'],
        'Std Dev CARE Expected Risks': std_scores['CARE_Expected_Risks']
    }

# Save the results to CSV
def CARE_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main(df):
    #input_file_path = './data/CARE_DATA_SET.csv'
    output_file_path = 'processed_care_results.csv'
    
    # Load CSV
    #df = CARE_access_csv(input_file_path)
    
    if df is not None:
        # Calculate scores
        df = CARE_calculate_scores(df)

        # Summarize results
        summary = CARE_summarize_results(df)

        # Save individual scores to CSV
        CARE_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
