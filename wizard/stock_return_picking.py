# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

from openerp import api, fields, models


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    return_reason_id = fields.Many2one(
        'stock.warehouse.return', 'Reason for return picking', required=True)

    @api.multi
    def _create_returns(self):
        new_picking_id, picking_type_id = super(
            StockReturnPicking, self)._create_returns()
        StockPicking = self.env['stock.picking']
        new_picking = StockPicking.browse(new_picking_id)
        new_picking.write({'return_reason_id': self.return_reason_id.id})
        return new_picking_id, picking_type_id
