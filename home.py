import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import io 
from  PIL import Image
from awesome_table import AwesomeTable
from awesome_table.column import Column


with st.container():
    with st.sidebar:
        choose = option_menu("Menu Bar", ["Home", "Dataset", "Pre-Processing", "Modelling"],
                            icons=['house', 'clipboard-data', 'activity', 'pie-chart'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#f5bc00"},
            "icon": {"color": "black", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color" : "black"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )

        
    if choose == "Home":
        st.title("Alcohol Effect on Study")
        pict = Image.open(rb'D:\Kuliah\SEMESTER 5\PENAMBANGAN DATA\PROJECT UAS-PENDAT\alcohol.png')
        st.subheader("Pengertian Alcohol")
        st.markdown('<div style="text-align: justify;">Alcohol adalah segala minuman difermentasi yang mengandung etil alkohol atau etanol sebagai zat yang memabukkan. Biasanya minuman alkohol dibuat dari gula yang difermentasi dalam buah-buahan, seperti beri, biji-bijian, dan bahan-bahan lain seperti getah tanaman, umbi-umbian, madu, dan susu. Fermentasi berbagai bahan ini dapat menghasilkan cairan yang memiliki kadar alkohol yang lebih besar dan lebih kuat.</div>', unsafe_allow_html=True)
        st.image(pict, width=700)
        st.markdown('<div style="text-align: justify;">Secara umum, jenis minuman keras dibedakan menjadi beberapa macam. Pertama adalah bir yaitu minuman alkohol yang terbuat dari bahan malt seperti jagung, beras, dan hop. Biasanya bir memiliki kandungan alkohol berkisar antara 2 persen hingga 8 persen. Kedua adalah anggur, yaitu minuman alkohol yang terbuat dari fermentasi jus anggur atau buah-buahan lain seperti apel, ceri, beri, atau prem. Pembuatan anggur dimulai dengan panen buah , yang sarinya difermentasi dalam tong besar di bawah kontrol suhu yang ketat. Saat fermentasi selesai, campuran disaring, didiamkan, dan dibotolkan.</div>', unsafe_allow_html=True)
        
    elif choose == "Dataset":
        st.title("Dataset Alcohol Effect On Study")
        st.subheader("About Dataset")
        st.markdown('<div style="text-align: justify;"> Dataset ini diperoleh dari pencapaian siswa dalam sekolah menengah di dua sekolah yang terletak di Portugis. Atribut dari dataset ini sendiri meliput nilai siswa, demografi, fitur sosial dan terkait sekolah. Dataset ini dikumpulkan dengan menggunakan laporan sekolah dan juga dari kuesioner.</div>', unsafe_allow_html=True)

        df = pd.read_csv("https://raw.githubusercontent.com/bintangradityaputra/contoh/master/Maths.csv")
        df

        st.subheader("Feature Description")

        sample_data = [
            {'fitur' : "school", "deskripsi" : "student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)" },
            {'fitur' : "age", "deskripsi" : "student's sex (binary: 'F' - female or 'M' - male)" },
            {'fitur' : "sex", "deskripsi" : "student's age (numeric: from 15 to 22)" },
            {'fitur' : "address", "deskripsi" : "student's home address type (binary: 'U' - urban or 'R' - rural)" },
            {'fitur' : "famsize", "deskripsi" : "family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)" },
            {'fitur' : "Pstatus", "deskripsi" : "parent's cohabitation status (binary: 'T' - living together or 'A' - apart)" },
            {'fitur' : "Medu", "deskripsi" : "mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)" },
            {'fitur' : "Fedu", "deskripsi" : "father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)" },
            {'fitur' : "Mjob", "deskripsi" : "mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')" },
            {'fitur' : "Fjob", "deskripsi" : "father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')" },
            {'fitur' : "reason", "deskripsi" : "reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')" },
            {'fitur' : "guardian", "deskripsi" : "student's guardian (nominal: 'mother', 'father' or 'other')" },
            {'fitur' : "traveltime", "deskripsi" : "home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)" },
            {'fitur' : "studytime", "deskripsi" : "weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)" },
            {'fitur' : "failures", "deskripsi" : "number of past class failures (numeric: n if 1<=n<3, else 4)" },
            {'fitur' : "schoolsup", "deskripsi" : "extra educational support (binary: yes or no)" },
            {'fitur' : "famsup", "deskripsi" : "family educational support (binary: yes or no)" },
            {'fitur' : "paid", "deskripsi" : "extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)" },
            {'fitur' : "activity", "deskripsi" : "extra-curricular activities (binary: yes or no)" },
            {'fitur' : "nursery", "deskripsi" : "attended nursery school (binary: yes or no)" },
            {'fitur' : "higher", "deskripsi" : "wants to take higher education (binary: yes or no)" },
            {'fitur' : "internet", "deskripsi" : "Internet access at home (binary: yes or no)" },
            {'fitur' : "romantic", "deskripsi" : "with a romantic relationship (binary: yes or no)" },
            {'fitur' : "famrel", "deskripsi" : "quality of family relationships (numeric: from 1 - very bad to 5 - excellent)" },
            {'fitur' : "freetime", "deskripsi" : "free time after school (numeric: from 1 - very low to 5 - very high)" },
            {'fitur' : "goout", "deskripsi" : "going out with friends (numeric: from 1 - very low to 5 - very high)" },
            {'fitur' : "Dalc", "deskripsi" : "workday alcohol consumption (numeric: from 1 - very low to 5 - very high)" },
            {'fitur' : "Walc", "deskripsi" : "weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)" },
            {'fitur' : "health", "deskripsi" : "current health status (numeric: from 1 - very bad to 5 - very good)" },
            {'fitur' : "absences", "deskripsi" : "number of school absences (numeric: from 0 to 93)" },
        ]

        AwesomeTable(pd.json_normalize(sample_data), columns=[
            Column(name='fitur', label='Fitur'),
            Column(name='deskripsi', label='Deskripsi'),
        ], key="deskripsi")

        st.subheader("Grades")

        grades = [
            {'grades' : 'G1', 'desc' : 'first period grade (numeric: from 0 to 20)'},
            {'grades' : 'G2', 'desc' : 'second period grade (numeric: from 0 to 20)'},
            {'grades' : 'G3', 'desc' : 'final grade (numeric: from 0 to 20, output target)'},
        ]

        AwesomeTable(pd.json_normalize(grades), columns=[
            Column(name='grades', label='Grades'),
            Column(name='desc', label='Description'),
        ], key="grades")

        

    
