import streamlit as st
from exports import save_markdown, save_text, save_pdf
from crew import ResearchAssistantCrew
from ai.crew_runner import CrewRunner

# Page Configuration
st.set_page_config(
    page_title="Research Assistant Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Research Assistant Agent")
st.markdown("Generate professional AI research reports using CrewAI and Gemini.")

st.divider()

# Input
topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Artificial Intelligence"
)

# Button
generate = st.button(
    "🚀 Generate Report",
    use_container_width=True
)

if generate:
    if not topic.strip():
        st.warning("⚠ Please enter a research topic.")

    else:
        try:
            with st.spinner("🤖 Generating research report..."):

                crew_builder = ResearchAssistantCrew(topic)
                crew = crew_builder.run()
                runner = CrewRunner()
                result = runner.run(topic)
                markdown_path = save_markdown(topic, str(result))
                text_path = save_text(topic, str(result))
                pdf_path = save_pdf(topic, str(result))

                markdown_content = markdown_path.read_text(encoding="utf-8")
                text_content = text_path.read_text(encoding="utf-8")
                pdf_content = pdf_path.read_bytes()
            
            st.success("✅ Report Generated Successfully!")
            st.info(f"📁 Report saved to: {markdown_path}")
          
            st.subheader("📄 Generated Report")
            with st.expander("📄 View Generated Report", expanded=True):
                st.markdown(result)

            st.divider()
            st.subheader("📥 Download Report")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.download_button(
                    label="📥 Markdown",
                    data=markdown_content,
                    file_name=markdown_path.name,
                    mime="text/markdown",
                    use_container_width=True
                )
                
            with col2:
                st.download_button(
                    label="📝 TXT",
                    data=text_content,
                    file_name=text_path.name,
                    mime="text/plain",
                    use_container_width=True
                )

            with col3:
                st.download_button(
                label="📄 PDF",
                data=pdf_content,
                file_name=pdf_path.name,
                mime="application/pdf",
                use_container_width=True
            )
                        
        except Exception as e:
                    
            error = str(e)

            if "RESOURCE_EXHAUSTED" in error or "429" in error:
                st.error(
                    "🚫 Gemini API quota exceeded.\n\n"
                    "Please wait a minute and try again, or use another API key/model."
                )
            else:
                st.error(f"❌ {error}")