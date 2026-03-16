"use strict";
const instructionsList = document.querySelector("#instructions-container");
const ingridientsList = document.querySelector("#ingridients-container");
function addingridientHTML() {
    return `
    <li class="ingridient-item">
      <div>
        <label for="recipe_ingridient"></label>
        <input
          type="text"
          name="recipe_ingridient"
          placeholder="e.g. butter"
        />
        <input type="text" name="ingridient_amount" placeholder="e.g. 170" />
        <select name="recipe_ingridient_unit">
          <option value="">unit</option>
          <option>g</option>
          <option>kg</option>
          <option>ml</option>
          <option>L</option>
          <option>pinch</option>
          <option>tsp</option>
          <option>tbsp</option>
        </select>
        <button type="button" onclick="rmvingridient(this)">Remove</button>
      </div>
    </li>
  `;
}
function createStepHTML() {
    return `
    <div class="drag-wrapper">
      <div id="instruction-step" class="drag-tool" aria-label="drag & drop">
        <img  class="drag-icon" alt="six dots that make it look dragable" src="/static/icons/drag_icon.svg"/>
        <label class="step-label" style="display: none;"></label>
        <textarea
        name="instruction"
        placeholder="Add Instruction here..."
        ></textarea>
      </div>
      <div class="step-actions">
        <button type="button" class="btn-rmv" onclick="rmvStep(this)">
          <img alt="plus-sign" src="/static/icons/delete_icon.svg" />
        </button>
      </div>
    </div>
  `;
}
function addingridient() {
    const li = document.createElement("li");
    li.innerHTML = addingridientHTML();
    ingridientsList?.appendChild(li);
}
function rmvingridient(btn) {
    if (ingridientsList && ingridientsList.children.length > 1) {
        btn.closest(".ingridient-item")?.remove();
    }
}
function addStep() {
    const row = document.createElement("li");
    row.draggable = true;
    row.className = "step-no";
    row.innerHTML = createStepHTML();
    instructionsList?.appendChild(row);
    row.querySelector("textarea")?.focus();
}
function rmvStep(btn) {
    if (instructionsList && instructionsList.children.length > 1) {
        btn.closest(".step-no")?.remove();
    }
}
// Drag & drop
function initDragDrop() {
    instructionsList?.addEventListener("dragstart", (e) => {
        const target = e.target.closest(".step-no");
        if (target) {
            target.classList.add("dragging");
            e.dataTransfer?.setData("text/plain", "");
        }
    });
    instructionsList?.addEventListener("dragend", () => {
        document.querySelector(".dragging")?.classList.remove("dragging");
    });
    instructionsList?.addEventListener("dragover", (e) => {
        e.preventDefault();
        const dragging = document.querySelector(".dragging");
        const target = e.target.closest(".step-no:not(.dragging)");
        if (dragging && target) {
            const rect = target.getBoundingClientRect();
            const midY = rect.top + rect.height / 2;
            if (e.clientY < midY) {
                instructionsList?.insertBefore(dragging, target);
            }
            else {
                instructionsList?.insertBefore(dragging, target.nextSibling);
            }
        }
    });
}
// Init on DOM ready
document.addEventListener("DOMContentLoaded", () => {
    initDragDrop();
});
//# sourceMappingURL=app.js.map