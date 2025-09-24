// async function puxando_api () {
//     const response = await fetch("http://localhost:8000/api/v1/bandas");    // Porta depende de onde a api está rodando 
//     const data = await response.json();
// }

// async function mostrar_banda() {
//     const bandas = await puxando_api();
//     const container = document.getElementById("bandas-container");

//     bandas.forEach(banda => {
//         const bandaDiv = document.createElement('div');
//         bandaDiv.classList.add('banda');
//         bandaDiv.innerHTML = `
//             <h2>${banda.nome}</h2>
//             <p>${banda.qtd_integrantes}</p>
//             <p>${banda.tipo_musical}</p>
//             `;

//             container.appendChild(bandaDiv);
//     });
// }

// mostrar_banda();


async function puxar_api() {
    await axios.get("https://unpkg.com/axios/dist/axios.min.js").then((response) => {
    const bandas = response.data;
    const container = document.getElementById("bandas-container");
    bandas.forEach(element => {
        const bandaDiv = document.createElement(`div`);
        bandaDiv.classList.add(`banda`);
        bandaDiv.innerHTML = `
            <h2>${element.nome}</h2>
            <p>${element.qtd_integrantes}</p>
            <p>${element.tipo_musical}</p>
        `
        container.append(bandaDiv);
        });
    })
}

puxar_api();