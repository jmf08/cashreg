function enterPassword() {
        var username = document.getElementById("Username").value;
        var password = document.getElementById("Password").value;
        if (username == "hello" && password == "1234") {
            window.location = "Cash Register 3.html";
            return true; 
            }
        else if (username == "" && password == "") {
            alert("Please Input Username or Password");
            return false;
            }
        else if (username !== "hello" && password !== "1234") {
            alert("Either Username or Password is incorrect");
            return false;
            }
        else if (username == "hello" && password !== "1234") {
            alert("Either Username or Password is incorrect");
            return false;
            }
        else if (username !== "hello" && password == "1234") {
            alert("Either Username or Password is incorrect");
            return false;
            }
}