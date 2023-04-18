<h2>Project Title</h2>
<p>Random Forest Classifier Project</p>
<h1>Project Description</h1>
  <p>I prepared a classification problem. I used data about local restaurants in Warsaw and based on some variables such as: variables such as votes, score, popularity, max delivery time, discounts, delivery, pickup, the model aim is to predict the cuisine type. A complete lack of normal distribution made me decide to build a classification model so I used random forest classifier. Also, I used streamlit package to present my visualisations.</p>
  <h2>The Steps I Took:</h2>
  <ol>
    <li>Gathered data via pyszne.pl api and Postman API Platform (import_requests.py file)</li>
    <li>Data Cleaning and Preprocessing (random_forest_classifier.ipynb file)</li>
    <li>Cleaned data are in df_cleaned.csv df_cleaned.xlsx</li>
    <li>Data visualization</li>
    <li>Statistics (variables distribution, correlation)</li>
    <li>Decide on what model to use</li>
    <li>Model preparation and evaluation</li>
  </ol>
</body>
</html>
<h2>Files</h2>
<ul>
<li><code>README.md</code>: This file, containing information about the project</li>
<li><code>df_cleaned.csv</code>: Cleaned dataset in CSV format</li>
<li><code>df_cleaned.xlsx</code>: Cleaned dataset in Excel format</li>
<li><code>import_requests.py</code>: Python script for importing data using requests</li>
<li><code>random_forest_classifier.ipynb</code>: Jupyter notebook containing the data analysis and model building</li>
<li><code>response.json</code>: Response data in JSON format</li>
<li><code>restaurants_dummies_by_score.csv</code>: Dummy variables dataset based on the score in CSV format</li>
<li><code>restaurants_dummies_nolunch.csv</code>: Dummy variables dataset without the lunch feature in CSV format</li>
<li><code>restaurants_dummies_nolunch_withscore_row_norm.csv</code>: Dummy variables dataset without the lunch feature, with the score feature normalized row-wise, in CSV format</li>
<li><code>streamlit.py</code>: Python script for creating a Streamlit dashboard</li>

<h2>Requirements</h2>

<p>To run the Jupyter notebook and Streamlit dashboard, the following packages are required:</p>
<h2>Requirements</h2>
<p>To run the Jupyter notebook and Streamlit dashboard, the following packages are required:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>matplotlib</li>
<li>seaborn</li>
<li>scikit-learn</li>
<li>streamlit</li>
</ul>
<p>To import data using requests, the requests package is also required.</p>
<h2>Usage</h2>
<p>To run the Jupyter notebook, open <code>projekt_glowny_notebook.ipynb</code> in Jupyter and run each cell in order.</p>
<p>To run the Streamlit dashboard, run <code>streamlit run streamlit.py</code> in the command line while in the project directory.</p>

<h2>Results<h2>
 The model achieved an accuracy score of 0.72, which is a good result considering the complexity of the problem and the limited number of variables used.

<h2>Future Work<h2>
  Future work could involve:

<ul> <li>Collecting more data to improve the accuracy of the model</li> <li>Trying out different algorithms to compare their performance with the random forest classifier</li> <li>Adding more variables to the model to improve its accuracy</li> </ul>

<h2>Conclusion<h2>

  In this project, I was able to successfully build a classification model using the random forest classifier algorithm to predict the cuisine type of local restaurants in Warsaw. The model achieved a good accuracy score and the visualizations provided insights into the data. This project has demonstrated the usefulness and versatility of the random forest classifier algorithm in classification problems.

<h2>Contributors</h2>
<ul>
<li>Laura Starzomska</li>
<li>[Insert name and contact information of other contributors, if applicable]</li>
</ul>
<h2>License</h2>
<p>[Insert license information here]</p>
