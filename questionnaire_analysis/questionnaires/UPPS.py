import pandas as pd
# Calculate UPPS-P subscale scores
def UPPSP_calculate_scores(df):
    """
    Calculate the UPPS-P subscale scores and add them to the DataFrame efficiently.
    """
    new_columns = {
        'UPPS_Negative_Urgency': df[['UPPS_07', 'UPPS_11', 'UPPS_17', 'UPPS_20']].mean(axis=1),
        'UPPS_Positive_Urgency': df[['UPPS_35', 'UPPS_36', 'UPPS_37', 'UPPS_39']].mean(axis=1),
        'UPPS_Lack_Premeditation': df[['UPPS_06', 'UPPS_16', 'UPPS_23', 'UPPS_28']].mean(axis=1),
        'UPPS_Lack_Perseverance': df[['UPPS_15', 'UPPS_19', 'UPPS_22', 'UPPS_24']].mean(axis=1),
        'UPPS_Sensation_Seeking': df[['UPPS_12', 'UPPS_18', 'UPPS_21', 'UPPS_27']].mean(axis=1)
    }
    df = pd.concat([df, pd.DataFrame(new_columns)], axis=1)
    return df

# Summarize results
def UPPSP_summarize_results(df):
    """
    Summarize the UPPS-P subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['UPPS_Negative_Urgency', 'UPPS_Positive_Urgency', 'UPPS_Lack_Premeditation', 
                      'UPPS_Lack_Perseverance', 'UPPS_Sensation_Seeking']].mean()
    std_scores = df[['UPPS_Negative_Urgency', 'UPPS_Positive_Urgency', 'UPPS_Lack_Premeditation', 
                     'UPPS_Lack_Perseverance', 'UPPS_Sensation_Seeking']].std()

    print("\nSummary of UPPS-P Scores:")
    print(df[['UPPS_Negative_Urgency', 'UPPS_Positive_Urgency', 'UPPS_Lack_Premeditation', 
              'UPPS_Lack_Perseverance', 'UPPS_Sensation_Seeking']])
    
    return {
        'Mean Negative Urgency': mean_scores['UPPS_Negative_Urgency'],
        'Mean Positive Urgency': mean_scores['UPPS_Positive_Urgency'],
        'Mean Lack of Premeditation': mean_scores['UPPS_Lack_Premeditation'],
        'Mean Lack of Perseverance': mean_scores['UPPS_Lack_Perseverance'],
        'Mean Sensation Seeking': mean_scores['UPPS_Sensation_Seeking'],
        'Std Dev Negative Urgency': std_scores['UPPS_Negative_Urgency'],
        'Std Dev Positive Urgency': std_scores['UPPS_Positive_Urgency'],
        'Std Dev Lack of Premeditation': std_scores['UPPS_Lack_Premeditation'],
        'Std Dev Lack of Perseverance': std_scores['UPPS_Lack_Perseverance'],
        'Std Dev Sensation Seeking': std_scores['UPPS_Sensation_Seeking']
    }

# Save the results to CSV
def UPPSP_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")
    selected_columns = [
        "UPPS_Negative_Urgency","UPPS_Positive_Urgency",
        "UPPS_Lack_Premeditation","UPPS_Lack_Perseverance",
        "UPPS_Sensation_Seeking"
    ]
    df_filtered = df[selected_columns] if set(selected_columns).issubset(df.columns) else df[list(set(selected_columns) & set(df.columns))]
    
    df_filtered.to_csv(output_file_path, index=False)  # Save filtered data to CSV
    print(f"Selected summary scores saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    if df is not None:
        # Step 1: Calculate UPPS-P subscale scores
        df = UPPSP_calculate_scores(df)

        # Step 2: Print summary stats (optional for dev)
        _ = UPPSP_summarize_results(df)

        # Only return the summary columns for concatenation
        summary_columns = [
            'UPPS_Negative_Urgency',
            'UPPS_Positive_Urgency',
            'UPPS_Lack_Premeditation',
            'UPPS_Lack_Perseverance',
            'UPPS_Sensation_Seeking'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
