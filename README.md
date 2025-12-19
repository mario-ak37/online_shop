# Online Shop

A Django-based online shop that supports browsing products, managing a shopping cart, applying discount codes, and completing a checkout flow using Stripe. The project includes order management, background task processing with Celery and RabbitMQ, PDF invoice generation, a recommendation system, and multi-language support.

## Features

- Product catalog with categories
- Session-based shopping cart
- Discount codes (coupons)
- Checkout and order creation
- Stripe payment integration with webhooks
- Background tasks using Celery and RabbitMQ
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

## Setup Virtual Environment and Dependencies

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Start Required Services

### RabbitMQ (via Docker)

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

### Start Celery Worker

```bash
celery -A myshop worker -l INFO
```

### Start Stripe Webhook Listener

```bash
stripe listen --forward-to localhost:8000/payment/webhook/
```

## Run Migrations and Start Django Server

```bash
python manage.py migrate
python manage.py runserver
```
