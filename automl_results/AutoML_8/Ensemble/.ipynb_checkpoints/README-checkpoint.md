# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                       |   Weight |
|:----------------------------|---------:|
| 10_Default_NearestNeighbors |        4 |
| 4_Default_LightGBM          |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.415375 | nan         |
| auc       | 0.898148 | nan         |
| f1        | 0.894737 |   0.326503  |
| accuracy  | 0.866667 |   0.326503  |
| precision | 1        |   0.739357  |
| recall    | 1        |   0.0449777 |
| mcc       | 0.721688 |   0.326503  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.415375 |  nan        |
| auc       | 0.898148 |  nan        |
| f1        | 0.894737 |    0.326503 |
| accuracy  | 0.866667 |    0.326503 |
| precision | 0.85     |    0.326503 |
| recall    | 0.944444 |    0.326503 |
| mcc       | 0.721688 |    0.326503 |


## Confusion matrix (at threshold=0.326503)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                9 |                3 |
| Labeled as 1 |                1 |               17 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)



[<< Go back](../README.md)
