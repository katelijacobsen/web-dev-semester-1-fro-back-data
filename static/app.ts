"use strict";

interface Step {
  id: number;
  content: string;
}

const addBtn = document.querySelector<HTMLButtonElement>("#add_btn");
const list = document.querySelector<HTMLOListElement>("#intructions_container");


// Function to create Element
function createElement(step: Step):any { //adding step as a param
    const li = document.createElement("li");
    li.className = "step-element";


    const no = document.createElement("span");
    no.className = "step_no";
    no.textContent = String(step.id);


    const field = document.createElement("input");
    field.type = "text";
    field.value = step.content;
    field.placeholder = "Add intructions...";


    const rmv = document.createElement("button");
    rmv.className = "rmv_btn";
    rmv.type = "button";

    rmv.addEventListener("click", () => rmvStep(li))
}


//Remove the element
function rmvStep(element:any):void {
    element.remove();
}

// Add Step
//addBtn.addEventListener("click", addStep());

