document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".load-link").forEach(function(link) {
        link.addEventListener("click", function() {
            document.getElementById("loader").classList.remove("d-none");
        });
    });
});
