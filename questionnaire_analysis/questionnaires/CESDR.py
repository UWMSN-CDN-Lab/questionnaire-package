import pandas as pd



# Calculate CESD-R scores
def CESDR_calculate_scores(df):
    """
    Calculate the total CESD-R score by summing all item responses.
    Assumes items are named CESDR_01 to CESDR_20.
    """
    cesdr_items = [f'CESDR_{i:02d}' for i in range(1, 21)]  # Adjust if you have a different item range

    for item in cesdr_items:
        df[item] = pd.to_numeric(df[item], errors='coerce')

    df['CESDR_Total_Score'] = df[cesdr_items].sum(axis=1)
    return df

# Summarize results
def CESDR_summarize_results(df):
    """
    Summarize the CESD-R scores by calculating the mean and standard deviation for the total score.
    """
    mean_total_score = df['CESDR_Total_Score'].mean()
    std_total_score = df['CESDR_Total_Score'].std()

    print("\nSummary of CESD-R Scores:")
    print(df[['CESDR_Total_Score']])

    print(f"\nMean Total CESD-R Score: {mean_total_score:.2f}")
    print(f"Standard Deviation of CESD-R Scores: {std_total_score:.2f}")

    return {
        'Mean Total CESD-R Score': mean_total_score,
        'Std Dev Total CESD-R Score': std_total_score
    }

# Calculate subgroup mean scores
def CESDR_subgroup_means(df, subgroup_column):
    """
    Calculate subgroup means and standard deviations for the CESD-R total score.
    The subgroup is defined by the 'subgroup_column'.
    """
    subgroup_stats = df.groupby(subgroup_column)['Total_CESDR_Score'].agg(['mean', 'std'])
    
    print(f"\nSubgroup Means and Standard Deviations for {subgroup_column}:")
    print(subgroup_stats)

    return subgroup_stats

# Save the results to CSV
def CESDR_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Save the summarized statistics to CSV
def CESDR_save_summary_to_csv(summary, subgroup_summary, output_file_path):
    """
    Save the summarized results to a separate CSV file.
    """
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df = pd.concat([summary_df, subgroup_summary])

    summary_df.to_csv(output_file_path, index=False)
    print(f"Summary saved to {output_file_path}.")

# Main function to execute the steps
def main(df):

    output_file_path = 'processed_cesdr_results.csv'
    summary_output_file_path = 'cesdr_summary_results.csv'


    if df is not None:
        # Calculate CESD-R scores
        df = CESDR_calculate_scores(df)

        # Summarize results
        summary = CESDR_summarize_results(df)

        # Calculate subgroup means and std for a specific subgroup, e.g., 'Gender' or 'Age'
        subgroup_column = 'Gender'  # Adjust this to your dataset's specific column
        subgroup_summary = CESDR_subgroup_means(df, subgroup_column)

        # Save individual scores to CSV
        CESDR_save_results_to_csv(df, output_file_path)

        # Save summarized results to CSV
        CESDR_save_summary_to_csv(summary, subgroup_summary, summary_output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'CESDR_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
