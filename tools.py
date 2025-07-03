import re
from docx import Document
from langchain.tools import Tool

def make_italic(doc: Document):
    for para in doc.paragraphs:
        for run in para.runs:
            run.italic = True

HELPERS = {
    "italic": make_italic,
    "italics": make_italic,
    "slanted": make_italic,
    }


def detect_and_call(input_str: str) -> str:
    """
    Detect formatting instruction in the input string and apply it to the document at the given path.
    Example input: "Make everything italic in the file path: outputs/abc.docx"
    """
    if not isinstance(input_str, str):
        raise ValueError("Invalid input format")

    lowered = input_str.lower()

    # Find formatting keyword
    helper_key = None
    for key in HELPERS:
        if key in lowered:
            helper_key = key
            break

    if not helper_key:
        raise ValueError("No formatting instruction found.")

    # Extract file path from the input string
    match = re.search(r"(?:file\s*path|path|file):\s*(\S+\.docx)", lowered)
    if not match:
        raise ValueError("No .docx file path found in input.")

    path = match.group(1)

    # Apply formatting
    doc = Document(path)
    HELPERS[helper_key](doc)
    doc.save(path)
    return f"FinalAnswer: Successfully applied '{helper_key}' formatting to the document at {path}."


# LangChain tool registration
format_tool = Tool(
    name="detect_and_call",
    func=detect_and_call,
    description=(
        "Use this to apply formatting (like italic) to a .docx file. "
        "Input must include a formatting keyword like 'italic' and the file path using 'File path: outputs/xyz.docx'."
    ),
    return_direct=True
)
