from odoo import models, fields

class Especie(models.Model):
    _name = 'especie'
    _description = 'Especie Model'

    name_vulgar = fields.Char(string="Nombre común", required=True)
    name_cientifico = fields.Char(string="Nombre científico", required=True)
    familia = fields.Char(string="Familia")
    peligro = fields.Selection(
        [   
            ('nulo', 'Nulo'),
            ('bajo', 'Bajo'),
            ('medio', 'Medio'),
            ('alto', 'Alto'),
        ],
        string="Nivel de peligro"
    )
    peligro_extincion = fields.Boolean(string="Peligro de extinción")
    
    #Relación con la tabla animal de OneToMany
    animal_ids = fields.One2many('animal', 'especie_id')
    