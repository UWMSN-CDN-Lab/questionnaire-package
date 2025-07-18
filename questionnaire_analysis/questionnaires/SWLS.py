import pandas as pd



# Calculate SWLS total score
def SWLS_calculate_score(df):
    """
    Calculate the total score for the SWLS.
    SWLS total score is the sum of the ratings for all 5 items.
    """
    swls_items = ['SWLS_01', 'SWLS_02', 'SWLS_03', 'SWLS_04', 'SWLS_05']
    df['SWLS_Total_Score'] = df[swls_items].sum(axis=1)
    return df

# Summarize results
def SWLS_summarize_results(df):
    """
    Summarize the SWLS total score by calculating the mean and standard deviation.
    """
    mean_score = df['SWLS_Total_Score'].mean()
    std_score = df['SWLS_Total_Score'].std()

    print("\nSummary of SWLS Scores:")
    print(df[['SWLS_Total_Score']])

    print(f"\nMean SWLS Total Score: {mean_score:.2f}")
    print(f"Standard Deviation of SWLS Total Score: {std_score:.2f}")
    
    return {
        'Mean SWLS Total Score': mean_score,
        'Standard Deviation SWLS Total Score': std_score
    }

# Save the results to CSV
def SWLS_save_results_to_csv(df, output_file_path):
    """
    Save the processed SWLS results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_swls_results.csv'
    if df is not None:
        # Calculate SWLS total score
        df = SWLS_calculate_score(df)

        # Summarize results
        summary = SWLS_summarize_results(df)

        # Save results to CSV
        # SWLS_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'SWLS_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None
    

if __name__ == "__main__":
    main()
