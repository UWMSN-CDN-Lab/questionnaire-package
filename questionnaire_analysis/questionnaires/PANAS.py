import pandas as pd



# Calculate Positive and Negative Affect Scores
def PANAS_calculate_affect_scores(df):
    """
    Calculate the Positive and Negative Affect scores for the PANAS-SF.
    Positive Affect: Items PANAS_01, PANAS_03, PANAS_05, PANAS_09, PANAS_10, PANAS_12, PANAS_14, PANAS_16, PANAS_17, PANAS_19
    Negative Affect: Items PANAS_02, PANAS_04, PANAS_06, PANAS_07, PANAS_08, PANAS_11, PANAS_13, PANAS_15, PANAS_18, PANAS_20
    """
    positive_items = ['PANAS_01', 'PANAS_03', 'PANAS_05', 'PANAS_09', 'PANAS_10', 'PANAS_12', 'PANAS_14', 'PANAS_16', 'PANAS_17', 'PANAS_19']
    negative_items = ['PANAS_02', 'PANAS_04', 'PANAS_06', 'PANAS_07', 'PANAS_08', 'PANAS_11', 'PANAS_13', 'PANAS_15', 'PANAS_18', 'PANAS_20']
    
    df['PANAS_Positive_Affect_Score'] = df[positive_items].sum(axis=1)
    df['PANAS_Negative_Affect_Score'] = df[negative_items].sum(axis=1)
    
    return df

# Summarize results
def PANAS_summarize_results(df):
    """
    Summarize the PANAS-SF scores by calculating the mean and standard deviation for positive and negative affect scores.
    """
    mean_scores = df[['PANAS_Positive_Affect_Score', 'PANAS_Negative_Affect_Score']].mean()
    std_scores = df[['PANAS_Positive_Affect_Score', 'PANAS_Negative_Affect_Score']].std()

    print("\nSummary of PANAS-SF Scores:")
    print(df[['PANAS_Positive_Affect_Score', 'PANAS_Negative_Affect_Score']])

    print(f"\nMean Positive Affect Score: {mean_scores['PANAS_Positive_Affect_Score']:.2f}")
    print(f"Mean Negative Affect Score: {mean_scores['PANAS_Negative_Affect_Score']:.2f}")

    return {
        'Mean Positive Affect Score': mean_scores['PANAS_Positive_Affect_Score'],
        'Mean Negative Affect Score': mean_scores['PANAS_Negative_Affect_Score'],
        'Std Dev Positive Affect': std_scores['PANAS_Positive_Affect_Score'],
        'Std Dev Negative Affect': std_scores['PANAS_Negative_Affect_Score']
    }

# Save the results to CSV
# try and catch here 
def PANAS_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_panas_sf_results.csv'

    if df is not None:
        # Calculate Positive and Negative Affect Scores
        df = PANAS_calculate_affect_scores(df)

        # Summarize results
        summary = PANAS_summarize_results(df)

        # Save results to CSV
        # PANAS_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'PANAS_Positive_Affect_Score',
            'PANAS_Negative_Affect_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
# pschy273
# unique method names, prefix - abbr of the paper for all functions
