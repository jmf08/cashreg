function isNumber(evt) {
        evt = (evt) ? evt : window.event;
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
            }
        return true;
        }
    function dis(val) 
        { 
            document.getElementById("calcu").value+=val; 
        }

    function solve() 
        { 
             let x = document.getElementById("calcu").value; 
             let y = eval(x); 
             document.getElementById("calcu").value = y;
        }

    function sukli()
        {
            let x = document.getElementById("total").value;
            let y = document.getElementById("cash").value;
            let z = y - x;
            document.getElementById("change").value = z;
        }

    function clr() 
        { 
             document.getElementById("calcu").value = ""; 
        }