import pandas as pd

# Access CSV file
def UCLA_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Reverse scoring for certain UCLA items
def UCLA_reverse_score(df):
    """
    Reverse score certain UCLA items that are positively worded.
    Items to reverse: 1, 5, 6, 9, 10, 15, 16, 19, 20
    """
    reverse_items = ['UCLA_1', 'UCLA_5', 'UCLA_6', 'UCLA_9', 'UCLA_10', 'UCLA_15', 'UCLA_16', 'UCLA_19', 'UCLA_20']
    for item in reverse_items:
        df[item] = 5 - df[item]  # Reverse score: 1 becomes 4, 4 becomes 1, etc.
    return df

# Calculate UCLA scores
def UCLA_calculate_scores(df):
    """
    Calculate the total UCLA score by summing all item responses.
    Assumes items are named UCLA_01 to UCLA_20.
    """
    ucla_items = [f'UCLA_{i:02d}' for i in range(1, 21)]  # Adjust if you have a different item range

    for item in ucla_items:
        df[item] = pd.to_numeric(df[item], errors='coerce')

    df['UCLA_Total_Score'] = df[ucla_items].sum(axis=1)
    return df

# Summarize results
def UCLA_summarize_results(df):
    """
    Summarize the UCLA scores by calculating the mean and standard deviation for the total score.
    """
    mean_total_score = df['UCLA_Total_Score'].mean()
    std_total_score = df['UCLA_Total_Score'].std()

    print("\nSummary of UCLA Loneliness Scale Scores:")
    print(df[['UCLA_Total_Score']])

    print(f"\nMean Total UCLA Score: {mean_total_score:.2f}")
    print(f"Standard Deviation of UCLA Scores: {std_total_score:.2f}")

    return {
        'Mean Total UCLA Score': mean_total_score,
        'Std Dev Total UCLA Score': std_total_score
    }

# Calculate subgroup mean scores
def UCLA_subgroup_means(df, subgroup_column):
    """
    Calculate subgroup means and standard deviations for the UCLA Loneliness Scale.
    The subgroup is defined by the 'subgroup_column'.
    """
    subgroup_stats = df.groupby(subgroup_column)['UCLA_Total_Score'].agg(['mean', 'std'])
    
    print(f"\nSubgroup Means and Standard Deviations for {subgroup_column}:")
    print(subgroup_stats)

    return subgroup_stats

# Save the results to CSV
def UCLA_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Save the summarized statistics to CSV
def UCLA_save_summary_to_csv(summary, subgroup_summary, output_file_path):
    """
    Save the summarized results to a separate CSV file.
    """
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df = pd.concat([summary_df, subgroup_summary])

    summary_df.to_csv(output_file_path, index=False)
    print(f"Summary saved to {output_file_path}.")

# Main function to execute the steps
def main(df):

    output_file_path = 'processed_ucla_results.csv'
    summary_output_file_path = 'ucla_summary_results.csv'
    

    if df is not None:
        # Calculate UCLA scores
        df = UCLA_calculate_scores(df)

        # Summarize results
        summary = UCLA_summarize_results(df)

        # Calculate subgroup means and std for a specific subgroup, e.g., 'Gender' or 'Age'
        subgroup_column = 'Gender'  # Adjust this to your dataset's specific column
        subgroup_summary = UCLA_subgroup_means(df, subgroup_column)

        # Save individual scores to CSV
        # UCLA_save_results_to_csv(df, output_file_path)  # Disabled for package use

        # Save summarized results to CSV
        #UCLA_save_summary_to_csv(summary, subgroup_summary, summary_output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'UCLA_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
