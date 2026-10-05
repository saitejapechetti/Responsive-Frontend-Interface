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


// Backend API
const API_URL = "https://backend-api-development-d0yy.onrender.com";

async function getProjects() {

    try {

        const response = await fetch(`${API_URL}/api/projects`);

        const data = await response.json();

        console.log("Projects from backend:", data);

        return data;

    } catch (error) {

        console.error("Backend connection error:", error);

    }

}


// Call backend
getProjects();
