const filter = document.getElementById('form_navbarSearch')
const filterMovil = document.getElementById('inputSearchMovil')

filter.addEventListener('input',(e)=>{
    getData(filter.value)
})

filterMovil.addEventListener('input',(e)=>{
    getData(filterMovil.value)
})

async function getData(pFilter) {
    if(body.offsetWidth > 1023){
        const result = document.getElementById('result')
        if(pFilter.length > 0){
            const api_url = 'http://127.0.0.1:8000/load_products/' + pFilter
            const res = await fetch(api_url)
            const data = await res.json();

            result.innerHTML = ''

            data.forEach(product => {
                const li = document.createElement('li')
                const url_image = '/media/' + product.ImagenArticulo
                //const productUrl = "{% url 'store:product_detail' IdArticulo_id="+product.IdArticulo+" slug="+product.SlugArticulo + " %}";
                const productUrl = "/store/"+product.IdArticulo + "/" + product.SlugArticulo + "/"

                li.innerHTML = `
                    <a href="${productUrl}" class="text-decoration-none">
                        <img src="${url_image}" alt="${product.NombreImagenArticulo}">
                        <div class="product-info">
                            <h5>${product.NombreArticulo}</h5>
                            <p>${product.DescripcionArticulo}</p>
                        </div>
                    </a>
                `

                result.appendChild(li)
            });
        }else{
            result.innerHTML = ''
        }
    }else{
        const result = document.getElementById('result-movil')
        if(pFilter.length > 0){
            const api_url = 'http://127.0.0.1:8000/load_products/' + pFilter
            const res = await fetch(api_url)
            const data = await res.json();

            result.innerHTML = ''

            data.forEach(product => {
                const li = document.createElement('li')
                const url_image = '/media/' + product.ImagenArticulo

                li.innerHTML = `
                    <img src="${url_image}" alt="${product.NombreImagenArticulo}">
                    <div class="product-info">
                        <h5>${product.NombreArticulo}</h5>
                        <p>${product.DescripcionArticulo}</p>
                    </div>
                `

                result.appendChild(li)
            });
        }else{
            result.innerHTML = ''
        }
    }
}
