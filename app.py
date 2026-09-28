"""
Research Assistant Agent
Streamlit Application
"""

import streamlit as st

from ui.styles import load_styles
from ui.components import (
    show_header,
    show_agents,
    show_report,
    show_history,
    show_about,
    show_footer
)

from ai.crew_runner import CrewRunner
from ai.topic_validator import TopicValidator

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Research Assistant Agent",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

if "report" not in st.session_state:
    st.session_state.report = None

if "last_topic" not in st.session_state:
    st.session_state.last_topic = ""

if "research_history" not in st.session_state:
    st.session_state.research_history = []

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

st.caption(
    "Enter a technology or computer-science topic "
    "to generate a structured research report."
)

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Retrieval Augmented Generation",
    label_visibility="collapsed"
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

    # Clear previous report whenever a new
    # research request is started
    st.session_state.report = None
    st.session_state.last_topic = ""

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a research topic first."
        )

    else:

        validator = TopicValidator()

        try:

            # Validate topic before starting CrewAI
            is_valid = validator.validate(topic)

            if is_valid is False:

                st.error(
                    "❌ Invalid Topic\n\n"
                    "Please enter a technology-related "
                    "research topic."
                )

            elif is_valid is None:

                st.error(
                    "⚠️ AI Validation Unavailable\n\n"
                    "The topic could not be validated because "
                    "the AI service is currently unavailable. "
                )
                
            else:

                st.info(
                    f"🔍 Starting research on: **{topic}**"
                )

                status = st.status(
                    "🤖 AI Research Pipeline Running...",
                    expanded=True
                )

                with status:

                    st.write(
                        "🧠 Researcher → collecting and structuring "
                        "technical information"
                    )

                    st.write(
                        "✍️ Writer → preparing the technical report"
                    )

                    st.write(
                        "✅ Reviewer → checking the final report"
                    )

                    runner = CrewRunner()

                    result = runner.run(topic)

                    st.write("🎉 Final report generated")

                status.update(
                    label="✅ Research completed successfully!",
                    state="complete",
                    expanded=False
                )
                st.success(
                    "✅ Research completed successfully!"
                )

                st.session_state.report = result
                st.session_state.last_topic = topic

                st.session_state.research_history.append({
                    "topic": topic,
                    "report": result
                })

                show_report(    
                    st.session_state.report
                )            

        except Exception as e:

            st.error(
                f"❌ Research failed: {str(e)}"
            )


# ============================================================
# DISPLAY STORED REPORT
# ============================================================

if (
    st.session_state.report is not None
    and not generate_button
):

    st.divider()

    st.info(
        f"📄 Showing report for: "
        f"**{st.session_state.last_topic}**"
    )

    show_report(
        st.session_state.report
    )

st.divider()

show_history(
    st.session_state.research_history
)

show_about()

show_footer()