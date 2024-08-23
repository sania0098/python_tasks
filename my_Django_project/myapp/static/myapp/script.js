document.addEventListener('DOMContentLoaded', function () {
    console.log("Welcome to My First Web App!");

    // Example: Show an alert when the user clicks on the 'About' link
    document.querySelector('a[href="#about"]').addEventListener('click', function() {
        alert("You clicked on the About link!");
    });
});
