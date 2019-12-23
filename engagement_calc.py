import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/processed_data/p1_vid_1_20.11.19_18.10.09.bp_processed.csv', header=0)
for i in range(len(df)):
    df.loc[i,"Final_Alpha"] = (df.loc[i, "POW.AF3.Alpha"] + df.loc[i,"POW.AF4.Alpha"])/2
    df.loc[i, "Final_Theta"] = (df.loc[i, "POW.AF3.Theta"] + df.loc[i, "POW.AF4.Theta"]) / 2
    df.loc[i, "Final_Beta"] = (((df.loc[i, "POW.AF3.BetaL"] + df.loc[i, "POW.AF3.BetaH"]) / 2)+((df.loc[i, "POW.AF4.BetaL"] + df.loc[i, "POW.AF4.BetaH"]) / 2))/2
    df.loc[i, "Engagement"] = df.loc[i, "Final_Beta"]/(df.loc[i, "Final_Alpha"] + df.loc[i, "Final_Theta"])
    df.loc[i, "Time"] = i

df2 = pd.DataFrame(columns=["Engagement"])
df2["Engagement"] = df["Engagement"]
print(df2)
with open('/Users/sarvi/PycharmProjects/BCI/Project/datasets/final_data/Video1_engagement.csv', 'a') as f:
    (df2).to_csv(f)




df = pd.read_csv('/Users/sarvi/PycharmProjects/BCI/Project/datasets/final_data/Video1_engagement.csv', delimiter=',')

Eng_avg = []
i = 0
while i < len(df):
    x = 0
    j=i
    while j != len(df) and j < i+4:

        x = x + df.loc[j, "Engagement"]
        j = j + 1

    Eng_avg.append(x/4)
    i = i + 4
Time_avg = []

for i in range(len(Eng_avg)):
    Time_avg.append(i)

plt.plot(Time_avg, Eng_avg)
plt.show()