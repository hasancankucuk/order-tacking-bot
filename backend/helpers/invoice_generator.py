import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos


def invoice_generator(invoice) -> str:
    os.makedirs("invoice", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", style="B", size=20)
    pdf.cell(0, 10, "INVOICE", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

    pdf.ln(10)
    pdf.set_font("Helvetica", size=12)

    customer_name = invoice.get("customer_name", "N/A")
    ordered_items = invoice.get("ordered_items", "No items listed")
    shipping_address = invoice.get("shipping_address", "N/A")
    shipping_method = invoice.get("shipping_method", "N/A")
    order_id = str(invoice.get("order_id", "N/A"))
    status = invoice.get("status", "N/A")

    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, "Invoice Details", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    basic_info = [
        ["Field", "Value"],
        ["Customer Name", customer_name],
        ["Order ID", order_id],
        ["Status", status],
        ["Shipping Method", shipping_method],
        ["Shipping Address", shipping_address],
    ]

    pdf.set_font("Helvetica", size=12)
    with pdf.table() as table:
        for data_row in basic_info:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))

    pdf.ln(10)

    pdf.set_font("Helvetica", style="B", size=14)
    pdf.cell(0, 10, "Items Ordered", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    if ordered_items and ordered_items != "No items listed":
        items = ordered_items.split(',')
        items_data = [["Item", "Price"]]
        
        for item in items:
            if '(Price: $' in item:
                item_name = item.split(' (Price: $')[0].strip()
                price = item.split(' (Price: $')[1].replace(')', '').strip()
                items_data.append([item_name, f"${price}"])
            else:
                items_data.append([item.strip(), "N/A"])
    else:
        items_data = [["Item", "Price"], ["No items", "N/A"]]

    pdf.set_font("Helvetica", size=12)
    with pdf.table() as table:
        for data_row in items_data:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))

    pdf.ln(10)
    pdf.cell(
            0,
            10,
            text="Thank you for your order!",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align="C",
        )

    file_path = f"invoice_{order_id}.pdf"
    full_path = f"invoice/{file_path}"
    pdf.output(full_path)

    return full_path