# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                  |   Weight |
|:-----------------------|---------:|
| 2_Linear               |        1 |
| 3_Default_RandomForest |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.604535 |  nan        |
| auc       | 0.736111 |  nan        |
| f1        | 0.809524 |    0.395226 |
| accuracy  | 0.766667 |    0.592758 |
| precision | 1        |    0.726915 |
| recall    | 1        |    0.101284 |
| mcc       | 0.521773 |    0.592758 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.604535 |  nan        |
| auc       | 0.736111 |  nan        |
| f1        | 0.8      |    0.592758 |
| accuracy  | 0.766667 |    0.592758 |
| precision | 0.823529 |    0.592758 |
| recall    | 0.777778 |    0.592758 |
| mcc       | 0.521773 |    0.592758 |


## Confusion matrix (at threshold=0.592758)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                9 |                3 |
| Labeled as 1 |                4 |               14 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
