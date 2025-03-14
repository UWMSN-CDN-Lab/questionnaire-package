import pandas as pd


# Calculate mean scores for the given subscale
def PMERQ_calculate_subscale_mean(df, items):
    """
    Calculate the average score for each subscale based on the item numbers.
    """
    subscale_items = [item for item in items]
    numeric_df = df[subscale_items].apply(pd.to_numeric, errors='coerce')
    return numeric_df.mean(axis=1)

# Define subscales based on the PMERQ questionnaire
subscales = {
    'Engagement_Situation_Selection': ["PMERQ_09", "PMERQ_11", "PMERQ_15", "PMERQ_28"],
    'Disengagement_Situation_Selection': ["PMERQ_04", "PMERQ_05", "PMERQ_12", "PMERQ_18", "PMERQ_42", "PMERQ_44"],
    'Engagement_Situation_Modification': ["PMERQ_06", "PMERQ_17", "PMERQ_19", "PMERQ_26", "PMERQ_36", "PMERQ_39"],
    'Disengagement_Situation_Modification': ["PMERQ_03", "PMERQ_10", "PMERQ_14", "PMERQ_37", "PMERQ_43"],
    'Engagement_Attentional_Deployment': ["PMERQ_02", "PMERQ_22", "PMERQ_23", "PMERQ_31"],
    'Disengagement_Attentional_Deployment': ["PMERQ_13", "PMERQ_27", "PMERQ_29", "PMERQ_33", "PMERQ_35"],
    'Engagement_Cognitive_Reappraisal': ["PMERQ_07", "PMERQ_20", "PMERQ_21", "PMERQ_24", "PMERQ_40", "PMERQ_45"],
    'Disengagement_Cognitive_Reappraisal': ["PMERQ_25", "PMERQ_38", "PMERQ_41"],
    'Engagement_Response_Modulation': ["PMERQ_08", "PMERQ_30", "PMERQ_32"],
    'Disengagement_Response_Modulation': ["PMERQ_01", "PMERQ_16", "PMERQ_34"],
}

# Calculate the mean scores for all subscales
def PMERQ_calculate_subscale_scores(df):
    """
    Calculate the mean score for each subscale in the PMERQ.
    """
    for subscale, items in subscales.items():
        df[subscale] = PMERQ_calculate_subscale_mean(df, items)
    return df

# Summarize the overall engagement and disengagement scores
def PMERQ_summarize_engagement_disengagement(df):
    """
    Summarize the engagement and disengagement orientation scores.
    """
    engagement_columns = [
        'Engagement_Situation_Selection', 'Engagement_Situation_Modification', 
        'Engagement_Attentional_Deployment', 'Engagement_Cognitive_Reappraisal', 
        'Engagement_Response_Modulation'
    ]
    disengagement_columns = [
        'Disengagement_Situation_Selection', 'Disengagement_Situation_Modification', 
        'Disengagement_Attentional_Deployment', 'Disengagement_Cognitive_Reappraisal', 
        'Disengagement_Response_Modulation'
    ]
    
    df['Engagement_Score'] = df[engagement_columns].mean(axis=1)
    df['Disengagement_Score'] = df[disengagement_columns].mean(axis=1)
    
    print("\nSummary of Engagement and Disengagement Scores:")
    print(df[['Engagement_Score', 'Disengagement_Score']])
    
    return df

# Save the results to CSV
def PMERQ_save_results_to_csv(df, output_file_path):
    """
    Save the processed results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_pmerq_results.csv'

    if df is not None:
        # Calculate subscale scores
        df = PMERQ_calculate_subscale_scores(df)

        # Summarize engagement and disengagement scores
        df = PMERQ_summarize_engagement_disengagement(df)

        # Save results to CSV
        PMERQ_save_results_to_csv(df, output_file_path)

if __name__ == "__main__":
    main()
