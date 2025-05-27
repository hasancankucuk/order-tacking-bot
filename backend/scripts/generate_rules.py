import os
import textwrap

def main():
    rules_content = textwrap.dedent("""\
    version: "3.1"
    rules:
      - rule: Greet the user
        steps:
          - intent: greet
          - action: utter_greet

      - rule: Say goodbye
        steps:
          - intent: goodbye
          - action: utter_goodbye

      - rule: Handle change_order
        steps:
          - intent: change_order
          - action: action_change_order

      - rule: Handle cancel_order
        steps:
          - intent: cancel_order
          - action: action_cancel_order

      - rule: Handle place_order
        steps:
          - intent: place_order
          - action: action_place_order

      - rule: Handle check_invoice and respond
        steps:
          - intent: check_invoice
          - action: action_retrieve_invoice

      - rule: Handle check_cancel_fee
        steps:
          - intent: check_cancel_fee
          - action: action_check_cancel_fee

      - rule: Handle change_shipping_address
        steps:
          - intent: change_shipping_address
          - action: action_change_shipping_address
                  
      - rule: Handle list_products
        steps:
          - intent: list_products
          - action: action_list_products
    """)

    os.makedirs("./data/", exist_ok=True)

    with open("./data/rules.yml", "w", encoding="utf-8") as f:
        f.write(rules_content)

if __name__ == "__main__":
    main()