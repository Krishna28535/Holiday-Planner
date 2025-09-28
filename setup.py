from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
	name="holiday-planner",
	version="0.1.0",
	description="Add your description here",
	long_description=(here / "README.md").read_text() if (here / "README.md").exists() else "" ,
	long_description_content_type="text/markdown",
	author="",
	python_requires=">=3.11",
	packages=find_packages(),
	install_requires=[
		"langchain",
		"langchain-community",
		"langchain-experimental",
		"fastapi",
		"python-dotenv",
		"streamlit",
		"uvicorn",
		"pydantic",
		"httpx",
		"requests",
		"langchain_google_community",
		"langchain_tavily",
		"langchain_groq",
		"langchain_openai",
		"langgraph",
		"langchain-google-community[places]",
	],
	include_package_data=True,
	entry_points={
		"console_scripts": [
			"holiday-planner=main:main",
		],
	},
)
