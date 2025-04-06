import streamlit as st
import pandas as pd

# Set up the page title and icon
st.set_page_config(page_title="🍴 Indian Restaurant Recommender", page_icon="🍴")

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .stSelectbox div {
        font-size: 18px;
    }
    .stHeader {
        font-size: 36px;
        color: #FF4B4B;
    }
    .stDataFrame {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and introduction
st.title("🍴 Indian Restaurant Recommender")
st.write("Find the best Indian restaurants based on your preferences!")

# Sample dataset of Indian restaurants
data = {
    "Name": [
        "Bombay Spice", "Delhi Darbar", "Taste of India", "Royal Curry House", "Spice Garden",
        "Mumbai Masala", "Punjab Grill", "Kerala Kitchen", "Hyderabad Biryani House", "Chennai Cafe",
        "Jaipur Flavors", "Goan Shack", "Lucknowi Dawat", "Bengali Bites", "Rajasthani Thali",
        "Gujarati Rasoi", "Kashmiri Kitchen", "Andhra Spice", "Tandoori Nights", "South Indian Delight",
        "North Indian Feast", "Street Food Junction", "Curry Leaf", "Chaat Corner", "Mughlai Mahal"
    ],
    "Cuisine": [
        "North Indian", "North Indian", "Pan-Indian", "Mughlai", "South Indian",
        "Street Food", "Punjabi", "Kerala", "Hyderabadi", "South Indian",
        "Rajasthani", "Goan", "Lucknowi", "Bengali", "Rajasthani",
        "Gujarati", "Kashmiri", "Andhra", "Tandoori", "South Indian",
        "North Indian", "Street Food", "South Indian", "Street Food", "Mughlai"
    ],
    "Location": [
        "Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai",
        "Mumbai", "Delhi", "Kochi", "Hyderabad", "Chennai",
        "Jaipur", "Goa", "Lucknow", "Kolkata", "Jaipur",
        "Ahmedabad", "Srinagar", "Vizag", "Delhi", "Bangalore",
        "Pune", "Mumbai", "Chennai", "Delhi", "Hyderabad"
    ],
    "Price Range": [
        "Medium", "High", "Medium", "High", "Low",
        "Low", "High", "Medium", "Medium", "Low",
        "Medium", "Low", "High", "Medium", "Medium",
        "Low", "High", "Medium", "High", "Low",
        "Medium", "Low", "Medium", "Low", "High"
    ],
    "Rating": [
        4.5, 4.7, 4.3, 4.6, 4.2,
        4.0, 4.8, 4.1, 4.4, 4.0,
        4.3, 4.2, 4.7, 4.1, 4.5,
        4.0, 4.6, 4.2, 4.8, 4.1,
        4.4, 4.0, 4.3, 4.2, 4.7
    ],
    "Description": [
        "Authentic North Indian flavors with a modern twist.",
        "Luxurious dining experience with royal Mughlai dishes.",
        "A mix of Indian cuisines from all over the country.",
        "Elegant restaurant serving rich and creamy curries.",
        "Traditional South Indian dishes in a cozy setting.",
        "Mumbai's famous street food served in a hygienic environment.",
        "Punjabi delicacies with a focus on tandoori dishes.",
        "Kerala's traditional cuisine with a coastal touch.",
        "Famous for its aromatic Hyderabadi biryani.",
        "South Indian breakfast and lunch specialties.",
        "Rajasthani thali with a variety of flavors.",
        "Goan seafood and coastal cuisine.",
        "Lucknowi kebabs and Awadhi cuisine.",
        "Bengali sweets and traditional dishes.",
        "Authentic Rajasthani thali with dal-bati-churma.",
        "Gujarati thali with a variety of vegetarian dishes.",
        "Kashmiri wazwan and traditional dishes.",
        "Spicy Andhra meals with a variety of curries.",
        "Tandoori dishes and kebabs in a lively ambiance.",
        "South Indian dosas, idlis, and vadas.",
        "North Indian curries and breads.",
        "Mumbai's famous street food like vada pav and pav bhaji.",
        "South Indian meals with a variety of curries.",
        "Delhi's famous chaat and street food.",
        "Mughlai dishes like biryani and kebabs."
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filter Restaurants")
cuisine = st.sidebar.selectbox("Select Cuisine", ["All"] + list(df["Cuisine"].unique()))
location = st.sidebar.selectbox("Select Location", ["All"] + list(df["Location"].unique()))
price_range = st.sidebar.selectbox("Select Price Range", ["All"] + list(df["Price Range"].unique()))

# Apply filters
filtered_df = df.copy()
if cuisine != "All":
    filtered_df = filtered_df[filtered_df["Cuisine"] == cuisine]
if location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == location]
if price_range != "All":
    filtered_df = filtered_df[filtered_df["Price Range"] == price_range]

# Display results
st.header("🍽️ Recommended Restaurants")
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.subheader(row["Name"])
        st.write(f"**Cuisine:** {row['Cuisine']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Price Range:** {row['Price Range']}")
        st.write(f"**Rating:** ⭐ {row['Rating']}")
        st.write(f"**Description:** {row['Description']}")
        st.write("---")
else:
    st.warning("No restaurants found matching your preferences. Try adjusting your filters!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 Indian Restaurant Recommender | Developed by Aditya Rajendra Talwatkar"
    "</div>",
    unsafe_allow_html=True,
)
