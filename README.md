# Netflix Business Analytics Project

## Business Objective
Analyze Netflix content, user behavior, and financial trends to support content strategy, subscription optimization, and market expansion decisions.

## Data Sources
- Netflix titles dataset (movies & TV shows catalog)
- User demographics & subscription data
- IMDb & Rotten Tomatoes ratings
- Stock price & financial performance data

## Analysis Performed

### 🔹 Exploratory Data Analysis (EDA)
- Content distribution analysis (movies vs TV shows)
- Release year trends and acquisition patterns
- Content quality assessment through ratings correlations
- Geographic user distribution analysis

### 🔹 Predictive Modeling
- Regression models for content success prediction
- K-Nearest Neighbors (KNN) clustering for content segmentation
- Classification for subscription plan preferences
- Time series forecasting for financial performance

### 🔹 Advanced Analytics
- Correlation analysis between IMDb and Rotten Tomatoes scores
- User segmentation based on viewing patterns
- Churn prediction modeling
- Revenue forecasting using ARIMA and Exponential Smoothing

## Key Insights
- Content library skews heavily toward movies, with recent expansion into TV shows
- Strong correlation (0.87) between IMDb and Rotten Tomatoes ratings
- Basic plan is the most popular subscription tier with diverse demographics
- Geographic markets show distinct content preferences and engagement patterns
- Predictive models reveal actionable trends in subscription growth

## Business Recommendations

1. **Content Investment** - Optimize content budget allocation by region based on user engagement patterns
2. **Quality Strategy** - Leverage rating metrics for data-driven acquisition decisions
3. **Pricing Optimization** - Use segmentation analysis to refine subscription tier targeting
4. **Expansion Strategy** - Focus on high-growth markets identified through predictive modeling

## Tools Used
- **Python** - Pandas, NumPy, Scikit-learn
- **Visualization** - Matplotlib, Seaborn
- **Statistical Analysis** - Regression, Classification, Forecasting
- **Business Intelligence** - Trend analysis, KPI tracking

## Project Structure
```
Netflix-Business-Analytics-Project/
├── README.md
├── data/
│   └── Netflix_Dataset.pdf
├── notebooks/
│   └── analysis.ipynb
├── scripts/
│   └── code-netflix.pdf
├── outputs/
│   └── figures/
│       └── [visualizations]
└── report/
    └── netflix-report.pdf
```
