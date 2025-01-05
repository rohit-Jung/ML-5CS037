# Logistic Regression for Binary Classification

## Why sigmoid ?

we use the sigmoid function in logistic regression to transform the linear output (which can be any real number) into a probability value between 0 and 1. This allows us to interpret the model's output as the probability that a given input belongs to class 𝑦 = 1. The sigmoid function also ensures smooth gradients for efficient optimization using algorithms like gradient descent, making it easier to learn the model's parameters.

## Binary Classification and Bernoulli Distribution

Logistic regression assumes that the labels \( y \) follow a **Bernoulli distribution** (binary outcomes). For a given input \( x \), the probability of \( y = 1 \) is modeled by the **logistic function** (sigmoid function):

$$
P(y = 1 | x, w) = \sigma(w^\top x) = \frac{1}{1 + e^{-w^\top x}}
$$

where \( \sigma(w^\top x) \) is the **sigmoid** function, and the probability of \( y = 0 \) is:

$$
P(y = 0 | x, w) = 1 - \sigma(w^\top x)
$$

## Likelihood Function

The **probability mass function (PMF)** for a Bernoulli distribution for a single data point \( (x_i, y_i) \) is:

$$
P(y_i | x_i, w) = \sigma(w^\top x_i)^{y_i} (1 - \sigma(w^\top x_i))^{1 - y_i}
$$

This represents the likelihood of observing \( y_i \) given \( x_i \) and the parameters \( w \).

## Log-Likelihood

The likelihood for the entire dataset (with \( n \) samples) is the product of the individual probabilities for each data point:

$$
L(w) = \prod_{i=1}^n \left[ \sigma(w^\top x_i)^{y_i} (1 - \sigma(w^\top x_i))^{1 - y_i} \right]
$$

To make the optimization easier (to turn products into sums), we take the logarithm:

$$
\log L(w) = \sum_{i=1}^n \left[ y_i \log(\sigma(w^\top x_i)) + (1 - y_i) \log(1 - \sigma(w^\top x_i)) \right]
$$

## Negative Log-Likelihood (NLL)

Since MLE maximizes the log-likelihood, and gradient descent minimizes functions, we take the **negative log-likelihood**:

$$
\text{NLL}(w) = -\sum_{i=1}^n \left[ y_i \log(\sigma(w^\top x_i)) + (1 - y_i) \log(1 - \sigma(w^\top x_i)) \right]
$$

This function is the **log loss** or **binary cross-entropy loss**.

## Optimization

To find the best parameters \( w \), we minimize the negative log-likelihood using gradient descent. The update rule for the weights \( w \) is:

$$
w = w_{\text{old}} - \alpha \cdot \nabla_w \text{NLL}(w)
$$

where \( \alpha \) is the learning rate, and \( \nabla_w \) is the gradient of the loss function with respect to the weights.

## Epochs

The optimization continues for a specified number of **epochs**, where in each epoch, the weights are updated based on the gradients calculated from the current data.
