# Online Shop

A Django-based online shop that supports browsing products, adding items to a cart, applying discount codes, and completing a basic checkout flow. The project also includes order handling, a simple recommendation system, and multi-language support.

## Features

- Product catalog
- Session-based cart
- Discount codes
- Checkout and order creation
- Recommendation engine
- Multi-language support

## Technologies Used

- Python
- Django
- Django Sessions
- Celery
- RabbitMQ
- Redis
- Stripe
- HTML, CSS, JavaScript
- uv

## Setup

Clone the repository:

```
git clone https://github.com/mario-ak37/online_shop.git
cd online_shop
```

Create a virtual environment and install dependencies:

```
uv venv
source .venv/bin/activate
uv sync
```

Run migrations and start the server:

```
python manage.py migrate
python manage.py runserver
```
