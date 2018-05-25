// $.ajax({
//     method: 'GET',
//     url: '/hw_actividades/data/hw/actividad',
//     success: function(data){
//         console.log(data)
//         exportData(data)
//     },
//     error: function(error){
//     }
//   })

// function exportData (data) {
//     var wb = XLSX.utils.book_new();
//     wb.SheetNames.push("Test Sheet");
//     var ws = XLSX.utils.aoa_to_sheet(data);
//     wb.Sheets["Test Sheet"] = ws;
//     var wbout = XLSX.write(wb, {bookType: 'xlsx',  type: 'binary'});
//     saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), 'test.xlsx');
// }

// function s2ab(s) { 
//     var buf = new ArrayBuffer(s.length); //convert s to arrayBuffer
//     var view = new Uint8Array(buf);  //create uint8array as viewer
//     for (var i=0; i<s.length; i++) view[i] = s.charCodeAt(i) & 0xFF; //convert to octet
//     return buf;    
// }