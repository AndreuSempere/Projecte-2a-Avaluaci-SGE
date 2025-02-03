from odoo import models, fields, api

class Zoo(models.Model):
    _name = 'zoo'
    _description = 'Zoo Model'
    _rec_name = 'nombre' 

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

    cantidad_animales = fields.Integer(string="Cantidad de animales", compute="_compute_cantidad_animales", store=True)

    # Relación con la tabla animal de OneToMany
    animal_ids = fields.One2many('animal', 'zoo_id', string="Animales")

    _sql_constraints = [
        ('check_superficie', 'CHECK(superficie > 0)', 
         'La superficie debe ser un número positivo'),
    ]

    @api.depends('animal_ids')
    def _compute_cantidad_animales(self):
        for zoo in self:
            zoo.cantidad_animales = len(zoo.animal_ids)
