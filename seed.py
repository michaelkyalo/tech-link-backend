from app import create_app
from app.config.database import db
from app.models.user_model import User
from app.models.product_model import Product
from werkzeug.security import generate_password_hash
from datetime import datetime

app = create_app()

with app.app_context():

    # ── 1. Get existing farmer or create new one ─────────────────────────
    farmer = (
        User.query.filter_by(email="farmer@agrilink.com").first() or
        User.query.filter_by(phone="0712345678").first()
    )

    if not farmer:
        farmer = User(
            full_name="John Kamau",
            email="farmer@agrilink.com",
            phone="0712345678",
            password=generate_password_hash("farmer123"),
            role="farmer",
            location="Nakuru, Kenya",
        )
        db.session.add(farmer)
        db.session.flush()
        print(f"✅ Farmer created: {farmer.full_name} (id={farmer.user_id})")
    else:
        print(f"ℹ️  Using existing farmer: {farmer.full_name} (id={farmer.user_id})")

    # ── 2. Seed products ─────────────────────────────────────────────────
    sample_products = [
        {
            "product_name": "Fresh Tomatoes",
            "description":  "Organically grown tomatoes from Nakuru highlands.",
            "category":     "Vegetables",
            "price":        120.00,
            "quantity":     200,
            "location":     "Nakuru, Kenya",
            "image_url":    None,
        },
        {
            "product_name": "Maize (1kg)",
            "description":  "Dried white maize, freshly harvested.",
            "category":     "Grains",
            "price":        60.00,
            "quantity":     500,
            "location":     "Eldoret, Kenya",
            "image_url":    None,
        },
        {
            "product_name": "Avocados (6 pack)",
            "description":  "Creamy Hass avocados, ready to eat.",
            "category":     "Fruits",
            "price":        150.00,
            "quantity":     100,
            "location":     "Murang'a, Kenya",
            "image_url":    None,
        },
        {
            "product_name": "Free Range Eggs (tray)",
            "description":  "30 fresh free-range eggs from village hens.",
            "category":     "Poultry",
            "price":        480.00,
            "quantity":     80,
            "location":     "Kiambu, Kenya",
            "image_url":    None,
        },
        {
            "product_name": "Fresh Milk (1L)",
            "description":  "Pure whole milk from grass-fed cows.",
            "category":     "Dairy",
            "price":        70.00,
            "quantity":     150,
            "location":     "Nyandarua, Kenya",
            "image_url":    None,
        },
        {
            "product_name": "Kale (Sukuma Wiki)",
            "description":  "Fresh kale bundles, harvested daily.",
            "category":     "Vegetables",
            "price":        30.00,
            "quantity":     300,
            "location":     "Nakuru, Kenya",
            "image_url":    None,
        },
    ]

    added = 0
    for p in sample_products:
        exists = Product.query.filter_by(
            product_name=p["product_name"],
            farmer_id=farmer.user_id
        ).first()
        if not exists:
            product = Product(
                farmer_id=farmer.user_id,
                created_at=datetime.utcnow(),
                **p
            )
            db.session.add(product)
            added += 1

    db.session.commit()
    print(f"✅ {added} products seeded successfully.")
    print("─────────────────────────────────────")
    print(f"  Farmer login:")
    print(f"  Email   : {farmer.email}")
    print(f"  Password: farmer123 (if newly created)")
    print("─────────────────────────────────────")