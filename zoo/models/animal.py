from odoo import models, fields,api
from datetime import date


class Animal(models.Model):
    _name = 'animal'
    _description = 'Animal Model'

    nombre = fields.Char(string="Nombre", required=True)
    continente_origen = fields.Selection(
        [   
            ('antartida', 'Antartida'),
            ('america', 'America'),
            ('europa', 'Europa'),
            ('asia', 'Asia'),
            ('africa', 'Africa'),
        ],
        string="Continente Origen"
    )
    pais_origen = fields.Char(string="Pais Origen")
    fecha_nacimiento = fields.Date(copy=False)
    edad = fields.Integer(string="Edad", compute="edad_computada")
    sexo = fields.Selection(
        [
            ('macho', 'Macho'),
            ('hembra', 'Hembra'),
        ],
        string="Sexo"
    )
    # Relación con la tabla zoo de ManyToOne
    zoo_id = fields.Many2one('zoo', string="Zoo", options={'no_create': True, 'no_edit': True})
    # Relación con la tabla especie de ManyToOne
    especie_id = fields.Many2one('especie', string="Especie", options={'no_create': True, 'no_edit': True})

    @api.depends('fecha_nacimiento')
    def edad_computada(self):
        today = date.today()
        for record in self:
            if record.fecha_nacimiento:
                birth_date = record.fecha_nacimiento
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.edad = age
            else:
                record.edad = 0
