import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def main():
    # Create a page dropdown
    image = Image.open('hsv.jpg')
    st.sidebar.image(image,width=100)
    st.sidebar.title("Guvi_Insurance")
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.title("Guvi_Insurance")   
    with col2:
        st.image(image,  width=150)
    page = st.sidebar.selectbox("Select One", ['ABOUT',"PREDICTION"])
    if page == "ABOUT":
        st.title('Welcome to Guvi_Insurance')
        st.subheader('.')
        st.write('Creator Profile:')
        st.write('**Creators:** Jayabarathi')
        st.write('**Creators:** Kaviarasan K G')
        st.write('**Creators:** Ashwin')

    if page == "PREDICTION":
        st.title('PREDICTION')
        age = st.slider("select the age of the person",int(data.age.min()),int(data.age.max()))
        job = st.selectbox("Select the occupation ",data.job.unique())
        if job == 'blue-collar':
            grouped=data[data['job']=='blue-collar']
            job = 0
        elif job == 'entrepreneur':
            grouped=data[data['job']=='entrepreneur']
            job = 1
        elif job == 'housemaid':
            grouped=data[data['job']=='housemaid']
            job = 2
        elif job == 'services':
            grouped=data[data['job']=='services']
            job = 3
        elif job == 'technician':
            grouped=data[data['job']=='technician']
            job = 4
        elif job == 'technician':
            grouped=data[data['job']=='unknown']
            job = 5
        elif job == 'self-employed':
            grouped=data[data['job']=='self-employed']
            job = 6
        elif job == 'admin.':
            grouped=data[data['job']=='admin.']
            job=7
        elif job == 'management':
            grouped=data[data['job']=='management']
            job=8
        elif job == 'unemployed':
            grouped=data[data['job']=='unemployed']
            job=9
        elif job == 'retired':
            grouped=data[data['job']=='retired']
            job=10
        elif job == 'student':
            grouped=data[data['job']=='student']
            job=11
        
        education_qual = st.selectbox("Select the education_qualification ",data.education_qual.unique())
        if education_qual == 'primary':
            grouped=data[data['education_qual']=='primary']
            education_qual = 0
        elif education_qual == 'secondary':
            grouped=data[data['education_qual']=='secondary']
            education_qual=1
        elif education_qual == 'unknown':
            grouped=data[data['education_qual']=='unknown']
            education_qual=2
        elif education_qual == 'tertiary':
            grouped=data[data['education_qual']=='tertiary']
            education_qual=3

        day = st.slider("select the day ",int(data.day.min()),int(data.day.max()))
        st.write('**from 0 to 11 is jan to dec')
        mon = st.slider("select the month ",int(data.mon.min()),int(data.mon.max()))
        dur = st.slider("select the call duration ",int(data.dur.min()),int(data.dur.max()))
        num_calls = st.slider("select the no of calls ",int(data.num_calls.min()),int(data.num_calls.max()))


        marital_divorced = st.radio("marital_divorced",data.marital_divorced.unique())
        if marital_divorced == 'Yes':
            marital_divorced = 1
        else:
            marital_divorced = 0
        
        marital_married = st.radio("marital_married",data.marital_married.unique())
        if marital_married == 'Yes':
            marital_married = 1
        else:
            marital_married = 0
        
        marital_single = st.radio("marital_single",data.marital_single.unique())
        if marital_single == 'Yes':
            marital_single = 1
        else:
            marital_single = 0
        
        prev_outcome_failure = st.radio("prev_outcome_failure",data.prev_outcome_failure.unique())
        if prev_outcome_failure == 'Yes':
            prev_outcome_failure=1
        else:
            prev_outcome_failure=0

        prev_outcome_other = st.radio("prev_outcome_other",data.prev_outcome_other.unique())
        if prev_outcome_other == 'Yes':
            prev_outcome_other=1
        else:
            prev_outcome_other=0
        
        prev_outcome_success = st.radio("prev_outcome_success",data.prev_outcome_success.unique())
        if prev_outcome_success == 'Yes':
            prev_outcome_success=1
        else:
            prev_outcome_success=0

        input = pd.DataFrame([age,job,education_qual,call_type, day, mon, dur,num_calls, marital_divorced,marital_married,
        marital_single,prev_outcome_failure,prev_outcome_other,prev_outcome_success,prev_outcome_unknown],columns=['age', 'job', 'education_qual', 'call_type', 'day', 'mon', 'dur','num_calls', 'marital_divorced', 'marital_married',
        'marital_single', 'prev_outcome_failure', 'prev_outcome_other','prev_outcome_success', 'prev_outcome_unknown'],index=['index'])


        if st.button("Predict"):
            valu = classifier.predict(input)
            if valu==0:
                st.write('DECLINED')
            else:
                st.write('DECLINED')
                st.snow()

        if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
