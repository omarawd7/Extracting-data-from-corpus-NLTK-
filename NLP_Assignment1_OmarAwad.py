import nltk
import re
import requests
from bs4 import BeautifulSoup
import os

# Get the directory of the current script (where your code file is located)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path for the new file (beside the code file)


# Download the required corpus
nltk.download('nps_chat')
# Load the NLTK corpus
corpus = nltk.corpus.nps_chat.raw()

# Task 1: Extract all words starting with a capital letter

#A regex to find the words starting with a capital letter
capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', corpus)
# Construct the full path for the new file (beside the code file)
file_path = os.path.join(script_dir, "WordsStartingWithCapLetter.txt")
try:
  with open(file_path, "x") as f:
    f.write("Words starting with capital letters:\n")
    f.write('\n'.join(capital_words))
except FileExistsError:
  print("File 'WordsStartingWithCapLetter.txt' already exists.")
  with open(file_path, "w") as f1:
    f1.write("Words starting with capital letters:\n")
    f1.write('\n'.join(capital_words))
# Task 2: Extract all dates with the given formats
# URL of a website that contains many date formats
url = "https://docs.oracle.com/cd/E41183_01/DR/Date_Format_Types.html"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all text elements in the HTML
text_elements = soup.find_all(text=True)

# Join the text elements into a single string
text = " ".join(text_elements)

date_formats = r'\b(\d{2}(/|-)\d{2}(/|-)\d{4})|(\d{1}(/|-)\d{2}(/|-)\d{4})|(\d{2}(/|-)\d{1}(/|-)\d{4})|(\d{4}(/|-)\d{2}(/|-)\d{2})\b'
dates = re.findall(date_formats, text)
dates = ["".join(date) for date in dates]  # Convert tuples to strings
# Remove double slashes at the end of dates
dates = [date.rstrip('/') for date in dates]
# Construct the full path for the new file (beside the code file)
file_path = os.path.join(script_dir, "ExtractedDates.txt")
try:
  with open(file_path, "x") as f:
       f.write("Extracted dates:\n")
       f.write('\n'.join(dates))
except:
  with open(file_path, "w") as f:
    f.write("Extracted dates:\n")
    f.write('\n'.join(dates))
#'(?!\b(auto|bool|break|case|catch|char|class|const|continue|default|delete|do|double|else|enum|extern|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|operator|private|protected|public|register|return|short|signed|sizeof|static|struct|switch|template|this|throw|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|wchar_t|while)\b)
# Task 3: Extract all C++ variables
#Exculding C++ keywords
    cpp_keywords = [
    "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit",
    "atomic_noexcept", "auto", "bitand", "bitor", "bool", "break", "case", "catch",
    "char", "char8_t", "char16_t", "char32_t", "class", "compl", "concept", "const",
    "consteval", "constexpr", "constinit", "const_cast", "continue", "co_await",
    "co_return", "co_yield", "decltype", "default", "delete", "do", "double",
    "dynamic_cast", "else", "enum", "explicit", "export", "extern", "false", "float",
    "for", "friend", "goto", "if", "inline", "int", "long", "mutable", "namespace",
    "new", "noexcept", "not", "not_eq", "nullptr", "operator", "or", "or_eq",
    "private", "protected", "public", "register", "reinterpret_cast", "requires",
    "return", "short", "signed", "sizeof", "static", "static_assert",
    "static_cast", "struct", "switch", "synchronized", "template", "this",
    "thread_local", "throw", "true", "try", "typedef", "typeid", "typename",
    "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t",
    "while", "xor", "xor_eq"
]
cpp_keywords_pattern = r'\b(?:{})\b'.format('|'.join(cpp_keywords))
cpp_variables = re.findall(r'\b(?!(?:{}))[a-zA-Z_][a-zA-Z0-9_]*\b'.format(cpp_keywords_pattern), corpus)

# Construct the full path for the new file (beside the code file)
file_path = os.path.join(script_dir, "CppVariables.txt")
try:
  with open(file_path, "x") as f:
    f.write("C++ variables:\n")
    f.write('\n'.join(cpp_variables))
except:
  with open(file_path, "w") as f:
    f.write("C++ variables:\n")
    f.write('\n'.join(cpp_variables))

print("Done!")