import pandas as pd



# Calculate SIAS scores
def SIAS_calculate_scores(df):
    """
    Calculate the SIAS total score by summing item scores.
    """
    df['SIAS_Total_Score'] = df[['SIAS_01', 'SIAS_02', 'SIAS_03', 'SIAS_04', 'SIAS_05', 'SIAS_06', 'SIAS_07', 'SIAS_08', 'SIAS_09', 'SIAS_10',
                                 'SIAS_11', 'SIAS_12', 'SIAS_13', 'SIAS_14', 'SIAS_15', 'SIAS_16', 'SIAS_17', 'SIAS_18', 'SIAS_19', 'SIAS_20']].sum(axis=1)
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
        return df
    return None

if __name__ == "__main__":
    main()
