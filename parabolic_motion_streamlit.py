import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

G = 9.8  # 地球上の重力加速度 [m/s²]

st.title("放物運動シミュレーション")

# -----------------------------
# 条件をスライダーで設定
# -----------------------------
v0 = st.slider(
    "初速度 v₀ [m/s]",
    min_value=1.0,
    max_value=30.0,
    value=15.0,
)

angle = st.slider(
    "投射角 θ [°]",
    min_value=0,
    max_value=90,
    value=45,
)

x_max = st.number_input(
    "X軸上限 [m]",
    min_value=1.0,
    value=100.0,
)

y_max = st.number_input(
    "Y軸上限 [m]",
    min_value=1.0,
    value=50.0,
)

# -----------------------------
# 放物運動の計算
# -----------------------------
theta = np.radians(angle)

vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

# 地面に戻ってくるまでの時間
if vy > 0:
    flight_time = 2 * vy / G
else:
    flight_time = 0.1

t = np.linspace(0, flight_time, 200)

# 位置
x = vx * t
y = vy * t - 0.5 * G * t**2

# -----------------------------
# 結果を表示
# -----------------------------
st.write(f"飛行時間：{flight_time:.2f} s")
st.write(f"水平到達距離：{x[-1]:.2f} m")
st.write(f"最高点：{(vy**2) / (2 * G):.2f} m")

# -----------------------------
# グラフ
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Projectile Motion")
ax.grid()
ax.set_xlim(0, x_max)
ax.set_ylim(0, y_max)

st.pyplot(fig)
