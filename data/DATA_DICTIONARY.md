# Data Dictionary - Netflix Business Analytics Project

## Dataset Overview
This document describes all variables and data fields used in the Netflix Business Analytics Project.

---

## Netflix Titles Dataset

### Column Definitions

| Column Name | Data Type | Description | Example |
|---|---|---|---|
| show_id | String | Unique identifier for each title | s1 |
| type | String | Content type (Movie or TV Show) | Movie, TV Show |
| title | String | Name of the content | Breaking Bad |
| director | String | Director(s) of the content | Vince Gilligan |
| cast | String | Main actors/cast members | Bryan Cranston, Aaron Paul |
| country | String | Country/countries of origin | United States |
| date_added | Date | Date content was added to Netflix | July 15, 2019 |
| release_year | Integer | Year the content was released | 2008 |
| rating | String | Content rating (PG, R, TV-MA, etc.) | TV-MA |
| duration | String | Duration in minutes (movies) or seasons (TV) | 120 min, 5 Seasons |
| listed_in | String | Genre categories | Drama, Crime, Thriller |
| description | String | Brief plot description | A high school chemistry teacher... |
| imdb_score | Float | IMDb rating (0-10) | 9.5 |
| tmdb_popularity | Float | TMDb popularity score | 183.91 |

## Key Metrics

### Derived Variables
- **Content_Age**: Years since release (release_year - current_year)
- **Days_On_Platform**: Days since date_added to current date
- **Genre_Count**: Number of genres per title
- **Cast_Size**: Number of actors listed

## Data Quality Notes

- Missing values in `director` and `cast` indicate single-person credits
- IMDb scores range from 0-10 with higher indicating better quality
- Duration format differs between Movies (minutes) and TV Shows (seasons)
- Some international titles may have multiple countries listed (comma-separated)
