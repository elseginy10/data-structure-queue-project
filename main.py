import streamlit as st

import json

with open("data/queue.json", "r") as file:
    queue = json.load(file)


enqueue_input_container, enqueue_btn_container = st.columns(2)

with enqueue_input_container:
    enqueue_input = st.number_input("Enter a number:", value=0)

with enqueue_btn_container:
    enqueue_btn = st.button("enqueue")

if enqueue_btn and enqueue_input != "":
    queue.append(enqueue_input)

dequeue_container, is_empty_btn_container = st.columns(2)

with dequeue_container:
    dequeue_btn = st.button("dequeue")

with is_empty_btn_container:
    is_empty_btn = st.button("Is empty")

if dequeue_btn:
    queue.pop(0)

st.write(queue)

if is_empty_btn:
    st.write(f"The queue is {'not empty' if queue else 'empty'}")

    if not queue:
        st.balloons()
    



with open("data/queue.json", "w") as file:
    json.dump(queue, file)
