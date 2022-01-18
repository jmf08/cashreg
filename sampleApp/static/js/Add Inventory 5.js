function addinv() {
    var itemcode = document.getElementById("Item Name").value;
    var productname = document.getElementById("Product Code").value;
    var stocks = document.getElementById("Stocks").value;
    var prices = document.getElementById("Price").value;
    if (itemcode !== "" && productname !== "" && stocks !== "" && prices !== "") {
        window.location = "Inventory 4.html";
        return true; 
        }
    else if (itemcode == "" || itemcode == null, productname == "" || productname == null, stocks == "" || stocks == null, prices == "" || prices == null) {
        alert("Please input missing fields!");
        return false; 
        }
    }
    function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
        }
    return true;
    }