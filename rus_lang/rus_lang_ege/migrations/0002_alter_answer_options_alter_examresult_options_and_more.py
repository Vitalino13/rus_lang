# Generated by Django 4.1.5 on 2023-01-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rus_lang_ege', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['id'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='examresult',
            options={'verbose_name': 'Результат теста', 'verbose_name_plural': 'Результаты тестов'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rus_lang_ege.test'),
            preserve_default=False,
        ),
    ]