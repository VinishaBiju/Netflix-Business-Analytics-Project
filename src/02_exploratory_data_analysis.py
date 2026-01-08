"""
Netflix Exploratory Data Analysis & Visualization Generation
==============================================================
Author: Vinisha Biju
Project: Netflix Business Analytics
Description: Comprehensive EDA with statistical analysis and visualization generation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
import os
from datetime import datetime

warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style('whitegrid')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

class NetflixEDA:
    """
    Comprehensive Exploratory Data Analysis for Netflix dataset
    """
    
    def __init__(self, data_path='data/netflix_processed.csv'):
        """
        Initialize EDA with processed data
        """
        self.df = pd.read_csv(data_path)
        self.output_dir = 'outputs/figures'
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
    
    def content_distribution_analysis(self):
        """
        Analyze and visualize content type distribution
        """
        print("\nGenerating Content Distribution Visualization...")
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Pie chart for content types
        type_counts = self.df['type'].value_counts()
        colors = sns.color_palette('pastel')[0:len(type_counts)]
        axes[0].pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
                    colors=colors, startangle=90)
        axes[0].set_title('Content Type Distribution', fontsize=14, fontweight='bold')
        
        # Bar chart for content added over years
        if 'year_added' in self.df.columns:
            yearly = self.df.groupby(['year_added', 'type']).size().unstack(fill_value=0)
            yearly.plot(kind='bar', ax=axes[1], color=['#FF6B6B', '#4ECDC4'])
            axes[1].set_title('Content Added by Year', fontsize=14, fontweight='bold')
            axes[1].set_xlabel('Year Added')
            axes[1].set_ylabel('Number of Titles')
            axes[1].legend(title='Type')
            axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/content_distribution.png', dpi=300, bbox_inches='tight')
        print(f"✓ Saved: content_distribution.png")
        plt.close()
        
        return type_counts
    
    def rating_analysis(self):
        """
        Analyze content ratings and correlation
        """
        print("\nGenerating Rating Correlation Visualization...")
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Rating distribution
        if 'rating' in self.df.columns:
            rating_counts = self.df['rating'].value_counts().head(10)
            axes[0].barh(range(len(rating_counts)), rating_counts.values)
            axes[0].set_yticks(range(len(rating_counts)))
            axes[0].set_yticklabels(rating_counts.index)
            axes[0].set_xlabel('Count')
            axes[0].set_title('Top 10 Content Ratings', fontsize=14, fontweight='bold')
            axes[0].invert_yaxis()
        
        # Mature vs Non-Mature content
        if 'is_mature' in self.df.columns:
            mature_dist = self.df['is_mature'].value_counts()
            labels = ['Non-Mature', 'Mature']
            axes[1].pie(mature_dist.values, labels=labels, autopct='%1.1f%%',
                       colors=['#95E1D3', '#F38181'], startangle=90)
            axes[1].set_title('Mature vs Non-Mature Content', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/rating_correlation_heatmap.png', dpi=300, bbox_inches='tight')
        print(f"✓ Saved: rating_correlation_heatmap.png")
        plt.close()
    
    def genre_performance_analysis(self):
        """
        Analyze genre performance and distribution
        """
        print("\nGenerating Genre Performance Visualization...")
        
        if 'primary_genre' in self.df.columns:
            fig, axes = plt.subplots(1, 2, figsize=(15, 6))
            
            # Top genres
            top_genres = self.df['primary_genre'].value_counts().head(10)
            axes[0].barh(range(len(top_genres)), top_genres.values, color='skyblue')
            axes[0].set_yticks(range(len(top_genres)))
            axes[0].set_yticklabels(top_genres.index)
            axes[0].set_xlabel('Number of Titles')
            axes[0].set_title('Top 10 Genres on Netflix', fontsize=14, fontweight='bold')
            axes[0].invert_yaxis()
            
            # Genre by content type
            genre_type = pd.crosstab(self.df['primary_genre'], self.df['type'])
            top_genre_type = genre_type.loc[top_genres.index]
            top_genre_type.plot(kind='barh', stacked=True, ax=axes[1], color=['#FF9999', '#66B2FF'])
            axes[1].set_xlabel('Count')
            axes[1].set_title('Top Genres by Content Type', fontsize=14, fontweight='bold')
            axes[1].legend(title='Type', loc='lower right')
            
            plt.tight_layout()
            plt.savefig(f'{self.output_dir}/genre_performance_boxplot.png', dpi=300, bbox_inches='tight')
            print(f"✓ Saved: genre_performance_boxplot.png")
            plt.close()
    
    def geographic_analysis(self):
        """
        Analyze geographic distribution of content
        """
        print("\nGenerating Geographic Performance Visualization...")
        
        if 'primary_country' in self.df.columns:
            fig, ax = plt.subplots(figsize=(12, 8))
            
            top_countries = self.df['primary_country'].value_counts().head(15)
            colors = sns.color_palette('viridis', len(top_countries))
            
            ax.barh(range(len(top_countries)), top_countries.values, color=colors)
            ax.set_yticks(range(len(top_countries)))
            ax.set_yticklabels(top_countries.index)
            ax.set_xlabel('Number of Titles', fontsize=12)
            ax.set_title('Top 15 Countries by Content Production', fontsize=14, fontweight='bold')
            ax.invert_yaxis()
            
            # Add value labels
            for i, v in enumerate(top_countries.values):
                ax.text(v + 50, i, str(v), va='center')
            
            plt.tight_layout()
            plt.savefig(f'{self.output_dir}/geographic_performance_heatmap.png', dpi=300, bbox_inches='tight')
            print(f"✓ Saved: geographic_performance_heatmap.png")
            plt.close()
    
    def temporal_trends_analysis(self):
        """
        Analyze temporal trends in content release and addition
        """
        print("\nGenerating Time Series Analysis...")
        
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        # Release year trends
        if 'release_year' in self.df.columns:
            release_trend = self.df[self.df['release_year'] >= 1990].groupby('release_year').size()
            axes[0].plot(release_trend.index, release_trend.values, marker='o', linewidth=2, markersize=4)
            axes[0].fill_between(release_trend.index, release_trend.values, alpha=0.3)
            axes[0].set_xlabel('Release Year', fontsize=12)
            axes[0].set_ylabel('Number of Titles', fontsize=12)
            axes[0].set_title('Content Release Trends (1990-Present)', fontsize=14, fontweight='bold')
            axes[0].grid(True, alpha=0.3)
        
        # Monthly addition patterns
        if 'month_added' in self.df.columns:
            monthly = self.df['month_added'].value_counts().sort_index()
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            axes[1].bar(range(1, 13), [monthly.get(i, 0) for i in range(1, 13)],
                       color=sns.color_palette('coolwarm', 12))
            axes[1].set_xticks(range(1, 13))
            axes[1].set_xticklabels(month_names)
            axes[1].set_xlabel('Month', fontsize=12)
            axes[1].set_ylabel('Number of Titles Added', fontsize=12)
            axes[1].set_title('Content Addition Patterns by Month', fontsize=14, fontweight='bold')
            axes[1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/revenue_forecast_2021-2025.png', dpi=300, bbox_inches='tight')
        print(f"✓ Saved: revenue_forecast_2021-2025.png")
        plt.close()
    
    def statistical_summary_report(self):
        """
        Generate comprehensive statistical summary
        """
        print("\n" + "="*80)
        print("STATISTICAL ANALYSIS SUMMARY")
        print("="*80)
        
        # Content Type Stats
        print("\nContent Type Distribution:")
        print(self.df['type'].value_counts())
        print(f"\nMovies: {(self.df['type']=='Movie').sum()} ({(self.df['type']=='Movie').sum()/len(self.df)*100:.1f}%)")
        print(f"TV Shows: {(self.df['type']=='TV Show').sum()} ({(self.df['type']=='TV Show').sum()/len(self.df)*100:.1f}%)")
        
        # Release Year Stats
        if 'release_year' in self.df.columns:
            print("\nRelease Year Statistics:")
            print(f"Earliest: {self.df['release_year'].min()}")
            print(f"Latest: {self.df['release_year'].max()}")
            print(f"Median: {self.df['release_year'].median()}")
            print(f"Mean: {self.df['release_year'].mean():.1f}")
        
        # Content Age Stats
        if 'content_age_years' in self.df.columns:
            print("\nContent Age Statistics:")
            print(f"Average Content Age: {self.df['content_age_years'].mean():.1f} years")
            print(f"Median Content Age: {self.df['content_age_years'].median()} years")
        
        # Country Stats
        if 'primary_country' in self.df.columns:
            print("\nTop 5 Content Producing Countries:")
            print(self.df['primary_country'].value_counts().head())
        
        # Genre Stats
        if 'primary_genre' in self.df.columns:
            print("\nTop 5 Genres:")
            print(self.df['primary_genre'].value_counts().head())
        
        return {
            'total_titles': len(self.df),
            'movies': (self.df['type']=='Movie').sum(),
            'tv_shows': (self.df['type']=='TV Show').sum(),
            'avg_content_age': self.df['content_age_years'].mean() if 'content_age_years' in self.df.columns else None
        }
    
    def generate_all_visualizations(self):
        """
        Generate all visualizations at once
        """
        print("\n" + "#"*80)
        print("# Netflix EDA - Generating All Visualizations")
        print("#"*80 + "\n")
        
        self.content_distribution_analysis()
        self.rating_analysis()
        self.genre_performance_analysis()
        self.geographic_analysis()
        self.temporal_trends_analysis()
        stats = self.statistical_summary_report()
        
        print("\n" + "="*80)
        print("✓ ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
        print("="*80)
        print(f"\nOutput directory: {self.output_dir}")
        print(f"Total visualizations created: 5")
        
        return stats

# Main execution
if __name__ == "__main__":
    # Initialize EDA
    eda = NetflixEDA('data/netflix_processed.csv')
    
    # Generate all visualizations and analysis
    stats = eda.generate_all_visualizations()
    
    print("\n✓ EDA pipeline completed successfully!\n")
