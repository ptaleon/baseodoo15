from odoo import models, fields, api, _


class InstitutoCursos(models.Model):
    _name = 'instituto.cursos'
    _description = 'Datos de Cursos'

    name = fields.Char(string='Nombre del Curso', required=True)
    descripcion = fields.Text(string='Descripción del Curso')
    duracion = fields.Integer(string='Duración en semanas')
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Fin')
    alumnos_ids = fields.One2many(
        'instituto.alumnos', 'curso_id', string='Alumnos Inscritos')
    activo = fields.Boolean(string='Activo', default=True)
