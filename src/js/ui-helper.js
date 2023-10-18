let mainContainer, paperSidebar, paperSidebarVisible;
paperSidebarVisible = false;

if (document.readyState === 'complete') {
    mainContainer = document.getElementById('main-container');
    paperSidebar = document.getElementById('paper-sidebar');
} else {
    document.addEventListener('DOMContentLoaded', () => {
        mainContainer = document.getElementById('main-container');
        paperSidebar = document.getElementById('paper-sidebar');
    });
}

function setCurrentPaperSidebar(title, image_path, id) {
    // TODO: Fetch Wallpaper information (filters) and put them into sliders

    mainContainer.classList.remove('col-lg-12');
    mainContainer.classList.add('col-lg-9');

    paperSidebar.style.display = 'block';

    this.currentWallpaper = new Wallpaper(title, image_path, id);
    document.getElementById("current_wallpaper_thumbnail").src = this.currentWallpaper.image_path;
    document.getElementById("current_wallpaper_background").src = this.currentWallpaper.image_path;
    document.getElementById("current_wallpaper_title").innerHTML = this.currentWallpaper.title;
}

class Wallpaper {
    constructor(title, image_path, id) {
        this.title = title;
        this.image_path = image_path;
        this.id = id;
    }

    getCard() {
        return `<div onclick="setCurrentPaperSidebar('${this.title}', '${this.image_path}', '${this.id}');" class="col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-3">
                    <!-- card -->
                    <div class="card">
                        <div class="card__background">
                            <img src="${this.image_path}" class="card__background__image" alt="Wallpaper - ${this.title}" />
                        </div>
                        <div class="card__content">
                            <h3 class="card__content__title">${this.title}</h3>
                        </div>
                    </div>
                </div>`;
    }
}

class UiHelper {
    wallpapersElm = document.getElementById("wallpaper_list");

    constructor() {
        for (let slider of document.getElementsByClassName("slider")) {
            slider.addEventListener("input", () => {
                document.getElementById(slider.id + "-val").innerHTML = slider.value;
            });
        }
    }

    addWallpaper(title, image_path, id) {
        const wallpaper = new Wallpaper(title, image_path, id);
        this.wallpapersElm.innerHTML += wallpaper.getCard();
    }
}