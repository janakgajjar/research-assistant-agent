"""
Research Assistant Agent
Streamlit Application
"""

import streamlit as st

from ui.styles import load_styles
from ui.components import (
    show_header,
    show_agents,
    show_report
)

from crew import ResearchAssistantCrew
from ai.llm_manager import get_llm


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Research Assistant Agent",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# LOAD UI STYLES
# ============================================================

load_styles()


# ============================================================
# HEADER
# ============================================================

show_header()

st.divider()


# ============================================================
# AGENT INFORMATION
# ============================================================

show_agents()

st.divider()


# ============================================================
# RESEARCH INPUT
# ============================================================

st.subheader("🔬 Start New Research")

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Agentic AI in Healthcare"
)


# ============================================================
# GENERATE REPORT
# ============================================================

generate_button = st.button(
    "🚀 Generate Research Report",
    type="primary",
    use_container_width=True
)


# ============================================================
# EXECUTION
# ============================================================

if generate_button:

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a research topic first."
        )

    else:

        st.info(
            f"🔍 Starting research on: **{topic}**"
        )

        try:

            with st.spinner(
                "🤖 Researcher → Writer → Reviewer are working..."
            ):

                llm = get_llm()

                crew = ResearchAssistantCrew(
                    topic=topic,
                    llm=llm
                )

                result = crew.run()

            st.success(
                "✅ Research completed successfully!"
            )

            show_report(result)

        except Exception as e:

            st.error(
                f"❌ Research failed: {str(e)}"
            )