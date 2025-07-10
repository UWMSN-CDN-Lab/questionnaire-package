import pandas as pd

# Reverse scoring for specific ALQ items
def ALQ_reverse_score(df):
    """
    Reverse score certain ALQ items that are negatively worded.
    Items to reverse: ALQ_4 and ALQ_6
    """
    # TODO change to reverse scoring 
    reverse_items = ['ALQ_4', 'ALQ_6']
    for item in reverse_items:
        df[item] = 6 - df[item]  # Reverse scoring: 1 becomes 5, 5 becomes 1, etc.
    return df
# Calculate subscale and total scores for ALQ
def ALQ_calculate_scores(df):
    """
    Calculate subscale and total scores for the Affect Labeling Questionnaire (ALQ).
    
    Conceptualization (Con): Items ALQ_1, ALQ_2, ALQ_3, ALQ_4
    Identification (Iden): Items ALQ_5, ALQ_6, ALQ_7
    Integration (Int): Items ALQ_8, ALQ_9, ALQ_10, ALQ_11
    """
    df = ALQ_reverse_score(df)
    # Calculate subscale scores
    df['ALQ_Conceptualization'] = df[['ALQ_01', 'ALQ_02', 'ALQ_03', 'ALQ_04']].mean(axis=1)
    df['ALQ_Identification'] = df[['ALQ_05', 'ALQ_06', 'ALQ_07']].mean(axis=1)
    df['ALQ_Integration'] = df[['ALQ_08', 'ALQ_09', 'ALQ_10', 'ALQ_11']].mean(axis=1)
    
    # Calculate total ALQ score
    df['ALQ_Total_Score'] = df[['ALQ_Conceptualization', 'ALQ_Identification', 'ALQ_Integration']].mean(axis=1)
    return df

# Summarize ALQ results
def ALQ_summarize_results(df):
    """
    Summarize the ALQ scores by calculating the mean and standard deviation for each subscale and the total score.
    """
    mean_scores = df[['ALQ_Conceptualization', 'ALQ_Identification', 'ALQ_Integration', 'ALQ_Total_Score']].mean()
    std_scores = df[['ALQ_Conceptualization', 'ALQ_Identification', 'ALQ_Integration', 'ALQ_Total_Score']].std()

    print("\nSummary of ALQ Scores:")
    print(df[['ALQ_Conceptualization', 'ALQ_Identification', 'ALQ_Integration', 'ALQ_Total_Score']])

    print(f"\nMean Conceptualization Score: {mean_scores['ALQ_Conceptualization']:.2f}")
    print(f"Mean Identification Score: {mean_scores['ALQ_Identification']:.2f}")
    print(f"Mean Integration Score: {mean_scores['ALQ_Integration']:.2f}")
    print(f"Mean Total ALQ Score: {mean_scores['ALQ_Total_Score']:.2f}")
    
    return {
        'Mean Conceptualization Score': mean_scores['ALQ_Conceptualization'],
        'Mean Identification Score': mean_scores['ALQ_Identification'],
        'Mean Integration Score': mean_scores['ALQ_Integration'],
        'Mean Total ALQ Score': mean_scores['ALQ_Total_Score'],
        'Std Dev Conceptualization': std_scores['ALQ_Conceptualization'],
        'Std Dev Identification': std_scores['ALQ_Identification'],
        'Std Dev Integration': std_scores['ALQ_Integration'],
        'Std Dev Total ALQ Score': std_scores['ALQ_Total_Score']
    }

# Calculate subgroup mean scores
def ALQ_subgroup_means(df, subgroup_column):
    """
    Calculate subgroup means and standard deviations for the ALQ.
    The subgroup is defined by the 'subgroup_column'.
    """
    subgroup_stats = df.groupby(subgroup_column)[['Conceptualization', 'Identification', 'Integration', 'Total_ALQ_Score']].agg(['mean', 'std'])
    
    print(f"\nSubgroup Means and Standard Deviations for {subgroup_column}:")
    print(subgroup_stats)

    return subgroup_stats

# Save the results to CSV
def ALQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Save the summarized statistics to CSV
def ALQ_save_summary_to_csv(summary, subgroup_summary, output_file_path):
    """
    Save the summarized results to a separate CSV file.
    """
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df = pd.concat([summary_df, subgroup_summary])

    summary_df.to_csv(output_file_path, index=False)
    print(f"Summary saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    if df is not None:
        # Step 1: Score calculations
        df = ALQ_calculate_scores(df)

        # Step 2: Subgroup stats and full summary (print only, optional)
        summary = ALQ_summarize_results(df)
        subgroup_column = 'Gender'
        subgroup_summary = ALQ_subgroup_means(df, subgroup_column)

        # Only return the summary columns for concatenation
        summary_columns = [
            'ALQ_Conceptualization',
            'ALQ_Identification',
            'ALQ_Integration',
            'ALQ_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
