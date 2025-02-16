document.getElementById('addClassForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  console.log('Form submission started');

  const title = document.getElementById('title').value;
  const weight = document.getElementById('weight').value;
  const dueDate = document.getElementById('dueDate').value;

  // Validate weight
  if (isNaN(weight) || weight < 0 || weight > 100) {
    alert('Weight must be a number between 0 and 100.');
    return;
  }

  // Validate due date
  const today = new Date();
  const selectedDate = new Date(dueDate);
  if (selectedDate < today) {
    alert('Due date must be in the future.');
    return;
  }

  if (title && weight && dueDate) {
    const data = {
      [title]: {
        "Weight": weight,
        "Due Date": dueDate,
        "Grade": "" // Default grade is an empty string
      }
    };

    try {
      const response = await fetch('/add_class', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' // Ensure this header is set
        },
        body: JSON.stringify(data) // Convert data to JSON
      });

      if (response.ok) {
        alert('Class added successfully!');
        closeModal();
        window.location.reload(); // Reload the page to show the updated list
      } else {
        const result = await response.json();
        alert(`Failed to add class: ${result.error}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while adding the class.');
    }
  } else {
    alert('Please fill out all fields.');
  }
});