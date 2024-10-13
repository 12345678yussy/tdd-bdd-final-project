from factory import Factory, Sequence, Faker
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category  # Asegúrate de importar el modelo Product y Category

class ProductFactory(Factory):
    """Creates fake products for testing"""
    
    class Meta:
        """Maps factory to data model"""
        model = Product

    id = Sequence(lambda n: n)
    name = FuzzyChoice(
        choices=[
            "Hat",
            "Pants",
            "Shirt",
            "Apple",
            "Banana",
            "Pots",
            "Towels",
            "Ford",
            "Chevy",
            "Hammer",
            "Wrench"
        ]
    )
    description = Faker("text")
    price = FuzzyDecimal(0.5, 2000.0, 2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )
