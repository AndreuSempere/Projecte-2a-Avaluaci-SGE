from odoo import models, fields

class Especie(models.Model):
    _name = 'especie'
    _description = 'Especie Model'
    _rec_name = 'name_vulgar' 


    name_vulgar = fields.Char(string="Nombre común", required=True)
    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name_vulgar)', 'El nombre vulgar no se puede repetir.')
    ]
    name_cientifico = fields.Char(string="Nombre científico", required=True)
    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name_cientifico)', 'El nombre cientifico no se puede repetir.')
    ]
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

    #Relación con Familia de Many2One
    familia_id = fields.Many2one('familia', string="Familia", options={'no_create': True, 'no_edit': True})
    
    #Relación con la tabla animal de OneToMany
    animal_ids = fields.One2many('animal', 'especie_id')
    