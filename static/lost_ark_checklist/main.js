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

var now = new Date();
if (now.getHours() >= 2){
    // If page is loaded after 2AM
    var reset_time = new Date(
        now.getFullYear(),
        now.getMonth(),
        now.getDate() + 1, // the next day, ...
        2, 0, 0 // ...at 02:00:00 hours
    );

} else {
    // If page is loaded between midnight and 2AM
    var reset_time = new Date(
        now.getFullYear(),
        now.getMonth(),
        now.getDate(), // the same day, ...
        2, 0, 0 // ...at 02:00:00 hours
    );
}

var msTillMidnight = reset_time.getTime() - now.getTime();
setTimeout(window.location.reload.bind(window.location), msTillMidnight);