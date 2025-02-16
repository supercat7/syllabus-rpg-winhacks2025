document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('uploadSyllabusForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    console.log('File upload started');
    
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
    
      if (response.ok) {
        const result = await response.json();
        console.log('Parsed data:', result);
        displayResultsInModal(result.data);
      } else {
        const errorText = await response.text();
        console.error('Failed to parse syllabus:', errorText);
        alert('Failed to parse syllabus. Please try again.');
      }
    } catch (error) {
      console.error('Error during file upload:', error);
      alert('An error occurred while uploading the file.');
    }
  });
});


function displayResultsInModal(data) {
  const resultsTableBody = document.getElementById('resultsTableBody');
  resultsTableBody.innerHTML = ''; // Clear previous results

  if (Array.isArray(data)) {
     data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
           <td class="px-4 py-2 border-b">${item.name}</td>
           <td class="px-4 py-2 border-b">${item.dueDate}</td>
           <td class="px-4 py-2 border-b">${item.weight}</td>
        `;
        resultsTableBody.appendChild(row);
     });
  } else {
     // Handle the case where data is not an array
     console.error('Data is not an array:', data);
     resultsTableBody.innerHTML = '<tr><td colspan="3" class="text-center">No valid results found</td></tr>';
  }

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
