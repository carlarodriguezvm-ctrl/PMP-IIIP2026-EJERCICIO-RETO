import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

import estilos
import logica


def comando_calcular():

    texto_fecha = fecha_entry.entry.get().strip()
    
    mensaje_resultado = logica.procesar_jubilacion(texto_fecha)
    
    es_error = (
        "inválido" in mensaje_resultado.lower() or 
        "no puede ser mayor" in mensaje_resultado.lower()
    )

    if es_error:

        Messagebox.show_error(mensaje_resultado, title="Atención")
        txtResultado.config(
            text=mensaje_resultado, 
            bootstyle=estilos.BOOTSTYLE_ERROR
        )
    else:
        Messagebox.show_info(mensaje_resultado, title="Resultado")
        
        if "ya puedes pensar" in mensaje_resultado.lower() or "puedes jubilarte" in mensaje_resultado.lower():
            estilo_aplicado = estilos.BOOTSTYLE_ADVERTENCIA
        else:
            estilo_aplicado = estilos.BOOTSTYLE_EXITO

        txtResultado.config(
            text=mensaje_resultado, 
            bootstyle=estilo_aplicado
        )

ventana = ttk.Window(
    title=estilos.TEXTO_TITULO, 
    themename=estilos.TEMA_VENTANA
)
ventana.geometry(f"{estilos.VENTANA_ANCHO}x{estilos.VENTANA_ALTO}")
ventana.resizable(False, False)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)


#VISTAAAA
lblTitulo = ttk.Label(
    ventana, 
    text=estilos.TEXTO_TITULO, 
    font=estilos.FUENTE_TITULO, 
    bootstyle=estilos.BOOTSTYLE_TITULO
)
lblTitulo.grid(
    row=0, 
    column=0, 
    columnspan=2, 
    pady=estilos.PAD_TITULO_Y
)

lblMensaje = ttk.Label(
    ventana, 
    text=estilos.TEXTO_ETIQUETA_FECHA, 
    font=estilos.FUENTE_ETIQUETA
)
lblMensaje.grid(
    row=1, 
    column=0, 
    padx=estilos.PAD_X, 
    pady=estilos.PAD_Y, 
    sticky="e"
)

fecha_entry = ttk.DateEntry(
    ventana, 
    dateformat="%d/%m/%Y", 
    bootstyle=estilos.BOOTSTYLE_CALENDARIO
)
fecha_entry.grid(
    row=1, 
    column=1, 
    padx=estilos.PAD_X, 
    pady=estilos.PAD_Y, 
    sticky="w"
)

btnCalcular = ttk.Button(
    ventana, 
    text=estilos.TEXTO_BOTON_CALCULAR, 
    command=comando_calcular, 
    bootstyle=estilos.BOOTSTYLE_BOTON
)
btnCalcular.grid(
    row=2, 
    column=0, 
    columnspan=2, 
    pady=estilos.PAD_Y
)

txtResultado = ttk.Label(
    ventana, 
    text="-", 
    font=estilos.FUENTE_RESULTADO, 
    wraplength=420,
    justify="center"
)
txtResultado.grid(
    row=3, 
    column=0, 
    columnspan=2, 
    padx=estilos.PAD_X, 
    pady=estilos.PAD_Y
)

if __name__ == "__main__":
    ventana.mainloop()