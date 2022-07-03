# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2022 Halltic Tech S.L. (https://www.halltic.com)
#                  Tristán Mozos <tristan.mozos@halltic.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This project is based on connector-magneto, developed by Camptocamp SA
##############################################################################

from odoo.addons.component.core import Component


class AmazonModelBinder(Component):
    """ Bind records and give odoo/amazon ids correspondence

    Binding models are models called ``amazon.{normal_model}``,
    like ``amazon.res.partner`` or ``amazon.product.product``.
    They are ``_inherits`` of the normal models and contains
    the Amazon ID, the ID of the Amazon Backend and the additional
    fields belonging to the Amazon instance.
    """
    _name = 'amazon.binder'
    _inherit = ['base.binder', 'base.amazon.connector']
    _apply_on = [
        'amazon.product.product',
        'amazon.product.product.detail',
        'amazon.sale.order',
        'amazon.sale.order.line',
        'amazon.res.partner',
        'amazon.res.partner.feedback',
    ]