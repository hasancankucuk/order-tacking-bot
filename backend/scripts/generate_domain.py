import os
import textwrap


def main():
    domain_content = textwrap.dedent(
        """\
    version: "3.1"
    intents:
      - greet
      - goodbye
      - accept
      - deny
      - change_order
      - change_shipping_address
      - check_invoice
      - check_cancel_fee
      - cancel_order
      - place_order
      - list_products
      - nlu_fallback

    entities:
      - order_id
      - address
      - new_address
      - shipping_method
      - product
      - quantity

    slots:
      order_id:
        type: text
        influence_conversation: true
        mappings:
          - type: from_entity
            entity: order_id
      address:
        type: text
        influence_conversation: true
        mappings:
          - type: from_entity
            entity: address
      new_address:
        type: text
        influence_conversation: true
        mappings:
          - type: from_entity
            entity: new_address
      shipping_method:
        type: text
        influence_conversation: true
        mappings:
          - type: from_entity
            entity: shipping_method
      product:
        type: text
        mappings:
          - type: from_entity
            entity: product
      quantity:
        type: text
        mappings:
          - type: from_entity
            entity: quantity

    responses:
      utter_greet:
        - text: Hello! How can I help you today?
        - text: Hi there! What can I assist you with?
        - text: Good day! How may I assist you?
        - text: Welcome! How can I help you today?

      utter_goodbye:
        - text: Goodbye! Have a great day!
        - text: See you later! If you need anything else, just ask.
        - text: Farewell! Don't hesitate to return if you need help.

      utter_accept:
        - text: Great!
        - text: Awesome! How can I assist you further?
        - text: Perfect! What would you like to do next?
        - text: Sure! Let me know how I can help.

      utter_deny:
        - text: Okay, let me know if you need anything else.
        - text: No problem! If you change your mind, I'm here to help.
        - text: Understood! If you have any other questions, feel free to ask.
        - text: Alright, if you need assistance later, just let me know.

      utter_default:
        - text: I'm sorry, I don't have information on that. How else can I assist?
        - text: I don't have that information. Is there anything else I can help you with?
        - text: Unfortunately, I can't assist with that. How else can I help?
        - text: I don't have the answer to that. Can I help you with something else?

    actions:
      - action_retrieve_invoice
      - action_check_cancel_fee
      - action_change_shipping_address
      - action_change_order
      - action_cancel_order
      - action_place_order
      - action_list_products

    session_config:
      session_expiration_time: 60
      carry_over_slots_to_new_session: true
    """
    )

    with open(
        os.path.join(os.path.dirname(__file__), "../domain.yml"), "w", encoding="utf-8"
    ) as file:
        file.write(domain_content)


if __name__ == "__main__":
    main()
