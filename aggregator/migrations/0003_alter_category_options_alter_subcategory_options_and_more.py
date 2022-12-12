# Generated by Django 4.1.3 on 2022-12-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aggregator", "0002_alter_media_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={"ordering": ["name"]},
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                choices=[
                    ("Transport", "Transport"),
                    ("Real Estate", "Real Estate"),
                    ("Job", "Job"),
                    ("Service", "Service"),
                    ("Personal Usage", "Personal Stuff"),
                    ("For Home", "For Home"),
                    ("Electronics", "Electronics"),
                    ("Hobby and Leisure", "Hobby and Leisure"),
                    ("Pets", "Pets"),
                    (
                        "Business and Business Equipment",
                        "Business and Business Equipment",
                    ),
                ],
                max_length=31,
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(
                choices=[
                    ("Cars", "Cars"),
                    ("Motorcycles", "Motorcycles"),
                    ("Trucks", "Trucks and Special Equipment"),
                    ("Water", "Water"),
                    ("Parts and Accessories", "Parts and Accessories"),
                    ("Overseas Properties", "Overseas Estate"),
                    ("Apartments", "Apartments"),
                    ("Rooms", "Rooms"),
                    ("Houses", "Houses"),
                    ("Parking", "Parking"),
                    ("Commercial Properties", "Commercial Properties"),
                    ("Vacancies", "Vacancies"),
                    ("IT/Telecom", "IT/Telecom"),
                    ("Business Services", "Business Services"),
                    ("Tutoring", "Tutoring"),
                    ("Building", "Building"),
                    ("Other", "Other"),
                    ("Clothes and Footwear", "Clothes and Footwear"),
                    ("Clothes and Footwear for Kids", "Clothes and Footwear for Kids"),
                    ("Baby Products and Toys", "Baby Products and Toys"),
                    ("Accessories", "Accessories"),
                    ("Health and Beauty", "Health and Beauty"),
                    ("Household Equipment", "Household Equipment"),
                    ("Furniture and Interior", "Furniture and Interior"),
                    ("Dishes and Kitchen Equipment", "Dishes and Kitchen Equipment"),
                    ("Groceries", "Groceries"),
                    ("Maintenance and Building", "Maintenance and Building"),
                    ("Plants", "Plants"),
                    ("Audio and Video", "Audio and Video"),
                    ("Videogaming", "Videogaming"),
                    ("Personal Computers", "Personal Computers"),
                    ("Laptops", "Laptops"),
                    ("Phones", "Phones"),
                    ("Other", "Other"),
                    ("Tickets", "Tickets"),
                    ("Bikes", "Bikes"),
                    ("Books and Magazines", "Books and Magazines"),
                    ("Collecting", "Collecting"),
                    ("Hunting and Fishing", "Hunting and Fishing"),
                    ("Sports and Leisure", "Sports and Leisure"),
                    ("Dogs", "Dogs"),
                    ("Cats", "Cats"),
                    ("Birds", "Birds"),
                    ("Fish", "Fish"),
                    ("Other Pets", "Other Pets"),
                    ("Pest Products", "Pest Products"),
                    ("Business for Sale", "Business for Sale"),
                    ("Business equipment", "Business equipment"),
                ],
                max_length=30,
            ),
        ),
    ]
