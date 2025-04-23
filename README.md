# ecommerce-website
This is a web-based user management platform built using Django. It allows users to register, log in, and manage their own Categories, Products, and Tags. The platform supports image uploads, tag-based labeling, and an admin panel with search and filtering capabilities.

# Features
### User Authentication
- User Registration & Login

### User Dashboard
- Personalized dashboard for each User
- Quick access to product and category management

### Category Management
- Add, update, delete categories
- Categories are User-specific

### Product Management
- Add, update, delete products
- Assign products to categories
- Upload product images
- Tag support for product labeling

### Tagging System
- Flexible tag input via comma-separated values
- Search products using tags

### Admin Panel
- Superuser access to all products and categories
- Search and filter products from the Django Admin
- View uploaded images and tags in admin

### Image Uploads
- Product images are uploaded to the `media/products/` directory.
- Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py`.

### Technologies Used
- Django (4.13.2)
- SQLite (default)n
- Bootstrap (for styling)
- django-taggit (for tags)
- Pillow (for image uploads)

### Example Use Cases
User A logs in and creates "Candles" and "Soap" categories.
User A uploads 5 products under "Candles", each tagged with keywords like trending, bestsellers, price drop.
Admin logs in to view all User products, filters by category or tags.

### Project Setup
Create Virtual Environment & Install Dependencies
python -m venv env
source env/bin/activate
pip install -r requirements.txt

Apply Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser

Run Development Server
python manage.py runserver

Access the App
Frontend: http://localhost:8000/
Admin Panel: http://localhost:8000/admin/
