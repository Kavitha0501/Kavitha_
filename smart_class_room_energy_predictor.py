import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Power Consumption Predictor",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("⚡ Smart Classroom Energy Predictor")
st.subheader("AI-Based Sustainable Energy Monitoring System")
st.write("Predict electricity usage, cost, and carbon impact in real time.")

# ---------------- SAMPLE DATA ----------------
data = {
    'hour': [1, 2, 3, 4, 5, 6, 7],
    'temperature': [28, 29, 30, 31, 32, 33, 34],
    'devices_on': [2, 3, 4, 5, 6, 7, 8],
    'power': [3, 4, 5, 6, 8, 9, 11]
}

df = pd.DataFrame(data)

# ---------------- MODEL TRAINING ----------------
X = df[['hour', 'temperature', 'devices_on']]
y = df['power']

model = LinearRegression()
model.fit(X, y)

# ---------------- SIDEBAR INPUT ----------------
st.sidebar.header("📊 Enter Current Data")

hour = st.sidebar.slider("Hour", 0, 24, 8)
temperature = st.sidebar.slider("Temperature (°C)", 20, 45, 30)
devices_on = st.sidebar.slider("Number of Devices ON", 1, 20, 5)

# ---------------- PREDICTION ----------------
prediction = model.predict([[hour, temperature, devices_on]])
predicted_power = prediction[0]

# ---------------- COST ----------------
rate_per_unit = 8
estimated_bill = predicted_power * rate_per_unit
monthly_bill = estimated_bill * 30

# ---------------- PEAK HOUR ----------------
peak_hour = hour + 2 if hour < 22 else hour

# ---------------- CARBON EMISSION ----------------
carbon = predicted_power * 0.82

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("⚡ Predicted Power", f"{predicted_power:.2f} kWh")

with col2:
    st.metric("💰 Estimated Cost", f"₹ {estimated_bill:.2f}")

with col3:
    st.metric("📅 Monthly Forecast", f"₹ {monthly_bill:.2f}")

# ---------------- ADDITIONAL METRICS ----------------
col4, col5 = st.columns(2)

with col4:
    st.metric("⏰ Peak Hour Forecast", f"{peak_hour}:00")

with col5:
    st.metric("♻ CO₂ Emission", f"{carbon:.2f} kg")

# ---------------- ALERT ----------------
if predicted_power > 15:
    st.error("⚠ High energy consumption detected!")
elif predicted_power > 10:
    st.warning("⚠ Moderate energy usage")
else:
    st.success("✅ Energy usage is efficient")

# ---------------- AI ADVISOR ----------------
st.subheader("🤖 AI Energy Advisor")

if predicted_power > 15:
    st.write("• Peak load risk detected")
    st.write("• Reduce AC usage during afternoon")
    st.write("• Switch off unused lights and fans")
    st.write("• Shift heavy appliances to morning hours")
elif predicted_power > 10:
    st.write("• Moderate consumption detected")
    st.write("• Monitor unused devices")
    st.write("• Optimize fan and AC usage")
else:
    st.write("• Energy usage is optimized")
    st.write("• Maintain current consumption pattern")

# ---------------- SUSTAINABILITY SCORE ----------------
st.subheader("🌍 Sustainability Score")

score = max(0, 100 - int(predicted_power * 4))
st.progress(score)
st.write(f"Score: {score}/100")

# ---------------- GRAPH ----------------
st.subheader("📈 Live Energy Trend")

fig, ax = plt.subplots()

ax.plot(df['hour'], df['power'], marker='o')
ax.scatter(hour, predicted_power, s=120)
ax.set_xlabel("Hour")
ax.set_ylabel("Power (kWh)")
ax.set_title("Power Consumption Trend")

st.pyplot(fig)

# ---------------- FUTURE DEPLOYMENT ----------------
st.subheader("🏫 Deployment Use Cases")
st.write("• Smart classrooms")
st.write("• College hostels")
st.write("• Computer labs")
st.write("• Office buildings")