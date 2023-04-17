from odoo import fields, models


class ProgramUsers(models.Model):
    _name = "g2p.program.user.mapping"
    _description = "Program user mapping"

    program_id = fields.Many2one("g2p.program")
    user_id = fields.Many2one("res.users")

    _sql_constraints = [
        (
            "program_user_unique",
            "unique (program_id, user_id)",
            "User must be unique per program.",
        ),
    ]


class ResUsers(models.Model):
    _inherit = "res.users"

    assigned_program_mapping = fields.One2many("g2p.program.user.mapping", "user_id")


class G2PProgram(models.Model):
    _inherit = "g2p.program"

    assigned_user_mapping = fields.One2many("g2p.program.user.mapping", "program_id")
