#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path

def run_questionnaire_analysis(input_file):
    """
    Run the questionnaire analysis package on the specified input file.
    
    Parameters:
    -----------
    input_file : str
        Path to the input CSV file containing questionnaire responses
    """
    try:
        # Get the absolute path of the input file
        input_path = Path(input_file).resolve()
        
        # Verify the file exists
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        # Get the directory of the input file for output
        output_dir = input_path.parent
        output_file = output_dir / f"analysis_results_{input_path.stem}.csv"
        
        # Construct the command
        cmd = f"python3 -m questionnaire_analysis {input_path}"
        
        print(f"\nRunning questionnaire analysis...")
        print(f"Input file: {input_path}")
        print(f"Output will be saved to: {output_file}")
        
        # Run the analysis
        os.system(cmd)
        
        print("\nAnalysis completed successfully!")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run questionnaire analysis package')
    parser.add_argument('input_file', help='Path to the input CSV file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the analysis
    run_questionnaire_analysis(args.input_file)

if __name__ == "__main__":
    main() 