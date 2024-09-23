
# Gurgaon Real Estate Price Prediction & Analytics Tool

This project is a comprehensive solution for predicting and analyzing real estate prices in Gurgaon. It leverages machine learning techniques and visualizations to provide accurate price predictions and insights.

## Features

- **Data Collection**: 
  - Scraped and curated real estate data for flats and houses in Gurgaon from [99acres.com](https://www.99acres.com/) for educational purpose only.
  
- **Data Preprocessing & Feature Engineering**:
  - Extensive cleaning and transformation of data to optimize model performance.
  - Applied feature engineering techniques to extract meaningful insights and improve prediction accuracy.

- **Exploratory Data Analysis (EDA)**:
  - Conducted univariate, bivariate, and multivariate analyses to explore the relationships between different features.
  - Visualized data distributions, correlations, and trends using scatter plots, pie charts, word clouds, and more.

- **Predictive Modeling**:
  - Developed multiple models including:
    - Linear Regression
    - Decision Trees
    - Random Forest (Achieved best performance with R² = 0.90 and Mean Absolute Error = ₹44,000)
    - XGBoost
  - Evaluated models based on key metrics to select the most accurate one for price prediction.

- **Analytics Dashboard**:
  - Designed an interactive dashboard using Streamlit, featuring:
    - **Geo-Map**: Visualizing price variations across different Gurgaon sectors.
    - **Dynamic Visualizations**: Including word clouds, scatter plots, pie charts, etc., for easy data exploration.
  
- **Recommender System**:
  - Implemented a two-level content-based recommendation system to suggest the top 5 properties to users based on their preferences.

- **Deployment**:
  - Deployed the model and dashboard using **Streamlit** and **AWS** for real-time access.
  - **Watch Live**: You can also check out the live version of the dashboard by clicking [here](http://3.89.162.248:8501/).

## Setup and Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MandarBhalerao/Gurgaon-Real-Estate-Price-Prediction.git
    cd Gurgaon-Real-Estate-Price-Prediction
    cd real-estate-app-master
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app locally:
    ```bash
    streamlit run Home.py
    ```

## Usage

Once the app is running, you can:

- Explore the **Geo-Map** to see pricing trends across different sectors in Gurgaon.
- Use the **Best Predictive Model** to estimate real estate prices.
- Get **property recommendations** based on your preferences.

## Model Performance

| Model              | R² Score | Mean Absolute Error (MAE) |
|--------------------|----------|---------------------------|
| Linear Regression   | 0.82     | ₹69 lakhs                |
| Decision Trees      | 0.82     | ₹59 lakhs                |
| Random Forest       | 0.90     | ₹44 lakhs                |
| XGBoost             | 0.89     | ₹50 lakhs                |

## Technologies Used

- **Python**: Core programming language.
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Scikit-learn**: For building and evaluating machine learning models.
- **Matplotlib & Seaborn**: For data visualization.
- **Streamlit**: For building the interactive dashboard.
- **AWS**: For deployment.

## Future Improvements

- Integrate user login and personalized recommendations.
- Expand data sources to include more real estate platforms.
- Optimize the recommendation algorithm for better performance.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
