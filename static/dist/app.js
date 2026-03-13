"use strict";
const instructionsList = document.querySelector("#instructions-container");
const ingredientsList = document.querySelector("#ingredients-container");
function addIngredientHTML() {
    return `
    <li class="ingredient-item">
      <div>
        <label for="ingredient"></label>
        <input
          type="text"
          name="ingridient_name"
          placeholder="e.g. butter"
        />
        <input type="text" name="ingridient_amount" placeholder="e.g. 170" />
        <select name="ingredient_unit">
          <option value="">unit</option>
          <option>g</option>
          <option>kg</option>
          <option>ml</option>
          <option>L</option>
          <option>pinch</option>
          <option>tsp</option>
          <option>tbsp</option>
        </select>
        <button type="button" onclick="rmvIngredient(this)">Remove</button>
      </div>
    </li>
  `;
}
function createStepHTML() {
    return `
    <div class="drag-tool" aria-label="drag to reorder">DRAG ME</div>
    <label class="step-label"></label>
    <textarea
      name="instruction"
      placeholder="Add Instruction here..."
    ></textarea>
    <div class="step-actions">
      <button type="button" class="btn-rmv" onclick="rmvStep(this)">Remove</button>
    </div>
  `;
}
function addIngredient() {
    const li = document.createElement("li");
    li.innerHTML = addIngredientHTML();
    ingredientsList?.appendChild(li);
}
function rmvIngredient(btn) {
    if (ingredientsList && ingredientsList.children.length > 1) {
        btn.closest(".ingredient-item")?.remove();
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