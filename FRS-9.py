import pandas as pd
import numpy as np
import openpyxl
import seaborn as sbn

data_col = pd.read_csv(r"C:\Users\Yogesh Raikwar\Desktop\Project\Project 1 - FRS\data\data\model_collateral.csv")
# print(data_1.head())

data_con = pd.read_csv(r"C:\Users\Yogesh Raikwar\Desktop\Project\Project 1 - FRS\data\data\model_config.csv")
# print(data_2.head())

data_auth = pd.read_excel(r"C:\Users\Yogesh Raikwar\Desktop\Project\Project 1 - FRS\data\data\model_auth.xlsx")
# print(data_3.head())

# print(data_auth.info())
# print(data_con.info())
# print(data_col.info())

# print(data_col.nunique())
# print(data_con.nunique())
# print(data_auth.nunique())

# print(data_auth.duplicated().sum())
# print(data_con.duplicated().sum())
# print(data_con.duplicated().sum())

# print(data_auth.isnull().sum())
## Insight - In this dataframe for 'DaysPastDue' nulls are present need to replace by '0'.
data_auth['DaysPastDue'] = data_auth['DaysPastDue'].fillna(0)
# print(data_auth['DaysPastDue'])
# print(data_auth.isnull().sum())

# print(data_con.isnull().sum())
## Insight - In this dataframe for column "default_date" nulls are present.

# print(data_col.isnull().sum())
## Insight - In this dataframe more than 2 columns have null values.

## ECL Report -->
# For Stage1ecl we need EAD, PD12, LGD from data_auth
stage1ecl = data_auth["EAD"] * data_auth["PD12"] * data_auth["LGD"]
stage1 = pd.DataFrame(stage1ecl)
stage1 = stage1.rename(columns={0:"stage1"})
# print(stage1)

# For stage2ecl we need EAD, PDLT, LGD from data_auth
stage2ecl = data_auth["EAD"] * data_auth["PDLT"] * data_auth["LGD"]
stage2 = pd.DataFrame(stage2ecl)
stage2 = stage2.rename(columns={0:"stage2"})
# print(stage2)

# For stage3ecl we need EAD and LGD from data_auth
stage3ecl = data_auth["EAD"] * data_auth["LGD"]
stage3 = pd.DataFrame(stage3ecl)
stage3 = stage3.rename(columns={0:"stage3"})
# print(stage3)


cols = data_auth[["EAD", "PD12", "PDLT", "LGD"]].copy()

EL_report = pd.concat([cols,stage1, stage2, stage3], axis=1)
# print(ED_report)

EL_report = EL_report.to_excel("ECL_Report.xlsx", index=False)

## EAD Report -->
# For change in EAD we need EAD, Previous EAD from data_auth
# changed_ead = data_auth["EAD"] - data_auth["Previous EAD"]
# changed_ead = pd.DataFrame(changed_ead)
# changed_ead = changed_ead.rename(columns={0:"Changed_EAD"})
# print(changed_ead)

# For change ead percent
# changed_ead_percentage = (changed_ead["Changed_EAD"]/data_auth["Previous EAD"])*100
# changed_ead_percentage = pd.DataFrame(changed_ead_percentage)
# changed_ead_percentage = changed_ead_percentage.rename(columns={0: "Changed_EAD_Percentage"})
# print(changed_ead_percentage)

# cols1 = data_auth[["EAD", "Previous EAD"]].copy()
# print(cols1)

# EAD_Report = pd.concat([cols1, changed_ead, changed_ead_percentage], axis=1)
# print(EAD_Report)

# EAD_Report = EAD_Report.to_excel("EAD_Report.xlsx", index=False)

## LGD Report -->
# For change in LGD we need LGD, Previous LGD from data_auth
# changed_lgd = data_auth["LGD"] - data_auth["Previous LGD"]
# changed_lgd = pd.DataFrame(changed_lgd)
# changed_lgd = changed_lgd.rename(columns={0:"Changed_LGD"})
# print(changed_lgd)

# For change lgd percent
# changed_lgd_percentage = (changed_lgd["Changed_LGD"]/data_auth["Previous LGD"])*100
# changed_lgd_percentage = pd.DataFrame(changed_lgd_percentage)
# changed_lgd_percentage = changed_lgd_percentage.rename(columns={0: "Changed_LGD_Percentage"})
# # print(changed_lgd_percentage)

# cols2 = data_auth[["LGD", "Previous LGD"]].copy()

# LGD_Report = pd.concat([cols2, changed_lgd, changed_lgd_percentage],axis=1)
# print(LGD_Report)

# LGD_Report = LGD_Report.to_excel("LGD_Report.xlsx", index=False)