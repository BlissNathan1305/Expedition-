import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Example data (same as before)
group1 = [23, 20, 22, 21, 24]
group2 = [30, 32, 29, 31, 33]
group3 = [40, 42, 39, 38, 41]

# Combine into a DataFrame
data = {
    'value': group1 + group2 + group3,
    'group': ['group1']*5 + ['group2']*5 + ['group3']*5
}
df = pd.DataFrame(data)

# 1. First do ANOVA
model = ols('value ~ C(group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Table:")
print(anova_table)

# 2. Now do Tukey HSD Test
tukey = pairwise_tukeyhsd(endog=df['value'], groups=df['group'], alpha=0.05)

print("\nTukey HSD Results:")
print(tukey)
