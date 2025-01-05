# Multiclass Logistic Regression using Softmax

## Softmax Function

For multiclass classification, instead of predicting a single probability, we use the **softmax** function to predict the probability of each class.

The softmax function for class \( k \) is given by:

$$
P(y = k | x, W) = \frac{e^{w_k^\top x}}{\sum_{j=1}^{C} e^{w_j^\top x}}
$$

Where:
- \( w_k \) is the weight vector for class \( k \),
- \( W \) is the matrix of weights for all classes,
- \( C \) is the number of classes.

## Likelihood Function

For \( n \) samples and \( C \) classes, the likelihood function is:

$$
L(W) = \prod_{i=1}^n \prod_{k=1}^C \left( P(y_i = k | x_i, W) \right)^{\mathbb{1}[y_i = k]}
$$

## Log-Likelihood

Taking the logarithm of the likelihood gives us the log-likelihood:

$$
\log L(W) = \sum_{i=1}^n \log\left( \frac{e^{w_{y_i}^\top x_i}}{\sum_{j=1}^C e^{w_j^\top x_i}} \right)
$$

## Negative Log-Likelihood (NLL)

To minimize the negative log-likelihood (NLL), we take the negative:

$$
\text{NLL}(W) = - \sum_{i=1}^n \log\left( \frac{e^{w_{y_i}^\top x_i}}{\sum_{j=1}^C e^{w_j^\top x_i}} \right)
$$

This is the **cross-entropy loss** for multiclass classification.

## Optimization

We minimize the negative log-likelihood using gradient descent:

$$
W = W_{\text{old}} - \alpha \cdot \nabla_W \text{NLL}(W)
$$

Where \( \alpha \) is the learning rate.
