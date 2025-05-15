import pandas as pd
import matplotlib.pyplot as plt

# Build evaluation method data (based on my bib.js 10 literature analysis)
data = {
    "Year": [2022, 2023, 2024, 2025],
    "Controlled User Study": [0, 0, 1, 0],
    "Simulation": [1, 1, 0, 0],
    "Clinical Trial": [0, 0, 1, 0],
    "Prototype Demo": [0, 1, 1, 0],
    "Case Study": [1, 0, 3, 0],
    "Empirical Study": [0, 0, 0, 1],
    "Taxonomy Evaluation": [0, 0, 0, 1]
}

# Convert to DataFrame and plot
df = pd.DataFrame(data)
df = df.groupby("Year").sum()
df = df.sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
bottom = [0] * len(df)
colors = ['#d55e00', '#999999', '#009e73', '#f0e442', '#56b4e9', '#cc79a7', '#0072b2']

# Draw a stacked bar chart
for i, column in enumerate(df.columns):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=colors[i])
    bottom = [i + j for i, j in zip(bottom, df[column])]

# Add chart elements
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Papers", fontsize=12)
ax.set_title("Number of Papers by Evaluation Method and Year", fontsize=14)
ax.legend(title="Evaluation Method")

# Beautify the layout and save it as a PNG file
plt.tight_layout()
plt.savefig("xai_eval_methods_by_year.png", dpi=300)
plt.show()