var c489ca6a253715bf5be2dd0a = {
    toggle: function (expandable) {
        var expParent = expandable.parentNode;
        var img = expParent.querySelector('img');
        if (img !== null) {
            if (img.addEventListener) {
                img.addEventListener('click', function (event) {
                    event.stopPropagation();
                });
            } else {
                img.attachEvent('onclick', function (event) {
                    event.cancelBubble = false;
                });
            }
        }
        var target = expParent.querySelector('.content');
        if (target !== null) {
            if (target.addEventListener) {
                target.addEventListener('click', function (event) {
                    event.stopPropagation();
                });
            } else {
                target.attachEvent('onclick', function (event) {
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
    },
    showAtLink: function (ele) {
        if (ele.nextSibling.style.display == 'block') {
            ele.nextSibling.style.display = 'none';
        } else {
            ele.nextSibling.style.display = 'block';
        }
    },
    toggleImg: function (ele) {
        if (ele.style.maxHeight == 'none') {
            ele.style.maxHeight = '4em';
        } else {
            ele.style.maxHeight = 'none';
        }
    }
}