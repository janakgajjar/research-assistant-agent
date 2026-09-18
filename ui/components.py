"""
Reusable Streamlit UI components.
"""

import streamlit as st

from utils.exporter import (
    export_txt,
    export_markdown,
    export_pdf
)

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
    st.subheader("📄 Final Research Report")

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

    st.markdown(report_content)

    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    st.subheader("⬇️ Export Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="📄 Download PDF",
            data=export_pdf(report_content),
            file_name="research_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with col2:
        st.download_button(
            label="📝 Download Markdown",
            data=export_markdown(report_content),
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col3:
        st.download_button(
            label="📃 Download TXT",
            data=export_txt(report_content),
            file_name="research_report.txt",
            mime="text/plain",
            use_container_width=True
        )

def show_history(history):
    """
    Display research history in the Streamlit sidebar.
    """

    with st.sidebar:

        st.markdown(
            "## 🤖 Research Assistant"
        )

        st.divider()

        if st.button(
            "➕ New Research",
            use_container_width=True
        ):
            st.session_state.report = None
            st.session_state.last_topic = ""
            st.rerun()

        st.divider()

        st.markdown("### 📚 History")

        if history:

            if st.button(
                "🗑️ Clear History",
                use_container_width=True
            ):
                st.session_state.research_history = []
                st.rerun()
                
        if not history:

            st.caption(
                "No research reports yet."
            )

            return

        for index, item in enumerate(
            reversed(history)
        ):

            topic = item["topic"]

            if st.button(
                f"🔬 {topic}",
                key=f"history_{index}",
                use_container_width=True
            ):

                st.session_state.report = item["report"]
                st.session_state.last_topic = topic

                st.rerun()