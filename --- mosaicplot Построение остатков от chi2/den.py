import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
patients = pd.DataFrame({"Thrombosis":
                             ["Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes",
                              "Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes",
                              "Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes",
                              "No","No","No","No","No","No","No","No","No","No",
                              "No","No","No","No","No","No","No","No","No","No"],
                         "Group":
                             ["Placebo","Placebo","Placebo","Placebo","Placebo","Placebo",
                              "Placebo","Placebo","Placebo","Placebo","Placebo","Placebo",
                              "Placebo","Placebo","Placebo","Placebo","Placebo","Placebo",
                              "Aspirin","Aspirin","Aspirin","Aspirin","Aspirin","Aspirin",
                              "Placebo","Placebo","Placebo","Placebo","Placebo","Placebo",
                              "Placebo","Aspirin","Aspirin","Aspirin","Aspirin","Aspirin",
                              "Aspirin","Aspirin","Aspirin","Aspirin","Aspirin","Aspirin",
                              "Aspirin","Aspirin"]})
#посмотрим на сводную таблицу пересечения признаков
print(pd.pivot_table(patients, index=["Group"], columns=["Thrombosis"], aggfunc=lambda x: len(x)))
#строим график
mosaic(patients, ["Thrombosis","Group"], gap=0.01)
plt.show()