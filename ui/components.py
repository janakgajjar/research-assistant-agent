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
    st.markdown(
        "# 🤖 Research Assistant Agent"
    )

    st.caption(
        "Multi-Agent AI Research System powered by CrewAI"
    )


def show_agents():
    st.subheader("🧠 Multi-Agent System")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="agent-card">
                <div style="font-size: 30px;">🔎</div>
                <div style="font-size: 20px; font-weight: 700;">
                    Researcher
                </div>
                <div class="status-text">
                    AI Research Analyst
                </div>
                <br>
                Finds and organizes relevant
                technical information.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="agent-card">
                <div style="font-size: 30px;">✍️</div>
                <div style="font-size: 20px; font-weight: 700;">
                    Writer
                </div>
                <div class="status-text">
                    Technical Content Writer
                </div>
                <br>
                Converts research into a
                structured technical report.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="agent-card">
                <div style="font-size: 30px;">✅</div>
                <div style="font-size: 20px; font-weight: 700;">
                    Reviewer
                </div>
                <div class="status-text">
                    Quality Reviewer
                </div>
                <br>
                Checks accuracy, clarity
                and completeness.
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

def show_about():
    """
    Display project information in the sidebar.
    """

    with st.sidebar:

        st.divider()

        with st.expander("ℹ️ About Project"):

            st.markdown("### 🤖 Research Assistant Agent")

            st.caption(
                "Multi-Agent AI Research System"
            )

            st.markdown(
                """
                An AI-powered research assistant that
                validates technology topics and uses
                specialized AI agents to research, write,
                and review technical reports.
                """
            )

            st.markdown("#### 🧠 Agent Architecture")

            st.markdown(
                """
                **🔎 Researcher**  
                Researches and structures technical information.

                **✍️ Writer**  
                Converts research into a professional report.

                **✅ Reviewer**  
                Reviews the report for accuracy,
                clarity and completeness.
                """
            )

            st.markdown("#### ⚙️ Technology Stack")

            st.markdown(
                """
                - 🐍 Python
                - 🤖 CrewAI
                - ✨ Google Gemini
                - 🔌 LiteLLM
                - 🎨 Streamlit
                - 📄 ReportLab
                """
            )

            st.markdown("#### 🔄 Workflow")

            st.code(
                "Topic Validation\n"
                "      ↓\n"
                "Researcher\n"
                "      ↓\n"
                "Writer\n"
                "      ↓\n"
                "Reviewer\n"
                "      ↓\n"
                "Final Report",
                language="text"
            )

            st.markdown("#### 📄 Export Formats")

            st.write(
                "PDF • Markdown • TXT"
            )

            st.caption(
                "Built as an MCA Agentic AI project."
            )

def show_footer():
    st.divider()

    st.caption(
        "🤖 Research Assistant Agent  •  "
        "Agentic AI Project  •  "
        "@copyright 2026 - All right reserved"
    )