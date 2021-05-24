
  function searchrecords(){
    var entry, table,tr,td,i,txtdata,filter;
    entry= document.getElementById("search_state");
    filter=entry.value;
    table=document.getElementById("table1");
    tr=table.getElementsByTagName("tr");

    
    for(i=0;i<tr.length;i++){
        td=tr[i].getElementsByTagName("td")[7]
        if(td){
                txtdata=td.innerText;
                if(txtdata==filter){
                    tr[i].style.display='';
                    continue;
                }
               else{
                    tr[i].style.display="none";
               }
        }
    }
}
 

function chartview(){

    table=document.getElementById("table1");
    tr=table.getElementsByTagName("tr");
    var dict ={}
    
    for(i=0;i<tr.length;i++){
        td=tr[i].getElementsByTagName("td")[7]

        if(td){
            txtdata=td.innerText;
            if(txtdata in key){
                dict[txtdata]+=1;
            }
            else{
                dict[txtdata]=1;
            }
        }

    }

}


    function showPage(page) {

        // Hide all of the divs:
        document.querySelectorAll('form').forEach(form => {
            form.style.display = 'none';
        });

        // Show the div provided in the argument
        document.querySelector(`#${page}`).style.display = 'block';
    }

    // Wait for page to loaded:
    document.addEventListener('DOMContentLoaded', function() {
       
        // Select all buttons
        document.querySelectorAll('a').forEach(a => {

            // When a button is clicked, switch to that page
            a.onclick = function() {
                showPage(this.dataset.page);
            }
        })
        document.querySelector('#search_state_button').onclick=function(){
            searchrecords();
        }
        
    });