"""
Streamlit UI Styles

Contains all custom CSS styling for the application.
"""

import streamlit as st


def load_styles():

    st.markdown(
        """
        <style>

        /* Main application container */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        /* Agent cards */
        .agent-card {
            padding: 22px;
            border-radius: 14px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            min-height: 175px;
            transition: all 0.2s ease;
        }

        .agent-card:hover {
            border-color: rgba(128, 128, 128, 0.45);
            transform: translateY(-2px);
        }

        /* Report container */
        .report-card {
            padding: 28px;
            border-radius: 14px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            margin-top: 20px;
            line-height: 1.7;
        }

        /* Secondary text */
        .status-text {
            font-size: 14px;
            opacity: 0.70;
        }

        /* Sidebar spacing */
        section[data-testid="stSidebar"] {
            padding-top: 1rem;
        }

        /* Download buttons */
        div.stDownloadButton > button {
            width: 100%;
        }

        /* Slightly cleaner dividers */
        hr {
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )