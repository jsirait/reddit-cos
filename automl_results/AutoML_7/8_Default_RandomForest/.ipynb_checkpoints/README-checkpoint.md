# Summary of 8_Default_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: logloss
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

6.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.657093 | nan         |
| auc       | 0.723958 | nan         |
| f1        | 0.780488 |   0.115465  |
| accuracy  | 0.678571 |   0.115465  |
| precision | 1        |   0.804875  |
| recall    | 1        |   0.0964058 |
| mcc       | 0.452267 |   0.804875  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.657093 |  nan        |
| auc       | 0.723958 |  nan        |
| f1        | 0.780488 |    0.115465 |
| accuracy  | 0.678571 |    0.115465 |
| precision | 0.64     |    0.115465 |
| recall    | 1        |    0.115465 |
| mcc       | 0.4      |    0.115465 |


## Confusion matrix (at threshold=0.115465)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                3 |                9 |
| Labeled as 1 |                0 |               16 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
