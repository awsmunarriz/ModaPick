class PosteoController {
  constructor() {
    this.listaPosteos = [];
    this.contenedor_posteos = document.getElementById("contenedor_posteos");
    this.contenedor_info = document.getElementById("contenedor_info");
    this.info = [];
    this.btnAnterior = document.getElementById("btnAnterior");
    this.btnSiguiente = document.getElementById("btnSiguiente");
    this.itemsPorPagina = 4;
    this.paginaActual = 0;
    this.userAuthenticated = false;

    this.btnAnterior.addEventListener("click", () =>
      this.cargarPagina(this.paginaActual - 1)
    );
    this.btnSiguiente.addEventListener("click", () =>
      this.cargarPagina(this.paginaActual + 1)
    );
  }

  cargar_y_mostrar(data) {
    this.listaPosteos = data.posteos;
    this.userAuthenticated = data.authenticated;
    this.cargarPagina(0);
  }

  cargarPagina(numeroPagina) {
    const inicio = numeroPagina * this.itemsPorPagina;
    const fin = inicio + this.itemsPorPagina;
    const posteosPagina = this.listaPosteos.slice(inicio, fin);

    this.paginaActual = numeroPagina;
    this.mostrarEnDOM(posteosPagina);
    this.actualizarBotones();
  }

  mostrarEnDOM(posteos) {
    this.contenedor_posteos.innerHTML = "";
    posteos.forEach((posteo) => {
      this.contenedor_posteos.innerHTML += `
          <div class="card text-center bg-dark mb-2 tarjeta">
            <img class="card-img-top" src="${posteo.imagen}" alt="img">
            <div class="card-body">
              <h5 class="card-title">#${posteo.id}</h5>
              <div>
                ${
                  this.userAuthenticated
                    ? `<button type="button" id="post-${posteo.id}" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Info</button>`
                    : ""
                }
              </div>
            </div>
          </div>
        `;
    });
    this.darEventoClickAPosteos();
  }

  darEventoClickAPosteos() {
    this.listaPosteos.forEach((posteo) => {
      const btnVotar = document.getElementById(`post-${posteo.id}`);
      if (btnVotar) {
        btnVotar.addEventListener("click", () => {
          this.mostrarInfoEnDOM(posteo);
        });
      }
    });
  }

  mostrarInfoEnDOM(posteo) {
    this.contenedor_info.innerHTML = `
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel" style="color:SlateGrey;">${posteo.title}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="${posteo.imagen}" class="img-fluid rounded-start" alt="${posteo.title}">
          <h3 style="color:SlateGrey;">${posteo.description}</h3>
        </div>
        <div class="modal-footer">
          <button type="button" id="like-${posteo.id}" class="css-button css-button-3d--green">
            <i class="fa-regular fa-thumbs-up"></i> Like
          </button>
          <button type="button" id="dislike-${posteo.id}" class="css-button css-button-3d--red">
            <i class="fa-regular fa-thumbs-down"></i> Dislike
          </button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      `;
    this.darEventoClickALike(posteo);
    this.darEventoClickADislike(posteo);
  }

  darEventoClickALike(posteo) {
    const btnAgregarFav = document.getElementById(`like-${posteo.id}`);
    if (btnAgregarFav) {
      btnAgregarFav.addEventListener("click", () => {
        if (!this.userAuthenticated) {
          alert("Debes iniciar sesión para agregar a favoritos.");
          return;
        }
        fetch("/dar_like/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"), // Obtener CSRF token
          },
          body: JSON.stringify({ posteo_id: posteo.id }),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(
                "Network response was not ok " + response.statusText
              );
            }
            return response.json();
          })
          .then((data) => {
            alert("Like agregado!");
          })
          .catch((error) => {
            console.error(
              "There was a problem with the fetch operation:",
              error
            );
          });
      });
    }
  }

  darEventoClickADislike(posteo) {
    const btnAgregarFav = document.getElementById(`dislike-${posteo.id}`);
    if (btnAgregarFav) {
      btnAgregarFav.addEventListener("click", () => {
        if (!this.userAuthenticated) {
          alert("Debes iniciar sesión para agregar a favoritos.");
          return;
        }
        fetch("/dar_dislike/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"), // Obtener CSRF token
          },
          body: JSON.stringify({ posteo_id: posteo.id }),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(
                "Network response was not ok " + response.statusText
              );
            }
            return response.json();
          })
          .then((data) => {
            alert("Disike agregado!");
          })
          .catch((error) => {
            console.error(
              "There was a problem with the fetch operation:",
              error
            );
          });
      });
    }
  }

  actualizarBotones() {
    this.btnAnterior.disabled = this.paginaActual === 0;
    this.btnSiguiente.disabled =
      (this.paginaActual + 1) * this.itemsPorPagina >= this.listaPosteos.length;
  }
}

// Instancia la clase PosteoController
const controladorPosteos = new PosteoController();

document.addEventListener("DOMContentLoaded", function () {
  fetch("/posteos/")
    .then((response) => response.json())
    .then((data) => {
      controladorPosteos.cargar_y_mostrar(data);
    })
    .catch((error) => console.error("Error:", error));
});

// Función para obtener el token CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
