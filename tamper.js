// ==UserScript==
// @name         Descifrar AES CFB
// @namespace    https://raw.githubusercontent.com/Francoco97/Tarea-3-Cripto/master/tamper.js
// @version      0.1
// @description  Descifra AES CFB de 127.0.0.1:5000
// @author       Franco Palma
// @match        127.0.0.1:5000
// @grant        none
// @require https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js
// @require https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/core-min.js
// @require https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/enc-base64.js
// @require https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

(function() {
    'use strict';

    var data = "w6kAegGNturTKr2U0pmiBnF5"
    var key = document.getElementsByTagName("form")[0].id
    var iv = document.getElementsByTagName("button")[0].name
    /*console.log(data)
    console.log(key)
    console.log(iv)*/
    key = CryptoJS.SHA256(key);
    //iv = CryptoJS.enc.Utf8.parse(iv);
    var decrypted = CryptoJS.AES.decrypt(data, key,{iv:iv},CryptoJS.mode.CFB);
    //var decrypted = CryptoJS.AES.decrypt(data, key, {iv :iv,  mode: CryptoJS.mode.CFB, padding: CryptoJS.pad.AnsiX923});

    var inputt = document.createElement("INPUT");
    inputt.setAttribute("type","text");
    inputt.setAttribute("value",decrypted);
    inputt.setAttribute("id",decrypted);
    document.getElementsByTagName("form")[0].appendChild(inputt)
    console.log(toString(decrypted))

})();//me amanezvo
