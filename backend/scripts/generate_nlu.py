import os
import textwrap


def main():
    nlu_content = textwrap.dedent("""\
    version: "3.1"
    nlu:
    - intent: greet
      examples: |
        - hi
        - hello
        - good morning
        - good evening
        - hey

    - intent: goodbye
      examples: |
        - bye
        - goodbye
        - see you later
        - farewell

    - intent: accept
      examples: |
        - yes
        - sure
        - of course
        - absolutely
        - okay
        - sounds good

    - intent: deny
      examples: |
        - no
        - not really
        - I don't want to
        - nope
        - never mind

    - intent: change_order
      examples: |
        - I want to change my order [10](order_id)
        - Can I modify my order [5](order_id)?
        - Change my order please
        - I need to update my order
        - Can I switch the shipping method for order [2](order_id) to [Express](shipping_method)?
        - Please update my order [4](order_id) to include [Standard](shipping_method) shipping
        - Update my order [14](order_id)'s shipping method to [Next Day](shipping_method)

    - intent: cancel_order
      examples: |
        - I want to cancel my order number [10](order_id)
        - Cancel my order [5](order_id)
        - Can I cancel my order [8](order_id)?
        - Please cancel my order [12](order_id)
        - Cancel order [ORD001](order_id)
        - I need to cancel order [123](order_id)
        - Delete my order [456](order_id)
        - Remove order [789](order_id)
        - Stop my order [ORD002](order_id)

    - intent: place_order
      examples: |
        - order [2](quantity) [smartphone cases](product) to [Ankara](address)
        - I want [3](quantity) [laptop stand](product)
        - Can I order [1](quantity) [phone case](product)?
        - I need [4](quantity) [bluetooth speaker](product) to [Frankfurt](address)
        - Can I order [3](quantity) [speakers](product) to [Washington](address)?
        - Place an order for [2](quantity) [coffee mug](product) to [New York](address)
        - Buy [1](quantity) [yoga mat](product)
        - I want to place an order for [5](quantity) [wireless headphones](product) to [Los Angeles](address)
        - Order [3](quantity) [running shoes](product) please
        - I'd like to order [2](quantity) [led desk lamp](product) to [Berlin](address)
        - Order [4](quantity) [desk lamp](product) to [Paris](address)
        - Place an order for [1](quantity) [mat](product) to [London](address)
          - I need [2](quantity) [lamp](product) to [Tokyo](address)
                                  
    - intent: check_invoice
      examples: |
        - Can I see my invoice for order [10](order_id)?
        - Show me my bill for order [5](order_id)
        - I need my invoice for order [8](order_id)
        - Where is my invoice? (order [12](order_id))

    - intent: check_cancel_fee
      examples: |
        - Is there a cancellation fee?
        - Will I be charged for cancelling?
        - Do I have to pay to cancel?
        - Any fee for cancellation?

    - intent: change_shipping_address
      examples: |
        - Change the address for order [10](order_id) to [Berlin](new_address)
        - Update shipping address for order [5](order_id) to [123 Main St, Springfield](new_address)
        - My order [8](order_id) should go to [Paris](new_address)
        - Please send order [12](order_id) to [London](new_address)

    - intent: list_products
      examples: |
        - What products do you have?
        - Show me your products
        - List all available products
        - What items are in stock?
        - Can I see your product catalog?
        - What do you sell?
        - Show me the product list
        - What products can I order?
        - Give me a list of your products
    """)

    os.makedirs("./data/", exist_ok=True)

    with open("./data/nlu.yml", "w", encoding="utf-8") as f:
        f.write(nlu_content)
