import pandas as pd

# Calculating MSPSS scores
def MSPSS_calculate_scores(df):
    """
    Calculate the subscale scores for MSPSS.
    Subscales include:
    - Family
    - Friends
    - Significant Others
    """
    df['MSPSS_Family_Score'] = df[['MSPSS_03', 'MSPSS_04', 'MSPSS_08', 'MSPSS_11']].mean(axis=1)
    df['MSPSS_Friends_Score'] = df[['MSPSS_06', 'MSPSS_07', 'MSPSS_09', 'MSPSS_12']].mean(axis=1)
    df['MSPSS_Significant_Others_Score'] = df[['MSPSS_01', 'MSPSS_02', 'MSPSS_05', 'MSPSS_10']].mean(axis=1)
    
    # Total MSPSS score
    df['MSPSS_Total_Score'] = df[['MSPSS_Family_Score', 'MSPSS_Friends_Score', 'MSPSS_Significant_Others_Score']].mean(axis=1)
    
    return df

# Summarize results
def MSPSS_summarize_results(df):
    mean_scores = df[['MSPSS_Family_Score', 'MSPSS_Friends_Score', 'MSPSS_Significant_Others_Score', 'MSPSS_Total_Score']].mean()
    std_scores = df[['MSPSS_Family_Score', 'MSPSS_Friends_Score', 'MSPSS_Significant_Others_Score', 'MSPSS_Total_Score']].std()

    print("\nSummary of MSPSS Scores:")
    print(df[['MSPSS_Family_Score', 'MSPSS_Friends_Score', 'MSPSS_Significant_Others_Score', 'MSPSS_Total_Score']])
    
    return {
        'Mean Family Score': mean_scores['MSPSS_Family_Score'],
        'Mean Friends Score': mean_scores['MSPSS_Friends_Score'],
        'Mean Significant Others Score': mean_scores['MSPSS_Significant_Others_Score'],
        'Mean Total MSPSS Score': mean_scores['MSPSS_Total_Score'],
        'Std Dev Family Score': std_scores['MSPSS_Family_Score'],
        'Std Dev Friends Score': std_scores['MSPSS_Friends_Score'],
        'Std Dev Significant Others Score': std_scores['MSPSS_Significant_Others_Score'],
        'Std Dev Total MSPSS Score': std_scores['MSPSS_Total_Score']
    }

# Save the results to CSV
def MSPSS_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main(df):
    output_file_path = 'processed_mspss_results.csv'

    
    if df is not None:
        # Calculate MSPSS scores
        df = MSPSS_calculate_scores(df)

        # Summarize results
        summary = MSPSS_summarize_results(df)

        # Save individual scores to CSV
        MSPSS_save_results_to_csv(df, output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'MSPSS_Family_Score',
            'MSPSS_Friends_Score',
            'MSPSS_Significant_Others_Score',
            'MSPSS_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
