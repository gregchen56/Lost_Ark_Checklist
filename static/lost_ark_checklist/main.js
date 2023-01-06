function assignmentFinish(element, name, id) {
    $.ajax({
        type:'POST',
        url: "add",
        data:{
            checked: element.checked,
            itemName: name,
            itemID: id,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
        }
    });
}