from odoo import models, fields

class Zoo(models.Model):
    _name = 'zoo'
    _description = 'Zoo Model'

    nombre = fields.Char(string="Nombre", required=True)
    continentes = fields.Selection(
        [   
            ('antartida', 'Antartida'),
            ('america', 'America'),
            ('europa', 'Europa'),
            ('asia', 'Asia'),
            ('africa', 'Africa'),
        ],
        string="Continente"
    )
    pais_id = fields.Many2one('res.country', string="País", required=True)
    provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', pais_id)]")
    ciudad = fields.Char(string="Ciudad")
    superficie = fields.Integer(string="Superficie (m2)")

    # Relación con la tabla animal de OneToMany
    animal_ids = fields.One2many('animal', 'zoo_id', string="Animales")
