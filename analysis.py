import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

dates = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(100)]
risk = [random.randint(20, 100) for i in range(100)]

df = pd.DataFrame({
    "Date": dates,
    "Risk Score": risk
})

df.to_csv("data.csv", index=False)

# Line Graph
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Risk Score"], marker="o")
plt.title("Supply Chain Risk Analysis")
plt.xlabel("Date")
plt.ylabel("Risk Score")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("risk_trend.png")
plt.show()

# Bar Graph
plt.figure(figsize=(10, 5))
plt.bar(df["Date"], df["Risk Score"])
plt.title("Supply Chain Risk Bar Chart")
plt.xlabel("Date")
plt.ylabel("Risk Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("risk_bar.png")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

dates = [datetime(2026,1,1) + timedelta(days=i) for i in range(100)]
risk = [random.randint(20,100) for i in range(100)]

df = pd.DataFrame({
    "Date": dates,
    "Risk Score": risk
})

df.to_csv("data.csv", index=False)

# Graph 1 - Line
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Risk Score"], marker="o")
plt.title("Supply Chain Risk Analysis")
plt.xlabel("Date")
plt.ylabel("Risk Score")
plt.grid(True)
plt.savefig("risk_trend.png")
plt.show()

# Graph 2 - Bar
plt.figure(figsize=(10,5))
plt.bar(df["Date"], df["Risk Score"], color="orange")
plt.title("Supply Chain Risk Bar Chart")
plt.xlabel("Date")
plt.ylabel("Risk Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Graph 3 - Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Risk Score"], bins=10, color="green", edgecolor="black")
plt.title("Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# Graph 4 - Scatter
plt.figure(figsize=(10,5))
plt.scatter(df["Date"], df["Risk Score"], color="red")
plt.title("Supply Chain Risk Scatter Plot")
plt.xlabel("Date")
plt.ylabel("Risk Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

print("All graphs generated successfully!")