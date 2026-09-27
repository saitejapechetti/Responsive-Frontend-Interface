function toggleMenu() {

    const navLinks = document.getElementById("navLinks");

    navLinks.classList.toggle("active");
}


function showMessage(courseName) {

    alert(
        "You selected: " + courseName +
        "\nRegistration is available below."
    );

}


function registerUser(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const course = document.getElementById("course").value;

    alert(
        "Registration successful!\n\n" +
        "Name: " + name +
        "\nCourse: " + course
    );

}