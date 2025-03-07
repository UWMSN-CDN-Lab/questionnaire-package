import pandas as pd

# Access CSV file
def EERQ_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

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
    df['Reappraisal_mean'] = df[['EERQ_01', 'EERQ_05', 'EERQ_10', 'EERQ_17', 'EERQ_19', 'EERQ_22']].mean(axis=1)
    df['Suppression_mean'] = df[['EERQ_04', 'EERQ_09', 'EERQ_13', 'EERQ_20']].mean(axis=1)
    df['Distraction_mean'] = df[['EERQ_06', 'EERQ_12', 'EERQ_15', 'EERQ_18', 'EERQ_21']].mean(axis=1)
    df['Selective_Attention_mean'] = df[['EERQ_07', 'EERQ_11', 'EERQ_14', 'EERQ_16']].mean(axis=1)
    df['Situation_Selection_mean'] = df[['EERQ_02', 'EERQ_03', 'EERQ_08']].mean(axis=1)
    
    # Optional: You can calculate the overall EERQ score by averaging all strategies
    df['Total_E_ERQ_Score_mean'] = df[['Reappraisal_mean', 'Suppression_mean', 'Distraction_mean', 'Selective_Attention_mean', 'Situation_Selection_mean']].mean(axis=1)

    return df

# Summarize results
def EERQ_summarize_results(df):
    """
    Summarize the EERQ scores by calculating mean and standard deviation.
    """
    mean_scores = df[['Reappraisal_mean', 'Suppression_mean', 'Distraction_mean', 'Selective_Attention_mean', 'Situation_Selection_mean', 'Total_E_ERQ_Score_mean']].mean()
    std_scores = df[['Reappraisal_mean', 'Suppression_mean', 'Distraction_mean', 'Selective_Attention_mean', 'Situation_Selection_mean', 'Total_E_ERQ_Score_mean']].std()
    
    print("\nSummary of E-ERQ Scores:")
    print(df[['Reappraisal_mean', 'Suppression_mean', 'Distraction_mean', 'Selective_Attention_mean', 'Situation_Selection_mean', 'Total_E_ERQ_Score_mean']])
    
    print(f"\nMean Reappraisal: {mean_scores['Reappraisal_mean']:.3f}")
    print(f"Mean Suppression: {mean_scores['Suppression_mean']:.3f}")
    print(f"Mean Distraction: {mean_scores['Distraction_mean']:.3f}")
    print(f"Mean Selective Attention: {mean_scores['Selective_Attention_mean']:.3f}")
    print(f"Mean Situation Selection: {mean_scores['Situation_Selection_mean']:.3f}")
    print(f"Mean Total E-ERQ Score: {mean_scores['Total_E_ERQ_Score_mean']:.3f}")
    
    return {
        'Mean Reappraisal': mean_scores['Reappraisal_mean'],
        'Mean Suppression': mean_scores['Suppression_mean'],
        'Mean Distraction': mean_scores['Distraction_mean'],
        'Mean Selective Attention': mean_scores['Selective_Attention_mean'],
        'Mean Situation Selection': mean_scores['Situation_Selection_mean'],
        'Mean Total E-ERQ Score': mean_scores['Total_E_ERQ_Score_mean'],
        'Std Dev Reappraisal': std_scores['Reappraisal_mean'],
        'Std Dev Suppression': std_scores['Suppression_mean'],
        'Std Dev Distraction': std_scores['Distraction_mean'],  # Fixed typo here
        'Std Dev Selective Attention': std_scores['Selective_Attention_mean'],
        'Std Dev Situation Selection': std_scores['Situation_Selection_mean']
    }

# Save the results to CSV
def EERQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    selected_columns = [
        'Reappraisal_mean','Suppression_mean','Distraction_mean',
        'Selective_Attention_mean','Situation_Selection_mean','Total_E_ERQ_Score_mean'
    ]
    
    # Ensure only existing columns are selected (in case of errors)
    df_filtered = df[selected_columns] if set(selected_columns).issubset(df.columns) else df[list(set(selected_columns) & set(df.columns))]
    
    df_filtered.to_csv(output_file_path, index=False)  # Save filtered data to CSV
    print(f"Selected summary scores saved to {output_file_path}.")

# Main function to execute the steps
def main():
    output_file_path = 'processed_eerq_results.csv'
    # Load the CSV file
    df = EERQ_access_csv('/Users/ayusmankhuntia/data-pipeline/emotion_regulation_risk_taking-scripts/Risk-Taking+and+Emotion+Regulation_February+4,+2025_15.23.csv')

    if df is not None:
        # Calculate E-ERQ subscale scores
        df = EERQ_calculate_scores(df)

        # Summarize results
        summary = EERQ_summarize_results(df)
        
        # Save individual scores to CSV
        EERQ_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
