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




