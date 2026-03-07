# import streamlit as st
# from utils.protocol_generator import generate_protocol

# st.set_page_config(page_title="Clinical Trial Protocol Generator")

# st.title("🧬 AI Clinical Trial Protocol Generator")

# st.write("Generate clinical trial protocols using AI + regulatory guidelines.")

# condition = st.text_input("Medical Condition")

# phase = st.selectbox(
#     "Trial Phase",
#     ["Phase 1","Phase 2","Phase 3"]
# )

# intervention = st.text_input("Intervention")

# sample_size = st.number_input(
#     "Sample Size",
#     min_value=10,
#     max_value=1000,
#     value=100
# )

# if st.button("Generate Protocol"):

#     with st.spinner("Generating protocol..."):

#         protocol = generate_protocol(
#             condition,
#             phase,
#             intervention,
#             sample_size
#         )

# st.subheader("Generated Protocol")

# st.write(protocol)
import streamlit as st
from utils.protocol_generator import generate_protocol

st.set_page_config(page_title="Clinical Trial Protocol Generator")

st.title("🧬 AI Clinical Trial Protocol Generator")

st.write("Generate clinical trial protocols using AI + regulatory guidelines.")

condition = st.text_input("Medical Condition")

phase = st.selectbox(
    "Trial Phase",
    ["Phase 1","Phase 2","Phase 3"]
)

intervention = st.text_input("Intervention")

sample_size = st.number_input(
    "Sample Size",
    min_value=10,
    max_value=1000,
    value=100
)

if st.button("Generate Protocol"):

    with st.spinner("Generating protocol..."):

        protocol = generate_protocol(
            condition,
            phase,
            intervention,
            sample_size
        )

    st.subheader("Generated Protocol")

    st.write(protocol)

    # Download button (must be inside this block)
    st.download_button(
        "Download Protocol",
        protocol,
        file_name="clinical_trial_protocol.txt"
    )