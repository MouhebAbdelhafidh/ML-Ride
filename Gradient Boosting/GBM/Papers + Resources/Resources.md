# Gradient Boosted Trees

## How Gradient Boosted Trees Work

1. **Initialize the Model**: Start with an initial prediction, often the mean of the target variable (for regression) or log odds (for classification).

2. **Calculate Residuals**: Compute the residual errors of the current model's predictions by comparing them to the actual target values.

3. **Fit a New Tree to Residuals**: Train a new tree to predict the residuals (the differences between the predicted and actual values). This tree is essentially "learning" the parts that the previous models missed.

4. **Update the Model**: Add the predictions of the new tree to the current model with a small scaling factor (learning rate) to control the contribution of each tree. The learning rate prevents the model from overfitting and improves generalization.

5. **Iterate**: Repeat steps 2-4 for a fixed number of iterations or until the improvement falls below a threshold. Each iteration adds a new tree that corrects the errors of the combined ensemble from previous trees.

6. **Final Prediction**: The final model's prediction is the sum of all individual tree predictions, weighted by the learning rate.

## Mathematical Expression

For a training dataset \((x_i, y_i)\) where \(i = 1, 2, \dots, N\), the model at step \(m\) is:

\[
F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)
\]

Where:

- \(F_{m-1}(x)\) is the prediction from the previous model.
- \(\eta\) (learning rate) controls the contribution of each tree.
- \(h_m(x)\) is the new tree that predicts the residuals of \(F_{m-1}(x)\).

---

This iterative process continues until the model reaches the desired level of accuracy, with each new tree focusing on the errors of the combined model so far. The final prediction is an ensemble of all trees, weighted by the learning rate, providing a strong and accurate predictive model.

# Gradient Boosting Example

We illustrate gradient boosting step by step using a simple regression problem where we want to predict target values \( y \) from feature \( X \).

Assume our dataset has the following values:

- \( X = [1, 2, 3] \)
- \( y = [3, 6, 8] \)

Our goal is to use gradient boosting to model the relationship between \( X \) and \( y \) by iteratively adding small decision trees that minimize the error.

## Step 1: Initialize the Model

For gradient boosting, we start with an initial prediction \( F_0(x) \), which is often the mean of \( y \) for regression tasks.

\[
F_0(x) = \text{mean}(y) = \frac{3 + 6 + 8}{3} = 5.67
\]

So our initial prediction for each point is 5.67.

## Step 2: Calculate Residuals

Now, we calculate the residuals, which are the differences between the actual values \( y \) and our initial predictions \( F_0(x) \).

\[
\text{Residuals} = y - F_0(x)
\]

For each \( x \):

- For \( x = 1 \): Residual = \( 3 - 5.67 = -2.67 \)
- For \( x = 2 \): Residual = \( 6 - 5.67 = 0.33 \)
- For \( x = 3 \): Residual = \( 8 - 5.67 = 2.33 \)

So, the residuals are:

\[
\text{Residuals} = [-2.67, 0.33, 2.33]
\]

## Step 3: Fit a New Tree to Residuals

Next, we train a new decision tree, \( h_1(x) \), to predict the residuals. For simplicity, let's assume this tree fits the residuals exactly, so the tree's predictions are:

\[
h_1(x) = [-2.67, 0.33, 2.33]
\]

## Step 4: Update the Model

We update our model by adding the predictions of this new tree, \( h_1(x) \), to the current model's predictions, scaled by a learning rate. Let's use a learning rate \( \alpha = 0.1 \).

\[
F_1(x) = F_0(x) + \alpha \cdot h_1(x)
\]

For each \( x \):

- For \( x = 1 \): \( F_1(x) = 5.67 + 0.1 \times (-2.67) = 5.67 - 0.267 = 5.403 \)
- For \( x = 2 \): \( F_1(x) = 5.67 + 0.1 \times 0.33 = 5.67 + 0.033 = 5.703 \)
- For \( x = 3 \): \( F_1(x) = 5.67 + 0.1 \times 2.33 = 5.67 + 0.233 = 5.903 \)

So, our updated predictions are:

\[
F_1(x) = [5.403, 5.703, 5.903]
\]

## Step 5: Iterate

Repeat steps 2-4 for more iterations. At each iteration, compute the residuals using the updated predictions and fit a new tree on these residuals. Then, update the model by adding the new tree's predictions scaled by the learning rate.

### Second Iteration:

1. **Calculate new residuals:**

   \[
   \text{Residuals} = y - F_1(x) = [3 - 5.403, 6 - 5.703, 8 - 5.903] = [-2.403, 0.297, 2.097]
   \]

2. **Fit a new tree** \( h_2(x) \) to the residuals:

   Assuming this tree can perfectly predict the residuals:

   \[
   h_2(x) = [-2.403, 0.297, 2.097]
   \]

3. **Update the model** with learning rate \( \alpha = 0.1 \):

   \[
   F_2(x) = F_1(x) + \alpha \cdot h_2(x)
   \]

   For each \( x \):

   - For \( x = 1 \): \( F_2(x) = 5.403 + 0.1 \times (-2.403) = 5.403 - 0.2403 = 5.1627 \)
   - For \( x = 2 \): \( F_2(x) = 5.703 + 0.1 \times 0.297 = 5.703 + 0.0297 = 5.7327 \)
   - For \( x = 3 \): \( F_2(x) = 5.903 + 0.1 \times 2.097 = 5.903 + 0.2097 = 6.1127 \)

   Updated predictions:

   \[
   F_2(x) = [5.1627, 5.7327, 6.1127]
   \]

## Step 6: Final Prediction

After a fixed number of iterations or when residuals become very small, we stop. The final model prediction \( F(x) \) is the sum of all the trees' predictions, weighted by the learning rate. In this example:

\[
F(x) = F_2(x) = [5.1627, 5.7327, 6.1127]
\]

---

[Gradient Boosted Decision Tree Algorithm + Visualizations](https://developers.google.com/machine-learning/decision-forests/intro-to-gbdt) 

