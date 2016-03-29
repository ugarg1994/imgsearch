
$(document).ready(function(){
    document.getElementById("search_text").focus();
	$('#img_srch').click(function(event){
        var srchtxt = document.getElementById("search_text").value;
        var csrftoken = document.getElementById("csrfmiddlewaretoken").value;
        var srch_data = {"csrfmiddlewaretoken":csrftoken,"srchtxt": srchtxt};
        if(srchtxt == ""){
            alert("Enter Characters to search");
        }
        
        else{
            //console.log(csrftoken);
            $.ajax({
                url: "/home/",
                data: srch_data,
                type: 'POST',
                success: function(result){
                    html_content = "";
                    console.log(result);
                    if(result.length>0){
                        for (var i = result.length - 1; i >= 0; i--) {
                        //result[i]
                            html_content=html_content + '<div class="col-lg-3 col-md-4 col-xs-6 thumb"><a class="thumbnail" href="'+result[i].url+'"><img class="img-responsive" src="'+result[i].url+'" alt="'+result[i].name+'"></a></div>'
                        };
                        console.log(html_content);
                         $("#image-container").html(html_content);
                    }
                    else{
                        $("#image-container").html("<h1>Sorry!!! No Match Found.</h1>");
                    }
                    //console.log(result);
    			//get_document();
                },
                error: function(xhr, textStatus, errorThrown){
                    console.log(xhr.status);
                    html_content = "";
                    $("#image-container").html("<h1>Opps. Error Occured</h1>");
                }
            });
        }
	})
});
