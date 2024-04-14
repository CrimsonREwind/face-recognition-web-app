import streamlit as st
import face_recognition as fr
from UserDetail import UserDetail
from db import Database

import image


def register():
    options = ["Camera", "Upload"]
    initial_selection = options.index("Upload")
    method = st.radio("Method", options, index=initial_selection)
    if method == "Camera":
        picture = st.camera_input("picture", key="loginPic", label_visibility='hidden')
    if method == "Upload":
        picture = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if picture:
        form = st.form("Register")
        name = form.text_input("Username")
        min_date = datetime.datetime(1900, 1, 1)
        max_date = datetime.datetime.today()
        dob = form.date_input("DOB", min_value=min_date, max_value=max_date)
        city = form.text_input("City")
        submit = form.form_submit_button("submit")
        if submit:
            if not name or not dob or not city:
                st.error("Please enter your name, DOB and city")
            else:
                st.success("registered successfully")
                user_id = insert_user_detail(city, dob, name)
                know_user_dir = "./known_user/"
                image.save_image(picture, know_user_dir, str(user_id))


def insert_user_detail(city, dob, name):
    user_detail = UserDetail(name, dob, city)
    db = Database()
    user_id = db.insert_user_detail(user_detail)
    return user_id




