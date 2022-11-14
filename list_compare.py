import pandas as pd
import numpy as np
BomData = {
    "partno":['ABC','XYZ','UK','ABC','UK','XYZ','DEF'],
    "quantity":[2,1,1,1,1,2,2]
}
bomdf = pd.DataFrame(BomData)
DistiData = {
    "partno":['XYZ','GEF','ABC','UK'],
    "quantity":[2,2,4,2]
}
counter = 0
Distidf = pd.DataFrame(DistiData)

df3 = Distidf
df4 = pd.DataFrame({
    "partno":[],
    "quantity":[]
})
df5 = pd.DataFrame({
    "partno":[],
    "quantity":[]
})
counter = 0
for partno,quantity in zip(BomData["partno"],BomData["quantity"]):
    select_indices = list(np.where(df3["partno"] == partno)[0])

    if df3["partno"].values[select_indices].size > 0:
            # final_data_df.iloc[bomdata_index] = bomdf.iloc[bomdata_index]
        if df3["quantity"].values[select_indices][0] > quantity:

            # print(bomdf["partno"][counter])
                # if copy_of_disti_df["quantity"][select_indices][0] = quantity-Distidf["quantity"].values[select_indices][0]
            df4.at[counter,'partno'] = bomdf.at[counter,'partno']
            df4.at[counter,'quantity'] = bomdf.at[counter,'quantity']
            df5.at[counter,'partno'] = bomdf.at[counter,'partno']
            df5.at[counter,'quantity'] = bomdf.at[counter,'quantity']
            df3.at[select_indices[0],'quantity'] = df3["quantity"].values[select_indices][0]-quantity
            # df3["quantity"].values[select_indices][0] = df3["quantity"].values[select_indices][0]-quantity
        elif df3["quantity"].values[select_indices][0] < quantity:
            # print(df3)
            df4.at[counter,'partno'] = bomdf.at[counter,'partno']
            df4.at[counter,'quantity'] = bomdf.at[counter,'quantity']
            df5.at[counter,'partno'] = df3.at[select_indices[0],'partno']
            df5.at[counter,'quantity'] = df3.at[select_indices[0],'quantity']
            df3.at[select_indices[0],'quantity'] = df3.at[select_indices[0],'quantity']-quantity
            # print(df4)
            # print(df5)
        else:
            df4.at[counter,'partno'] = bomdf.at[counter,'partno']
            df4.at[counter,'quantity'] = bomdf.at[counter,'quantity']
            df5.at[counter,'partno'] = df3.at[select_indices[0],'partno']
            df5.at[counter,'quantity'] = df3.at[select_indices[0],'quantity']
            df3.at[select_indices[0],'quantity'] = df3.at[select_indices[0],'quantity']-quantity

            # print(df4)
            # print(df5)
    else:
        df4.at[counter,'partno'] = bomdf.at[counter,'partno']
        df4.at[counter,'quantity'] = bomdf.at[counter,'quantity']
        df5.at[counter,'partno'] = ''
        df5.at[counter,'quantity'] = ''
    counter = counter+1
for index, row in df3.iterrows():
    if row["quantity"]!=0 and row["quantity"]!=-1:
        df4.at[counter,"partno"] = ''
        df4.at[counter,"quantity"] = ''
        df5.at[counter,"partno"] = row['partno']
        df5.at[counter,"quantity"] = row['quantity']
        counter = counter+1
    counter=counter+1




# Distidf = Distidf.set_index("partno")
# Distidf = Distidf.reindex(index=bomdf['partno'])
# Distidf = Distidf.reset_index()

combineddf = pd.concat([df4, df5],axis=1, keys = ['BomData', 'Distidf'])
# print(df3)
print(combineddf)


