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

13.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.254666 |  nan        |
| auc       | 0.594724 |  nan        |
| f1        | 0.968641 |    0.36     |
| accuracy  | 0.939189 |    0.36     |
| precision | 0.952756 |    0.787879 |
| recall    | 1        |    0.36     |
| mcc       | 0.139605 |    0.787879 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.254666 |      nan    |
| auc       | 0.594724 |      nan    |
| f1        | 0.968641 |        0.36 |
| accuracy  | 0.939189 |        0.36 |
| precision | 0.939189 |        0.36 |
| recall    | 1        |        0.36 |
| mcc       | 0        |        0.36 |


## Confusion matrix (at threshold=0.36)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                0 |                9 |
| Labeled as 1 |                0 |              139 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
