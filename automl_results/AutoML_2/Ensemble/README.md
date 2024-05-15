# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                  |   Weight |
|:-----------------------|---------:|
| 3_Default_RandomForest |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.179772 |  nan        |
| auc       | 0.876457 |  nan        |
| f1        | 0.965944 |    0.194433 |
| accuracy  | 0.934132 |    0.194433 |
| precision | 1        |    0.957614 |
| recall    | 1        |    0.194433 |
| mcc       | 0.462405 |    0.831834 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.179772 |  nan        |
| auc       | 0.876457 |  nan        |
| f1        | 0.965944 |    0.194433 |
| accuracy  | 0.934132 |    0.194433 |
| precision | 0.934132 |    0.194433 |
| recall    | 1        |    0.194433 |
| mcc       | 0        |    0.194433 |


## Confusion matrix (at threshold=0.194433)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                0 |               11 |
| Labeled as 1 |                0 |              156 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
