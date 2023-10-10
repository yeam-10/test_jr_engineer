# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    user_site_id = fields.Many2one('res.users', string="Project site", default=lambda self: self.env.user, tracking=True)
    date_deadline = fields.Date('Deadline')
    budget = fields.Float('Budget')
    project_size = fields.Selection(selection=[ 
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ], string="Project Size", help="")
    
    stage_id = fields.Many2one('site.stage', string="Stage ID")