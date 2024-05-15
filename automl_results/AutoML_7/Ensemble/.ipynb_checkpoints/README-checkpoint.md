# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 5_Default_Xgboost       |        1 |
| 7_Default_NeuralNetwork |        1 |
| 9_Default_ExtraTrees    |        3 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.510656 |  nan        |
| auc       | 0.848958 |  nan        |
| f1        | 0.814815 |    0.571078 |
| accuracy  | 0.821429 |    0.571078 |
| precision | 1        |    0.571078 |
| recall    | 1        |    0.167866 |
| mcc       | 0.696631 |    0.571078 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.510656 |  nan        |
| auc       | 0.848958 |  nan        |
| f1        | 0.814815 |    0.571078 |
| accuracy  | 0.821429 |    0.571078 |
| precision | 1        |    0.571078 |
| recall    | 0.6875   |    0.571078 |
| mcc       | 0.696631 |    0.571078 |


## Confusion matrix (at threshold=0.571078)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               12 |                0 |
| Labeled as 1 |                5 |               11 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
