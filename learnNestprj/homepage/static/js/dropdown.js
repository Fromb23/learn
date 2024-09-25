const userIcon = document.querySelector('.user-icon');
if (userIcon) {
    userIcon.addEventListener('click', function() {
        document.querySelector('.user-dropdown_content').classList.toggle('show');
    });
}

const dropdown = document.querySelector('.header .dropdown #services');

const textElement = document.querySelector('#services');

if (textElement) {
    textElement.addEventListener('mouseover', function() {
        textElement.style.color = 'red';
    });

    textElement.addEventListener('mouseout', function() {
        textElement.style.color = 'black';
    });
}

 // display edxcel section
document.getElementById('edexcel-link').addEventListener('click', function(event) {
        fetch('/edexcel/')
        .then(response => response.text())
        .then(data => {
                event.preventDefault();
                console.log("Edexcel link clicked");
                document.getElementById('description').innerHTML = data;
        })
        .catch(error => console.error('Error loading the curriculum:', error));
});

// display igcse section
document.getElementById('igcse-link').addEventListener('click', function(event) {
        fetch('/igcse/')
        .then(response => response.text())
        .then (data => {
                event.preventDefault();
                console.log("IGCSE link clicked");
                document.getElementById('description').innerHTML = data;
        })
        .catch (error => console.error("Error laodin the igcse:", error));
});

// display 8-4-4 section
document.getElementById('eight-four-four-link').addEventListener('click', function(event) {
        fetch('/844/')
        .then(response => response.text())
        .then (data => {
                event.preventDefault();
                console.log("8-4-4 link clicked");
                document.getElementById('description').innerHTML = data;
        })
        .catch (error => console.error("Error laodin the igcse:", error));
});
