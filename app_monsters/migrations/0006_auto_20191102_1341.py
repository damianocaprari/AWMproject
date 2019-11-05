# Generated by Django 2.1.5 on 2019-11-02 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_monsters', '0005_auto_20191102_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monsteraction',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterconditionimmunity',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterdamageimmunity',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterdamageresistance',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterdamagevulnerability',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterlanguage',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterlegendaryaction',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterreaction',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monstersave',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monstersense',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterskill',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterspecialabilities',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monsterspeed',
            old_name='monster',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='monstertrait',
            old_name='monster',
            new_name='owner',
        ),
    ]
