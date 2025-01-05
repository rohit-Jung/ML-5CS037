# Linear Regression

In classical linear regression, the goal is to find the best-fitting line for a given dataset, so that the line represents the relationship between the independent variable(s) (input features) and the dependent variable (target variable).

## 1. Model Setup

For a single feature (univariate linear regression), the model assumes that the relationship between the input feature \( x \) and the output \( y \) is linear:

$$
y = w \cdot x + b
$$

Where:

- \( y \) is the target variable (output).
- \( x \) is the input feature (independent variable).
- \( w \) is the weight (slope of the line).
- \( b \) is the bias (intercept of the line).

For multiple features (multivariate linear regression), the model becomes:

$$
y = w_1 \cdot x_1 + w_2 \cdot x_2 + \dots + w_n \cdot x_n + b
$$

Where:

- \( x_1, x_2, \dots, x_n \) are the input features.
- \( w_1, w_2, \dots, w_n \) are the weights (coefficients) corresponding to each feature.
- \( b \) is the bias term.

## 2. Objective

The goal of linear regression is to find the values of the weights \( w \) and the bias \( b \) that minimize the difference between the predicted values \( \hat{y} \) and the true values \( y \) in the training data.

## 3. Cost Function (Mean Squared Error)

We need a **cost function** that measures the difference between the predicted values \( \hat{y} \) and the actual values \( y \). The most commonly used cost function for linear regression is the **Mean Squared Error (MSE)**:

$$
\text{MSE}(w, b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Where:

- \( n \) is the number of training examples.
- \( y_i \) is the actual value of the target variable for the \( i^{th} \) sample.
- \( \hat{y}\_i = w \cdot x_i + b \) is the predicted value for the \( i^{th} \) sample.

## 4. Goal: Minimize the Cost Function

The objective is to **minimize** the MSE, i.e., we want to find the parameters \( w \) and \( b \) that make the predictions \( \hat{y}\_i \) as close as possible to the true values \( y_i \).

## 5. Gradient Descent for Optimization

One way to minimize the MSE is by using **gradient descent**, which is an optimization algorithm. The idea behind gradient descent is to update the parameters \( w \) and \( b \) in the direction that reduces the cost function.

For each iteration, the updates are computed as follows:

- **Gradient with respect to \( w \)**:

$$
\frac{\partial \text{MSE}}{\partial w} = -\frac{2}{n} \sum_{i=1}^{n} x_i (y_i - \hat{y}_i)
$$

- **Gradient with respect to \( b \)**:

$$
\frac{\partial \text{MSE}}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)
$$

Where:

- \( \frac{\partial \text{MSE}}{\partial w} \) is the derivative of the MSE with respect to \( w \).
- \( \frac{\partial \text{MSE}}{\partial b} \) is the derivative of the MSE with respect to \( b \).
- \( x_i \) is the feature value for the \( i^{th} \) sample.
- \( y_i \) is the true target value for the \( i^{th} \) sample.
- \( \hat{y}\_i = w \cdot x_i + b \) is the predicted value.

After calculating the gradients, the parameters are updated using the following update rule:

$$
w = w - \alpha \cdot \frac{\partial \text{MSE}}{\partial w}
$$

$$
b = b - \alpha \cdot \frac{\partial \text{MSE}}{\partial b}
$$

Where \( \alpha \) is the **learning rate**, which controls how big a step to take towards the minimum.

## 6. Final Equation for Prediction

Once we have trained the model and found the optimal values for \( w \) and \( b \), we can use the linear regression model to make predictions on new data points:

$$
\hat{y} = w \cdot x + b
$$

## Summary of Steps in Linear Regression

1. **Model Setup**: \( y = w \cdot x + b \)
2. **Cost Function (MSE)**: \( \text{MSE}(w, b) = \frac{1}{n} \sum\_{i=1}^{n} (y_i - \hat{y}\_i)^2 \)
3. **Gradient Descent**: Update \( w \) and \( b \) using the gradients:
   - \( w = w - \alpha \cdot \frac{\partial \text{MSE}}{\partial w} \)
   - \( b = b - \alpha \cdot \frac{\partial \text{MSE}}{\partial b} \)
4. **Prediction**: \( \hat{y} = w \cdot x + b \)

## Conclusion

In summary, linear regression tries to find the best parameters \( w \) and \( b \) by minimizing the Mean Squared Error (MSE) using optimization techniques like gradient descent. The key objective is to make the predicted values \( \hat{y} \) as close as possible to the true values \( y \).
