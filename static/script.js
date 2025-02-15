console.log('script.js loaded');

document.getElementById('addClassForm').addEventListener('submit', async function(event) {
    event.preventDefault();
  
    const title = document.getElementById('title').value;
    const weight = document.getElementById('weight').value;
    
    if (title && weight) {
      const data = {
        [title]: {
          "Weight": weight,
          "Grade": ""  // Initial grade is empty
        }
      };
  
      try {
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
          window.location.reload();  // Reload the page to show the updated list
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
  