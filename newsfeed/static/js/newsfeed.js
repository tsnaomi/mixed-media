(function() {
    var $GRID = $('.grid');
    var $COLLECTION = $('.collection');
    var $POST = $('.post');

    initMasonry();
    populateNewsfeed();
    detectHashChange();

    function populateNewsfeed() {
        // populate the newsfeed with the relevant posts
        var theCollection = window.location.hash.slice(1);
        transitionCollection(theCollection);
    }

    function detectHashChange() {
        // populate the newsfeed on hash change
        $(window).on('hashchange', function() {
            populateNewsfeed();
        });        
    }

    function transitionCollection(theCollection) {
        // hide all posts
        $POST.css('display', 'none');

        // if theCollection is not null, display a specific collection
        if (theCollection) {
            // hide all posts
            $POST.css('display', 'none');
                    
            // unhide posts in theCollection
            $('.post#' + theCollection).css('display', 'block');

        // if theCollection is null, display all collections
        } else {
            // display all posts
            $POST.css('display', 'block');

            theCollection = 'all';
        }

        // trigger masonry layout update
        $GRID.masonry();

        // remove existing highlights
        $COLLECTION.removeClass('active-collection');

        // highlight theCollection (or 'all')
        $('.collection#' + theCollection).addClass('active-collection');
    }

    function initMasonry() {
        // initialize masonry
        $GRID.masonry({
            itemSelector: '.grid-item',
            columnWidth: 400,
        });
    }
})();
