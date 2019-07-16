from odoo import models,fields
from odoo.addons import decimal_precision as dp

class AssetType(models.Model):
    _inherit = 'account.asset.category'

    method_progress_factor = fields.Float('Degressive Factor',digits=dp.get_precision('asset_decimal'))
