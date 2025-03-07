import pandas as pd

# Access CSV file
def GCF_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Summarize results
def GCF_summarize_results(df):
    """
    Summarize the GCF scores by calculating the mean and standard deviation for the total score.
    """
    mean_total_score = df['Total_GCF_Score'].mean()
    std_total_score = df['Total_GCF_Score'].std()

    print("\nSummary of Greenleaf Content-free Scale Scores:")
    print(df[['Total_GCF_Score']])

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
def main():
    input_file_path = './data/GCF_DATA_SET.csv'
    output_file_path = 'processed_GCF_results.csv'
    summary_output_file_path = 'GCF_summary_results.csv'
    
    # Load the CSV file
    df = GCF_access_csv(input_file_path)

    if df is not None:
        # Summarize results
        summary = GCF_summarize_results(df)

        # Save individual scores to CSV
        GCF_save_results_to_csv(df, output_file_path)

        # Save summarized results to CSV
        GCF_save_summary_to_csv(summary,summary_output_file_path)

if __name__ == "__main__":
    main()
