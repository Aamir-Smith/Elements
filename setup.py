from setuptools import setup

try:
    from streamlit_elements.core.render import declare_component
    print("declare_component function found")
except ImportError:
    print("streamlit_elements.core.render module not found")
except AttributeError:
    print("declare_component function not found in streamlit_elements.core.render module")
