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

1.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 2.57217  |       nan   |
| auc       | 0.75     |       nan   |
| f1        | 0.758621 |         0.4 |
| accuracy  | 0.75     |         0.4 |
| precision | 1        |         0.8 |
| recall    | 0.75     |         0   |
| mcc       | 0.516811 |         0.4 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 2.57217  |       nan   |
| auc       | 0.75     |       nan   |
| f1        | 0.758621 |         0.4 |
| accuracy  | 0.75     |         0.4 |
| precision | 0.846154 |         0.4 |
| recall    | 0.6875   |         0.4 |
| mcc       | 0.516811 |         0.4 |


## Confusion matrix (at threshold=0.4)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               10 |                2 |
| Labeled as 1 |                5 |               11 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
