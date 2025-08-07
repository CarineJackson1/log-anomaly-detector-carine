import matplotlib.pyplot as plt

def plot_issue_counts(data):
    data['severity'].value_counts().plot(kind='bar', title='Issue Severity Count')
    plt.xlabel('Severity')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
