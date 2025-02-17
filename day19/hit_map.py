import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# 다변량 함수 : heatmap
student = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

score = {
    'math': [70, 60, 50, 50, 60, 80, 100],
    'eng': [50, 80, 60, 70, 80, 80, 90],
    'japanese': [60, 80, 80, 80, 40, 50, 90],
}
df = pd.DataFrame(score, index=student)
sns.heatmap(df, cmap='Blues')  #cmap은 색을 나타냄.
plt.show()
