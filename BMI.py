import streamlit as st
import pandas as pd
import numpy as np

height = st.text_input("请输入身高(cm)", "190")
height = np.float64(height) / 100

weight = st.text_input("请输入体重(kg)", "50")
weight = np.float64(weight)

BMI = weight / height ** 2

st.write(BMI)

if BMI < 18.5:
    st.error("偏瘦")
    st.write("需要适当增重")

elif 18.5 <= BMI < 24:
    st.error("正常")
    st.write("请继续保持")

elif 24 <= BMI <28:
    st.error("偏重")
    st.write("请适当控制饮食")

else:
    st.error("肥胖")
    st.write("请适当减肥")