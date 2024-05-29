import re
from collections import defaultdict
import os


def AddressExtractor(text):
    # Read the entity keywords, their variations, and limits from the file
    with open(os.getcwd() + '/info/AddressEntities.txt', 'r', encoding='utf-8') as file:
        entity_mapping = defaultdict(list)
        entity_limits = {}
        for line in file:
            parts = line.strip().split('\u060C')
            base_entity = parts[0]
            variations = parts[:-1]
            limit = int(parts[-1])  # The last part is the limit
            entity_limits[base_entity] = limit
            for variation in variations:
                entity_mapping[base_entity].append(variation.strip())

    # Initialize a list to store the dictionaries of extracted addresses
    addresses = []
    current_address = defaultdict(list)
    current_entity = None
    current_value = []

    # Split the text by spaces to process word by word
    words = text.split()
    for word in words:
        # Check if the word is an entity
        matched_entity = next((base_entity for base_entity, variations in entity_mapping.items() if word in variations), None)
        if matched_entity:
            # If we have captured a value for the current entity, save it
            if current_entity and current_value:
                current_address[current_entity].append(' '.join(current_value))
            current_entity = matched_entity
            current_value = []
        else:
            # If the word is not an entity, add it to the current value
            if current_entity:
                # Check if adding the word exceeds the limit
                if len(current_value) < entity_limits[current_entity]:
                    current_value.append(word)
                else:
                    # If the limit is exceeded, finalize the current address and start a new one
                    if current_value:
                        current_address[current_entity].append(' '.join(current_value))
                    if current_address:
                        addresses.append(dict(current_address))
                    current_address = defaultdict(list)
                    current_entity = None
                    current_value = []

    # Finalize the last address
    if current_entity and current_value:
        current_address[current_entity].append(' '.join(current_value))
    if current_address:
        addresses.append(dict(current_address))

    # Convert lists of values to a single value or a numbered series
    final_addresses = []
    for address in addresses:
        final_address = {}
        for base_entity, values in address.items():
            if len(values) == 1:
                final_value = re.sub(r"[^آ-یA-Za-z0-9 \u06F0-\u06F9 ]", "", values[0]).strip() # Remove non-letter and non-space characters and remove leading and trailing spaces
                final_address[base_entity] = final_value
            else:
                for i, value in enumerate(values, 1):
                    final_value = re.sub(r"[^آ-یA-Za-z0-9 \u06F0-\u06F9 ]", "", value).strip()  # Remove non-letter and non-space characters and remove leading and trailing spaces
                    final_address[f"{base_entity} {i}"] = final_value
        final_addresses.append(final_address)

    return final_addresses

# Example input text
input_text = "این یک پیام تست است که در آن آدرس ما این است: محله ونک، خیابان میرزای شیرازی خیابان مطهری خیابان شهید صدوقی ک خورشید پلاک ۸ واحد 6 سپس بلوار الغدیر شمالی - میدان شهید صیاد شیرازی، کوچه بابایی، پ 5 است."

# Extract the address entities
extracted_addresses = AddressExtractor(input_text)

# Print the extracted addresses
#for address in extracted_addresses:
#    print(address)
