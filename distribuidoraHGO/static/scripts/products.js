
//Actualizar urls en caso de cambio de servidor de imagenes,etc
const host_url='https://distribuidora-hgo-17835e2f8f84.herokuapp.com/'
const image_url='https://res.cloudinary.com/dohwjsbvr/image/upload/v1/'

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
            const api_url = host_url + 'load_products/' + pFilter
            const res = await fetch(api_url)
            const data = await res.json();

            result.innerHTML = ''

            data.forEach(product => {
                const li = document.createElement('li')
                const url_image = image_url + product.ImagenArticulo
                console.log(url_image)
                //const productUrl = "{% url 'store:product_detail' IdArticulo_id="+product.IdArticulo+" slug="+product.SlugArticulo + " %}";
                const productUrl = "/store/product/"+product.IdArticulo + "/" + product.SlugArticulo + "/"

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
            const api_url = host_url + 'load_products/' + pFilter
            const res = await fetch(api_url)
            const data = await res.json();

            result.innerHTML = ''

            data.forEach(product => {
                const li = document.createElement('li')
                const url_image = image_url + product.ImagenArticulo

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
