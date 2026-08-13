function toggle(expandable) {
    var expParent = expandable.parentNode;
    var img = expParent.querySelector('img');
    if (img !== null) {
        if (img.addEventListener) {
            img.addEventListener('click', function(event) {
                event.stopPropagation();
            });
        } else {
            img.attachEvent('onclick', function(event) {
                event.cancelBubble = false;
            });
        }
    }
    var target = expParent.querySelector('.content');
    if (target !== null) {
        if (target.addEventListener) {
            target.addEventListener('click', function(event) {
                event.stopPropagation();
            });
        } else {
            target.attachEvent('onclick', function(event) {
                event.cancelBubble = false;
            });
        }
    }
    var arrow = expParent.querySelector('span.arrow');
    if (arrow !== null) {
        if (target.style.display == 'block') {
            target.style.display = 'none';
            arrow.innerHTML = '\u25BA';
        } else {
            target.style.display = 'block';
            arrow.innerHTML = '\u25BC';
        }
    }
}
