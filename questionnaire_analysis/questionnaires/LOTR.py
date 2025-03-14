import pandas as pd



# Reverse scoring for specific items
def LOTR_reverse_score(df, items):
    """
    Reverse scores the specified items for the LOT-R.
    Original scale is 0-4, where reverse scoring is calculated as 4 - original response.
    """
    for item in items:
        df[f'LOT_R_{item}'] = 4 - df[f'LOT_R_{item}']
    return df

# Calculate LOT-R total score
def LOTR_calculate_score(df):
    """
    Calculate the total score for the LOT-R based on the scoring rules.
    Sum items 1, 3, 4, 7, 9, and 10 after reverse scoring items 3, 7, and 9.
    Items 2, 5, 6, and 8 are filler items and are not included in the score.
    """
    # Reverse score items 3, 7, and 9
    reverse_items = [3, 7, 9]
    df = LOTR_reverse_score(df, reverse_items)
    
    # Calculate total score by summing specified items
    score_items = ['LOT_R_1', 'LOT_R_3', 'LOT_R_4', 'LOT_R_7', 'LOT_R_9', 'LOT_R_10']
    df['LOT_R_Total_Score'] = df[score_items].sum(axis=1)
    
    return df

# Summarize results
def LOTR_summarize_results(df):
    """
    Summarize the LOT-R total score by calculating the mean and standard deviation.
    """
    mean_score = df['LOT_R_Total_Score'].mean()
    std_score = df['LOT_R_Total_Score'].std()

    print("\nSummary of LOT-R Scores:")
    print(df[['LOT_R_Total_Score']])

    print(f"\nMean LOT-R Total Score: {mean_score:.2f}")
    print(f"Standard Deviation of LOT-R Total Score: {std_score:.2f}")
    
    return {
        'Mean LOT-R Total Score': mean_score,
        'Standard Deviation LOT-R Total Score': std_score
    }

# Save the results to CSV
def LOTR_save_results_to_csv(df, output_file_path):
    """
    Save the processed LOT-R results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_lotr_results.csv'
    

    if df is not None:
        # Calculate LOT-R total score
        df = LOTR_calculate_score(df)

        # Summarize results
        summary = LOTR_summarize_results(df)

        # Save results to CSV
        LOTR_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
