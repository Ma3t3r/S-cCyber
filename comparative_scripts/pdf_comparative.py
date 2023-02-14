import PyPDF2

def extract_text_from_pdf(filename):
    with open(filename, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()
        return text

def compare_pdfs(pdf_filenames):
    vulnerabilities = {}
    for filename in pdf_filenames:
        text = extract_text_from_pdf(filename)
        for vulnerability in text.split():
            if vulnerability in vulnerabilities:
                vulnerabilities[vulnerability].append(filename)
            else:
                vulnerabilities[vulnerability] = [filename]
    return vulnerabilities

pdf_filenames = ['report1.pdf', 'report2.pdf', 'report3.pdf']
vulnerabilities = compare_pdfs(pdf_filenames)

for vulnerability, filenames in vulnerabilities.items():
    if len(filenames) > 1:
        print(f'Vulnerability "{vulnerability}" found in the following reports:')
        for filename in filenames:
            print(f'- {filename}')
