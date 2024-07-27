import os

# Function to generate HTML for each image
def generate_html_for_images(base_dir, folder_names):
    html_content = ""

    for folder in folder_names:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img_src = os.path.join(folder, file_name)
                html_content += f'''
<!-- Portfolio Item -->
<figure style="position: absolute; left: 0px; top: 0px; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1); width: 337px; opacity: 1;" class="portfolio-item one-four {folder} isotope-item effect-oscar">
  <div class="portfolio_img"> 
      <img src="img/{img_src}" alt="Portfolio"> 
  </div> 
  <figcaption>
      <div></div>
  </figcaption>
</figure>
<!--/Portfolio Item -->
'''

    return html_content

# Define your base directory and folder names
base_directory = 'img'
folder_names = ['bau', 'dach', 'elektro', 'garage', 'pool', 'sanitar']

# Generate HTML
html_code = generate_html_for_images(base_directory, folder_names)

# Save the HTML to a file
with open('js/portfolio.html', 'w') as file:
    file.write(html_code)

print("HTML code has been generated and saved to 'portfolio.html'.")
