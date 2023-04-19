

# Random Forest Classifier Project

I prepared a classification problem using data about local restaurants in Warsaw and based on some variables such as: variables such as votes, score, popularity, max delivery time, discounts, delivery, pickup, the model aims to predict the cuisine type. A complete lack of normal distribution made me decide to build a classification model so I used random forest classifier. Also, I used streamlit package to present my visualisations.

## The Steps I Took:

1. Gathered data via pyszne.pl api and Postman API Platform (`import_requests.py` file)
2. Data Cleaning and Preprocessing (`random_forest_classifier.ipynb` file)
3. Cleaned data are in `df_cleaned.csv` and `df_cleaned.xlsx`
4. Data visualization
5. Statistics (variables distribution, correlations etc.)
6. Decide on what model to use
7. Model preparation and evaluation

## Files

- `README.md`: This file, containing information about the project
- `df_cleaned.csv`: Cleaned dataset in CSV format
- `df_cleaned.xlsx`: Cleaned dataset in Excel format
- `import_requests.py`: Python script for importing data using requests
- `random_forest_classifier.ipynb`: Jupyter notebook containing the data analysis and model building
- `response.json`: Response data in JSON format
- `restaurants_dummies_by_score.csv`: Dummy variables dataset based on the score in CSV format
- `restaurants_dummies_nolunch.csv`: Dummy variables dataset without the lunch feature in CSV format
- `restaurants_dummies_nolunch_withscore_row_norm.csv`: Dummy variables dataset without the lunch feature, with the score feature normalized row-wise, in CSV format
- `streamlit.py`: Python script for creating a Streamlit dashboard

## Requirements

To run the Jupyter notebook and Streamlit dashboard, the following packages are required:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- streamlit
- json
- missingno
- plotly
- folium
- scipy, stats
- statsmodels
- sklearn


To import data using requests, the requests package is also required.

## Usage

To run the Jupyter notebook, open `random_forest_classifier.ipynb` in Jupyter and run each cell in order.

To run the Streamlit dashboard, run `streamlit run streamlit.py` in the command line while in the project directory.

## Results

The model achieved an accuracy score of 0.15, which isn't a satisfying result.

## Future Work

Future work could involve:

- Collecting more data to improve the accuracy of the model
- Trying out different algorithms to compare their performance with the random forest classifier
- Adding more variables to the model to improve its accuracy

## Conclusion

In this project, I was able to successfully build a classification model using the random forest classifier algorithm to predict the cuisine type of local restaurants in Warsaw. The model unfortunately achieved a bad accuracy score. The visualizations provided insights into the data. This project has demonstrated the usefulness and versatility of the random forest classifier algorithm in classification problems.

## Contributors
- Laura Starzomska
