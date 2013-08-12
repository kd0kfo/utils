// This takes an object and shows components.
//
function show_stuff(thing){
        var retval = "";
        $.each(thing, function(key, val){
                retval += key + " => " + val + "\n";
        });
        return retval;
}

