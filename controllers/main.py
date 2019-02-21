# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import ensure_db

import werkzeug.utils
import werkzeug.wrappers
from werkzeug import url_encode

logger = logging.getLogger(__name__)


class Website(http.Controller):

    def _redirect_to_view(self, action_id, res_id=False):
        params = {'view_type': action_id['view_mode'], 'model': 'crm.lead', 'action': action_id.id}
        if res_id:
            params.update({'id': res_id})
            params.update({'view_type': 'form'})
        url = '/web#%s' % url_encode(params)
        return werkzeug.utils.redirect(url)

    @http.route([
        '/in/<string:in_route>',
        '/in/<string:in_route>/<int:res_id>'], type='http', auth="none")
    def object_in_route(self, in_route, res_id=False, **kw):
        # action_id = request.env.ref('crm.crm_lead_opportunities_tree_view', raise_if_not_found=False)
        ensure_db()
        action_id = request.env['ir.actions.act_window'].sudo().search([
            ('in_route', '=', in_route)], limit=1)
        if action_id:
            return self._redirect_to_view(action_id, res_id)
        else:
            return werkzeug.utils.redirect('/web/login?error=access')
