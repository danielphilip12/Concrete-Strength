# Concrete-Strength

## Problem Statement
- This dataset includes information about concrete strenth and the ingredients used to create the concrete. 

- The purpose of this analysis and modeling is to see which ingredients (and proportions) will create the best concrete.

## Data Dictionary

| Column Name | Description | Units |
|-------------|-------------| ----- |
Cement | component 1 | kg (number of kilograms of the component in a cubic meter of concrete)
Blast Furnace Slag | component 2 | kg (in a cubic meter of concrete)
Fly Ash | component 3 | kg (in a cubic meter of concrete)
Water | component 4 | kg (in a cubic meter of concrete)
Superplasticizer | component 5 | kg (in a cubic meter of concrete)
Coarse Aggregate | component 6 | kg (in a cubic meter of concrete)
Fine Aggregate | component 7 | kg (in a cubic meter of concrete)
Age | Age of concrete | Day (1~365)
Concrete compressive strength | Target variable | [MPa](https://www.sensorsone.com/mpa-megapascal-pressure-unit/)

## Executive Summary

### Data Cleaning Steps
The data included an unneccesary column (Unnamed: 32) which was dropped from the data. There was also around 379 missing values for Superplasticizer, which was filled in with 0s, as the missing values were clerical errors. 

Superplastizer Before
![superplasticizer before](./images/superplasticizer_before.png)

Superplastizer After
![superplasticizer after](./images/superplasticizer_after.png)

After filling in the missing values with 0s, we can see the effect that had on the distribution. 

The number of outliers reduced to just 2 and the bounds of what was considered an outlier also changed. 

### Key Visualizations

#### Visualization 1: [Cement vs Concrete Strength]
This visualization shows the affect the number of Cement kg per cubic meter in Concrete has on the strength of it. The correlation coefficent is 0.5, which is a moderate positive correlation. This means as the amount of cement increases, so does the strength. 

![Cement vs Concrete Strength](./images/cement_concrete.png)

#### Visualization 2: [Age vs Concrete Strength]
We see the same with Age and the strength of the concrete. It seems that over time, concrete gets stronger, as it has time to harden. 

However, we can also see that most of the values are in the early days of the concrete. On the far right of the plot, we see the strength going down, which likely happens after it completes hardening, and starts to deteriorate. 

![age vs concrete strength](./images/age_concrete.png)

## Conclusions/Recommendations
To model the algorithims to predict the strength of the concrete, I used Linear Regression (Ridge and Lasso as well), Random Forest, and K Nearest Neighbors (KNN).

I used GridSearchCV to cross validate the the models in order to get the best performing model to evaluate. 

Random Forest performed the best out of the 5. Results are below. 

| Model | R2 | RMSE |
| ----- | -- | ---- |
| Random Forest | 0.89 | 5.49 |
| KNN | 0.77 | 7.84 |
| Linear Regression | 0.625 | 10.08 |
| Ridge Regression | 0.625 | 10.08 |
| Lasso Regression | 0.625 | 10.08 |

For more information on the models and their parameters, please see the regression notebook. 

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.

---

Feel free to replace the placeholders with your actual content. Additionally, if you have images for your visualizations, make sure to replace the placeholder paths with the correct file paths or URLs.

Once you've filled in the content, save the file with a `.md` extension (e.g., `README.md`). You can use this Markdown file on platforms like GitHub to provide a well-structured README for your analysis.
