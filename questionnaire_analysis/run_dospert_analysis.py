import pandas as pd
from questionnaires.DOSPERT import (
    DOSPERT_calculate_scores,
    DOSPERT_summarize_results,
    DOSPERT_save_results_to_csv
)

def run_dospert_analysis(input_file_path, output_file_path):
    """
    Run the complete DOSPERT questionnaire analysis pipeline.
    
    Parameters:
    -----------
    input_file_path : str
        Path to the input CSV file containing DOSPERT responses
    output_file_path : str
        Path where the analysis results should be saved
    """
    try:
        # Read the input data
        print(f"Reading data from {input_file_path}...")
        df = pd.read_csv(input_file_path)
        
        # Calculate scores
        print("\nCalculating DOSPERT scores...")
        df = DOSPERT_calculate_scores(df)
        
        # Summarize results
        print("\nGenerating summary statistics...")
        summary = DOSPERT_summarize_results(df)
        
        # Save results
        print("\nSaving results...")
        DOSPERT_save_results_to_csv(df, output_file_path)
        
        print("\nAnalysis completed successfully!")
        return df, summary
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    input_file = "path/to/your/input_data.csv"  # Replace with your input file path
    output_file = "path/to/your/output_results.csv"  # Replace with your desired output path
    
    # Run the analysis
    df, summary = run_dospert_analysis(input_file, output_file) 