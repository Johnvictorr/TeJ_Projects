# Generated by Django 5.1 on 2024-08-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(unique=True)),
                ('telefone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('valorPago', models.DecimalField(decimal_places=2, max_digits=100)),
                ('pagamento', models.BooleanField(default=True)),
                ('produtosComprados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
