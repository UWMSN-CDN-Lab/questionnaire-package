import pandas as pd


# Calculate the SD4 subscale scores
def SD4_calculate_scores(df):
    """
    Calculate the subscale scores for the Four Identities Questionnaire (SD4).
    Machiavellianism: mean of items 1-7
    Narcissism: mean of items 8-14
    Psychopathy: mean of items 15-21
    Sadism: mean of items 22-28
    """
    df['SD4_Machiavellianism'] = df[['SD4_1', 'SD4_2', 'SD4_3', 'SD4_4', 'SD4_5', 'SD4_6', 'SD4_7']].mean(axis=1)
    df['SD4_Narcissism'] = df[['SD4_8', 'SD4_9', 'SD4_10', 'SD4_11', 'SD4_12', 'SD4_13', 'SD4_14']].mean(axis=1)
    df['SD4_Psychopathy'] = df[['SD4_15', 'SD4_16', 'SD4_17', 'SD4_18', 'SD4_19', 'SD4_20', 'SD4_21']].mean(axis=1)
    df['SD4_Sadism'] = df[['SD4_22', 'SD4_23', 'SD4_24', 'SD4_25', 'SD4_26', 'SD4_27', 'SD4_28']].mean(axis=1)
    
    # Optional: Calculate total mean score for overall "dark personality"
    df['SD4_Total_Score'] = df[['SD4_Machiavellianism', 'SD4_Narcissism', 'SD4_Psychopathy', 'SD4_Sadism']].mean(axis=1)
    
    return df

# Summarize results
def SD4_summarize_results(df):
    """
    Summarize the SD4 scores by calculating the mean and standard deviation for each subscale and the total score.
    """
    mean_scores = df[['SD4_Machiavellianism', 'SD4_Narcissism', 'SD4_Psychopathy', 'SD4_Sadism', 'SD4_Total_Score']].mean()
    std_scores = df[['SD4_Machiavellianism', 'SD4_Narcissism', 'SD4_Psychopathy', 'SD4_Sadism', 'SD4_Total_Score']].std()

    print("\nSummary of SD4 Scores:")
    print(df[['SD4_Machiavellianism', 'SD4_Narcissism', 'SD4_Psychopathy', 'SD4_Sadism', 'SD4_Total_Score']])

    print(f"\nMean Machiavellianism: {mean_scores['SD4_Machiavellianism']:.2f}")
    print(f"Mean Narcissism: {mean_scores['SD4_Narcissism']:.2f}")
    print(f"Mean Psychopathy: {mean_scores['SD4_Psychopathy']:.2f}")
    print(f"Mean Sadism: {mean_scores['SD4_Sadism']:.2f}")
    print(f"Mean Total SD4 Score: {mean_scores['SD4_Total_Score']:.2f}")
    
    return {
        'Mean Machiavellianism': mean_scores['SD4_Machiavellianism'],
        'Mean Narcissism': mean_scores['SD4_Narcissism'],
        'Mean Psychopathy': mean_scores['SD4_Psychopathy'],
        'Mean Sadism': mean_scores['SD4_Sadism'],
        'Mean Total SD4 Score': mean_scores['SD4_Total_Score'],
        'Std Dev Machiavellianism': std_scores['SD4_Machiavellianism'],
        'Std Dev Narcissism': std_scores['SD4_Narcissism'],
        'Std Dev Psychopathy': std_scores['SD4_Psychopathy'],
        'Std Dev Sadism': std_scores['SD4_Sadism'],
        'Std Dev Total SD4 Score': std_scores['SD4_Total_Score']
    }

# Calculate subgroup mean scores
def SD4_subgroup_means(df, subgroup_column):
    """
    Calculate subgroup means and standard deviations for the SD4 subscales.
    The subgroup is defined by the 'subgroup_column'.
    """
    subgroup_stats = df.groupby(subgroup_column)[['SD4_Machiavellianism', 'SD4_Narcissism', 'SD4_Psychopathy', 'SD4_Sadism', 'SD4_Total_Score']].agg(['mean', 'std'])
    
    print(f"\nSubgroup Means and Standard Deviations for {subgroup_column}:")
    print(subgroup_stats)

    return subgroup_stats

# Save the results to CSV
def SD4_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Save the summarized statistics to CSV
def SD4_save_summary_to_csv(summary, subgroup_summary, output_file_path):
    """
    Save the summarized results to a separate CSV file.
    """
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df = pd.concat([summary_df, subgroup_summary])

    summary_df.to_csv(output_file_path, index=False)
    print(f"Summary saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_sd4_results.csv'
    summary_output_file_path = 'sd4_summary_results.csv'


    if df is not None:
        # Calculate SD4 subscale scores
        df = SD4_calculate_scores(df)

        # Summarize results
        summary = SD4_summarize_results(df)

        # Calculate subgroup means and std for a specific subgroup, e.g., 'Gender' or 'Age'
        subgroup_column = 'Gender'  # Adjust this to your dataset's specific column
        subgroup_summary = SD4_subgroup_means(df, subgroup_column)

        # Save individual scores to CSV
        SD4_save_results_to_csv(df, output_file_path)

        # Save summarized results to CSV
        SD4_save_summary_to_csv(summary, subgroup_summary, summary_output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'SD4_Machiavellianism',
            'SD4_Narcissism',
            'SD4_Psychopathy',
            'SD4_Sadism',
            'SD4_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
