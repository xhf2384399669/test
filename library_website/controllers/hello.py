from odoo import http
from odoo.http import request


class Hello(http.Controller):
    @http.route('/HelloWorld', auth='public', website=True)
    def HelloWorld(self, **kwargs):
        return request.render('library_website.HelloWorld')

    @http.route('/HelloCms/<page>', auth='public', website=True)
    def HelloCms(self, page, **kwargs):
        return http.request.render(page)
