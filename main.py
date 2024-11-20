import streamlit as st
import dictionary_work as dw
import pandas as pd


directory_path='./files'
information='aqui va algo'

st.set_page_config("Blood sugar log", "🤖", "wide")
# Title of the app
st.title('Blood sugar🍬...👻')

questions = dw.file_form
if len(questions) < 4:
    st.error("The questions list does not have enough elements.")




input_tab,view_tab, info_tab=st.tabs(["🎁 Register", "📝 views", "🗨️ Information"])
# save result
with input_tab:
    #date
    date= str(pd.to_datetime('today').date())
    # question 1    
    question1 = st.text_input(questions[1], 'answer here')

    # question 2
    question2 = st.text_input(questions[2], 'answer here')
    # question 3
    question3 = st.text_input(questions[3], 'answer here')

    if st.button('Save'):
        file={questions[0]:str(date) ,questions[1]:question1, questions[2]: question2, questions[3]:question3}
        dw.save_directory(directory_path,file)
        st.write('good!!Come back!')
    
with  view_tab:  
    questions = dw.file_form
   
    # Open the JSON data
    json_data=dw.open_dictionary(directory_path)
   
    # Create a DataFrame from the JSON data
    df = pd.DataFrame.from_dict(json_data, orient='index').reset_index()
    df.columns = ['Index', questions[0], questions[1], questions[2], questions[3]]
    
    # Display the table in Streamlit
    st.write("log:")
    st.write(df)
#new code
      # Add delete buttons
    for index, row in df.iterrows():
        if st.button(f'Delete row {index}'):
            # Remove the row from the DataFrame
            dw.delete_row(directory_path, str(index))
            st.rerun()


with info_tab:
    
    st.write(information)
        