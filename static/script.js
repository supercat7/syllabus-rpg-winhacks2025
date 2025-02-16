document.getElementById('uploadSyllabusForm').addEventListener('submit', async function(event) {
  event.preventDefault();

  const fileInput = document.getElementById('syllabusFile');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please select a file before uploading.');
    return;
  }

  const formData = new FormData();
  formData.append('syllabusFile', file);

  try {
    const response = await fetch('/parse_syllabus', {
      method: 'POST',
      body: formData
    });

    const result = await response.json();

    if (response.ok) {
      displayResultsInModal(result.data);
    } else {
      alert('Failed to parse the syllabus.');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred while processing the syllabus.');
  }
});

function displayResultsInModal(data) {
  const resultsTableBody = document.getElementById('resultsTableBody');
  resultsTableBody.innerHTML = ''; // Clear previous results

  data.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td class="px-4 py-2 border-b">${item.name}</td>
      <td class="px-4 py-2 border-b">${item.dueDate}</td>
      <td class="px-4 py-2 border-b">${item.weight}</td>
    `;
    resultsTableBody.appendChild(row);
  });

  openResultsModal();
}

function openResultsModal() {
  const modal = document.getElementById('resultsModal');
  modal.classList.remove('hidden');
  document.getElementById('resultsModalContent').classList.add('scale-100');
}

function closeResultsModal() {
  const modal = document.getElementById('resultsModal');
  modal.classList.add('hidden');
  document.getElementById('resultsModalContent').classList.remove('scale-100');
}

function openModal() {
  document.getElementById('modal').classList.remove('hidden');
  document.getElementById('modal-content').classList.add('scale-100');
}

function closeModal() {
  document.getElementById('modal').classList.add('hidden');
  document.getElementById('modal-content').classList.remove('scale-100');
}
