import pandas as pd



# Calculate SIAS scores
def SIAS_calculate_scores(df):
    """
    Calculate the SIAS total score by summing item scores.
    """
    df['SIAS_Total_Score'] = df[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10',
                                 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20']].sum(axis=1)
    return df

# Summarize results
def SIAS_summarize_results(df):
    mean_scores = df[['SIAS_Total_Score']].mean()
    std_scores = df[['SIAS_Total_Score']].std()

    print("\nSummary of SIAS Scores:")
    print(df[['SIAS_Total_Score']])
    
    return {
        'Mean SIAS Score': mean_scores['SIAS_Total_Score'],
        'Std Dev SIAS Score': std_scores['SIAS_Total_Score']
    }

# Save the results to CSV
def SIAS_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function
def main(df):

    output_file_path = 'processed_sias_results.csv'
    
    
    if df is not None:
        # Calculate SIAS total score
        df = SIAS_calculate_scores(df)

        # Summarize results
        summary = SIAS_summarize_results(df)

        # Save individual scores to CSV
        SIAS_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
