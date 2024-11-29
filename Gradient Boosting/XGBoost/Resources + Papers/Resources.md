 [Main XGBoost paper](https://arxiv.org/pdf/1603.02754v1) <br>
---
**Note:** Make sure to checkout theses videos in order <br>
1. [XGBoost for regression YT Video](https://www.youtube.com/watch?v=OtD8wVaFm6E) <br>
2. [XGBoost for classification YT Video](https://www.youtube.com/watch?v=8b1JEDvenQU) <br>
3. [XGBoost mathematical details YT Video](https://www.youtube.com/watch?v=ZVFeW798-2I) <br>
4. [XGBoost optimizations YT Video](https://www.youtube.com/watch?v=oRrKeUCEbq8) <br>
---
** Weighted quantile sketches steps** <br>
1. Sort data by feature.<br>
2. Compute the cumulative weight for each sorted feature value.<br>
For regression it's the number of residuals <br>
For classification it ∑ p(1-p) <br>
3.  Identify quantiles based on the cumulative weight distribution.<br>
4. Construct the quantile sketch to represent the feature space.<br>
5. Use the weighted quantile sketch to find the best split at each decision tree node.<br>
Recursively repeat the process for each node of the tree.<br>
---
**Note:** XGBM uses approximate algorithm and weighted quantile sketches only with huge datasets<br>