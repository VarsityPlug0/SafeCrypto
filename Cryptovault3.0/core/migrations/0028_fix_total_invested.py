from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_backup'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='total_invested',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ] 