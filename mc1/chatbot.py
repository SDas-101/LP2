def get_response(text):
    text = text.lower()

    # Greeting
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello, how can I assist you today?"

    # Order support
    if any(word in text for word in ["order", "tracking", "status", "shipped"]):
        return "Your order is currently being processed. Tracking updates within 24 hours."

    # Refund / cancellation
    if any(word in text for word in ["refund", "return", "cancel"]):
        return "Refunds are usually processed within five to seven business days."

    # Payment issues
    if any(word in text for word in ["payment", "card", "transaction", "failed"]):
        return "Please verify your payment details and try again after a few minutes."

    # Product inquiry
    if any(word in text for word in ["price", "stock", "discount"]):
        return "Pricing and stock depend on product category. Please check current listings."

    # Delivery support
    if any(word in text for word in ["delivery", "shipping", "late"]):
        return "Standard delivery takes three to five business days."

    # Exit
    if any(word in text for word in ["bye", "thanks", "thank you", "exit"]):
        return "Goodbye. Have a nice day."

    return "Please repeat your query using order, refund, payment, delivery or price."