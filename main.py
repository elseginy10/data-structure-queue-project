import streamlit as st

import json

with open("data/queue.json", "r") as file:
    queue = json.load(file)

st.title(':rainbow[Mahmoud amgad elseginy] \n')
st.title(':rainbow[4211027]')

enqueue_input = st.number_input("Enter a number:", value=0)

enqueue_btn_container,dequeue_container, is_empty_btn_container = st.columns(3)

with enqueue_btn_container:
    enqueue_btn = st.button("enqueue")

if enqueue_btn and enqueue_input != "":
    queue.append(enqueue_input)

with dequeue_container:
    dequeue_btn = st.button("dequeue")

with is_empty_btn_container:
    is_empty_btn = st.button("Is empty")

if dequeue_btn:
    queue.pop(0)

st.write(' <- '.join(map(str, queue)))

if is_empty_btn:
    if not queue:
        st.error("The queue is empty")
        st.balloons()
    else:
        st.success("The queue is not empty")
        st.snow()
    
with open("data/queue.json", "w") as file:
    json.dump(queue, file)
