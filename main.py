import stripe

# YOUR stripe API key the SK_Key
stripe.api_key = "your_key_goes_here"

# Input and output files
input_file = "cc.txt"
output_file = "results.txt"

def check_card(card_number, exp_month, exp_year, cvc):
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": card_number,
                "exp_month": int(exp_month),
                "exp_year": int(exp_year),
                "cvc": cvc,
            },
        )

        customer = stripe.Customer.create(
            payment_method=payment_method.id,
            invoice_settings={"default_payment_method": payment_method.id},
        )

        intent = stripe.PaymentIntent.create(
            amount=100,  # Small charge for verification
            currency="usd",
            payment_method=payment_method.id,
            customer=customer.id,
            confirm=True,
        )

        return f"{card_number} | {exp_month} | {exp_year} | {cvc} - Approved ✅"

    except stripe.error.CardError as e:
        return f"{card_number} | {exp_month} | {exp_year} | {cvc} - Declined ❌ ({e.user_message})"

    except Exception as e:
        return f"{card_number} | {exp_month} | {exp_year} | {cvc} - Error ⚠️ ({str(e)})"

def process_cards():
    """Reads credit cards from a file, checks them, and writes results to a file."""
    with open(input_file, "r") as file:
        cards = [line.strip() for line in file if line.strip()]

    results = []
    for card in cards:
        try:
            card_number, exp_month, exp_year, cvc = [x.strip() for x in card.split("|")]
            result = check_card(card_number, exp_month, exp_year, cvc)
            results.append(result)
            print(result)  # Show progress in console
        except ValueError:
            results.append(f"Invalid format: {card}")

    with open(output_file, "w") as file:
        file.write("\n".join(results))

    print("\n✅ Finished Checking. Check results.txt")

# Run the checker
if __name__ == "__main__":
    process_cards()
