function getinfo() {
        var fname = document.getElementById("First Name").value;
        var lname = document.getElementById("Last Name").value;
        var mm = document.getElementById("mm").value;
        var dd = document.getElementById("dd").value;
        var yyyy = document.getElementById("yyyy").value;
        var bplace = document.getElementById("birthplace").value;
        var uname = document.getElementById("Username").value;
        var pword = document.getElementById("Password").value;
        var copword = document.getElementById("Confirm Password").value
        if (fname !== "" && lname !== "" && mm !== "" && dd !== "" && yyyy !== "" && bplace !== "" && uname !== "" && pword !== "" && copword !== ""){
            matchPassword();
            }
        else if (fname == "" || fname == null,
            lname == "" || lname == null,
            mm == "" || mm == null,
            dd == "" || dd == null,
            yyyy == "" || yyyy == null,
            bplace == "" || bplace == null,
            uname == "" || uname == null,
            pword == "" || pword == null,
            copword == "" || copword == null){
            alert("Please input missing fields!");
            return false;
            }
        }

    function matchPassword() {
        var p1 = document.getElementById("Password").value;
        var p2 = document.getElementById("Confirm Password").value;
        if (p1 == p2){
            alert("Passwords are match!")
            window.location = "Log-in 1.html";
            return true;
        }
        else if (p1 !== p2){
            alert("Passwords do not match!");
            return false;
        }
    }
    function lettersOnly(evt) {
        evt = (evt) ? evt : event;
        var charCode = (evt.charCode) ? evt.charCode : ((evt.keyCode) ? evt.keyCode :
            ((evt.which) ? evt.which : 0));
        if (charCode > 31 && (charCode < 65 || charCode > 90) &&
            (charCode < 97 || charCode > 122)) {
            return false;
        }
        return true;
        }
    function isNumber(evt) {
        evt = (evt) ? evt : window.event;
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
            }
        return true;
        }