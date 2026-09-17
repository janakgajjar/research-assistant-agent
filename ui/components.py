"""
Reusable Streamlit UI components.
"""

import streamlit as st


def show_header():
    """
    Display application header.
    """

    st.markdown(
        '<div class="main-title">🤖 Research Assistant Agent</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Multi-Agent AI Research System powered by CrewAI'
        '</div>',
        unsafe_allow_html=True
    )


def show_agents():
    """
    Display the three AI agents.
    """

    st.subheader("🧠 Multi-Agent System")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="agent-card">

            ### 🔎 Researcher

            **Role:** AI Research Analyst

            Finds and organizes relevant information.

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="agent-card">

            ### ✍️ Writer

            **Role:** Technical Content Writer

            Converts research into a structured report.

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="agent-card">

            ### ✅ Reviewer

            **Role:** Quality Reviewer

            Checks accuracy, clarity and completeness.

            </div>
            """,
            unsafe_allow_html=True
        )


def show_report(report):
    """
    Display the final generated research report.
    """

    st.subheader("📄 Final Research Report")

    # CrewAI returns a CrewOutput object.
    # We need to extract the actual final content.
    if hasattr(report, "raw"):
        report_content = report.raw
    elif hasattr(report, "output"):
        report_content = report.output
    else:
        report_content = str(report)

    st.markdown(
        '<div class="report-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        report_content
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )