# Generated by Django 3.1.4 on 2021-01-07 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('galpao', models.CharField(max_length=50)),
                ('corredor', models.CharField(max_length=50)),
                ('quantidade_prateleiras', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=15)),
                ('tipo', models.CharField(choices=[('OP', 'Operador'), ('GER', 'Gerente')], default='OP', max_length=3)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code_url', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('largura', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('comprimento', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('descricao', models.CharField(max_length=350)),
                ('num_prateleira', models.IntegerField(default=0)),
                ('valor_compra', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
                ('valor_venda', models.DecimalField(decimal_places=2, default=15.0, max_digits=12)),
                ('numero_prateleira', models.IntegerField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRcodeStock.categoria', verbose_name='ID Categoria')),
                ('id_estante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRcodeStock.estante', verbose_name='ID Estante')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('observacoes', models.CharField(max_length=100)),
                ('data_fabricacao', models.DateField()),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRcodeStock.produto', verbose_name='ID Produto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRcodeStock.usuario', verbose_name='Usuario criador')),
            ],
        ),
    ]
