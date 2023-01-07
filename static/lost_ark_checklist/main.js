function assignmentFinish(element, model, name, id) {
    $.ajax({
        type:"POST",
        url: "",
        data:{
            modelName: model,
            itemName: name,
            itemID: id,
            checked: element.checked,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
        }
    });
}