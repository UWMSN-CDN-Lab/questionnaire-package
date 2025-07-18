import pandas as pd
import numpy as np

# Load CSV file
def RAS_access_csv(file_path):
    """
    Load the CSV file containing RAS data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Reverse score items 4 and 7
def RAS_reverse_score(df):
    """
    Reverse score items 4 and 7 for the RAS questionnaire.
    Items 4 and 7 are reverse-scored (1 becomes 5, 2 becomes 4, etc.).
    """
    # Reverse score item 4: "How often do you wish you hadn't gotten into this relationship?"
    if 'RAS_04' in df.columns:
        df['RAS_04'] = 6 - df['RAS_04']  # Reverse scoring: 1->5, 2->4, 3->3, 4->2, 5->1
    
    # Reverse score item 7: "How many problems are there in your relationship?"
    if 'RAS_07' in df.columns:
        df['RAS_07'] = 6 - df['RAS_07']  # Reverse scoring: 1->5, 2->4, 3->3, 4->2, 5->1
    
    return df

# Calculate RAS total score
def RAS_calculate_scores(df):
    """
    Calculate the total RAS score by summing all 7 items after reverse scoring.
    
    RAS Items:
    1. How well does your partner meet your needs?
    2. In general, how satisfied are you with your relationship?
    3. How good is your relationship compared to most?
    4. How often do you wish you hadn't gotten into this relationship? (REVERSE SCORED)
    5. To what extent has your relationship met your original expectations?
    6. How much do you love your partner?
    7. How many problems are there in your relationship? (REVERSE SCORED)
    
    Scoring: 1-5 scale, items 4 and 7 are reverse-scored
    Total score range: 7-35, higher scores indicate greater relationship satisfaction
    """
    # First reverse score items 4 and 7
    df = RAS_reverse_score(df)
    
    # Calculate total RAS score by summing all 7 items
    ras_items = ['RAS_01', 'RAS_02', 'RAS_03', 'RAS_04', 'RAS_05', 'RAS_06', 'RAS_07']
    
    # Ensure all items are numeric
    for item in ras_items:
        if item in df.columns:
            df[item] = pd.to_numeric(df[item], errors='coerce')
    
    # Calculate total score
    df['RAS_Total_Score'] = df[ras_items].sum(axis=1)
    
    return df

# Summarize results
def RAS_summarize_results(df):
    """
    Summarize the RAS scores by calculating the mean and standard deviation for the total score.
    """
    mean_total_score = df['RAS_Total_Score'].mean()
    std_total_score = df['RAS_Total_Score'].std()

    print("\nSummary of Relationship Assessment Scale (RAS) Scores:")
    print(df[['RAS_Total_Score']])

    print(f"\nMean Total RAS Score: {mean_total_score:.2f}")
    print(f"Standard Deviation of RAS Scores: {std_total_score:.2f}")
    print(f"Score Range: {df['RAS_Total_Score'].min():.0f} - {df['RAS_Total_Score'].max():.0f}")
    print("Note: Higher scores indicate greater relationship satisfaction (range: 7-35)")

    return {
        'Mean Total RAS Score': mean_total_score,
        'Std Dev Total RAS Score': std_total_score,
        'Min RAS Score': df['RAS_Total_Score'].min(),
        'Max RAS Score': df['RAS_Total_Score'].max()
    }

# Save results to CSV
def RAS_save_results_to_csv(df, output_file_path):
    """
    Save the processed RAS results to a CSV file.
    """
    try:
        df.to_csv(output_file_path, index=False)
        print(f"RAS results saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

# Main function to execute the steps
def main(df):
    output_file_path = 'processed_ras_results.csv'

    if df is not None:
        # Calculate RAS total score
        df = RAS_calculate_scores(df)

        # Summarize results
        summary = RAS_summarize_results(df)

        # Save results to CSV
        # RAS_save_results_to_csv(df, output_file_path)  # Disabled for package use
        
        # Only return the summary columns for concatenation
        summary_columns = [
            'RAS_Total_Score'
        ]
        # Only return columns that exist (in case of errors)
        return df[[col for col in summary_columns if col in df.columns]]
    return None
