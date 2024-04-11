import re

def parse_receipt(text):
    match = re.search(r'Филиал (.+)\n', text)
    branch = match.group(1) if match else None

    match = re.search(r'БИН (\d+)\n', text)
    bin_number = match.group(1) if match else None

    match = re.search(r'Чек №(\d+)\n', text)
    check_number = match.group(1) if match else None

    match = re.search(r'Касс (.+)\n', text)
    cash_register = match.group(1) if match else None

    match = re.search(r'Смена (\d+)\n', text)
    shift = match.group(1) if match else None

    match = re.search(r'ПРОДАЖА\n((?:.+\n)+)', text)
    sales_items = match.group(1) if match else None

    match = re.search(r'ИТОГО:\n([\d\s,]+)', text)
    total = match.group(1).replace(" ", "") if match else None
    return {
        "branch": branch,
        "bin_number": bin_number,
        "check_number": check_number,
        "cash_register": cash_register,
        "shift": shift,
        "sales_items": sales_items,
        "total": total
    }
with open('row.txt', 'r', encoding='utf-8') as file:
    receipt_text = file.read()

parsed_receipt = parse_receipt(receipt_text)
for key, value in parsed_receipt.items():
    print(f"{key}: {value}")