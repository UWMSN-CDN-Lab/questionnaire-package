"""
Questionnaire Module Generator

This module automatically generates questionnaire scoring modules from JSON configuration files.
It creates standardized Python modules that follow the package's existing patterns.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
import re

class QuestionnaireModuleGenerator:
    """
    Generates questionnaire modules from JSON configuration files.
    """
    
    def __init__(self, questionnaires_dir: str = None):
        """
        Initialize the generator.
        
        Args:
            questionnaires_dir: Directory where questionnaire modules are stored
        """
        if questionnaires_dir is None:
            self.questionnaires_dir = Path(__file__).parent / "questionnaires"
        else:
            self.questionnaires_dir = Path(questionnaires_dir)
    
    def load_config(self, json_path: str) -> Dict[str, Any]:
        """
        Load and validate JSON configuration file.
        
        Args:
            json_path: Path to JSON configuration file
            
        Returns:
            Parsed configuration dictionary
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Basic validation
            required_fields = ['questionnaire_name', 'prefix', 'items', 'subscales']
            for field in required_fields:
                if field not in config:
                    raise ValueError(f"Missing required field: {field}")
            
            return config
        except Exception as e:
            raise ValueError(f"Error loading configuration: {e}")
    
    def generate_reverse_scoring_code(self, config: Dict[str, Any]) -> str:
        """
        Generate reverse scoring function code.
        
        Args:
            config: Questionnaire configuration
            
        Returns:
            Generated Python code for reverse scoring
        """
        if not config.get('reverse_scoring', {}).get('enabled', False):
            return ""
        
        reverse_items = config['reverse_scoring']['items']
        scale_max = config['reverse_scoring'].get('scale_max', 5)
        prefix = config['prefix']
        name = config['questionnaire_name']
        
        items_list = [f"'{prefix}{item:02d}'" for item in reverse_items]
        items_str = ", ".join(items_list)
        
        code = f'''
def {name}_reverse_score(df):
    """
    Reverse score specific {name} items.
    Items to reverse: {reverse_items}
    """
    reverse_items = [{items_str}]
    for item in reverse_items:
        if item in df.columns:
            df[item] = pd.to_numeric(df[item], errors='coerce')
            df[item] = {scale_max + 1} - df[item]  # Reverse scoring
    return df
'''
        return code
    
    def generate_subscale_scoring_code(self, config: Dict[str, Any]) -> str:
        """
        Generate subscale scoring function code.
        
        Args:
            config: Questionnaire configuration
            
        Returns:
            Generated Python code for subscale scoring
        """
        prefix = config['prefix']
        name = config['questionnaire_name']
        subscales = config['subscales']
        
        # Build subscale calculations
        subscale_calcs = {}
        for subscale in subscales:
            items = [f"'{prefix}{item:02d}'" for item in subscale['items']]
            items_str = ", ".join(items)
            method = subscale['scoring_method']
            
            if method == 'mean':
                calc = f"df[[{items_str}]].mean(axis=1)"
            elif method == 'sum':
                calc = f"df[[{items_str}]].sum(axis=1)"
            else:
                calc = f"df[[{items_str}]].mean(axis=1)  # Default to mean"
            
            subscale_calcs[f"'{prefix}{subscale['name']}'"] = calc
        
        # Generate the function
        code = f'''
def {name}_calculate_scores(df):
    """
    Calculate subscale scores for the {config.get('full_name', name)} questionnaire.
    """
    # Apply reverse scoring if needed
'''
        
        if config.get('reverse_scoring', {}).get('enabled', False):
            code += f"    df = {name}_reverse_score(df)\n"
        
        code += '''
    # Convert all relevant columns to numeric
    for col in df.columns:
        if col.startswith('{prefix}'):
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Calculate all subscale scores at once to avoid DataFrame fragmentation
    subscale_scores = {{
'''.format(prefix=prefix)
        
        for col_name, calculation in subscale_calcs.items():
            code += f"        {col_name}: {calculation},\n"
        
        code += "    }\n    df = df.assign(**subscale_scores)\n"
        
        # Add total score if enabled
        if config.get('total_score', {}).get('enabled', False):
            total_method = config['total_score'].get('method', 'mean_of_subscales')
            total_name = config['total_score'].get('name', 'Total_Score')
            
            if total_method == 'mean_of_subscales':
                subscale_cols = [f"'{prefix}{sub['name']}'" for sub in subscales]
                subscale_cols_str = ", ".join(subscale_cols)
                code += f"    df['{prefix}{total_name}'] = df[[{subscale_cols_str}]].mean(axis=1)\n"
        
        code += "\n    return df\n"
        
        return code
    
    def generate_summarize_code(self, config: Dict[str, Any]) -> str:
        """
        Generate summarize results function code.
        
        Args:
            config: Questionnaire configuration
            
        Returns:
            Generated Python code for summarizing results
        """
        prefix = config['prefix']
        name = config['questionnaire_name']
        output_columns = config.get('output_columns', [])
        
        columns_str = ", ".join([f"'{col}'" for col in output_columns])
        
        code = f'''
def {name}_summarize_results(df):
    """
    Summarize the {config.get('full_name', name)} scores.
    """
    summary_columns = [{columns_str}]
    existing_columns = [col for col in summary_columns if col in df.columns]
    
    if not existing_columns:
        print("No {name} columns found for summary")
        return {{}}
    
    mean_scores = df[existing_columns].mean()
    std_scores = df[existing_columns].std()
    
    print("\\nSummary of {config.get('full_name', name)} Scores:")
    print(df[existing_columns])
    
    summary = {{}}
    for col in existing_columns:
        summary[f'Mean {{col}}'] = mean_scores[col]
        summary[f'Std Dev {{col}}'] = std_scores[col]
    
    return summary
'''
        return code
    
    def generate_main_function_code(self, config: Dict[str, Any]) -> str:
        """
        Generate main function code.
        
        Args:
            config: Questionnaire configuration
            
        Returns:
            Generated Python code for main function
        """
        name = config['questionnaire_name']
        output_columns = config.get('output_columns', [])
        columns_str = ", ".join([f"'{col}'" for col in output_columns])
        
        code = f'''
def main(df):
    """
    Main function to execute {config.get('full_name', name)} scoring.
    """
    if df is not None:
        # Calculate scores
        df = {name}_calculate_scores(df)
        
        # Summarize results (optional logging)
        summary = {name}_summarize_results(df)
        
        # Return only the summary columns for concatenation
        summary_columns = [{columns_str}]
        existing_columns = [col for col in summary_columns if col in df.columns]
        
        if existing_columns:
            return df[existing_columns]
        else:
            print(f"Warning: No {name} columns found in DataFrame")
            return None
    return None

if __name__ == "__main__":
    main()
'''
        return code
    
    def generate_module_code(self, config: Dict[str, Any]) -> str:
        """
        Generate complete module code.
        
        Args:
            config: Questionnaire configuration
            
        Returns:
            Complete Python module code
        """
        name = config['questionnaire_name']
        full_name = config.get('full_name', name)
        description = config.get('description', f'Auto-generated module for {full_name}')
        
        # Module header
        code = f'''"""
{full_name} Questionnaire Module

{description}

Auto-generated by QuestionnaireModuleGenerator
"""

import pandas as pd
'''
        
        # Add reverse scoring function
        code += self.generate_reverse_scoring_code(config)
        
        # Add scoring function
        code += self.generate_subscale_scoring_code(config)
        
        # Add summarize function
        code += self.generate_summarize_code(config)
        
        # Add main function
        code += self.generate_main_function_code(config)
        
        return code
    
    def generate_module(self, json_path: str, output_path: str = None) -> str:
        """
        Generate a complete questionnaire module from JSON configuration.
        
        Args:
            json_path: Path to JSON configuration file
            output_path: Optional output path for generated module
            
        Returns:
            Path to generated module file
        """
        # Load configuration
        config = self.load_config(json_path)
        
        # Generate module code
        module_code = self.generate_module_code(config)
        
        # Determine output path
        if output_path is None:
            module_name = f"{config['questionnaire_name']}.py"
            output_path = self.questionnaires_dir / module_name
        
        # Write module file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(module_code)
        
        print(f"Generated questionnaire module: {output_path}")
        return str(output_path)
    
    def update_package_imports(self, config: Dict[str, Any]):
        """
        Update package __init__.py files to include the new questionnaire.
        
        Args:
            config: Questionnaire configuration
        """
        name = config['questionnaire_name']
        prefix = config['prefix'].rstrip('_')
        
        # Update questionnaires/__init__.py
        init_path = self.questionnaires_dir / "__init__.py"
        
        if init_path.exists():
            with open(init_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add to __all__ list if it exists
            if '__all__' in content:
                # Find the __all__ list and add the new module
                all_pattern = r'__all__\s*=\s*\[(.*?)\]'
                match = re.search(all_pattern, content, re.DOTALL)
                if match:
                    current_items = match.group(1)
                    if f'"{name}"' not in current_items:
                        new_all = current_items.rstrip() + f',\n"{name}"'
                        content = re.sub(all_pattern, f'__all__ = [{new_all}]', content, flags=re.DOTALL)
            
            # Add import statement
            if f'from . import {name}' not in content:
                content += f'\nfrom . import {name}'
            
            with open(init_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # Update main common.py questionnaire_map
        common_path = self.questionnaires_dir.parent / "common.py"
        
        if common_path.exists():
            with open(common_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add to questionnaire_map
            map_pattern = r'questionnaire_map\s*=\s*\{(.*?)\}'
            match = re.search(map_pattern, content, re.DOTALL)
            if match:
                current_items = match.group(1)
                new_entry = f'"{prefix}_": {name}.main'
                if new_entry not in current_items:
                    # Clean up current items and ensure proper comma placement
                    current_items_clean = current_items.rstrip().rstrip(',')
                    new_map = current_items_clean + f',\n    {new_entry}'
                    content = re.sub(map_pattern, f'questionnaire_map = {{{new_map}\n}}', content, flags=re.DOTALL)
            
            # Add import if needed
            if f'{name},' not in content and f'{name} ' not in content:
                # Find the import section and add the new questionnaire
                import_pattern = r'from questionnaire_analysis\.questionnaires import \((.*?)\)'
                match = re.search(import_pattern, content, re.DOTALL)
                if match:
                    current_imports = match.group(1)
                    new_imports = current_imports.rstrip() + f', {name}'
                    content = re.sub(import_pattern, f'from questionnaire_analysis.questionnaires import ({new_imports})', content, flags=re.DOTALL)
            
            with open(common_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f"Updated package imports for {name}")


def generate_questionnaire_from_json(json_path: str, questionnaires_dir: str = None) -> str:
    """
    Convenience function to generate a questionnaire module from JSON.
    
    Args:
        json_path: Path to JSON configuration file
        questionnaires_dir: Directory for questionnaire modules
        
    Returns:
        Path to generated module
    """
    generator = QuestionnaireModuleGenerator(questionnaires_dir)
    module_path = generator.generate_module(json_path)
    
    # Load config to update imports
    config = generator.load_config(json_path)
    generator.update_package_imports(config)
    
    return module_path


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python module_generator.py <json_config_path>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    try:
        module_path = generate_questionnaire_from_json(json_path)
        print(f"Successfully generated module: {module_path}")
    except Exception as e:
        print(f"Error generating module: {e}")
        sys.exit(1)

