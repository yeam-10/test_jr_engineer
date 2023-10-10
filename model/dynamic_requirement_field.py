#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning, ValidationError

class DynamicRequirement(models.Model):


    _name = 'dynamic.requirement.field'

    sequence = fields.Integer(string='Sequence', default=10)
    type_site = fields.Selection(selection=[ 
        ('Site', ' Milestone')],  
        required=True, string="Type", help="")
    name_dy = fields.Char(string="Name", default="New", copy=False)
    active = fields.Boolean(string="Active", default="True")
    project_line_ids = fields.One2many("dynamic.requirement.field.line", 'requirement_project_id', string="Project Line")
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)


    @api.model
    def create(self, vals):
        res = super(DynamicRequirement, self).create(vals)
        if self.type_site == False or self.name_dy == False :
            raise UserError(_('Revise que los siguientes campos no se encuentren vacios Name, type site'))
        return res



