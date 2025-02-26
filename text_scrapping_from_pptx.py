from pptx import Presentation

# Load the presentation
presentation = Presentation('your_pptx_file_name.pptx')

# Open a file to save the text
with open('desire_output_file_name.txt', 'w') as f:
    # Extract text and write it to the file
    for slide in presentation.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                f.write(shape.text + '\n')  # Write the text and add a newline

print("Text extracted and saved to 'desire_output_file_name.txt'")