import pandas as pd

# Define subscales
general_distress_items = [2, 3, 7, 12, 13, 17, 20, 21]  # General Distress (GD)
anxious_arousal_items = [4, 6, 8, 10, 14, 16, 18, 22, 24, 2, 3, 7, 12, 13, 17, 20, 21, 26]  # Anxious Arousal (AA)
anhedonic_depression_forward_items = [5, 11]  # Anhedonic Depression forward scored items
anhedonic_depression_reverse_items = [1, 9, 15, 19, 23, 25]  # Anhedonic Depression reverse scored items

# Calculate mean scores for a set of items
def MASQ_calculate_mean(df, items, label):
    """
    Calculate the mean score for a given list of item numbers.
    """
    item_columns = [f'MASQ_{item:02d}' for item in items]
    mean_score = df[item_columns].mean(axis=1)
    df[label] = mean_score
    return df

# Process the data to calculate subscale scores
def MASQ_process_data(df):
    """
    Calculate subscale and overall scores for the MINI-MASQ.
    Subscales:
    - General Distress (GD)
    - Anxious Arousal (AA)
    - Anhedonic Depression (AD)
    """
    # Calculate all scores at once to avoid fragmentation
    
    # General Distress (GD): Items 2, 3, 7, 12, 13, 17, 20, 21
    masq_gd_columns = ['MASQ_02', 'MASQ_03', 'MASQ_07', 'MASQ_12', 'MASQ_13', 'MASQ_17', 'MASQ_20', 'MASQ_21']
    
    # Anxious Arousal (AA): Items 4, 6, 8, 10, 14, 16, 18, 22, 24, 2, 3, 7, 12, 13, 17, 20, 21, 26
    masq_aa_columns = ['MASQ_04', 'MASQ_06', 'MASQ_08', 'MASQ_10', 'MASQ_14', 'MASQ_16', 'MASQ_18', 'MASQ_22', 'MASQ_24', 
                       'MASQ_02', 'MASQ_03', 'MASQ_07', 'MASQ_12', 'MASQ_13', 'MASQ_17', 'MASQ_20', 'MASQ_21', 'MASQ_26']
    
    # Anhedonic Depression (AD): Forward items 5, 11; Reverse items 1, 9, 15, 19, 23, 25
    masq_ad_forward_columns = ['MASQ_05', 'MASQ_11']
    masq_ad_reverse_columns = ['MASQ_01', 'MASQ_09', 'MASQ_15', 'MASQ_19', 'MASQ_23', 'MASQ_25']
    
    # Reverse score the AD reverse items (assuming 1-5 scale: reverse = 6 - original)
    ad_reverse_scored = 6 - df[masq_ad_reverse_columns]
    
    # Combine forward and reverse scored items for AD
    ad_all_items = pd.concat([df[masq_ad_forward_columns], ad_reverse_scored], axis=1)
    
    masq_scores = {
        'MASQ_General_Distress_Score': df[masq_gd_columns].mean(axis=1),
        'MASQ_Anxious_Arousal_Score': df[masq_aa_columns].mean(axis=1),
        'MASQ_Anhedonic_Depression_Score': ad_all_items.mean(axis=1)
    }
    df = df.assign(**masq_scores)
    df['MASQ_Overall_Score'] = df[['MASQ_General_Distress_Score', 'MASQ_Anxious_Arousal_Score', 'MASQ_Anhedonic_Depression_Score']].mean(axis=1)
    return df

# Summarize results
def MASQ_summarize_results(df):
    """
    Summarize the MINI-MASQ subscale and overall scores by calculating mean and standard deviation.
    """
    mean_scores = df[['MASQ_General_Distress_Score', 'MASQ_Anxious_Arousal_Score', 'MASQ_Anhedonic_Depression_Score', 'MASQ_Overall_Score']].mean()
    std_scores = df[['MASQ_General_Distress_Score', 'MASQ_Anxious_Arousal_Score', 'MASQ_Anhedonic_Depression_Score', 'MASQ_Overall_Score']].std()

    print("\nSummary of MINI-MASQ Scores:")
    print(df[['MASQ_General_Distress_Score', 'MASQ_Anxious_Arousal_Score', 'MASQ_Anhedonic_Depression_Score', 'MASQ_Overall_Score']])

    return {
        'Mean General Distress Score': mean_scores['MASQ_General_Distress_Score'],
        'Mean Anxious Arousal Score': mean_scores['MASQ_Anxious_Arousal_Score'],
        'Mean Anhedonic Depression Score': mean_scores['MASQ_Anhedonic_Depression_Score'],
        'Mean Overall Score': mean_scores['MASQ_Overall_Score'],
        'Std Dev General Distress': std_scores['MASQ_General_Distress_Score'],
        'Std Dev Anxious Arousal': std_scores['MASQ_Anxious_Arousal_Score'],
        'Std Dev Anhedonic Depression': std_scores['MASQ_Anhedonic_Depression_Score'],
        'Std Dev Overall': std_scores['MASQ_Overall_Score']
    }

# Save the results to CSV
def MASQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_emotion_survey_results.csv'


    if df is not None:
        # Process the data to calculate subscale and overall scores
        df = MASQ_process_data(df)

        # Summarize results
        summary = MASQ_summarize_results(df)

        # Save results to CSV
        # MASQ_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'MASQ_General_Distress_Score',
            'MASQ_Anxious_Arousal_Score',
            'MASQ_Anhedonic_Depression_Score',
            'MASQ_Overall_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None

if __name__ == "__main__":
    main()
