
    function validateForm() {
        var x1 = document.forms["loginform"]["username"].value;
        if (x1 == "") {
            alert("اطلاعات نا معتبر است1");
            return false;
        }
        var x2 = document.forms["loginform"]["email"].value;
        if (x2.substr(x2.length - 8 ) != "ut.ac.ir") {
            alert("اطلاعات نا معتبر است2");
            return false;
        }
        else if (x2==""){
            alert("اطلاعات نا معتبر است3");
            return false
        }
        var x3 = document.forms["loginform"]["pass"].value;
        var x4 = document.forms["loginform"]["pass2"].value;
        var1 = false;
        var2 = false;
        var3 = false;

        if (x3 != x4){
            alert("اطلاعات نا معتبر است4")
        }
        var x5 = document.forms["loginform"]["stdid"].value;
        if (x5.length != 9){
            alert("اطلاعات نا معتبر است5")
        }

        var str = document.forms["loginform"]["pass"].value;

        if (str.search(/\d/) == -1) {
            alert("اطلاعات نا معتبر است6");
            return(false);
        } else if (str.search(/[^0-9a-zA-Z+$]/) == -1) {
            alert("اطلاعات نا معتبر است8");
            return(false);
        }
        return true;
    }
