function fetchImageTitles() {
    return fetch('MemeTitlez.txt')
        .then(response => response.text())
        .then(text => {
            const lines = text.split('\n'); //each image and cooresponding comment are on each line in the MemeTitlez.txt file
            const images = [];

            //split the image file names from the comments in the text file in the images array
            for (let i = 0; i < lines.length; i++) { 
                const parts = lines[i].split('~/'); 
                images.push({
                    fileName: parts[0].trim(), 
                    title: parts[1] ? parts[1].trim() : ''
                });
            }
            images.pop(); // delete the last item of the image array, which is blank

            return images;
        });
}

function setupSlideshow() {
    const folderPath = './memez/'; 
    const slideshowImg = document.getElementById('slide');
    const slideshowTitle = document.getElementById('title');
    let currentIndex = 0;

    fetchImageTitles().then(imageList => {
        //using the fetchImageTitles function, call the folder path, image name and image title and display them using .getElementById
        function showSlide(index) {
            slideshowImg.src = `${folderPath}${imageList[index].fileName}`;
            slideshowTitle.textContent = imageList[index].title;
        }

        showSlide(currentIndex);

        setInterval(() => {
            currentIndex = (currentIndex + 1) % imageList.length;
            showSlide(currentIndex);
        }, 30000); // timing of the slideshow is adjusted here, 30000 is 30 seconds
    });
}

setupSlideshow();