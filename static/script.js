console.log('script.js loaded');

document.getElementById('addClassButton').addEventListener('click', openModal);

function openModal() {
  document.getElementById('modal').classList.remove('hidden');
  document.getElementById('modal-content').classList.add('scale-100');
}

function closeModal() {
  document.getElementById('modal').classList.add('hidden');
  document.getElementById('modal-content').classList.remove('scale-100');
}

document.getElementById('addClassForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  console.log('trying 2');

  const title = document.getElementById('title').value;
  const weight = document.getElementById('weight').value;
  const dueDate = document.getElementById('dueDate').value;

  if (title && weight && dueDate) {
    const data = {
      [title]: {
        "Weight": weight,
        "Due Date": dueDate,
        "Grade": "" // Default grade is an empty string
      }
    };

    try {
      console.log('trying 1');
      const response = await fetch('/add_class', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        alert('Class added successfully!');
        closeModal();
        window.location.reload(); // Reload the page to show the updated list
      } else {
        alert('Failed to add class. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while adding the class.');
    }
  } else {
    alert('Please fill out all fields.');
  }
});
