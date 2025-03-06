import streamlit as st

def convert(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict[from_unit]:
        return value * conversion_dict[from_unit][to_unit], f"📏 Formula: {value} * {conversion_dict[from_unit][to_unit]}"
    return "❌ Invalid conversion", ""

def convert_temperature(value, from_unit, to_unit):
    if from_unit in temperature_units and to_unit in temperature_units[from_unit]:
        formula = f"🔥 Formula: ({value} * 9/5) + 32" if from_unit == "Celsius" else f"❄️ Formula: ({value} - 32) * 5/9"
        return temperature_units[from_unit][to_unit](value), formula
    return "❌ Invalid conversion", ""

# Conversion data
length_units = {"meters": {"feet": 3.28084, "inches": 39.3701, "cm": 100}, "feet": {"meters": 0.3048, "inches": 12, "cm": 30.48}}
weight_units = {"kg": {"pounds": 2.20462}, "pounds": {"kg": 0.453592}}
temperature_units = {"Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32}, "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9}}
time_units = {"seconds": {"minutes": 1/60, "hours": 1/3600}, "minutes": {"seconds": 60, "hours": 1/60}, "hours": {"seconds": 3600, "minutes": 60}}

# Streamlit UI
st.set_page_config(page_title="Unit Convert", page_icon="🌍", layout="centered")
# Custom CSS for background color and styling
st.markdown(
    """
    <style>
        /* Main Page Styling */
        body {
            background-color: #ede7f6;
        }
        .stApp {
            background-color:rgb(248, 208, 185);
            padding: 20px;
            border-radius: 10px;
        }
        
           h1 {
            color: black !important;
            text-align: center;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
           background:black;
            padding: 20px;
            
        }
        
        [data-testid="stSidebar"] h2 {
            color: white !important;
            text-align: center;
        }
       [data-testid="stSidebarContent"] label, 
       [data-testid="stSidebar > stSelectbox"] label {
           color: white !important;
          }
        [data-testid="stSelectbox"] label {
            color: black;
        }
        [data-testid="stNumberInput"] label {
            color:black;
        }
       
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("🌎 Universal Unit Converter")
st.sidebar.header("⚙️ Select Conversion Type")
unit_type = st.sidebar.selectbox("🔀 Conversion Type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "⏳ Time"])
value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)

if unit_type == "📏 Length":
    with col1:
        from_unit = st.selectbox("🔄 From", list(length_units.keys()))
    with col2:
        to_unit = st.selectbox("➡️ To", list(length_units.keys()))
    if st.button("🔄 Convert"):
        result, formula = convert(value, from_unit, to_unit, length_units)
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")
        st.info(formula)

elif unit_type == "⚖️ Weight":
    with col1:
        from_unit = st.selectbox("🔄 From", list(weight_units.keys()))
    with col2:
        to_unit = st.selectbox("➡️ To", list(weight_units.keys()))
    if st.button("🔄 Convert"):
        result, formula = convert(value, from_unit, to_unit, weight_units)
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")
        st.info(formula)

elif unit_type == "🌡️ Temperature":
    with col1:
        from_unit = st.selectbox("🔄 From", list(temperature_units.keys()))
    with col2:
        to_unit = st.selectbox("➡️ To", list(temperature_units.keys()))
    if st.button("🔄 Convert"):
        result, formula = convert_temperature(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")
        st.info(formula)

elif unit_type == "⏳ Time":
    with col1:
        from_unit = st.selectbox("🔄 From", list(time_units.keys()))
    with col2:
        to_unit = st.selectbox("➡️ To", list(time_units.keys()))
    if st.button("🔄 Convert"):
        result, formula = convert(value, from_unit, to_unit, time_units)
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")
        st.info(formula)

st.markdown("---")
st.markdown("<h6 style='text-align: center; color:black'>Created by 💖 Rimsha Sultan</h4>", unsafe_allow_html=True)


