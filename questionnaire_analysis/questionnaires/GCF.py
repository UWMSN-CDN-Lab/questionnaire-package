import pandas as pd

def GCF_calculate_scores(df):
    """
    Calculate the total GCF score by averaging all GCF item responses.
    Assumes items are named GCF_01 to GCF_20.
    """
    gcf_items = [f'GCF_{i:02d}' for i in range(1, 21)]  # Adjust if you have a different item range

    for item in gcf_items:
        df[item] = pd.to_numeric(df[item], errors='coerce')

    df['GCF_Total_Score'] = df[gcf_items].mean(axis=1)
    return df
# Summarize results
def GCF_summarize_results(df):
    """
    Summarize the GCF scores by calculating the mean and standard deviation for the total score.
    """
    mean_total_score = df['GCF_Total_Score'].mean()
    std_total_score = df['GCF_Total_Score'].std()

    print("\nSummary of Greenleaf Content-free Scale Scores:")
    print(df[['GCF_Total_Score']])

    print(f"\nMean Total GCF Score: {mean_total_score:.2f}")
    print(f"Standard Deviation of GCF Scores: {std_total_score:.2f}")

    return {
        'Mean Total GCF Score': mean_total_score,
        'Std Dev Total GCF Score': std_total_score
    }

# Save the results to CSV
def GCF_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Save the summarized statistics to CSV
def GCF_save_summary_to_csv(summary, output_file_path):
    """
    Save the summarized results to a separate CSV file.
    """
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df = pd.concat([summary_df])

    summary_df.to_csv(output_file_path, index=False)
    print(f"Summary saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_GCF_results.csv'
    summary_output_file_path = 'GCF_summary_results.csv'

    if df is not None:
        # Summarize results
        df = GCF_calculate_scores(df)


        summary = GCF_summarize_results(df)

        # Save individual scores to CSV
        # GCF_save_results_to_csv(df, output_file_path)  # Disabled for package use

        # Save summarized results to CSV
        # GCF_save_summary_to_csv(summary,summary_output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'GCF_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
