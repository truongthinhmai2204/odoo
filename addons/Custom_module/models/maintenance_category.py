class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    
    maintenance_category_id = fields.Many2one(
        "maintenance.category", 
        string="Category", 
        ondelete="set null"
    )
