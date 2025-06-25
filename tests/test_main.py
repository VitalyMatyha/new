from main import Category, Product


def test_product_init():
    product = Product("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init():
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [
                        product1, product2])
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 2


def test_category_counts():
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category(
        "Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1, product2])
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category2 = Category(
        "Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3
