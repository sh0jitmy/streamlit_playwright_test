import streamlit as st

def main():
    st.title("周波数および送信出力設定")

    # 周波数の入力フォーム
    frequency = st.number_input("周波数 (225-399MHz)", min_value=225, max_value=399, step=1)

    # 送信出力の選択フォーム
    output_power = st.selectbox("送信出力", ["高", "中", "低"])

    # 送信ボタン
    if st.button("送信"):
        st.write(f"周波数: {frequency} MHz")
        st.write(f"送信出力: {output_power}")

if __name__ == "__main__":
    main()
