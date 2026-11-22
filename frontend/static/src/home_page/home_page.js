/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class TaskManagementHome extends Component {
    static template = "frontend.HomePage";
}

registry.category("actions").add("frontend.home_page", TaskManagementHome);
