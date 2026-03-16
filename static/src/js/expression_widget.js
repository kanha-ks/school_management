/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

export class ExpressionWidget extends Component {

//      static template = "school_management.ExpressionWidget";
//      static props = {...standardWidgetProps};

    setup(){
        console.log("I am the expression_widget js file")
    }

  //after clicking on enter this field called
//  ev.target.value; <- with ev
    onInputChange(ev) {

//    debugger;

        let expression = ev.target.value;

        // with This we can--> store expression in the actual field
        this.props.record.update({ //with this we have the access of all the fields
            [this.props.name]: expression, // this.prop.name is giving us the name of the current field where the widget is applied that's why we'll get the current field name
        });

        //props.name	- name of the field the widget is attached to
        //props.value	- current value of that field
        //props.record	- the record being edited in the form

        if (!expression) {
    //        throw new Error("The expression can't be null");
    //          this.props.update(expression);
            this.props.record.update({
            result_field: 0, // with the props.record -> contains ALL fields of the form view
            });
            return; //jump out directly from the function
        }

    //    debugger;
        let calculatedResult;
        try {
            calculatedResult = eval(expression); //eval means evaluate the expression
        } catch (e) { //if any error occur we can pass e and handle with catch
            console.error("Invalid expression", e); //here handlin the expression
            calculatedResult = 0;
        }

        // only update result field for display
        this.props.record.update({
            result_field: calculatedResult,
        });
    }
}

ExpressionWidget.template = "school_management.ExpressionWidget";

ExpressionWidget.props = {
    ...standardFieldProps,
};

registry.category("fields").add("expression", {
    component: ExpressionWidget,
});


/* This runs when the user stops typing and clicks away (change event)
    onChangeInput(ev) {
        const newValue = ev.target.value;
        // This tells Odoo to save the "2+2" string into the database
        this.props.update(newValue); --> it is throwing the error
    }
    */

//    calculateResult() {
//        console.log("Result calculated")
     /* if (!val) {
            return "";
        }
        try {
            // eval() works like it converts string "2+2" into the number 4
            return eval(val);
        } catch (error) {
            // If the user types something wrong like "2+abc", show this:
            return "Invalid Math";
        } */
//    }