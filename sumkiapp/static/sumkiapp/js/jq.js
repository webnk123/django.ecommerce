const fetchPage = async (url) => {
  let headers = new Headers()
  headers.append("X-Requested-With", "XMLHttpRequest")
  return fetch(url, { headers })
}

const appendElements = async (scrollElement, counter, baseUrl) => {
  let url = `${baseUrl}?page=${counter + 1}`

  let req = await fetchPage(url);

  if (req.ok) {
    let body = await req.text();
    // Be careful of XSS if you do this. Make sure
    // you remove all possible sources of XSS.
    scrollElement.innerHTML += body;
  } else {
    end = true;
  }
}


const attachInfiniteScroll = (sentinel, scrollElement, baseUrl) => {
  let counter = 1;
  let end = false;

  let observer = new IntersectionObserver(async (entries) => {
    let bottomEntry = entries[0];

    if (!end && bottomEntry.intersectionRatio > 0) {
      await appendElements(scrollElement, counter, baseUrl);
      counter += 1;
    }
  })


  observer.observe(sentinel);
};



$('#carouselExampleIndicators').on('touchstart', function(event){
    const xClick = event.originalEvent.touches[0].pageX;
    $(this).one('touchmove', function(event){
        const xMove = event.originalEvent.touches[0].pageX;
        const sensitivityInPx = 5;

        if( Math.floor(xClick - xMove) > sensitivityInPx ){
            $(this).carousel('.carousel-control-prev');
        }
        else if( Math.floor(xClick - xMove) < -sensitivityInPx ){
            $(this).carousel('next');
        }
    });
    $(this).on('touchend', function(){
        $(this).off('touchmove');
    });
});


