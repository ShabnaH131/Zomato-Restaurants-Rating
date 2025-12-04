import streamlit as st
import pandas as pd
import joblib
import gdown
import os
import time


#page config
st.set_page_config(
    page_title="Zomato Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="wide"  # 👈 This makes the page stretch fully
)



# ---------- LOADING SCREEN ----------
if "loaded" not in st.session_state:
    st.session_state.loaded = True

    loader = st.empty()
    with loader.container():
        st.markdown(
            """
            <style>
            .image-container {
                position:relative;
                width:100%;
                text-align:center;
            }
            .bg-image{
                width:100%;
                opacity:0.35;

            }
            .overlay-text {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 48px;
                font-weight: 700;
                color: #e23744;
                text-shadow: 2px 2px #ffffff;
            }
            .loader-container{
                display:flex;
                flex-direction:column;
                justify-content:center;
                align-items:center;
                height:80vh;
            }
            .emoji{
                font-size:80px;
                animation: spin 1.5s linear infinite;
            }
            @keyframes spin{
                0%{transform:rotate(0deg);}
                100%{transform:rotate(360deg);}
            }
            </style>

            <div class="loader-container">
                <div class="emoji">🍽️</div>
                <h3>Zomato Restaurant Rating Predictor...</h3>
            </div>
            """,
            unsafe_allow_html=True
            
        )
    time.sleep(2)
    loader.empty()

# ---------- PAGE STYLING ----------

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Zomato Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="wide"
)

# ------------------ CSS Styles ------------------
st.markdown("""
<style>
/* Page background */
body {
    background-color: #fff7ee;
}

/* Big title & subtitle (if needed elsewhere) */
.big-title {
    font-size: 48px;
    font-weight: 800;
    color: #e23744;
    text-align: center;
    margin-top: 30px;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}

/* Feature box style */
.feature-box {
    background: white;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}

/* Button style */
.btn-start {
    display: block;
    width: 220px;
    margin: 0 auto;
    margin-top: 25px;
    background-color: #e23744;
    color: white;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    text-decoration: none;
}
.btn-start:hover {
    background-color: #c71f2e;
}

/* Banner image container */
.image-container {
    position: relative;
    width: 100%;
    text-align: center;
    margin-bottom: 20px;
    border-radius: 12px;
}


</style>
""", unsafe_allow_html=True)



# Initial Page State-----------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"


# Load the trained model  (csv file is uploaded in the google drive)
file_id = "14n-s4J1GLh4jnqnqXqA6COdGvut1MVm3"
model_path = "best_model.pkl"

if not os.path.exists(model_path):
    st.write("Downloading model... Please wait!")
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, model_path, quiet=False)

best_model = joblib.load(model_path)

# ------------------ SIDEBAR ----------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ("Home", "Prediction", "Review", "History")
)

#---------Home Page -------------------------------------------------
# ---------- HEADER ----------
if page=="Home":
    page_bg = """
<style>
body {
    background-color: #fff7ee;
}
.big-title {
    font-size: 48px;
    font-weight: 800;
    color: #e23744;
    text-align: center;
    margin-top: 30px;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}
.feature-box {
    background: white;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}
.btn-start {
    display: block;
    width: 220px;
    margin: 0 auto;
    margin-top: 25px;
    background-color: #e23744;
    color: white;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    text-decoration: none;
}
.btn-start:hover {
    background-color: #c71f2e;
}
</style>
"""

    st.markdown("<h1 class='big-title'>Zomato Restaurant Rating Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Predict restaurant ratings using machine learning and real-world data!</p>", unsafe_allow_html=True)

    # ---------- IMAGE BANNER ----------
    st.image(
    "Banner.jpg",
    use_container_width=True,width="content"
    )

    st.write("")
    st.write("---")

    # ---------- FEATURES SECTION ----------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='feature-box'><h3>📊 Smart Predictions</h3><p>Our ML model gives accurate restaurant rating predictions.</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='feature-box'><h3>🍽️ Food Insights</h3><p>Analyze cuisine types, cost, online orders & more.</p></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='feature-box'><h3>⚡ Fast & Easy</h3><p>Simple input form with instant results.</p></div>", unsafe_allow_html=True)

    st.write("---")
    st.write("")

    st.markdown("<div id='predict-section'></div>", unsafe_allow_html=True)


##best_model = joblib.load('https://drive.google.com/file/d/14n-s4J1GLh4jnqnqXqA6COdGvut1MVm3/view?usp=drive_link')

