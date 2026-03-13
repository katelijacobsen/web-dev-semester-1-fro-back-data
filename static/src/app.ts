"use strict";

const instructionsList = document.querySelector<HTMLOListElement>(
  "#instructions-container",
);
const ingridientsList = document.querySelector<HTMLUListElement>(
  "#ingridients-container",
);

function addingridientHTML(): string {
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

function createStepHTML(): string {
  return `
    <div id="instruction-step" class="drag-tool" aria-label="drag & drop">DRAG ME</div>
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


function addingridient(): void {
  const li = document.createElement("li");
  li.innerHTML = addingridientHTML();
  ingridientsList?.appendChild(li);
}


function rmvingridient(btn: HTMLButtonElement): void {
  if (ingridientsList && ingridientsList.children.length > 1) {
    btn.closest(".ingridient-item")?.remove();
  }
}

function addStep(): void {
  const row = document.createElement("li");
  row.draggable = true;
  row.className = "step-no";
  row.innerHTML = createStepHTML();

  instructionsList?.appendChild(row);
  row.querySelector("textarea")?.focus();
}

function rmvStep(btn: HTMLButtonElement): void {
  if (instructionsList && instructionsList.children.length > 1) {
    btn.closest(".step-no")?.remove();
  }
}

// Drag & drop
function initDragDrop(): void {
  instructionsList?.addEventListener("dragstart", (e: DragEvent) => {
    const target = (e.target as HTMLElement).closest<HTMLElement>(".step-no");
    if (target) {
      target.classList.add("dragging");
      e.dataTransfer?.setData("text/plain", "");
    }
  });

  instructionsList?.addEventListener("dragend", () => {
    document.querySelector(".dragging")?.classList.remove("dragging");
  });

  instructionsList?.addEventListener("dragover", (e: DragEvent) => {
    e.preventDefault();
    const dragging = document.querySelector<HTMLElement>(".dragging");
    const target = (e.target as HTMLElement).closest<HTMLElement>(
      ".step-no:not(.dragging)",
    );

    if (dragging && target) {
      const rect = target.getBoundingClientRect();
      const midY = rect.top + rect.height / 2;
      if (e.clientY < midY) {
        instructionsList?.insertBefore(dragging, target);
      } else {
        instructionsList?.insertBefore(dragging, target.nextSibling);
      }
    }
  });
}

// Init on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  initDragDrop();
});