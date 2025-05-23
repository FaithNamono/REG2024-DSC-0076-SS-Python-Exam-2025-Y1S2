from flask import   request, jsonify, Blueprint
from app.models import Category, Product, Customer


category_bp=Blueprint('category',__name__)
# Create a category
@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.json() # Get json data from request
    name= data.get("name")

    if not name:
        return jsonify({"error":"category not created"})
# stores products in memory
products = []
product_bp=Blueprint("product",__name__)
#  POST Creates a product
@product_bp.route("/products", methods=['POST'])
def create_products():
    """Create a new product"""
    data = request.get_json()#get Json data from request
    name=data.get('name')
    price=data.get('price')
    stock=data.get('stock')
    color=data.get('color')

    if not name or not price or not stock or not color:
        return jsonify({"error":"missing required field"}), 400
    product={
        "id":len(products) + 1,
        "name":name,
        "price": price,
        "stock": stock,
        "color": color
    }
    products.append(product)
    return jsonify(product), 201
customer_bp=Blueprint("customer",__name__)
#Create a customer
@customer_bp.route("/customers", methods=["POST"])
def create_customer():
    data=request.json()
    first_name=data.get("name")
    last_name=data.get("last_name")
    address=data.get("address")
    contact = data.get("contact")
    email=data.get("email")

    if not first_name or not last_name or not address or not contact or not email:
        return jsonify({"error":"Customer not created"})

# PUT Update a product by ID
@product_bp.route("/products/<int:id>",methods=['PUT'])
def update_product(id):
    data=request.get_json()
    for product in products:
        if product["id"]==id:
            product.update(data)
            return jsonify(product)
    return jsonify({"error":"product not found"}), 404

# Get retrieves all products
@product_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

#Delete removes a program  from the list
@ product_bp.route('/delete/<int:author_id>', methods=['DELETE'])
def delete_product():
    product=id

    if not product:
        return jsonify({"error": "product not found"}), 404

    products.session.delete(product)
    products.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

    

    

