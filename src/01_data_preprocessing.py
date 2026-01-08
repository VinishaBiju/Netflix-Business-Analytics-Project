"""
Netflix Data Preprocessing and Cleaning
==========================================
Author: Vinisha Biju
Project: Netflix Business Analytics
Description: Comprehensive data cleaning, preprocessing, and feature engineering for Netflix dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

class NetflixDataPreprocessor:
    """
    Comprehensive data preprocessing pipeline for Netflix analytics
    """
    
    def __init__(self, filepath):
        """
        Initialize the preprocessor with data file path
        
        Parameters:
        -----------
        filepath : str
            Path to the Netflix dataset CSV file
        """
        self.filepath = filepath
        self.df = None
        self.original_shape = None
        
    def load_data(self):
        """
        Load Netflix dataset from CSV file
        """
        print("Loading Netflix dataset...")
        self.df = pd.read_csv(self.filepath)
        self.original_shape = self.df.shape
        print(f"Data loaded successfully: {self.original_shape[0]} rows, {self.original_shape[1]} columns")
        return self
    
    def explore_data(self):
        """
        Perform initial data exploration
        """
        print("\n" + "="*80)
        print("DATA EXPLORATION SUMMARY")
        print("="*80)
        
        print("\nDataset Info:")
        print(self.df.info())
        
        print("\nFirst 5 rows:")
        print(self.df.head())
        
        print("\nStatistical Summary:")
        print(self.df.describe())
        
        print("\nMissing Values:")
        missing = self.df.isnull().sum()
        missing_pct = (missing / len(self.df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Percentage': missing_pct
        }).sort_values('Missing Count', ascending=False)
        print(missing_df[missing_df['Missing Count'] > 0])
        
        return self
    
    def handle_missing_values(self):
        """
        Handle missing values in the dataset
        """
        print("\nHandling missing values...")
        
        # Fill missing directors with 'Unknown Director'
        if 'director' in self.df.columns:
            self.df['director'].fillna('Unknown Director', inplace=True)
        
        # Fill missing cast with 'Unknown Cast'
        if 'cast' in self.df.columns:
            self.df['cast'].fillna('Unknown Cast', inplace=True)
        
        # Fill missing country with 'Unknown Country'
        if 'country' in self.df.columns:
            self.df['country'].fillna('Unknown Country', inplace=True)
        
        # Fill missing date_added with mode
        if 'date_added' in self.df.columns:
            mode_date = self.df['date_added'].mode()[0] if not self.df['date_added'].mode().empty else 'Unknown'
            self.df['date_added'].fillna(mode_date, inplace=True)
        
        # Fill missing rating with 'Not Rated'
        if 'rating' in self.df.columns:
            self.df['rating'].fillna('Not Rated', inplace=True)
        
        # Drop rows with missing critical information
        critical_cols = ['type', 'title']
        for col in critical_cols:
            if col in self.df.columns:
                self.df.dropna(subset=[col], inplace=True)
        
        print(f"Missing values handled. New shape: {self.df.shape}")
        return self
    
    def feature_engineering(self):
        """
        Create new features from existing data
        """
        print("\nPerforming feature engineering...")
        
        # Extract year added
        if 'date_added' in self.df.columns:
            try:
                self.df['date_added_clean'] = pd.to_datetime(self.df['date_added'], errors='coerce')
                self.df['year_added'] = self.df['date_added_clean'].dt.year
                self.df['month_added'] = self.df['date_added_clean'].dt.month
                self.df['day_of_week_added'] = self.df['date_added_clean'].dt.dayofweek
            except:
                print("Warning: Could not parse date_added column")
        
        # Create duration in minutes for movies
        if 'duration' in self.df.columns and 'type' in self.df.columns:
            self.df['duration_value'] = self.df['duration'].str.extract('(\d+)').astype(float)
            self.df['duration_type'] = self.df['duration'].str.extract('([a-zA-Z]+)')
            
            # Convert to minutes
            self.df['duration_minutes'] = self.df.apply(
                lambda row: row['duration_value'] if row['type'] == 'Movie' else row['duration_value'] * 45,
                axis=1
            )
        
        # Count number of countries
        if 'country' in self.df.columns:
            self.df['num_countries'] = self.df['country'].apply(
                lambda x: len(str(x).split(',')) if pd.notna(x) else 0
            )
            self.df['primary_country'] = self.df['country'].apply(
                lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Unknown'
            )
        
        # Count number of genres/categories
        if 'listed_in' in self.df.columns:
            self.df['num_genres'] = self.df['listed_in'].apply(
                lambda x: len(str(x).split(',')) if pd.notna(x) else 0
            )
            self.df['primary_genre'] = self.df['listed_in'].apply(
                lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Unknown'
            )
        
        # Count cast members
        if 'cast' in self.df.columns:
            self.df['num_cast'] = self.df['cast'].apply(
                lambda x: len(str(x).split(',')) if pd.notna(x) and x != 'Unknown Cast' else 0
            )
        
        # Calculate content age (years since release)
        if 'release_year' in self.df.columns:
            current_year = datetime.now().year
            self.df['content_age_years'] = current_year - self.df['release_year']
        
        # Create decade feature
        if 'release_year' in self.df.columns:
            self.df['release_decade'] = (self.df['release_year'] // 10) * 10
        
        # Binary encoding for content type
        if 'type' in self.df.columns:
            self.df['is_movie'] = (self.df['type'] == 'Movie').astype(int)
            self.df['is_tv_show'] = (self.df['type'] == 'TV Show').astype(int)
        
        # Create mature content flag based on rating
        if 'rating' in self.df.columns:
            mature_ratings = ['R', 'NC-17', 'TV-MA', 'TV-14']
            self.df['is_mature'] = self.df['rating'].isin(mature_ratings).astype(int)
        
        print(f"Feature engineering completed. New shape: {self.df.shape}")
        return self
    
    def remove_duplicates(self):
        """
        Remove duplicate entries
        """
        print("\nRemoving duplicates...")
        before = len(self.df)
        self.df.drop_duplicates(subset=['title', 'type', 'release_year'], keep='first', inplace=True)
        after = len(self.df)
        print(f"Removed {before - after} duplicate entries")
        return self
    
    def data_validation(self):
        """
        Validate data quality
        """
        print("\nPerforming data validation...")
        
        issues = []
        
        # Check for negative release years
        if 'release_year' in self.df.columns:
            invalid_years = self.df[self.df['release_year'] < 1900]
            if len(invalid_years) > 0:
                issues.append(f"Found {len(invalid_years)} entries with invalid release years")
        
        # Check for future release years
        if 'release_year' in self.df.columns:
            future_years = self.df[self.df['release_year'] > datetime.now().year]
            if len(future_years) > 0:
                issues.append(f"Found {len(future_years)} entries with future release years")
        
        # Check for invalid durations
        if 'duration_minutes' in self.df.columns:
            invalid_duration = self.df[self.df['duration_minutes'] <= 0]
            if len(invalid_duration) > 0:
                issues.append(f"Found {len(invalid_duration)} entries with invalid durations")
        
        if issues:
            print("Data quality issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✓ All data quality checks passed")
        
        return self
    
    def save_processed_data(self, output_path='data/netflix_processed.csv'):
        """
        Save the processed dataset
        
        Parameters:
        -----------
        output_path : str
            Path to save the processed data
        """
        print(f"\nSaving processed data to {output_path}...")
        self.df.to_csv(output_path, index=False)
        print(f"✓ Data saved successfully")
        print(f"Final dataset shape: {self.df.shape}")
        return self
    
    def generate_preprocessing_report(self):
        """
        Generate a comprehensive preprocessing report
        """
        print("\n" + "="*80)
        print("PREPROCESSING SUMMARY REPORT")
        print("="*80)
        
        report = {
            'Original Rows': self.original_shape[0],
            'Original Columns': self.original_shape[1],
            'Final Rows': self.df.shape[0],
            'Final Columns': self.df.shape[1],
            'Rows Removed': self.original_shape[0] - self.df.shape[0],
            'Columns Added': self.df.shape[1] - self.original_shape[1],
            'Missing Values Remaining': self.df.isnull().sum().sum()
        }
        
        for key, value in report.items():
            print(f"{key}: {value}")
        
        print("\nNew Features Created:")
        new_features = [
            'year_added', 'month_added', 'day_of_week_added',
            'duration_minutes', 'num_countries', 'primary_country',
            'num_genres', 'primary_genre', 'num_cast',
            'content_age_years', 'release_decade',
            'is_movie', 'is_tv_show', 'is_mature'
        ]
        
        existing_features = [f for f in new_features if f in self.df.columns]
        for feature in existing_features:
            print(f"  ✓ {feature}")
        
        return report

# Main execution
if __name__ == "__main__":
    print("\n" + "#"*80)
    print("# Netflix Data Preprocessing Pipeline")
    print("#"*80 + "\n")
    
    # Initialize preprocessor
    preprocessor = NetflixDataPreprocessor('data/netflix_titles.csv')
    
    # Execute preprocessing pipeline
    (preprocessor
     .load_data()
     .explore_data()
     .handle_missing_values()
     .remove_duplicates()
     .feature_engineering()
     .data_validation()
     .save_processed_data()
     .generate_preprocessing_report())
    
    print("\n✓ Preprocessing pipeline completed successfully!\n")
