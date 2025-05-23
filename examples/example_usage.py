#!/usr/bin/env python3
"""
Example script demonstrating how to use the questionnaire analysis package.
"""

import pandas as pd
from questionnaire_analysis.questionnaires.DOSPERT import (
    DOSPERT_calculate_scores,
    DOSPERT_summarize_results,
    DOSPERT_save_results_to_csv
)

def main():
    # Example 1: Using the package programmatically
    print("Example 1: Using the package programmatically")
    print("-" * 50)
    
    # Create sample data
    data = {
        'DOSPERT_01': [1, 2, 3],
        'DOSPERT_02': [2, 3, 4],
        # ... Add all DOSPERT items
        'DOSPERT_30': [5, 4, 3]
    }
    df = pd.DataFrame(data)
    
    # Calculate scores
    df = DOSPERT_calculate_scores(df)
    
    # Get summary statistics
    summary = DOSPERT_summarize_results(df)
    
    # Save results
    DOSPERT_save_results_to_csv(df, "example_results.csv")
    
    print("\nExample 2: Using the command-line interface")
    print("-" * 50)
    print("To run the analysis from command line:")
    print("python3 -m questionnaire_analysis path/to/your/data.csv")
    print("or")
    print("python3 question_analysis_runner.py path/to/your/data.csv")

if __name__ == "__main__":
    main() 