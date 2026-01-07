# Netflix Business Analytics Project - Quick Start Guide

## 🎯 Project Structure

This repository follows a professional business analytics project structure:

```
Netflix-Business-Analytics-Project/
├── README.md                    # Main project documentation
├── QUICK_START_GUIDE.md        # This file - setup instructions
├── data/
│   ├── DATA_DICTIONARY.md      # Dataset variable definitions
│   ├── netflix_titles.csv      # Netflix content dataset
│   └── ratings_data.csv        # IMDb & Rotten Tomatoes ratings
├── notebooks/
│   ├── 01_EDA_Analysis.ipynb          # Exploratory Data Analysis
│   ├── 02_Correlation_Analysis.ipynb  # Ratings correlation study
│   ├── 03_Predictive_Modeling.ipynb   # Regression & Classification
│   └── 04_TimeSeries_Forecasting.ipynb # Financial forecasting
├── scripts/
│   ├── data_cleaning.py        # Data preprocessing functions
│   ├── eda_functions.py        # EDA utility functions
│   ├── modeling.py             # ML model implementations
│   └── visualization.py        # Plotting utilities
├── outputs/
│   ├── figures/
│   │   ├── content_distribution.png
│   │   ├── rating_correlation.png
│   │   ├── forecast_analysis.png
│   │   └── segmentation_clusters.png
│   └── results/
│       ├── model_performance.csv
│       ├── key_insights.txt
│       └── business_recommendations.md
└── report/
    ├── ANALYSIS_REPORT.md      # Comprehensive findings
    └── BUSINESS_RECOMMENDATIONS.md
```

## 📊 Key Analyses Performed

### 1. Exploratory Data Analysis (EDA)
- **Content Distribution**: Movies vs TV Shows breakdown
- **Release Year Trends**: Content acquisition patterns over time
- **Geographic Analysis**: Country of origin distribution
- **Rating Analysis**: IMDb scores and Rotten Tomatoes ratings

### 2. Correlation Analysis
- **IMDb vs Rotten Tomatoes**: Correlation coefficient = 0.87
- **Duration Impact**: Relationship between length and ratings
- **Genre Performance**: Which genres receive highest ratings?

### 3. Predictive Modeling
- **Regression Models**: Predict ratings based on content features
- **K-Nearest Neighbors (KNN)**: Content classification
- **Feature Importance**: Identify key rating drivers

### 4. Time Series Forecasting
- **Revenue Projections**: Using ARIMA models
- **Growth Trends**: Long-term subscription patterns
- **Seasonal Patterns**: Identify cyclical trends

## 🔑 Key Findings

- **Content Mix**: 69% movies, 31% TV shows
- **Quality Metrics**: Strong correlation between IMDb and Rotten Tomatoes
- **Market Leaders**: US, India, and UK are top content producers
- **Subscription Tiers**: Basic plan most popular (45% of subscribers)

## 💡 Business Recommendations

1. **Content Investment**: Allocate 35% more budget to high-rating genres
2. **Regional Strategy**: Customize content by geographic market
3. **Pricing Optimization**: Implement dynamic pricing based on subscriber segments
4. **Expansion Focus**: Target emerging markets with proven content preferences

## 🛠️ Technologies Used

- **Python 3.9+** - Data processing and analysis
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning models
- **Matplotlib & Seaborn** - Data visualization
- **Statsmodels** - Time series analysis

## 📖 How to Use This Project

1. **Review the Analysis**: Start with the notebooks in order (01 → 04)
2. **Check Data**: Review `data/DATA_DICTIONARY.md` for variable definitions
3. **Run Scripts**: Execute analysis scripts from `scripts/` folder
4. **View Results**: Check `outputs/figures/` for visualizations
5. **Read Report**: Review comprehensive findings in `report/ANALYSIS_REPORT.md`

## 📝 Project Status

✅ Data collection and cleaning completed
✅ EDA and statistical analysis completed
✅ Predictive models trained and evaluated
✅ Business recommendations formulated
✅ Documentation finalized

## 🤝 Author

**Vinisha Biju**
- MSc Business Analytics, Oxford Brookes University
- Email: vinisha.biju25@gmail.com
- LinkedIn: [linkedin.com/in/vinishabiju](https://linkedin.com/in/vinishabiju)
- Portfolio: [github.com/VinishaBiju](https://github.com/VinishaBiju)

---

**Last Updated**: January 2026
**Project Duration**: 3 months
**Status**: Complete
