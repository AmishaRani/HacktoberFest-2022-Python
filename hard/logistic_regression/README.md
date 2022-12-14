# Hacktoberfest 2022

## Logistic Regression

### Problem Statement

Logistic regression is a supervised machine learning algorithm that is used to predict the value of a categorical variable (y) based on the value of another variable (x). It is used to find the relationship between variables by fitting a logistic equation to observed data. In other words, it is used to find the best fit line for the given data. Create a class called `LogisticRegression` that has the following methods:

- `fit(X, y)`: Fit the model on the training data.
- `predict(X)`: Predict the target variable on the given data.
- `score(X, y)`: Return the score of the model on the given data.

### Input Format

The `fit` method takes the following arguments:

- `X`: The features.
- `y`: The target variable.

The `predict` method takes the following arguments:

- `X`: The features.

The `score` method takes the following arguments:

- `X`: The features.
- `y`: The target variable.

### Output Format

The `fit` method returns the model object.
The `predict` method returns the predicted values.
The `score` method returns the score of the model.

### Example

```python
from solution import LogisticRegression

# Load the data
data = pd.read_csv('data.csv')

# Split the data into features and target
X = data.drop('target', axis=1)

y = data['target']

# Create an instance of the model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X, y)

# Predict the target variable on the given data
y_pred = model.predict(X)

# Return the score of the model on the given data
score = model.score(X, y)
```

### Rules

- Implement the class in `solution.py`.
- The class should have the following methods:
    - `fit(X, y)`: Fit the model on the training data.
    - `predict(X)`: Predict the target variable on the given data.
    - `score(X, y)`: Return the score of the model on the given data.

- The `fit` method should take the following arguments:
    - `X`: The features.
    - `y`: The target variable.

- The `predict` method should take the following arguments:
    - `X`: The features.

- The `score` method should take the following arguments:
    - `X`: The features.
    - `y`: The target variable.

## Acknowledgments
- [Python](https://www.python.org/)
- [Hacktoberfest](https://hacktoberfest.digitalocean.com/)
- [GitHub](https://github.com)
- [Git](https://git-scm.com/)

## Maintainer
- [Anamaya](https://www.linkedin.com/in/anamaya1729/)
- [Kartik](https://github.com/kartik007007)
- [Shantanu](https://github.com/neutralWire)
- [Shailesh](https://github.com/ShaileshKumar007)

## License
**This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](../../LICENSE) file for details**

## Happy Coding! :smile: :tada: