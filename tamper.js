// ==UserScript==
// @name         Descifrar AES CFB
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Descifra AES CFB de 127.0.0.1:5000
// @author       Franco Palma
// @match        127.0.0.1:5000
// @grant        none
// ==/UserScript==

'use strict';

var data = document.getElementsByTagName("button")[0].id
var key = document.getElementsByTagName("form")[0].id

var inputt = document.createElement("INPUT");
inputt.setAttribute("type","text");
inputt.setAttribute("value",key);
inputt.setAttribute("id",key);
document.getElementsByTagName("form")[0].appendChild(inputt)

<script type="text/javascript" src="lib/cryptojs-aes.min.js"></script>
<script type="text/javascript" src="build/mode-cfb-b.min.js"></script>
<script type="text/javascript">
    var key = CryptoJS.enc.Hex.parse('2b7e151628aed2a6abf7158809cf4f3c');
    var iv = CryptoJS.lib.WordArray.random(128/8);
    var mode = CryptoJS.mode.CFBb;
    var padding = {
        pad: function () {},
        unpad: function () {}
    }; // NoPadding
    var segmentSize = 8; // bits; can also be 1, 2, 4, 16, 32, 64, 128 for AES

    var message = "This is some secret message";

    var encrypted = CryptoJS.AES.encrypt(message, key, {
        iv: iv,
        mode: mode,
        padding: padding,
        segmentSize: segmentSize
    });
    var recoveredPlaintext = CryptoJS.AES.decrypt(encrypted, key, {
        iv: iv,
        mode: mode,
        padding: padding,
        segmentSize: segmentSize
    });

    console.log(recoveredPlaintext.toString(CryptoJS.enc.Utf8) === message);
</script>
