import streamlit as st
import pandas as pd

st.title("Streamlit BMI Calculator with experimental_data_editor")


def bmi_calc(weight, height):
    return weight / (height / 100) ** 2


def bmi_result_classifier(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"



data_list = {"Name": ["Oğuzhan"],
             "Gender": ["Male"],
             "Weight": [90],
             "Height": [181]}

last_calculations = []
last_data_size = 0
dataframe = pd.DataFrame(data_list)
st.text("Please enter your information below")
edited_df = st.experimental_data_editor(dataframe, num_rows="dynamic")


st.write(f"Last Record: **{edited_df.Name.iloc[-1]}**'s BMI result is "
         f"{bmi_calc(edited_df.Weight.iloc[-1], edited_df.Height.iloc[-1]):.2f}, "
         f"this considering as "
         f"'{bmi_result_classifier(bmi_calc(edited_df.Weight.iloc[-1], edited_df.Height.iloc[-1]),edited_df.Gender.iloc[-1])}'")

if edited_df.iloc[-1].isnull().values.any():
    for index, record in edited_df[:-1].iterrows():
        last_record_name = record['Name']
        last_record_gender = record.Gender
        last_record_bmi = record.Weight / (record.Height / 100) ** 2
        last_record_label = bmi_result_classifier(last_record_bmi, last_record_gender)
        last_calculations.append([last_record_name, last_record_gender, last_record_bmi, last_record_label])
        last_data_size = len(edited_df)
else:
    if last_data_size != len(edited_df):
        for index, record in edited_df.iterrows():
            last_record_name = record['Name']
            last_record_gender = record.Gender
            last_record_bmi = record.Weight / (record.Height / 100) ** 2
            last_record_label = bmi_result_classifier(last_record_bmi, last_record_gender)
            last_calculations.append([last_record_name, last_record_gender, last_record_bmi, last_record_label])
            last_data_size = len(edited_df)

st.title("Last Calculations")
last_calculations_df = pd.DataFrame(last_calculations, columns=['Name', 'Gender', 'BMI', 'Result'], index=None)
st.dataframe(last_calculations_df)


