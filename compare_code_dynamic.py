import streamlit as st
import difflib
import re
import os

st.success("Interactive Source Code Comparison Developed By Bahrul Rozak")

# Language selection
language = st.selectbox("Select Programming Language", ["Python", "JavaScript", "Java", "C++"])
col1, col2 = st.columns(2)

with col1:
    st.subheader("First Source Code")
    code1 = st.text_area("Enter First Source Code", height=300)

with col2:
    st.subheader("Second Source Code")
    code2 = st.text_area("Enter Second Source Code", height=300)

uploaded_file1 = st.file_uploader("Or upload the first source code file", type=["py", "js", "java", "cpp"])
uploaded_file2 = st.file_uploader("Or upload the second source code file", type=["py", "js", "java", "cpp"])

if uploaded_file1 is not None:
    code1 = uploaded_file1.read().decode("utf-8")

if uploaded_file2 is not None:
    code2 = uploaded_file2.read().decode("utf-8")

def highlight_differences(code1, code2):
    d = difflib.ndiff(code1.splitlines(), code2.splitlines())
    diff = '\n'.join(d)
    colored_diff = re.sub(r'^\s*[-].*$', lambda x: f"<span style='color:red;'>{x.group()}</span>", diff, flags=re.MULTILINE)
    colored_diff = re.sub(r'^\s*[+].*$', lambda x: f"<span style='color:green;'>{x.group()}</span>", colored_diff, flags=re.MULTILINE)
    return colored_diff

if st.button("Compare"):
    if code1 and code2:
        st.subheader("First File Content")
        st.code(code1, language=language.lower())
        st.subheader("Second File Content")
        st.code(code2, language=language.lower())
        
        st.subheader("Comparison:")
        diff = highlight_differences(code1, code2)
        st.markdown(diff, unsafe_allow_html=True)
        
        st.markdown("### Explanation of Symbols:")
        st.markdown("""    
            - <span style='color:red;'>`-`</span> indicates lines present in the first file but not in the second.
            - <span style='color:green;'>`+`</span> indicates lines present in the second file but not in the first.
            - Unchanged lines are not highlighted.
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter both code snippets or upload files to compare.")

st.markdown("<div style='text-align: center;'><img src='https://dashboard.codepolitan.com/assets/img/codepolitan-logo.png' alt='Placeholder Image' /></div>", unsafe_allow_html=True)
