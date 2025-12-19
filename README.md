````md
# Online Shop

A Django-based online shop that supports browsing products, managing a shopping cart, applying discount codes, and completing a checkout flow using Stripe. The project includes order management, background task processing, PDF invoice generation, a recommendation system, and multi-language support.

## Features

- Product catalog with categories
- Session-based shopping cart
- Discount codes (coupons)
- Checkout and order creation
- Stripe payment integration with webhooks
- Background tasks using Celery
- Recommendation engine
- PDF invoice generation
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
- Docker

## Setup

### Clone the repository

```bash
git clone https://github.com/mario-ak37/online_shop.git
cd online_shop
```
````

### Create a virtual environment and install dependencies

```bash
uv venv
source .venv/bin/activate
uv sync
```

### Run required services

The following services must be running before starting the Django server.

#### RabbitMQ (via Docker)

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

RabbitMQ management interface is available at `http://localhost:15672`
(Default credentials: `guest / guest`)

#### Celery worker

```bash
celery -A myshop worker -l INFO
```

#### Stripe webhook listener

```bash
stripe listen --forward-to localhost:8000/payment/webhook/
```

### Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

The application will be available at `http://localhost:8000`.

## Notes

- The Stripe CLI must be installed and authenticated.
- RabbitMQ must be running before starting the Celery worker.
- Redis is used as the message broker and result backend for Celery.
- Static files and PDF styles are configured for both development and production use.
