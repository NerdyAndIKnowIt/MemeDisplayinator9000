async function ReadMemeFile() {
    try {
        // Fetch the text file
        const response = await fetch('MemeTitlez.txt');
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        // Read the content as text
        const text = await response.text();

        // Split the text into lines
        const lines = text.split(/\r?\n/); // Handles both Windows (\r\n) and Unix (\n) line endings

        // Process each line
        lines.forEach((line, index) => {
            console.log(`Line ${index + 1}: ${line}`);
        });

        // Example: Store each line as variables
        const [line1, image1, line2, image2, line3, image3] = lines;

    } 
    catch (error) {
        console.error("Error reading the text file:", error);
    }

    showSlides();
}

let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }

    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1
    } 

    slides[slideIndex-1].style.display = "block";  
    
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}