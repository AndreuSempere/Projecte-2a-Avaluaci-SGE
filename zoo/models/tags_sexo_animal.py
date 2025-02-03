from odoo import models, fields

class AnimalSexoTags(models.Model):
    _name = 'animal.sexo.tags'
    _rec_name = 'sexo'

    sexo = fields.Selection(
        [
            ('Macho', 'Macho'),
            ('Hembra', 'Hembra'),
        ],
        string="Tipo"
    )
    color = fields.Integer(string="Color", default=0)

    animal_ids = fields.One2many('animal', 'sexo_id', string="Animales")

    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(sexo)', 'The tag name must be unique.')
    ]
