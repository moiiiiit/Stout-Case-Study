import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

df_fraud = df[df.isFraud == 1]
df_fraud_isFlagged = df_fraud[df_fraud.isFlaggedFraud == 1]
df_fraud_notFlagged = df_fraud[df_fraud.isFlaggedFraud == 0]
df_notFraud = df[df.isFraud == 0]
df_notFraud_isFlagged = df_notFraud[df_notFraud.isFlaggedFraud == 1]

# # Pie Chart
# x = ['DEBIT', 'TRANSFER', 'CASH_OUT',
#           'PAYMENT']
# colors = ['r', 'y', 'g', 'b']
# y = np.array([len(df_fraud_isFlagged[df_fraud_isFlagged.type == 'DEBIT']), len(df_fraud_isFlagged[df_fraud_isFlagged.type == 'TRANSFER']), len(df_fraud_isFlagged[df_fraud_isFlagged.type == 'CASH_OUT']), len(df_fraud_isFlagged[df_fraud_isFlagged.type == 'PAYMENT'])])
# percents = 100.*y/y.sum()
# patches, texts = plt.pie(y, colors=colors,
#                          startangle=90,
#                          radius=1.2, )
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, percents)]
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
#                                           key=lambda x: x[2],
#                                           reverse=True))
# plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
#            fontsize=8)
# plt.show()

# # Scatter chart
# y = df_fraud_isFlagged.oldbalanceOrg
# x = df_fraud_isFlagged.oldbalanceDest
# plt.scatter(x,y,s=10)
# plt.ylabel("Balance in Original Account")
# plt.xlabel("Balance in Destination Account")


# y = df_fraud_notFlagged.oldbalanceOrg
# x = df_fraud_notFlagged.oldbalanceDest
# plt.ylabel("Balance in Original Account")
# plt.xlabel("Balance in Destination Account")
# plt.scatter(x, y, s=10)

# plt.show() 

# # Histogram chart for amount
# y = df_fraud_notFlagged.amount
# plt.hist(y, density=True, bins=40)
# plt.ylabel("Probability of fraud")
# plt.xlabel("$ Amount of Fraud Committed")

# plt.legend()
# plt.show()

# # Histogram 2d for amount and oldbalanceDest
# y = df_fraud.amount
# x = df_fraud.oldbalanceDest
# plt.hist2d(x, y, bins=(20, 40))
# plt.title("Heatmap showing the probability of committing fraud")
# plt.xlabel("$ Old Balance in Destination Account")
# plt.ylabel("$ Amount of Fraud Committed")
# plt.legend()
# plt.show()

# Scatter Area Chart for amount and oldbalanceOrg
y = df_fraud.amount
x = df_fraud.oldbalanceOrg
plt.scatter(x, y, s=40, alpha=0.2)
plt.xlabel("$ Old Balance in Original Account")
plt.ylabel("$ Amount of Fraud Committed")
plt.legend()
plt.show()