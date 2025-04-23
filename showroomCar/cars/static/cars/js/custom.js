document.getElementById('view-grid').addEventListener('click', function() {
    document.getElementById('car-container').setAttribute('data-view', 'grid');
    document.querySelectorAll('.car-item').forEach(function(item) {
        item.classList.add('d-none');
        if (item.classList.contains('grid-view')) {
        item.classList.remove('d-none');
        }
    });
    });

    document.getElementById('view-list').addEventListener('click', function() {
    document.getElementById('car-container').setAttribute('data-view', 'list');
    document.querySelectorAll('.car-item').forEach(function(item) {
        item.classList.add('d-none');
        if (item.classList.contains('list-view')) {
        item.classList.remove('d-none');
        }
    });
    });

    // Select the button using its class
    const closeButton = document.querySelector('.close');

    // Add a click event listener
    closeButton.addEventListener('click', () => {
        console.log('Close button clicked!');
        // Add your logic here, e.g., hiding a modal or alert
    });

    // Close button functionality
    document.querySelectorAll('.close').forEach(function(button) {
        button.addEventListener('click', function() {
            const card = this.closest('.car-item');
            card.remove();
        });
    });