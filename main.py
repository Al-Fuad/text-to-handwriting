import pywhatkit as pw

txt = """Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation"""

pw.text_to_handwriting(txt)
print("End...")