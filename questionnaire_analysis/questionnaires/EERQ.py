import pandas as pd



# Calculating total scores
def EERQ_calculate_scores(df):
    """
    Calculate the total score for the EERQ scale.
    Each subscale is calculated by averaging or summing relevant items.
    """
    df = df.iloc[2:].reset_index(drop=True)  # Reset index after skipping

    # Convert all relevant columns to numeric (ignoring errors)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['EERQ_Reappraisal_mean'] = df[['EERQ_01', 'EERQ_05', 'EERQ_10', 'EERQ_17', 'EERQ_19', 'EERQ_22']].mean(axis=1)
    df['EERQ_Suppression_mean'] = df[['EERQ_04', 'EERQ_09', 'EERQ_13', 'EERQ_20']].mean(axis=1)
    df['EERQ_Distraction_mean'] = df[['EERQ_06', 'EERQ_12', 'EERQ_15', 'EERQ_18', 'EERQ_21']].mean(axis=1)
    df['EERQ_Selective_Attention_mean'] = df[['EERQ_07', 'EERQ_11', 'EERQ_14', 'EERQ_16']].mean(axis=1)
    df['EERQ_Situation_Selection_mean'] = df[['EERQ_02', 'EERQ_03', 'EERQ_08']].mean(axis=1)
    
    # Optional: You can calculate the overall EERQ score by averaging all strategies
    df['EERQ_Total_E_ERQ_Score_mean'] = df[['EERQ_Reappraisal_mean', 'EERQ_Suppression_mean', 'EERQ_Distraction_mean', 'EERQ_Selective_Attention_mean', 'EERQ_Situation_Selection_mean']].mean(axis=1)

    return df

# Summarize results
def EERQ_summarize_results(df):
    """
    Summarize the EERQ scores by calculating mean and standard deviation.
    """
    mean_scores = df[['EERQ_Reappraisal_mean', 'EERQ_Suppression_mean', 'EERQ_Distraction_mean', 'EERQ_Selective_Attention_mean', 'EERQ_Situation_Selection_mean', 'EERQ_Total_E_ERQ_Score_mean']].mean()
    std_scores = df[['EERQ_Reappraisal_mean', 'EERQ_Suppression_mean', 'EERQ_Distraction_mean', 'EERQ_Selective_Attention_mean', 'EERQ_Situation_Selection_mean', 'EERQ_Total_E_ERQ_Score_mean']].std()
    
    print("\nSummary of E-ERQ Scores:")
    print(df[['EERQ_Reappraisal_mean', 'EERQ_Suppression_mean', 'EERQ_Distraction_mean', 'EERQ_Selective_Attention_mean', 'EERQ_Situation_Selection_mean', 'EERQ_Total_E_ERQ_Score_mean']])
    
    print(f"\nMean Reappraisal: {mean_scores['EERQ_Reappraisal_mean']:.3f}")
    print(f"Mean Suppression: {mean_scores['EERQ_Suppression_mean']:.3f}")
    print(f"Mean Distraction: {mean_scores['EERQ_Distraction_mean']:.3f}")
    print(f"Mean Selective Attention: {mean_scores['EERQ_Selective_Attention_mean']:.3f}")
    print(f"Mean Situation Selection: {mean_scores['EERQ_Situation_Selection_mean']:.3f}")
    print(f"Mean Total E-ERQ Score: {mean_scores['EERQ_Total_E_ERQ_Score_mean']:.3f}")
    
    return {
        'Mean Reappraisal': mean_scores['EERQ_Reappraisal_mean'],
        'Mean Suppression': mean_scores['EERQ_Suppression_mean'],
        'Mean Distraction': mean_scores['EERQ_Distraction_mean'],
        'Mean Selective Attention': mean_scores['EERQ_Selective_Attention_mean'],
        'Mean Situation Selection': mean_scores['EERQ_Situation_Selection_mean'],
        'Mean Total E-ERQ Score': mean_scores['EERQ_Total_E_ERQ_Score_mean'],
        'Std Dev Reappraisal': std_scores['EERQ_Reappraisal_mean'],
        'Std Dev Suppression': std_scores['EERQ_Suppression_mean'],
        'Std Dev Distraction': std_scores['EERQ_Distraction_mean'],  # Fixed typo here
        'Std Dev Selective Attention': std_scores['EERQ_Selective_Attention_mean'],
        'Std Dev Situation Selection': std_scores['EERQ_Situation_Selection_mean']
    }

# Save the results to CSV
def EERQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    selected_columns = [
        'EERQ_Reappraisal_mean','EERQ_Suppression_mean','EERQ_Distraction_mean',
        'EERQ_Selective_Attention_mean','EERQ_Situation_Selection_mean','EERQ_Total_E_ERQ_Score_mean'
    ]
    
    # Ensure only existing columns are selected (in case of errors)
    df_filtered = df[selected_columns] if set(selected_columns).issubset(df.columns) else df[list(set(selected_columns) & set(df.columns))]
    
    df_filtered.to_csv(output_file_path, index=False)  # Save filtered data to CSV
    print(f"Selected summary scores saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    if df is not None:
        # Step 1: Calculate scores
        df = EERQ_calculate_scores(df)

        # Step 2: Optional log summary
        _ = EERQ_summarize_results(df)


        return df
    return None

if __name__ == "__main__":
    main()
