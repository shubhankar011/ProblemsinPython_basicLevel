from PyPDF2 import PdfReader, PdfWriter

input_path = "D:\\PracticeInProgramming\\Python\\HeadFirstPython.pdf"
reader = PdfReader(input_path)
total_pages = len(reader.pages)
n = int(input("Enter the number of parts you want to make: "))

print(f"Total pages: {total_pages}")
part_size = total_pages // n

for i in range(n):
    writer = PdfWriter()
    start_page = i * part_size
    end_page = (i + 1) * part_size if i < (n-1) else total_pages 

    for j in range(start_page, end_page):
        writer.add_page(reader.pages[j])

    output_path = f"Part_{i+1}.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Created {output_path} ({end_page - start_page} pages)")