# Object Route
Adds routes to the web client actions so that you can use in an email or message:
e.g.

/in/leads
/in/leads/345
/in/partner/1200
...

You just need to add this additional argument to the action you want to add to the "in" rout:

```xml
    <record model="ir.actions.act_window" id="crm.crm_lead_opportunities_tree_view">
        <field name="in_route">leads</field>
    </record>
```

See it in action:

https://twitter.com/diogormcduarte/status/1098703437611573248
