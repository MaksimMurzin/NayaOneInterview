from Model.file_converter import FileToFrameConverter as file_converter
from Logic.data_operator import DataOperator as data_operator
import numpy as np


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # ============================ Clean data from empty cells ==========================

    df = file_converter("nayaone_loan_data.csv").create_df()
    df = df.replace(r'^\s*$', np.nan, regex=True)[['emp_title', 'annual_income', 'homeownership']]

    # probably not good to drop all NaNs but this is just a demo
    # I didn't want to have everything on one line hence why I put dropna() on a seperate line
    df = df.dropna()

    # new_df.to_csv("dropped_nulls.csv")
# ======================= test the functions ================================

    data_op = data_operator(df)
    mean_value = data_op.get_mean_value('annual_income')
    std_value = data_op.get_std_dev('annual_income')
    outliers = data_op.get_outliers('annual_income')


# ====================== who gets paid the most and do they own property? ======================

#     most_paid = df.nlargest(n=10, columns='annual_income', keep='first')
    # print(most_paid)  # -> vp was the top position for annual income
    # data_frame[(data_frame['emp_title'] == 'vp')]

#  ======================= VPs and Home Ownership =======================================

#     vp_stats = df[(df['emp_title'] == "vp")]
    # print(vp_stats)
# vp_stats.to_csv("vp_stats.csv")

# ========================= Lowest paid Workers ================================================

    # least_paid = df.nsmallest( n= 10, columns='annual_income', keep='first')
    # print(least_paid.mean())

