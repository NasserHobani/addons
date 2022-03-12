odoo.define('website_nfc.form', function (require) {
'use strict';

var core = require('web.core');
var FormEditorRegistry = require('website.form_editor_registry');

var _t = core._t;

FormEditorRegistry.add('create_nfc', {
    formFields: [{
        type: 'Integer',
        required: true,
        name: 'nf_card_id',
        fillWith: 'nf_card_id',
        string: 'Card ID',
    }, {
        type: 'Integer',
        name: 'nf_qr_id',
        fillWith: 'nf_qr_id',
        string: 'QR ID',
    }, {
        type: 'Selection',
        required: true,
        fillWith: 'nf_type',
        name: 'nf_type',
        string: 'NFC Type',
    }, {
        type: 'Selection',
        required: true,
        fillWith: 'action_type',
        name: 'action_type',
        string: 'Action Type',
    }, {
        type: 'char',
        modelRequired: true,
        name: 'instagram_user',
        string: 'Instagram User',
    }, {
        type: 'char',
        required: true,
        name: 'whatsapp_user',
        string: 'Whatsapp User',
    },{
        type: 'char',
        required: true,
        name: 'instagram_link',
        string: 'Instagram Link',
    },{
        type: 'char',
        required: true,
        name: 'whatspp_link',
        string: 'Whatsapp Link',
    },{
        type: 'Html',
        required: true,
        name: 'description',
        string: 'Description',
    }],
    fields: [{
        name: 'partner_id',
        type: 'many2one',
        relation: 'res.partner',
//        domain: [['use_opportunities', '=', true]],
        string: _t('Partner'),
        title: _t('Partner'),
    }],
});

});