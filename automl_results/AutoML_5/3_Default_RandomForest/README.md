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

2.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.62405  |  nan        |
| auc       | 0.666667 |  nan        |
| f1        | 0.809524 |    0.291285 |
| accuracy  | 0.733333 |    0.291285 |
| precision | 1        |    0.786921 |
| recall    | 1        |    0.184939 |
| mcc       | 0.442269 |    0.291285 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.62405  |  nan        |
| auc       | 0.666667 |  nan        |
| f1        | 0.809524 |    0.291285 |
| accuracy  | 0.733333 |    0.291285 |
| precision | 0.708333 |    0.291285 |
| recall    | 0.944444 |    0.291285 |
| mcc       | 0.442269 |    0.291285 |


## Confusion matrix (at threshold=0.291285)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                5 |                7 |
| Labeled as 1 |                1 |               17 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
