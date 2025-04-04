import pandas as pd
# factor analysis. 

# Calculate subscale scores
def DOSPERT_calculate_subscale_scores(df):
    """
    Calculate the subscale scores for the DOSPERT scale.
    """
    risk_taking_subscales = {
    'Ethical': ["DOSPERT_06", "DOSPERT_09", "DOSPERT_10", "DOSPERT_16", "DOSPERT_29", "DOSPERT_30"],
    'Financial': ["DOSPERT_03", "DOSPERT_04", "DOSPERT_08", "DOSPERT_12", "DOSPERT_14", "DOSPERT_18"],
    'Health_Safety': ["DOSPERT_05", "DOSPERT_15", "DOSPERT_17", "DOSPERT_20", "DOSPERT_23", "DOSPERT_26"],
    'Recreational': ["DOSPERT_02", "DOSPERT_11", "DOSPERT_13", "DOSPERT_19", "DOSPERT_24", "DOSPERT_25"],
    'Social': ["DOSPERT_01", "DOSPERT_07", "DOSPERT_21", "DOSPERT_22", "DOSPERT_27", "DOSPERT_28"]
}
    for subscale, items in risk_taking_subscales.items():
        df[f'{subscale}_Score'] = df[items].mean(axis=1)
    return df

# Calculate overall scores for both risk-taking
def DOSPERT_calculate_scores(df):
    print("2")
    """
    Calculate the overall score for risk-taking and risk-perception.
    """
    risk_taking_subscales = {
    'Ethical': ["DOSPERT_06", "DOSPERT_09", "DOSPERT_10", "DOSPERT_16", "DOSPERT_29", "DOSPERT_30"],
    'Financial': ["DOSPERT_03", "DOSPERT_04", "DOSPERT_08", "DOSPERT_12", "DOSPERT_14", "DOSPERT_18"],
    'Health_Safety': ["DOSPERT_05", "DOSPERT_15", "DOSPERT_17", "DOSPERT_20", "DOSPERT_23", "DOSPERT_26"],
    'Recreational': ["DOSPERT_02", "DOSPERT_11", "DOSPERT_13", "DOSPERT_19", "DOSPERT_24", "DOSPERT_25"],
    'Social': ["DOSPERT_01", "DOSPERT_07", "DOSPERT_21", "DOSPERT_22", "DOSPERT_27", "DOSPERT_28"]
}
    
    for subscale, items in risk_taking_subscales.items():
        for col in items:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df[f'{subscale}_Score'] = df[items].mean(axis=1)
    dospert_items = [
    "DOSPERT_01", "DOSPERT_02", "DOSPERT_03", "DOSPERT_04", "DOSPERT_05",
    "DOSPERT_06", "DOSPERT_07", "DOSPERT_08", "DOSPERT_09", "DOSPERT_10",
    "DOSPERT_11", "DOSPERT_12", "DOSPERT_13", "DOSPERT_14", "DOSPERT_15",
    "DOSPERT_16", "DOSPERT_17", "DOSPERT_18", "DOSPERT_19", "DOSPERT_20",
    "DOSPERT_21", "DOSPERT_22", "DOSPERT_23", "DOSPERT_24", "DOSPERT_25",
    "DOSPERT_26", "DOSPERT_27", "DOSPERT_28", "DOSPERT_29", "DOSPERT_30"
]   
    df['Overall_Score'] = df[dospert_items].sum(axis=1)
    
    return df

# Summarize the results
def DOSPERT_summarize_results(df):
    """
    Summarize the subscale and overall scores for the DOSPERT risk-taking scale.
    """
    risk_taking_subscales = {
    'Ethical': ["DOSPERT_06", "DOSPERT_09", "DOSPERT_10", "DOSPERT_16", "DOSPERT_29", "DOSPERT_30"],
    'Financial': ["DOSPERT_03", "DOSPERT_04", "DOSPERT_08", "DOSPERT_12", "DOSPERT_14", "DOSPERT_18"],
    'Health_Safety': ["DOSPERT_05", "DOSPERT_15", "DOSPERT_17", "DOSPERT_20", "DOSPERT_23", "DOSPERT_26"],
    'Recreational': ["DOSPERT_02", "DOSPERT_11", "DOSPERT_13", "DOSPERT_19", "DOSPERT_24", "DOSPERT_25"],
    'Social': ["DOSPERT_01", "DOSPERT_07", "DOSPERT_21", "DOSPERT_22", "DOSPERT_27", "DOSPERT_28"]
}
    subscales = ['Ethical', 'Financial', 'Health_Safety', 'Recreational', 'Social']
    print("\nSummary of Risk-Taking Scores:")
    print(df[[f'{subscale}_Score' for subscale in subscales] + ['Overall_Score']])
    
    summary = {
        f'{subscale} Risk-Taking Mean': df[f'{subscale}_Score'].mean() for subscale in subscales
    }
    summary['Overall Risk-Taking Mean'] = df['Overall_Score'].mean()
    
    for key, value in summary.items():
        print(f"{key}: {value:.3f}")
    
    return summary

# Save the results to CSV
# def DOSPERT_save_results_to_csv(df, output_file_path):
#     """
#     Save the processed results to a CSV file.
#     """
#     df.to_csv(output_file_path, index=False)
#     print(f"Results saved to {output_file_path}.")
    
def DOSPERT_save_results_to_csv(df, output_file_path):
    """
    Save only the specified subscale scores and overall score to a CSV file.
    """
    selected_columns = [
        'Ethical_Score', 'Financial_Score', 'Health_Safety_Score', 
        'Recreational_Score', 'Social_Score', 'Overall_Score'
    ]
    
    # Ensure only existing columns are selected (in case of errors)
    df_filtered = df[selected_columns] if set(selected_columns).issubset(df.columns) else df[list(set(selected_columns) & set(df.columns))]
    
    df_filtered.to_csv(output_file_path, index=False)  # Save filtered data to CSV
    print(f"Selected summary scores saved to {output_file_path}.")



def main(df):
    if df is not None:
        # Step 1: Calculate subscale & overall scores
        df = DOSPERT_calculate_scores(df)

        # Step 2: Optional logging
        _ = DOSPERT_summarize_results(df)
        return df
    return None

if __name__ == "__main__":
    main()
