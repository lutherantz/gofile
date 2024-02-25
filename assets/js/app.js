document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file");
    const form = document.querySelector(".form_otp");
    const fileUrl = document.querySelector(".dowL");
    
    fileUrl.style.display = "none";

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData();
        for (const file of fileInput.files) {
            formData.append("files", file);
        }

        fetch("/upload", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            fileUrl.style.display = "block";

            if(String(data).includes("were")) {
                fileUrl.innerHTML = data;
                return
            }

            fileUrl.innerHTML = `<a href="${data}" target="_blank">See Link</a>`;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});

function updateFileName() {
    const fileInput = document.getElementById("file");
    const fileUrl = document.querySelector(".dowL");
    const fileNameElement = document.getElementById("fileName");

    if (fileInput.files.length > 0) {
        fileUrl.style.display = "none";
        const fileName = fileInput.files[0].name;
        fileNameElement.innerHTML = `<i class="fa-solid fa-file"></i> ${fileName}`;
        document.querySelector(".fileUrl").style.display = "flex";
    } else {
        fileNameElement.innerText = "";
        fileUrl.style.display = "none";
        document.querySelector(".fileUrl").style.display = "none";
    }
}