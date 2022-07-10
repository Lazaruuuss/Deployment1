//Mobile Menu / Hamburger
const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');

// To Display Mobile Menu / Hamburger
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);



//Admin-Borrower Login Switcher
const switchers = [...document.querySelectorAll('.switcher')]

switchers.forEach(item => {
    item.addEventListener('click', function() {
        switchers.forEach(item => item.parentElement.classList.remove('is-active'))
        this.parentElement.classList.add('is-active')
    })
})


var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function adminvalidate(){
    var admin_password = document.getElementById("admin_password").value;
    
    if ( admin_password == "122000"){
        alert ("Login successfully");
        document.getElementById("admin_password").value="";
        window.location = "3.1_Admin_Home.html"; // Redirecting to other page.
        return false;
    }
    else{
        attempt --;// Decrementing by one.
        alert("You have "+attempt+" left attempt;");
        document.getElementById("admin_password").value="";
        // Disabling fields after 3 attempts.
        if( attempt == 0){
            document.getElementById("admin_password").disabled = true;
            document.getElementById("admin_btn").disabled = true;
            return false;
        }
    }
}