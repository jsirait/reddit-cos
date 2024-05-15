# Summary of 1_Baseline

[<< Go back](../README.md)


## Baseline Classifier (Baseline)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.673012 |      nan    |
| auc       | 0.5      |      nan    |
| f1        | 0.75     |        0.54 |
| accuracy  | 0.6      |        0.54 |
| precision | 0.6      |        0.54 |
| recall    | 1        |        0.54 |
| mcc       | 0        |        0.54 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.673012 |      nan    |
| auc       | 0.5      |      nan    |
| f1        | 0.75     |        0.54 |
| accuracy  | 0.6      |        0.54 |
| precision | 0.6      |        0.54 |
| recall    | 1        |        0.54 |
| mcc       | 0        |        0.54 |


## Confusion matrix (at threshold=0.54)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                0 |               12 |
| Labeled as 1 |                0 |               18 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
