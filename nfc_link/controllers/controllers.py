# -*- coding: utf-8 -*-
from odoo import http


# class NfcLink(http.Controller):
#     @http.route('/nfc_link/<int:cc_id>', type='http', methods=['GET'], website=True, auth='public')
#     def index(self, cc_id, **kw):
#         return "Hello, world" + str(cc_id) + "ID"


class NfcCard(http.Controller):
    @http.route('/nfc_link/<int:cc_id>', type='http', methods=['GET'], website=True, auth='public')
    def index(self, cc_id, **kw):
        return "Hello, world" + str(cc_id) + "ID"

    @http.route('/card/<int:cc_id>', type='http', methods=['GET'], website=True, auth='public')
    def card(self, cc_id, **kw):
        card = http.request.env['nfc_link.nfc_link'].search([('nf_card_id','=',cc_id)])
        return "Hello, world" + str(card.instagram_user) + "card"

    @http.route('/qr/<int:cc_id>', type='http', methods=['GET'], website=True, auth='public')
    def qr(self, cc_id, **kw):
        return "Hello, world" + str(cc_id) + "qr"

#     @http.route('/nfc_link/nfc_link/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nfc_link.listing', {
#             'root': '/nfc_link/nfc_link',
#             'objects': http.request.env['nfc_link.nfc_link'].search([]),
#         })

#     @http.route('/nfc_link/nfc_link/objects/<model("nfc_link.nfc_link"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nfc_link.object', {
#             'object': obj
#         })
