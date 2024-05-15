# AutoML Leaderboard

| Best model   | name                                                       | model_type    | metric_type   |   metric_value |   train_time |
|:-------------|:-----------------------------------------------------------|:--------------|:--------------|---------------:|-------------:|
|              | [1_DecisionTree](1_DecisionTree/README.md)                 | Decision Tree | logloss       |       2.62537  |        14.19 |
|              | [2_Linear](2_Linear/README.md)                             | Linear        | logloss       |       0.746647 |         7.93 |
|              | [3_Default_RandomForest](3_Default_RandomForest/README.md) | Random Forest | logloss       |       0.62405  |         4.14 |
| **the best** | [Ensemble](Ensemble/README.md)                             | Ensemble      | logloss       |       0.604535 |         1.1  |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

