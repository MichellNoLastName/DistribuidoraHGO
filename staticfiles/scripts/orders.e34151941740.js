'use strict'

/*document.addEventListener('keydown',(e) =>{
    if(e.key ==='Enter'){
        e.preventDefault()
    }
})*/

const entidadFederativa = document.querySelector('[name="EntidadFederativaOrdenCliente"]')
const localidad = document.querySelector('[name="LocalidadOrdenCliente"]')
const colonia = document.querySelector('[name="ColoniaOrdenCliente"]')
const cp = document.querySelector('[name="CodigoPostalOrdenCliente"]')

function invocarLocalidades(){
    if(entidadFederativa.value){
        localidad.disabled = false
        $('[name="LocalidadOrdenCliente"]').html('<option value="">--- Seleccione una opción---</option>')
        $.ajax({
            url: "load_towns/",
            data:{
                'idEntidadFederativa': entidadFederativa.value
            },
            success: function(data){
                $.each(data,(key,value)=>{
                    $('[name="LocalidadOrdenCliente"]').append('<option value="' + value.IdLocalidad + '">' + value.NombreLocalidad + '</option>')
                })
            }
        })
    } else{
        cp.value = ''
        cp.disabled = false
        localidad.value = ''
        localidad.disabled = true
    }
}

function invocarColonias(){
    if(localidad.value){
        colonia.disabled = false
        $('[name="ColoniaOrdenCliente"]').html('<option value="">--- Seleccione una opción---</option>')
        $.ajax({
            url:"load_streets/",
            data:{
                'idEntidadFederativa': entidadFederativa.value,
                'idLocalidad': localidad.value
            },
            success: function(data){
                $.each(data,(key,value)=>{
                    $('[name="ColoniaOrdenCliente"]').append('<option value="' + value.IdColonia + '">' + value.NombreColonia + '</option>')
                })
            }
        })
    } else{
        colonia.value = ''
        colonia.disabled = true
    }
}
document.addEventListener("DOMContentLoaded",()=>{

    entidadFederativa.addEventListener('change',invocarLocalidades)

    localidad.addEventListener('change',invocarColonias)

    cp.addEventListener('keydown',(e)=>{
        if(e.key === 'Enter'){
            if(cp.value.length == 5){
                $.ajax({
                    url:"load_location/",
                    data:{
                        'idCodigoPostal': cp.value
                    },
                    success: function(data){
                        if(data.length > 0){
                            entidadFederativa.value = data[data.length - 2].IdEntidadFederativa
                            invocarLocalidades()
                            setTimeout(()=>{
                                localidad.value = data[data.length - 1].IdLocalidad
                            },500)
                            setTimeout(invocarColonias,500)
                        }else{
                            Swal.fire({
                                title: "Código Postal",
                                text: "El código postal ingresado es invalido, intente de nuevo.",
                                icon: "error"
                              });
                        }
                    }
                })
            } else{
                Swal.fire({
                    title: "Código Postal",
                    text: "El código postal ingresado es invalido, intente de nuevo.",
                    icon: "error"
                  });
            }
        }
    })


})
