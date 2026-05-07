from app import app
from models import db, Category, Product


def slugify(text):
    return (
        text.lower()
        .strip()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("&", "and")
    )


sample_products = [
    {
        "name": "Luxe Satin Dress",
        "description": "Elegant satin dress perfect for weddings, dinner dates, and special occasions.",
        "price": 24500,
        "category": "Dresses",
        "is_available": True,
        "is_featured": True,
    },
    {
        "name": "Pleated Two Piece Set",
        "description": "Stylish two-piece outfit with a flattering pleated finish.",
        "price": 21000,
        "category": "Two Pieces",
        "is_available": True,
        "is_featured": True,
    },
    {
        "name": "Floral Maxi Dress",
        "description": "Soft floral maxi dress for classy casual and semi-formal outings.",
        "price": 19500,
        "category": "Dresses",
        "is_available": True,
        "is_featured": True,
    },
    {
        "name": "Classic Blazer",
        "description": "Clean and stylish blazer suitable for work, church, and elegant outings.",
        "price": 18000,
        "category": "Tops",
        "is_available": False,
        "is_featured": True,
    },
    {
        "name": "Sunset Wrap Dress",
        "description": "Beautiful wrap dress with a soft feminine fit.",
        "price": 17500,
        "category": "Dresses",
        "is_available": True,
        "is_featured": False,
    },
    {
        "name": "Linen Co-ord Set",
        "description": "Comfortable linen co-ord set for relaxed but classy styling.",
        "price": 20000,
        "category": "Two Pieces",
        "is_available": True,
        "is_featured": False,
    },
    {
        "name": "Off-Shoulder Top",
        "description": "Chic off-shoulder top that pairs beautifully with skirts or jeans.",
        "price": 9500,
        "category": "Tops",
        "is_available": True,
        "is_featured": False,
    },
    {
        "name": "Chain Strap Bag",
        "description": "Elegant chain strap bag for outings, events, and everyday styling.",
        "price": 12000,
        "category": "Bags",
        "is_available": True,
        "is_featured": False,
    },
]


with app.app_context():
    for item in sample_products:
        category = Category.query.filter_by(name=item["category"]).first()

        if not category:
            category = Category(
                name=item["category"],
                slug=slugify(item["category"])
            )
            db.session.add(category)
            db.session.commit()

        existing_product = Product.query.filter_by(name=item["name"]).first()

        if existing_product:
            print(f"Skipped: {item['name']} already exists.")
            continue

        product = Product(
            name=item["name"],
            slug=slugify(item["name"]),
            description=item["description"],
            price=item["price"],
            category_id=category.id,
            is_available=item["is_available"],
            is_featured=item["is_featured"],
        )

        db.session.add(product)

    db.session.commit()

    print("Sample products added successfully.")
