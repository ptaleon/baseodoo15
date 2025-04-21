from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class institutoAlumnos(models.Model):
    _name = 'instituto.alumnos'
    _description = 'Datos de Alumnos'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    direccion = fields.Text(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    # curso_id = fields.Many2one('instituto.cursos', string='Curso')
    fecha_inscripcion = fields.Date(string='Fecha de Inscripción')
