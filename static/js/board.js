function generateQRCode() {
    let size = Math.min(window.innerHeight*0.9, window.innerWidth - document.getElementById('table').offsetWidth*1.25);
    var qrcode = new QRCode(document.getElementById("QRCode"), {
        text: window.location.host + "/key/?id={{color_grid_code}}",
        width: size,
        height: size,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
}
function resizeTable() {
    document.getElementById('table').style.height = window.innerHeight*0.95 + "px";
    document.getElementById('table').style.width = window.innerHeight*0.95 + "px";
    document.getElementById('QRCodeContainer').style.left = (document.getElementById('table').offsetWidth*1.1) + "px";
}
function changeColor(element, color) {
    if(!element.style.backgroundColor) {
        if(color == "Black") {
            element.style.color = "white";
        }
        element.style.backgroundColor = color;
    }
    else {
        if(color == "Black") {
            element.style.color = "black";
        }
        element.style.backgroundColor = "";
    }
}
function setupMousetrapEvents() {
    for(let i = 1; i <= 25; i += 1) { 
        let cell_num = "" + i;
        if(i < 10) {
            cell_num = "0" + cell_num;
        }

        // convert from '12' to '1 2'
        let hotkey = cell_num.charAt(0) + " " + cell_num.charAt(1);

        Mousetrap.bind(hotkey, function() {
            $("#" + i).trigger("click");
        });
    }
}
function main() {
    setupMousetrapEvents();
    generateQRCode();
    resizeTable();
}
