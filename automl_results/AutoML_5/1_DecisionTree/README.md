# Summary of 1_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

12.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 2.62537  |  nan        |
| auc       | 0.685185 |  nan        |
| f1        | 0.736842 |    0        |
| accuracy  | 0.666667 |    0        |
| precision | 0.769231 |    0.733333 |
| recall    | 0.777778 |    0        |
| mcc       | 0.327327 |    0.444444 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 2.62537  |         nan |
| auc       | 0.685185 |         nan |
| f1        | 0.736842 |           0 |
| accuracy  | 0.666667 |           0 |
| precision | 0.7      |           0 |
| recall    | 0.777778 |           0 |
| mcc       | 0.288675 |           0 |


## Confusion matrix (at threshold=0.0)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                6 |                6 |
| Labeled as 1 |                4 |               14 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
