// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3.0

window.onload = function() {
   settingsPanel = document.getElementById("settingspanel");
   settingsPanel.innerHTML='<div id="settingspart">BG <input type="color" value="#ffffff" oninput="document.body.style.backgroundColor = this.value;"onchange="document.body.style.backgroundColor=this.value;" />' +
   ' FONT <select onchange="document.body.style.fontFamily = this.value;">' + 
   '<option value="serif" selected="selected">Default Serif</option>' +
   '<option value="sans-serif">Default Sans</option>' +
   '<option value="monospace">Default Monospace</option>' +   
   '<option value="\'Comic Sans MS\', cursive">Comic Sans</option>' +
   '<option value="\'Courier New\', \'Courier Std\', \'Courier 10 Pitch\', Courier, monospace, Monospace">Courier</option>' +
   '<option value="\'Adobe Garamond Pro\', \'Garamond Premier Pro\', Garamond, \'EB Garamond\', \'Cormorant Garamond\', \'ITC Garamond Std\', \'Garamond 3 LT Std\', \'Stempel Garamond LT Std\', \'Simoncini Garamond Std\', \'URW Garamond\'">Garamond</option>' +
   '<option value="Georgia, serif, Serif">Georgia</option>' +
   '<option value="FreeSans, \'TeX Gyre Heros\', \'Nimbus Sans L\', \'Helvetica LT Std\', \'Helvetica Neue LT Pro\', \'Helvetica Neue LT Std\', \'Helvetica Neue\', Helvetica, Arial, Arimo, sans-serif, Sans">Helvetica / Arial</option>' +
   '<option value="\'Impact LT Std\',Impact, Oswald, Charcoal, sans-serif">Impact</option>' +
   '<option value="\'Lucida Console\', Monaco, \'Lucida Sans Typewriter Std\', monospace, Monospace">Lucida Console / Monaco</option>' +
   '<option value="\'Lucida Sans Unicode\', \'Lucida Sans Std\', \'Lucida Grande\'">Lucida Sans</option>  ' +
   '<option value="\'Palatino Linotype\', \'Palatino LT Std\', \'Book Antiqua\', Palatino, \'URW Palladio L\', \'TeX Gyre Pagella\', serif, Serif">Palatino</option>' +
   '<option value="Tahoma, Geneva, sans-serif, Sans">Tahoma / Geneva</option>' +
   '<option value="\'Times New Roman\', Times, \'Times New Roman MT Std\', \'Times Ten LT Std\', \'Times LT Std\', \'TeX Gyre Termes\', Tinos, serif, Serif">Times</option>' +
   '<option value="\'Trebuchet MS\', \'Gill Sans Std\', \'Gill Sans MT Pro\', \'Gillius ADF\', \'Frutiger LT Std\', \'Grotesque MT Std\', sans-serif, Sans">Trebuchet MS</option>' +
   '<option value="Verdana, \'Verana Sans\', Geneva, sans-serif, Sans">Verdana / Geneva</option>' +
   '</select>' +
   '<input type="number" value="16" onchange="document.body.style.fontSize=this.value + \'px\';" />' +
   '<input type="color" value="#000000" oninput="document.body.style.color = this.value;" onchange="document.body.style.color = this.value; "/>' +
   ' SPACING ' + '<input type="number" step=0.2 value=1.2 onchange="document.getElementById(\'bodytext\').style.lineHeight = this.value; "/>' +
   ' WIDTH ' + '<input type="number" step=4 value=40 onchange="document.getElementById(\'bodytext\').style.maxWidth = this.value + \'em\'; "/>' +
      ' ALIGN ' + '<select onchange="document.getElementById(\'bodytext\').style.textAlign = this.value;">' +
      '<option value="justify" selected="selected">justified</option>' +
      '<option value="left" >left</option>' +
      '<option value="center" >center</option>' +
      '<option value="right" >right</option></select>' +
      ' PAGE #S&nbsp; <input type="checkbox" id="pagenumcb" onchange="togglePageNums();" />' +
      '&nbsp; <button type="button" onclick="resetSettings();">reset</button>' + 
      '<a href="#table_of_contents" style="vertical-align: middle; color: blue; float: right;text-decoration: underline; border: none; font-size: 150%; margin-left: 1em; margin-right: 1em; display: inline-block;">TOC</a>' +
      '<br style="clear: both;"></div> <div id="menu_lines" class="menu_btn"></div>';
   if (document.documentElement.clientWidth >= 860) {
      document.getElementById("pagenumcb").checked = true;
      togglePageNums();
   }
   
}

function resetSettings() {
   var sp = document.getElementById("settingspanel");
   var sels = sp.getElementsByTagName("select");
   var inps = sp.getElementsByTagName("input");
   document.body.style.backgroundColor = '#ffffff';
   inps[0].value = '#ffffff';
   document.body.style.fontFamily = 'serif';
   sels[0].getElementsByTagName("option")[0].selected="selected";
   document.body.style.fontSize = '16px';
   inps[1].value = 16;
   document.body.style.color = "#000000";
   inps[2].value = "#000000";
   document.getElementById("bodytext").style.lineHeight = "1.2";
   inps[3].value = 1.2;
   document.getElementById("bodytext").style.maxWidth = "40em";
   inps[4].value = 40;
   document.getElementById("bodytext").style.textAlign = "justify";
   sels[1].getElementsByTagName("option")[0].selected = "selected";
   if (document.documentElement.clientWidth >= 860) {
      inps[5].checked = true;
   } else {
      inps[5].checked = false;
   }
   togglePageNums();
}

function togglePageNums() {
   if (document.getElementById("pagenumcb").checked) {
      var searchas = document.body.getElementsByTagName("a");
      for (var i=0; i<searchas.length; i++) {
         var a= searchas[i];
         if ((a.id != 'undefined') && (a.id.substring(0,4) == "page")) {
            a.innerHTML = "&nbsp;";
            a.className = "pagemarker";
            var m = document.createElement("span");
            m.innerHTML = a.id.substring(4);
            m.className = "sidepagenumber";
            a.parentNode.insertBefore(m, a.nextSibling);
         }
      }
   } else {
      var searchas = document.body.getElementsByTagName("a");
      for (var i=0; i<searchas.length; i++) {
         var a= searchas[i];
         if ((a.id != 'undefined') && (a.id.substring(0,4) == "page")) {
               a.innerHTML = "";
               a.className = "";
            if (a.nextSibling.className == "sidepagenumber") {
               a.parentNode.removeChild(a.nextSibling);
            }
         }
         
      }
   }
}

// @license-end