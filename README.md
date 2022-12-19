# Auction Tool

> Players Auction Tool - Cricket, Football

## Steps to Follow to Setup

- `team_names.txt` includes names of all the teams that are participating


## Background Image Code

```python
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('./event-img/jito-background.png')   
```
