
# Week 3 — Exploratory Data Analysis (Wine Quality Dataset)

**Dataset Source (UCI ML Repository):**  
- [Red Wine Quality](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)  
- [White Wine Quality](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv)

---

## What I Did
- Loaded the red & white wine datasets using **pandas**.
- Added a new `type` column to distinguish between red and white wines.
- Cheched duplicate rows and checked for missing values.
- Performed **Exploratory Data Analysis (EDA)** including:
  - Descriptive statistics
  - Histograms for quality, alcohol, sugar, acidity, and pH
  - Boxplots comparing red vs white wines
  - Correlation heatmap
  - Scatter plots (e.g., Alcohol vs Quality)

---

## Key Findings
- Wine **quality** ratings cluster around 5–6 (few very high or low ratings).
- **Alcohol** content shows a positive relationship with quality.
- **White wines** generally have higher residual sugar, while **red wines** have higher volatile acidity.
- **Residual sugar and density** are strongly correlated.
- Outliers exist in sugar and acidity — future modeling may need robust scaling.

---

## Files in this folder
- `Week3_WineQuality_EDA.ipynb` → Jupyter notebook with full EDA  
- `wine_quality_clean.csv` → Cleaned dataset with engineered features  
- `README.md` → This summary  

---

## How to Run
1. Clone this repo  
   ```bash
   git clone https://github.com/LuckyAV/mlcohort-wk2-web-scraping.git
   cd mlcohort-wk2-web-scraping/week3_eda_wine_quality
