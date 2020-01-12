## How To Try It Out

```shell
# Migration
$ python manage.py makemigrations polymorphic_associations
$ python manage.py migrate polymorphic_associations
$ python manage.py shell

# Create Data
>>> from polymorphic_associations.models import Employee, Product
>>>
>>> employee = Employee(name='John', email='test@example.com')
>>> employee.save()
>>> employee.pictures.create(file_name='employee.jpg')
<Picture: Picture object (1)>
>>>
>>> product = Product(name='Desk', price=1000)
>>> product.save()
>>> product.pictures.create(file_name='product.jpg')
<Picture: Picture object (2)>


# Get Data
>>> employee.pictures.all()
<QuerySet [<Picture: Picture object (1)>]>
>>> employee.pictures.first().file_name
'employee.jpg'
>>>
>>> product.pictures.all()
<QuerySet [<Picture: Picture object (2)>]>
>>> product.pictures.first().file_name
'product.jpg'


# Confirm SQL
>>> str(employee.pictures.all().query)
'SELECT
    "polymorphic_associations_picture"."id",
    "polymorphic_associations_picture"."object_id",
    "polymorphic_associations_picture"."content_type_id",
    "polymorphic_associations_picture"."file_name"
FROM
    "polymorphic_associations_picture"
WHERE
    (
        "polymorphic_associations_picture"."content_type_id" = 2
    AND "polymorphic_associations_picture"."object_id" = 1
    )'
>>>
>>> str(product.pictures.all().query)
'SELECT
    "polymorphic_associations_picture"."id",
    "polymorphic_associations_picture"."object_id",
    "polymorphic_associations_picture"."content_type_id",
    "polymorphic_associations_picture"."file_name"
FROM
    "polymorphic_associations_picture"
WHERE
    (
        "polymorphic_associations_picture"."content_type_id" = 3
    AND "polymorphic_associations_picture"."object_id" = 1
    )'

```