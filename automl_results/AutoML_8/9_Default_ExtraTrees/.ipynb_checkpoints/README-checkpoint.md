# Summary of 9_Default_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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

2.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.53249  |  nan        |
| auc       | 0.766204 |  nan        |
| f1        | 0.782609 |    0.217391 |
| accuracy  | 0.7      |    0.479654 |
| precision | 1        |    0.768116 |
| recall    | 1        |    0.075    |
| mcc       | 0.480065 |    0.479654 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.53249  |  nan        |
| auc       | 0.766204 |  nan        |
| f1        | 0.689655 |    0.479654 |
| accuracy  | 0.7      |    0.479654 |
| precision | 0.909091 |    0.479654 |
| recall    | 0.555556 |    0.479654 |
| mcc       | 0.480065 |    0.479654 |


## Confusion matrix (at threshold=0.479654)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               11 |                1 |
| Labeled as 1 |                8 |               10 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
