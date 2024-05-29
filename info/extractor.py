import re
from .address import AddressExtractor
from .number import getMobiles, getLandlineNumbers
import json


def EmailExtractor(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, text)


def MessageClassifier(texts, char_threshold):
    lens = [len(text) for text in texts]
    if sum(lens) < char_threshold:  # Assuming short messages are less than 100 characters
        return 'پیام کوتاه'
    else:
        return 'پیام بلند'


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]


def Extractor(input_text, char_threshold=100):
    landlineList = flatten_list([getLandlineNumbers(target) for target in input_text])
    mobileList = flatten_list([getMobiles(target) for target in input_text])
    emailList = flatten_list([EmailExtractor(target) for target in input_text])
    addressList = flatten_list([AddressExtractor(target) for target in input_text])

    output = {
        "تلفن": {"ثابت": landlineList, "همراه": mobileList},
        "ایمیل": emailList,
        "نشانی‌ها": addressList,
        "طبقه‌بندی پیام": MessageClassifier(input_text, char_threshold)
    }
    return json.dumps(output, ensure_ascii=False)


# تست کد
# input_text = ("این یک پیام تست است که در آن ایمیل ما iliahashemirad@yahoo.co.uk و آدرس ما این است: محله ونک، خیابان میرزای شیرازی خیابان مطهری خیابان شهید صدوقی ک خورشید پلاک ۸ واحد 6 سپس بلوار الغدیر شمالی - میدان شهید صیاد شیرازی، کوچه بابایی، پ 5 است."
#             "همجنین شماره تلفن بصورت +۹۸ (۹۱٤) ۸۰ ۸۰   ۸۸۸ میباشد."
#              "jafang 0 21 666 23 5331 djj 6623 53(3) 12 jafang or 0 91 2 (123) 45-67 gjgj  +91228734793 ")

def get_multiline_input():
    print("Please enter the text (press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


if __name__ == "__main__":
    CHAR_THRESHOLD = 100
    import sys

    if len(sys.argv) > 1:
        # Read from the file provided as a command-line argument
        with open(sys.argv[1], 'r') as file:
            target = file.read().split('\n')
    else:
        # Prompt the user to enter text manually
        target = get_multiline_input()

    output = Extractor(target, CHAR_THRESHOLD)

    pretty(output)
