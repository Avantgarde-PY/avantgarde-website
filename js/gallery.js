function fetchImageData() {
    fetch('/portfolio.json')
      .then((response) => response.json())
      .then((data) => {
        const container = document.getElementById("portfolio_wrapper");
  
        if (!container) {
          console.error("Container element not found!");
          return;
        }
  
        container.innerHTML = "";
  
        data.forEach((itemData, index) => {
          const folderPathParts = itemData.src.split('/');
          const folderName = folderPathParts[2]; // Extract folder name
          const imgPath = itemData.src;
  
          if (!folderName) {
            console.error("Folder name is empty or undefined");
            return;
          }
  
          const portfolioItem = document.createElement("figure");
          portfolioItem.classList.add("portfolio-item", "one-four", folderName, "isotope-item", "effect-oscar");
          portfolioItem.style.cssText = "position: absolute; left: 0px; top: 0px; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1); width: 337px; opacity: 1;";
  
          portfolioItem.innerHTML = `
            <div class="portfolio_img">
              <img src="${imgPath}" alt="Portfolio ${index + 1}">
            </div>
            <figcaption>
              <div></div>
            </figcaption>
          `;
  
          container.appendChild(portfolioItem);
        });
      })
      .catch((error) => console.error("Error fetching data:", error));
  }
  
  // Initial fetch and update
  fetchImageData();
  