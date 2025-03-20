import streamlit as st
import calendar


def main():
    st.title("Gregorian Calendar Viewer")

    year = st.number_input("Enter Year:", min_value=1, max_value=9999, value=2024, step=1)

    if st.button("Show Calendar"):
        cal = calendar.TextCalendar()
        calendar_text = "".join(cal.formatyear(year, 2, 1, 1, 2))
        st.text_area("Gregorian Calendar:", calendar_text, height=400)


if __name__ == "__main__":
    main()