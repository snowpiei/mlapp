import streamlit as st 
import numpy as np 
from io import BytesIO

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

def app():
     
      st.title(":family:Select the photo you want to use for face recognition ")
      st.subheader("Upload your image and the output will be displayed on the screen")

      uploaded_files = st.file_uploader("", accept_multiple_files=True)
      for uploaded_file in uploaded_files:
       bytes_data = uploaded_file.read()
