# Summary of 3_Default_RandomForest

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

1.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.592545 |  nan        |
| auc       | 0.707407 |  nan        |
| f1        | 0.823529 |    0.459194 |
| accuracy  | 0.75     |    0.459194 |
| precision | 1        |    0.842638 |
| recall    | 1        |    0.303667 |
| mcc       | 0.450341 |    0.459194 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.592545 |  nan        |
| auc       | 0.707407 |  nan        |
| f1        | 0.823529 |    0.459194 |
| accuracy  | 0.75     |    0.459194 |
| precision | 0.736842 |    0.459194 |
| recall    | 0.933333 |    0.459194 |
| mcc       | 0.450341 |    0.459194 |


## Confusion matrix (at threshold=0.459194)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                4 |                5 |
| Labeled as 1 |                1 |               14 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
