# Summary of 10_Default_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 5
- **weights**: uniform
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.424817 |       nan   |
| auc       | 0.877315 |       nan   |
| f1        | 0.864865 |         0.2 |
| accuracy  | 0.833333 |         0.2 |
| precision | 1        |         0.8 |
| recall    | 1        |         0   |
| mcc       | 0.6495   |         0.2 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.424817 |       nan   |
| auc       | 0.877315 |       nan   |
| f1        | 0.864865 |         0.2 |
| accuracy  | 0.833333 |         0.2 |
| precision | 0.842105 |         0.2 |
| recall    | 0.888889 |         0.2 |
| mcc       | 0.6495   |         0.2 |


## Confusion matrix (at threshold=0.2)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                9 |                3 |
| Labeled as 1 |                2 |               16 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
