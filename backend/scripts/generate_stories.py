import os
import textwrap

def main():
    stories_content = textwrap.dedent("""\
    version: "3.1"
    stories:
      - story: greet
        steps:
          - intent: greet
          - action: utter_greet

      - story: goodbye
        steps:
          - intent: goodbye
          - action: utter_goodbye

      - story: accept
        steps:
          - intent: accept
          - action: utter_accept

      - story: deny
        steps:
          - intent: deny
          - action: utter_deny

      - story: change_order
        steps:
          - intent: change_order
          - action: action_change_order

      - story: cancel_order
        steps:
          - intent: cancel_order
          - action: action_cancel_order

      - story: place_order
        steps:
          - intent: place_order
          - action: action_place_order

      - story: check_invoice
        steps:
          - intent: check_invoice
          - action: action_retrieve_invoice

      - story: check_cancel_fee
        steps:
          - intent: check_cancel_fee
          - action: action_check_cancel_fee

      - story: change_shipping_address
        steps:
          - intent: change_shipping_address
          - action: action_change_shipping_address

      - story: list_products
        steps:
          - intent: list_products
          - action: action_list_products

      - story: fallback
        steps:
          - intent: nlu_fallback
          - action: utter_default
    """)

    os.makedirs("./data/", exist_ok=True)

    with open("./data/stories.yml", "w", encoding="utf-8") as f:
        f.write(stories_content)

if __name__ == "__main__":
    main()