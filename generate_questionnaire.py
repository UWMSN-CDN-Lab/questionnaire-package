#!/usr/bin/env python3
"""
Command Line Interface for Questionnaire Module Generation

Usage:
    python generate_questionnaire.py config.json
    python generate_questionnaire.py --interactive
    python generate_questionnaire.py --example
"""

import argparse
import json
import sys
from pathlib import Path
from questionnaire_analysis.module_generator import generate_questionnaire_from_json

def create_example_config():
    """Create an example configuration file."""
    example_config = {
        "questionnaire_name": "SAMPLE",
        "full_name": "Sample Questionnaire",
        "description": "A sample questionnaire demonstrating the JSON configuration format",
        "prefix": "SAMPLE_",
        "items": {
            "total_items": 10,
            "item_range": [1, 10],
            "item_format": "SAMPLE_{:02d}"
        },
        "reverse_scoring": {
            "enabled": True,
            "items": [3, 7],
            "scale_max": 5,
            "formula": "scale_max + 1 - original_value"
        },
        "subscales": [
            {
                "name": "Positive_Subscale",
                "items": [1, 2, 4, 5, 8],
                "scoring_method": "mean",
                "description": "Measures positive aspects"
            },
            {
                "name": "Negative_Subscale",
                "items": [3, 6, 7, 9, 10],
                "scoring_method": "mean",
                "description": "Measures negative aspects"
            }
        ],
        "total_score": {
            "enabled": True,
            "method": "mean_of_subscales",
            "name": "Total_Score",
            "description": "Overall questionnaire score"
        },
        "validation": {
            "min_items_required": 8,
            "handle_missing": "skip_na",
            "error_on_insufficient_data": False
        },
        "output_columns": [
            "SAMPLE_Positive_Subscale",
            "SAMPLE_Negative_Subscale",
            "SAMPLE_Total_Score"
        ]
    }
    
    with open("sample_questionnaire_config.json", "w", encoding="utf-8") as f:
        json.dump(example_config, f, indent=2)
    
    print("Created sample_questionnaire_config.json")
    print("Edit this file with your questionnaire details, then run:")
    print("python generate_questionnaire.py sample_questionnaire_config.json")

def interactive_config_creation():
    """Create a configuration file interactively."""
    print("=== Interactive Questionnaire Configuration ===")
    
    # Basic information
    name = input("Questionnaire name (e.g., NEWQ): ").upper().strip()
    if not name:
        print("Error: Questionnaire name is required")
        return
    
    full_name = input(f"Full name (e.g., New Questionnaire): ").strip()
    if not full_name:
        full_name = f"{name} Questionnaire"
    
    description = input("Description: ").strip()
    if not description:
        description = f"Questionnaire module for {full_name}"
    
    prefix = f"{name}_"
    
    # Items
    try:
        total_items = int(input("Total number of items: "))
        if total_items <= 0:
            raise ValueError("Must be positive")
    except ValueError:
        print("Error: Please enter a valid positive number for total items")
        return
    
    # Reverse scoring
    reverse_enabled = input("Does this questionnaire have reverse-scored items? (y/n): ").lower().startswith('y')
    reverse_items = []
    scale_max = 5
    
    if reverse_enabled:
        try:
            scale_max = int(input("Scale maximum (e.g., 5 for 1-5 scale): "))
            reverse_input = input("Enter reverse-scored item numbers separated by commas (e.g., 3,7,12): ")
            if reverse_input.strip():
                reverse_items = [int(x.strip()) for x in reverse_input.split(',')]
        except ValueError:
            print("Error: Please enter valid numbers for reverse-scored items")
            return
    
    # Subscales
    subscales = []
    print(f"\n--- Subscales ---")
    print("Enter subscales (press Enter with empty name to finish)")
    
    while True:
        sub_name = input("Subscale name (or Enter to finish): ").strip()
        if not sub_name:
            break
        
        try:
            sub_items_input = input(f"Items for {sub_name} (comma-separated, e.g., 1,2,3,4): ")
            sub_items = [int(x.strip()) for x in sub_items_input.split(',') if x.strip()]
            
            if not sub_items:
                print("Warning: No items specified for this subscale, skipping...")
                continue
            
            scoring_method = input("Scoring method (mean/sum) [default: mean]: ").lower().strip()
            if scoring_method not in ['mean', 'sum']:
                scoring_method = 'mean'
            
            subscales.append({
                "name": sub_name,
                "items": sub_items,
                "scoring_method": scoring_method,
                "description": f"{sub_name} subscale"
            })
            
        except ValueError:
            print("Error: Please enter valid item numbers")
            continue
    
    if not subscales:
        print("Error: At least one subscale is required")
        return
    
    # Total score
    total_enabled = input("Calculate total score? (y/n): ").lower().startswith('y')
    
    # Build configuration
    config = {
        "questionnaire_name": name,
        "full_name": full_name,
        "description": description,
        "prefix": prefix,
        "items": {
            "total_items": total_items,
            "item_range": [1, total_items],
            "item_format": f"{prefix}{{:02d}}"
        },
        "reverse_scoring": {
            "enabled": reverse_enabled,
            "items": reverse_items,
            "scale_max": scale_max,
            "formula": "scale_max + 1 - original_value"
        },
        "subscales": subscales,
        "total_score": {
            "enabled": total_enabled,
            "method": "mean_of_subscales",
            "name": "Total_Score",
            "description": "Overall questionnaire score"
        },
        "validation": {
            "min_items_required": max(1, total_items - 2),
            "handle_missing": "skip_na",
            "error_on_insufficient_data": False
        },
        "output_columns": []
    }
    
    # Build output columns
    for subscale in subscales:
        config["output_columns"].append(f"{prefix}{subscale['name']}")
    
    if total_enabled:
        config["output_columns"].append(f"{prefix}Total_Score")
    
    # Save configuration
    config_filename = f"{name.lower()}_config.json"
    with open(config_filename, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    
    print(f"\n=== Configuration saved to {config_filename} ===")
    
    # Generate module
    generate_now = input("Generate module now? (y/n): ").lower().startswith('y')
    if generate_now:
        try:
            module_path = generate_questionnaire_from_json(config_filename)
            print(f"Successfully generated module: {module_path}")
        except Exception as e:
            print(f"Error generating module: {e}")

def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Generate questionnaire modules from JSON configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_questionnaire.py my_questionnaire.json
  python generate_questionnaire.py --interactive
  python generate_questionnaire.py --example
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("config_file", nargs="?", help="JSON configuration file")
    group.add_argument("--interactive", "-i", action="store_true", 
                      help="Create configuration interactively")
    group.add_argument("--example", "-e", action="store_true",
                      help="Create example configuration file")
    
    args = parser.parse_args()
    
    try:
        if args.example:
            create_example_config()
        elif args.interactive:
            interactive_config_creation()
        elif args.config_file:
            if not Path(args.config_file).exists():
                print(f"Error: Configuration file '{args.config_file}' not found")
                sys.exit(1)
            
            module_path = generate_questionnaire_from_json(args.config_file)
            print(f"Successfully generated module: {module_path}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