#---Prediction Page--------------
elif page=="Prediction":
    page_bg = """
<style>
body {
    background-color: #fff7ee;
}
.big-title {
    font-size: 48px;
    font-weight: 800;
    color: #e23744;
    text-align: center;
    margin-top: 30px;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}
.feature-box {
    background: white;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}
.btn-start {
    display: block;
    width: 220px;
    margin: 0 auto;
    margin-top: 25px;
    background-color: #e23744;
    color: white;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    text-decoration: none;
}
.btn-start:hover {
    background-color: #c71f2e;
}
</style>
"""
    st.markdown("<div id='predict-section'></div>", unsafe_allow_html=True)
    st.header("🔮 Prediction Section")

    st.write("""
    Predict the rating of a restaurant based on key features.
    """)

    # Input features
    online_order = st.selectbox("Online Order Available?", ["Yes", "No"])
    book_table = st.selectbox("Book Table Available?", ["Yes", "No"])
    votes = st.number_input("Number of Votes", min_value=0, step=1)
    approx_cost = st.number_input("Approx Cost for Two People", min_value=0)

    # Convert inputs to model-ready format
    input_data = pd.DataFrame({
    'online_order': [1 if online_order == "Yes" else 0],
    'book_table': [1 if book_table == "Yes" else 0],
    'votes': [votes],
    'approx_cost(for two people)': [approx_cost]
    })

    # Predict button
    if st.button("Predict Rating"):
        prediction = best_model.predict(input_data)
        st.success(f"Predicted Restaurant Rating: {round(prediction[0], 2)} / 5")

#------ Review Page --------

elif page == "Review":
    st.header("📝 Customer Review & Rating")
    st.write("Share your experience and help improve recommendations!")

    # Initialize session storage
    if "reviews" not in st.session_state:
        st.session_state.reviews = []

    with st.form("review_form"):
        name = st.text_input("Your Name", placeholder="e.g., Ananya")
        rating = st.slider("Your Rating", 1, 5, 5)
        review_text = st.text_area("Write your review")
        submitted = st.form_submit_button("Submit Review")

        if submitted:
            if name and review_text:
                st.session_state.reviews.append({
                    "Name": name,
                    "Rating": rating,
                    "Review": review_text
                })
                st.success("Review submitted successfully!")
            else:
                st.warning("Please fill in all fields!")

    st.write("---")
    st.subheader("📌 Recent Reviews")

    if st.session_state.reviews:
        for r in st.session_state.reviews[::-1]:
            st.markdown(f"**{r['Name']}** — ⭐ {r['Rating']}/5")
            st.write(f"{r['Review']}")
            st.write("---")
    else:
        st.info("No reviews yet — be the first to share!")


# --- History Page -------------------------------------------------
elif page == "History":
    st.header("🏛️ Restaurant History & Highlights")
    st.write("Explore famous restaurants and their stories!")

    restaurant_data = {
        "Barbeque Nation": {
            "location": "Multiple Cities, India",
            "founded": "2006",
            "speciality": "Buffet & Live Grill Experience",
            "story": "Started the concept of live grills at the table and popularized all-you-can-eat dining in India."
        },
        "KFC": {
            "location": "Global • India Launch: 1995",
            "founded": "1930",
            "speciality": "Fried Chicken (Secret 11 Herbs & Spices)",
            "story": "Colonel Sanders turned his home-style fried chicken into a worldwide fast-food empire."
        },
        "Domino's Pizza": {
            "location": "Global • India Launch: 1996",
            "founded": "1960",
            "speciality": "Quick-Serve Pizza Delivery",
            "story": "Became India’s most loved pizza brand with 30-minute delivery and localized flavours."
        },
        "McDonald's": {
            "location": "Global • India Launch: 1996",
            "founded": "1940",
            "speciality": "Burgers & Fast Food",
            "story": "Adapted its menu for India — McAloo Tikki & Maharaja Mac made it a household favourite."
        },
        "Anjappar Chettinad": {
            "location": "Tamil Nadu, India",
            "founded": "1964",
            "speciality": "Authentic Chettinad Cuisine",
            "story": "Brought the fiery flavours of Chettinad to the world with 70+ outlets across countries."
        }
    }

    selected_restaurant = st.selectbox(
        "Choose a restaurant to explore",
        list(restaurant_data.keys())
    )

    details = restaurant_data[selected_restaurant]

    st.subheader(f"🍽️ {selected_restaurant}")
    st.write(f"📍 **Location:** {details['location']}")
    st.write(f"📅 **Established:** {details['founded']}")
    st.write(f"⭐ **Speciality:** {details['speciality']}")
    st.write("📖 **Story:**")
    st.info(details['story'])



