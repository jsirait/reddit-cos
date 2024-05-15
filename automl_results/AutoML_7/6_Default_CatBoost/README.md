# Summary of 6_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 1
- **loss_function**: Logloss
- **eval_metric**: Logloss
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
| logloss   | 0.625571 |  nan        |
| auc       | 0.697917 |  nan        |
| f1        | 0.820513 |    0.255827 |
| accuracy  | 0.75     |    0.255827 |
| precision | 1        |    0.870016 |
| recall    | 1        |    0.18981  |
| mcc       | 0.538382 |    0.255827 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.625571 |  nan        |
| auc       | 0.697917 |  nan        |
| f1        | 0.820513 |    0.255827 |
| accuracy  | 0.75     |    0.255827 |
| precision | 0.695652 |    0.255827 |
| recall    | 1        |    0.255827 |
| mcc       | 0.538382 |    0.255827 |


## Confusion matrix (at threshold=0.255827)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                5 |                7 |
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
