import pandas as pd


def PSS_reverse_scores(df, reverse_columns):
    """
    Reverse the scores for specific columns.
    """
    for col in reverse_columns:
        df[col] = 4 - df[col]
    return df

def PSS_calculate_pss_score(row):
    """
    Calculate the total PSS score for a single row.
    """
    pss_columns = [
        'PSS_01', 'PSS_02', 'PSS_03', 'PSS_04r', 'PSS_05r', 
        'PSS_06r', 'PSS_07r', 'PSS_08', 'PSS_09r', 'PSS_10r', 
        'PSS_11', 'PSS_12', 'PSS_13r', 'PSS_14'
    ]
    return row[pss_columns].sum()

def PSS_determine_stress_level(score):
    """
    Determine the stress level based on the total score.
    """
    if score <= 13:
        return "Low Stress"
    elif 14 <= score <= 26:
        return "Moderate Stress"
    else:
        return "High Stress"

def PSS_calculate_subgroup_means(df):
    """
    Calculate mean scores for each subgroup: anxiety and stress.
    """
    anxiety_columns = ['PSS_3', 'PSS_8', 'PSS_11']
    stress_columns = [
        'PSS_1', 'PSS_2', 'PSS_4r', 'PSS_5r', 'PSS_6r', 
        'PSS_7r', 'PSS_9r', 'PSS_10r', 'PSS_12', 'PSS_13r', 
        'PSS_14'
    ]

    # Calculate mean score for each subgroup
    mean_anxiety_score = df[anxiety_columns].mean().mean()
    mean_stress_score = df[stress_columns].mean().mean()
    
    print(f"Mean Anxiety Score: {mean_anxiety_score:.2f}")
    print(f"Mean Stress Score: {mean_stress_score:.2f}")

    return mean_anxiety_score, mean_stress_score

def PSS_calculate_overall_mean(df):
    """
    Calculate the overall mean score for all PSS items.
    """
    pss_columns = [
        'PSS_1', 'PSS_2', 'PSS_3', 'PSS_4r', 'PSS_5r', 'PSS_6r', 'PSS_7r', 
        'PSS_8', 'PSS_9r', 'PSS_10r', 'PSS_11', 'PSS_12', 'PSS_13r', 'PSS_14'
    ]
    
    overall_mean_score = df[pss_columns].mean().mean()
    print(f"Overall Mean PSS Score: {overall_mean_score:.2f}")
    
    return overall_mean_score

def PSS_calculate_individual_scores(df):
    """
    Calculate individual scores for each participant in each subcategory.
    """
    anxiety_columns = ['PSS_3', 'PSS_8', 'PSS_11']
    stress_columns = [
        'PSS_1', 'PSS_2', 'PSS_4r', 'PSS_5r', 'PSS_6r', 
        'PSS_7r', 'PSS_9r', 'PSS_10r', 'PSS_12', 'PSS_13r', 
        'PSS_14'
    ]
    
    df['PSS_Anxiety_Score'] = df[anxiety_columns].sum(axis=1)
    df['PSS_Stress_Score'] = df[stress_columns].sum(axis=1)
    
    print("\nIndividual Scores for Each Subcategory:")
    print(df[['PSS_Anxiety_Score', 'PSS_Stress_Score']])
    
    return df

def PSS_summarize_scores(df):
    """
    Summarize the mean scores for each subgroup and overall scores.
    """
    mean_anxiety_score, mean_stress_score = PSS_calculate_subgroup_means(df)
    overall_mean_score = PSS_calculate_overall_mean(df)
    
    summary = {
        'Mean Anxiety Score': mean_anxiety_score,
        'Mean Stress Score': mean_stress_score,
        'Overall Mean PSS Score': overall_mean_score
    }
    
    print("\nSummary of Scores:")
    for key, value in summary.items():
        print(f"{key}: {value:.2f}")

    return summary

def PSS_process_pss(df):
    """
    Process each row in the DataFrame to calculate PSS scores, stress levels,
    mean scores for subgroups, and overall mean score.
    """
    # Reverse the necessary scores for PSS questions
    reverse_columns = ['PSS_4r', 'PSS_5r', 'PSS_6r', 'PSS_7r', 'PSS_9r', 'PSS_10r', 'PSS_13r']
    df = PSS_reverse_scores(df, reverse_columns)
    
    # Calculate PSS score and determine stress level
    df['PSS_Total_Score'] = df.apply(PSS_calculate_pss_score, axis=1)
    df['PSS_Stress_Level'] = df['PSS_Total_Score'].apply(PSS_determine_stress_level)
    
    # Calculate individual scores
    df = PSS_calculate_individual_scores(df)
    
    # Summarize scores
    PSS_summarize_scores(df)
    
    return df

def PSS_save_results_to_csv(df, output_file_path):
    """
    Save the results to a CSV file.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}.")

def main(df):
    output_file_path = 'processed_survey_results.csv'
    

    if df is not None:
        # Process the data
        processed_df = PSS_process_pss(df)

        # Save the results to a new CSV file
        PSS_save_results_to_csv(processed_df, output_file_path)
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'PSS_Total_Score',
            'PSS_Stress_Level',
            'PSS_Anxiety_Score',
            'PSS_Stress_Score'
        ]
        # Only return columns that exist (in case of errors)
        return processed_df[[col for col in summary_columns if col in processed_df.columns]]
    return None

if __name__ == "__main__":
    main()
