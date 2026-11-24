from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Тауар атауы")),
                ("quantity", models.PositiveIntegerField(verbose_name="Ағымдағы саны")),
                ("min_quantity", models.PositiveIntegerField(verbose_name="Ең аз қор мөлшері")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Тіркелген уақыты")),
            ],
            options={
                "verbose_name": "Тауар",
                "verbose_name_plural": "Тауарлар",
                "ordering": ["name"],
            },
        ),
    ]
