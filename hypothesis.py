from scipy import stats
import numpy as np

class trend():
 def statcalc(df1,df2):
  stat_hypo, p_value  = stats.ttest_ind(df1["nn_occurences"],df2["vb_occurences"])
  # Interpret the results:
  alpha = 0.05
  if p_value < alpha:
    print("Reject the null hypothesis; there is a significant difference between the noun frequency this texts and verbs frequency.")
  else:
    print("Fail to reject the null hypothesis; there is no significant difference between the noun frequency this texts and verbs frequency.")

  trends = stats.chi2_contingency([df1["nn_occurences"].head(10),df2["vb_occurences"].head(10)])

        #print(f"chi2 statistic:     {chi2:.5g}")
        #print(f"p-value:            {p:.5g}")
        #print(f"degrees of freedom: {dof}")
        #print("expected frequencies:")
        #print(expected)
  return trends
 def shannonDiversity(df):
        #print(df[1])
  df["proportion"] = df[1] / sum(df[1])
  df["naturalLog"] = np.log(df["proportion"])
  df["summation"] = df["proportion"] * df["naturalLog"]
  df = df.dropna(how='any',axis=0)

  df["diversityScore"]=-1*sum(df["summation"])

  if df["diversityScore"][0] <= 1.99:
    df["diversityType"]="Very Low"
  elif df["diversityScore"][0] <= 2.49:
    df["diversityType"]="Low"
  elif df["diversityScore"][0] <= 2.99:
    df["diversityType"]="Moderate"
  elif df["diversityScore"][0] <= 3.49:
    df["diversityType"]="High"
  elif df["diversityScore"][0] >= 3.50:
    df["diversityType"]="Very High"
  else:
    df["diversityType"]="Unknown"

  return df
