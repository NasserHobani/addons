# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nfc_link(models.Model):
    _name = 'nfc_link.nfc_link'
    _description = 'nfc_link.nfc_link'

    nf_card_id = fields.Integer('Card ID')
    nf_qr_id = fields.Char('Qr ID')
    nf_type = fields.Selection([('card', 'Card'), ('qr', 'Qr')], 'Type')
    action_type = fields.Selection([('insta', 'Instagram'), ('wh_app', 'Whatsapp')], 'Action Type')
    instagram_user = fields.Char('Instagram User')
    whatsapp_user = fields.Char('Whatsapp User')
    instagram_link = fields.Char('Instagram Link')
    whatspp_link = fields.Char('Whatsapp Link')
    partner_id = fields.Many2one('res.partner', 'Partner',default=lambda self: self.env.user.partner_id)
    description = fields.Html('Notes')

class Contact(models.Model):
    _inherit = 'res.partner'

    nfc_ids = fields.One2many('nfc_link.nfc_link','partner_id','NFC')
