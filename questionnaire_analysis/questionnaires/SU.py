import pandas as pd

# SU NOT SETUP FOR OUR SU QUESTIONS!

# Calculate Substance Use scores
def SU_calculate_scores(df):
    """
    Calculate the scores for the Substance Use questionnaire.
    Subscales could include:
    - Frequency of Use
    - Substance Type (e.g., alcohol, tobacco, drugs)
    - Consequences of Use
    Reverse scoring is applied where necessary.
    """
    
    # Example: Reverse scoring (modify as needed)
    reverse_substance_use_items = ['SU_05', 'SU_10']  # Example reverse items for substance use
    
    # Apply reverse scoring for relevant items
    for item in reverse_substance_use_items:
        df[item] = pd.to_numeric(df[item], errors='coerce')
        df[item] = 6 - df[item]  # Assuming a 1-5 scale, reverse scoring is 6 - original response

    # Calculate subscale scores
    numeric_columns = ['SU_01', 'SU_02', 'SU_03', 'SU_04', 'SU_05', 'SU_06',
                   'SU_07', 'SU_08', 'SU_09', 'SU_10']

    # Convert columns to numeric FIRST
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # NOW calculate subscale scores
    su_scores = {
        'SU_Frequency_Use': df[['SU_01', 'SU_02', 'SU_03']].mean(axis=1),
        'SU_Substance_Type_Use': df[['SU_04', 'SU_05', 'SU_06']].mean(axis=1),
        'SU_Consequences_Use': df[['SU_07', 'SU_08', 'SU_09', 'SU_10']].mean(axis=1)
    }
    df = df.assign(**su_scores)
    
    # Calculate total SU score
    df['SU_Total_Score'] = df[['SU_Frequency_Use', 'SU_Substance_Type_Use', 'SU_Consequences_Use']].mean(axis=1)

    return df

# Summarize results
def SU_summarize_results(df):
    """
    Summarize the Substance Use subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['SU_Frequency_Use', 'SU_Substance_Type_Use', 'SU_Consequences_Use']].mean()
    std_scores = df[['SU_Frequency_Use', 'SU_Substance_Type_Use', 'SU_Consequences_Use']].std()

    print("\nSummary of Substance Use Scores:")
    print(df[['SU_Frequency_Use', 'SU_Substance_Type_Use', 'SU_Consequences_Use']])
    
    return {
        'Mean Frequency of Use': mean_scores['SU_Frequency_Use'],
        'Mean Substance Type Use': mean_scores['SU_Substance_Type_Use'],
        'Mean Consequences of Use': mean_scores['SU_Consequences_Use'],
        'Std Dev Frequency of Use': std_scores['SU_Frequency_Use'],
        'Std Dev Substance Type Use': std_scores['SU_Substance_Type_Use'],
        'Std Dev Consequences of Use': std_scores['SU_Consequences_Use']
    }

# Save the results to CSV
def SU_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    if df is not None:
        # Step 1: Score calculations
        df = SU_calculate_scores(df)

        # Step 2: Optional summary logging
        _ = SU_summarize_results(df)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'SU_Frequency_Use',
            'SU_Substance_Type_Use', 
            'SU_Consequences_Use',
            'SU_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
