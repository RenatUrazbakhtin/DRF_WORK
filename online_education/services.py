import stripe

from config.settings import STRIPE_API_KEY
from online_education.models import Course


def create_product(instance: Course):
    stripe.api_key = STRIPE_API_KEY

    response = stripe.Product.create(name=f"{instance.title}")

    product_id = response['id']

    return product_id

def create_price(instance: Course):
    stripe.api_key = STRIPE_API_KEY
    product_id = create_product(instance)
    response = stripe.Price.create(
        unit_amount=100,
        currency="usd",
        recurring={"interval": "month"},
        product=f"{product_id}",
    )
    price_id = response["id"]

    return price_id
def create_session_and_take_url(instance):
    stripe.api_key = STRIPE_API_KEY
    price_id = create_price(instance)

    response = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": f"{price_id}",
                "quantity": 2,
            },
        ],
        mode="subscription",
    )

    return response["url"]
