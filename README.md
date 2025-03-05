# Hotel Review Sentiment Analysis

## Project Overview
This project focuses on analyzing hotel reviews to classify them into sentiment categories (negative, neutral, positive) using machine learning models. The goal is to improve customer experience by identifying trends in user feedback.

## Dataset
The dataset consists of hotel reviews labeled as negative, neutral, or positive. These labels serve as the ground truth for training and evaluating sentiment classification models.

## Models Used
1. **Logistic Regression**
2. **XGBoost**

## Model Performance

### Logistic Regression
- Precision: **0.73 (Negative), 0.33 (Neutral), 0.93 (Positive)**
- Recall: **0.78 (Negative), 0.39 (Neutral), 0.89 (Positive)**
- F1-score: **0.76 (Negative), 0.36 (Neutral), 0.91 (Positive)**
- Accuracy: **0.82**

### XGBoost
- Precision: **0.74 (Class 0), 0.32 (Class 1), 0.87 (Class 2)**
- Recall: **0.67 (Class 0), 0.26 (Class 1), 0.92 (Class 2)**
- F1-score: **0.70 (Class 0), 0.29 (Class 1), 0.89 (Class 2)**
- Accuracy: **0.81**

## Dependencies
To run this project, install the required dependencies using:
```bash
pip install -r requirements.txt
```

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/nba26/hotel-reviews.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hotel-reviews
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook HotelReviewsAnalysis.ipynb
   ```

## Conclusion
Logistic Regression achieved slightly higher accuracy (82%) compared to XGBoost (81%). However, XGBoost performed better in classifying the positive sentiment category, while Logistic Regression showed a better balance across all categories. This analysis helps in understanding customer sentiments and can aid hotels in improving their services.

