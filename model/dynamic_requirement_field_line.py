#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class DynamicRequirementLine(models.Model):


    _name = 'dynamic.requirement.field.line'

    sequence = fields.Integer(string='Sequence', default=10)
    requirement_project_id = fields.Many2one("dynamic.requirement.field", string="Requerement Project")
    stage_id = fields.Many2one("project.project.stage", string="Site Stage")
    mandatory_fields_ids = fields.Many2many("ir.model.fields", string="Mandatory Fields")
    custom_warning = fields.Char(string="Custom Warning Message")
    company_id = fields.Many2one("res.company", string="Company")
    
    
    @api.model
    def create(self, vals):
        res = super(DynamicRequirementLine, self).create(vals)
        if self.custom_warning == False:
            raise UserError(_('Campo requerido'))
        return res

