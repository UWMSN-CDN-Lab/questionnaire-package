import pandas as pd

# Access CSV file for UPPS-P
def UPPSP_access_csv(file_path, delimiter=","):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        print(f"Data loaded successfully from {file_path}.")
        df = df.iloc[2:].reset_index(drop=True)  # Reset index after skipping

        # Convert all relevant columns to numeric (ignoring errors)
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Calculate UPPS-P subscale scores
def UPPSP_calculate_scores(df):
    """
    Calculate the subscale scores for the UPPS-P questionnaire.
    Subscales include:
    - Negative Urgency (NU)
    - Positive Urgency (PU)
    - Lack of Premeditation (LP)
    - Lack of Perseverance (LPer)
    - Sensation Seeking (SS)
    Reverse scoring is applied where necessary.
    """
    
    # Reverse-scored items for each subscale
    reverse_neg_urgency = ["UPPS_07", "UPPS_11", "UPPS_17", "UPPS_20"] # Item numbers for Negative Urgency (reverse)
    reverse_pos_urgency = ["UPPS_35", "UPPS_36", "UPPS_37", "UPPS_39"] # Positive Urgency (reverse)
    reverse_sensation_seeking = ["UPPS_12", "UPPS_18", "UPPS_21", "UPPS_27"] # Sensation Seeking (reverse)

    # Apply reverse scoring for relevant items
    for item in reverse_neg_urgency:
        df[item] = 5 - df[item]  # Assuming a 1-4 scale, reverse scoring is 5 - original response
    
    for item in reverse_pos_urgency:
        df[item] = 5 - df[item]

    for item in reverse_sensation_seeking:
        df[item] = 5 - df[item]
        
    
    # Calculate subscale scores
    df['Negative_Urgency'] = df[['UPPS_07', 'UPPS_11', 'UPPS_17', 'UPPS_20']].mean(axis=1)
    df['Positive_Urgency'] = df[['UPPS_35', 'UPPS_36', 'UPPS_37', 'UPPS_39']].mean(axis=1)
    df['Lack_Premeditation'] = df[['UPPS_06', 'UPPS_16', 'UPPS_23', 'UPPS_28']].mean(axis=1)
    df['Lack_Perseverance'] = df[['UPPS_15', 'UPPS_19', 'UPPS_22', 'UPPS_24']].mean(axis=1)
    df['Sensation_Seeking'] = df[['UPPS_12', 'UPPS_18', 'UPPS_21', 'UPPS_27']].mean(axis=1)
    
    return df

# Summarize results
def UPPSP_summarize_results(df):
    """
    Summarize the UPPS-P subscale scores by calculating the mean and standard deviation.
    """
    mean_scores = df[['Negative_Urgency', 'Positive_Urgency', 'Lack_Premeditation', 
                      'Lack_Perseverance', 'Sensation_Seeking']].mean()
    std_scores = df[['Negative_Urgency', 'Positive_Urgency', 'Lack_Premeditation', 
                     'Lack_Perseverance', 'Sensation_Seeking']].std()

    print("\nSummary of UPPS-P Scores:")
    print(df[['Negative_Urgency', 'Positive_Urgency', 'Lack_Premeditation', 
              'Lack_Perseverance', 'Sensation_Seeking']])
    
    return {
        'Mean Negative Urgency': mean_scores['Negative_Urgency'],
        'Mean Positive Urgency': mean_scores['Positive_Urgency'],
        'Mean Lack of Premeditation': mean_scores['Lack_Premeditation'],
        'Mean Lack of Perseverance': mean_scores['Lack_Perseverance'],
        'Mean Sensation Seeking': mean_scores['Sensation_Seeking'],
        'Std Dev Negative Urgency': std_scores['Negative_Urgency'],
        'Std Dev Positive Urgency': std_scores['Positive_Urgency'],
        'Std Dev Lack of Premeditation': std_scores['Lack_Premeditation'],
        'Std Dev Lack of Perseverance': std_scores['Lack_Perseverance'],
        'Std Dev Sensation Seeking': std_scores['Sensation_Seeking']
    }

# Save the results to CSV
def UPPSP_save_results_to_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")
    selected_columns = [
        "Negative_Urgency","Positive_Urgency",
        "Lack_Premeditation","Lack_Perseverance",
        "Sensation_Seeking"
    ]
    df_filtered = df[selected_columns] if set(selected_columns).issubset(df.columns) else df[list(set(selected_columns) & set(df.columns))]
    
    df_filtered.to_csv(output_file_path, index=False)  # Save filtered data to CSV
    print(f"Selected summary scores saved to {output_file_path}.")

# Main function to execute the steps
def main():
    input_file_path = '/Users/ayusmankhuntia/data-pipeline/emotion_regulation_risk_taking-scripts/Risk-Taking+and+Emotion+Regulation_February+4,+2025_15.23.csv'
    output_file_path = 'processed_upps_results.csv'
    
    # Load CSV
    df = UPPSP_access_csv(input_file_path)

    if df is not None:
        # Calculate UPPS-P subscale scores
        df = UPPSP_calculate_scores(df)

        # Summarize results
        summary = UPPSP_summarize_results(df)

        # Save individual scores to CSV
        UPPSP_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
