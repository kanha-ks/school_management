/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class ThreeStateToggle extends Component {

    setup() {
        console.log("Setup of Toggle state called ")
    }

    async toggleState(value) {

        // update the field locally
        console.log("It could be show in another field : ",value)
        // Update the main toggle field (performance_toggle)
        this.props.record.update({
            [this.props.name]: value,  // updates 'performance_toggle'
        });

          // save to database
        await this.props.record.save();

        console.log("Saved:", value);

//        this.props.record.update({
//            performance_level: value
//        });

//        this.props.record.setValue(this.props.name, value);  // updatng 'performance_toggle'

//        this.props.record.data.performance_level = value;    // updatng 'performance_level' visually


//        this.props.record.data.performance_level = value;

        // commented because setValue Now deprecated & we replaced it by using update
//        this.props.record.setValue(this.props.name, value);


    }



//    async toggleState(ev) {
//
//        debugger;
//
//        // move to next state
////        this.state.position = (this.state.position + 1) % 3;
//
//        const value = ev.target.value;
//
//        // update the stored field
//        this.props.record.update({
//            performance_level: value
//        });
//
////        await this.props.record.save();
//
//        console.log(value);
//    }
//
//
}

ThreeStateToggle.template = "school_management.ThreeStateToggle";

ThreeStateToggle.props = {
    ...standardFieldProps,
};

registry.category("fields").add("three_state_toggle", {
    component: ThreeStateToggle,
});