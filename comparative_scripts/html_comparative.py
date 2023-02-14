import re
import requests

def extract_text_from_html(filename):
    with open(filename, 'r') as file:
        return file.read()

def compare_htmls(html_filenames):
    vulnerabilities = {}
    for filename in html_filenames:
        text = extract_text_from_html(filename)
        for vulnerability in re.findall(r'<td>(.*?)</td>', text):
            if vulnerability in vulnerabilities:
                vulnerabilities[vulnerability].append(filename)
            else:
                vulnerabilities[vulnerability] = [filename]
    return vulnerabilities

html_filenames = ['report1.html', 'report2.html', 'report3.html']
vulnerabilities = compare_htmls(html_filenames)

for vulnerability, filenames in vulnerabilities.items():
    if len(filenames) > 1:
        print(f'Vulnerability "{vulnerability}" found in the following reports:')
        for filename in filenames:
            print(f'- {filename}')
