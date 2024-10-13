def test_read_a_product(self):
    """It should Read a Product"""
    # Crear un producto utilizando la fábrica
    product = ProductFactory()
    
    # Establecer el ID del objeto producto a None y luego llamar al método create() en el producto.
    product.id = None
    product.create()  # Asumiendo que hay un método create() que guarda el producto en la base de datos
    
    # Afirmar que el ID del objeto producto no es None después de llamar al método create().
    self.assertIsNotNone(product.id)
    
    # Recuperar el producto de la base de datos usando el ID del producto y almacenarlo en found_product
    found_product = Product.find(product.id)  # Asumiendo que hay un método find() que busca por ID
    
    # Afirmar que las propiedades de found_product coinciden con las propiedades del objeto producto original
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)
    self.assertEqual(found_product.description, product.description)
    self.assertEqual(found_product.price, product.price)
   def test_update_a_product(self):
        """It should Update a Product"""
        product = ProductFactory()
        product.id = None
        product.create()
        self.assertIsNotNone(product.id)
        # Change it an save it
        product.description = "testing"
        original_id = product.id
        product.update()
        self.assertEqual(product.id, original_id)
        self.assertEqual(product.description, "testing")
        # Fetch it back and make sure the id hasn't changed
        # but the data did change
        products = Product.all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].id, original_id)
        self.assertEqual(products[0].description, "testing")