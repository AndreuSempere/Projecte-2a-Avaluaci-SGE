from odoo import models, fields

class Familia(models.Model):
    _name = 'familia'
    _rec_name = 'nombre'


    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    
    # Relación con la tabla Especie de One2Many
    especie_id = fields.One2many('especie', 'familia_id', string="Especies")

    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(nombre)', 'La familia no se puede repetir.')
    ]