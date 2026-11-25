// app.js — vanilla JS frontend for the Flask notes app (P1)
// Teaches: fetch, DOM manipulation, template literals, async/await.

const noteList = document.getElementById("note-list");
const noteInput = document.getElementById("note-input");
const noteForm = document.getElementById("note-form");

async function fetchNotes() {
  const res = await fetch("/api/notes");
  if (!res.ok) return;
  noteList.innerHTML = "";
  const notes = await res.json();
  for (const note of notes) {
    const div = document.createElement("div");
    div.className = "note";
    div.innerHTML = `
      <p>${escapeHtml(note.text)}</p>
      <button data-id="${note.id}" class="delete-btn">Delete</button>
    `;
    noteList.appendChild(div);
  }
  document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      await fetch(`/api/notes/${btn.dataset.id}`, { method: "DELETE" });
      fetchNotes();
    });
  });
}

async function addNote(text) {
  await fetch("/api/notes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  fetchNotes();
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

noteForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = noteInput.value.trim();
  if (text) {
    addNote(text);
    noteInput.value = "";
  }
});

fetchNotes();
