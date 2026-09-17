"""
Streamlit UI Styles

Contains all custom CSS styling for the application.
"""

import streamlit as st


def load_styles():
    """
    Load custom CSS styles for the Streamlit application.
    """

    st.markdown(
        """
        <style>

        /* -----------------------------
           Main Application
        ----------------------------- */

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }


        /* -----------------------------
           Main Title
        ----------------------------- */

        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            opacity: 0.70;
            margin-bottom: 25px;
        }


        /* -----------------------------
           Agent Cards
        ----------------------------- */

        .agent-card {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            min-height: 150px;
        }


        /* -----------------------------
           Report Container
        ----------------------------- */

        .report-card {
            padding: 25px;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            margin-top: 20px;
        }


        /* -----------------------------
           Small Status Text
        ----------------------------- */

        .status-text {
            font-size: 14px;
            opacity: 0.70;
        }

        </style>
        """,
        unsafe_allow_html=True
    )