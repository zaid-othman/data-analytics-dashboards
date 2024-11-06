
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
df = pd.read_csv('tips.csv')
st.set_page_config(layout='wide')
#sidebar
st.sidebar.header('tips dashBoard')
st.sidebar.image('tips.jpg')
st.sidebar.text('this is a dash board for tips wellllcome')

st.sidebar.write('')
st.sidebar.markdown('made with creativity !! [Zaid Othman](https://www.udemy.com/course/python-data-analysis-diploma/learn/lecture/41036084#overview) ')
st.sidebar.write('')
st.sidebar.write('filters !')
cat_filtering=st.sidebar.selectbox('Categorical',[None,'sex','smoker','day','time'])
con_filtering=st.sidebar.selectbox('cont. data',[None,'size','tip'])


rowFilter=st.sidebar.selectbox('row',[None,'sex','smoker','day','time'])
colFilter=st.sidebar.selectbox('col',[None,'size','tip'])



# main
st.subheader('tips vs total bills')
a1,a2,a3=st.columns(3)
a1.metric('max',df['total_bill'].max())
a2.metric('min',df['total_bill'].min())
a3.metric('avg',df['total_bill'].mean())

fig = px.scatter(data_frame =df , x='total_bill',
                 y='tip',
                 color = cat_filtering,
                 size =con_filtering,
                 facet_col=colFilter,
                 facet_row=rowFilter)


st.plotly_chart(fig , use_container_width=True)




c1,c2,c3=st.columns((4,3,3))


with c1:
    st.text('sex vs TB')
    fig2=px.bar(df,x='sex',y='total_bill',color=cat_filtering)
    st.plotly_chart(fig2, use_container_width=True)

with c2:
    st.text('smoker vs tips')
    fig3=px.pie(df,names='smoker',values='tip',color=cat_filtering)
    st.plotly_chart(fig3, use_container_width=True)

with c3:
    st.text('days vs tips')
    fig4=px.pie(df,names='day',values='tip',hole=0.4)
    st.plotly_chart(fig4, use_container_width=True)