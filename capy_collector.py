
import flet as ft
from pathlib import Path


# ==========================================
# CAPY COLLECTOR - JUEGO PRINCIPAL
# Python + Flet 1.0
# ==========================================

def main(page: ft.Page):

    # 1. CONFIGURACION
    page.title = "Capy Collector 🍓"
    page.bgcolor = "#FCEAF1"
    page.padding = 15
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1050
    page.window.height = 780
    page.window.min_width = 750
    page.window.min_height = 600

    # COLORES
    ROSA = "#F4A6C1"
    ROSA_CLARO = "#FCE4EC"
    CREMA = "#FFF5E8"
    MARRON = "#80513E"
    VERDE = "#B8D6A0"
    BLANCO = "#FFFFFF"

    # CARPETA DE IMAGENES
    CARPETA = Path(__file__).parent / "assets"

    # 2. VARIABLES DEL JUEGO
    fresas = 0
    puntos = 0
    felicidad = 0
    ropa_actual = "normal"
    nombre_capy = "Capy"

    ropas = {
        "normal": ("Normal", "🐹", "capy_normal.png"),
        "rosa": ("Lazo Rosa", "🎀", "capy_rosa.png"),
        "fresa": ("Gorro Fresa", "🍓", "capy_fresa.png"),
        "azul": ("Suéter Azul", "💙", "capy_azul.png")
    }

    # 3. FUNCIONES DE DISEÑO

    def titulo(texto, tamano=25):
        return ft.Text(
            texto,
            size=tamano,
            weight=ft.FontWeight.BOLD,
            color=MARRON
        )

    def tarjeta(contenido, color=BLANCO, ancho=None):
        return ft.Container(
            content=contenido,
            bgcolor=color,
            padding=20,
            border_radius=22,
            width=ancho,
            border=ft.Border.all(2, "#F5C4D5")
        )

    def imagen_capy(tipo=None, tamano=150):

        if tipo is None:
            tipo = ropa_actual

        archivo = ropas[tipo][2]
        ruta = CARPETA / archivo

        if ruta.exists():
            return ft.Image(
                src=archivo,
                width=tamano,
                height=tamano,
                fit=ft.BoxFit.CONTAIN
            )

        return ft.Text(
            ropas[tipo][1],
            size=tamano * 0.65
        )

    def boton(texto, accion, color=ROSA, ancho=190):
        return ft.Button(
            content=texto,
            width=ancho,
            height=55,
            on_click=accion,
            style=ft.ButtonStyle(
                bgcolor=color,
                color=MARRON,
                shape=ft.RoundedRectangleBorder(radius=18),
                elevation=2
            )
        )

    def actualizar():
        page.update()

    # 4. FUNCIONES DEL JUEGO

    def recolectar(e):
        nonlocal fresas, puntos

        fresas += 1
        puntos += 1

        mensaje.value = "¡Encontraste una fresita! 🍓"
        mostrar_inicio()

    def alimentar(e):
        nonlocal fresas, puntos, felicidad

        if fresas > 0:
            if felicidad < 100:
                fresas -= 1
                puntos += 2
                felicidad = min(100, felicidad + 10)
                mensaje.value = (
                    f"¡{nombre_capy} está muy feliz! 💗"
                )
            else:
                mensaje.value = "¡Capy ya está muy feliz! 🥰"

        else:
            mensaje.value = "¡Primero recoge algunas fresas! 🍓"

        mostrar_inicio()




    def seleccionar_ropa(tipo):
        nonlocal ropa_actual

        ropa_actual = tipo
        mensaje.value = (
            f"¡{nombre_capy} ahora lleva {ropas[tipo][0]}! 💗"
        )

        mostrar_vestuario()

    def reiniciar(e):
        nonlocal fresas, puntos, felicidad, ropa_actual

        fresas = 0
        puntos = 0
        felicidad = 0
        ropa_actual = "normal"

        mensaje.value = "¡Empecemos una nueva aventura! 🐹"
        mostrar_inicio()

    def cambiar_nombre(e):
        nonlocal nombre_capy

        nuevo = campo_nombre.value.strip()

        if nuevo:
            nombre_capy = nuevo
            mensaje.value = f"¡Hola! Soy {nombre_capy} 💗"
        else:
            mensaje.value = "Escribe un nombre para Capy."

        actualizar()

    # MENSAJE DEL JUEGO
    mensaje = ft.Text(
        "¡Hola! Soy Capy. ¡Vamos a jugar! 💗",
        size=16,
        color=MARRON,
        text_align=ft.TextAlign.CENTER
    )

    # CAMPO DE NOMBRE
    campo_nombre = ft.TextField(
        label="Nombre de tu capibara",
        value="Capy",
        width=280,
        border_radius=15,
        bgcolor=CREMA,
        on_submit=cambiar_nombre
    )

    boton_nombre = ft.Button(
        content="Guardar nombre",
        on_click=cambiar_nombre,
        bgcolor=ROSA_CLARO,
        color=MARRON
    )

   
                        
 # 5. PANTALLA DE CARGA

    
    # ==========================================
    # PANTALLA PRINCIPAL - JARDIN DE CAPY
    # ==========================================

    def mostrar_inicio(e=None):

        page.clean()

        # ENCABEZADO DEL JUEGO
        encabezado = ft.Row(
            [
                ft.Text(
                    "🍓 CAPY COLLECTOR",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=MARRON
                ),
                ft.Text(
                    "🌸 Mi pequeño jardín 🌸",
                    size=17,
                    color=MARRON
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            wrap=True
        )

        # CONTADOR DE PUNTOS
        panel_puntos = ft.Container(
            content=ft.Row(
                [
                    ft.Text("⭐", size=28),
                    ft.Text(
                        f"Puntuación: {puntos}",
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color=MARRON
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=CREMA,
            padding=12,
            border_radius=25,
            border=ft.Border.all(2, ROSA)
        )

        # CONTADOR DE FRESAS
        panel_fresas = ft.Container(
            content=ft.Row(
                [
                    ft.Text("🍓", size=28),
                    ft.Text(
                        f"Fresas: {fresas}",
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color=MARRON
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=CREMA,
            padding=12,
            border_radius=25,
            border=ft.Border.all(2, ROSA)
        )

        estadisticas = ft.Row(
            [
                panel_puntos,
                panel_fresas
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            wrap=True
        )

        
        # ESCENARIO DEL JARDIN
        jardin = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "☁️       🌳       ☁️       🌳",
                        size=29
                    ),
                    ft.Text(
                        "🌷  🌼  🌸  🌼  🌷",
                        size=25
                    ),
                    imagen_capy(tamano=250),
                    ft.Text(
                        nombre_capy,
                        size=27,
                        weight=ft.FontWeight.BOLD,
                        color=MARRON
                    ),
                    ft.Container(
                        content=mensaje,
                        bgcolor=CREMA,
                        padding=12,
                        border_radius=20,
                        width=320
                    ),
                    ft.Text(
                        "🌼    🌿    🌷    🌿    🌼",
                        size=27
                    ),
                    ft.Text(
                        "🍓 ¡Bienvenido a tu jardín! 🍓",
                        size=17,
                        color=MARRON,
                        weight=ft.FontWeight.BOLD
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=9
            ),
            bgcolor="#D9EEC8",
            padding=15,
            border_radius=25,
            border=ft.Border.all(3, "#A4C88D"),
            height=450,
            expand=False
        )


        # PANEL LATERAL
        panel_lateral = ft.Container(
            content=ft.Column(
                [
                    ft.Text("💗", size=35),

                    titulo("Felicidad", 21),

                    ft.ProgressBar(
                        value=felicidad / 100,
                        width=220,
                        color=ROSA,
                        bgcolor=ROSA_CLARO,
                        bar_height=15
                    ),

                    ft.Text(
                        f"{felicidad} / 100",
                        color=MARRON,
                        size=17
                    ),

                    ft.Divider(color=ROSA),

                    titulo("🐹 Mi capibara", 19),

                    campo_nombre,

                    boton_nombre,

                    ft.Divider(color=ROSA),

                    titulo("🎯 Mi misión", 19),

                    ft.Text(
                        "Recolecta fresas, alimenta "
                        "a Capy y consigue puntos "
                        "para desbloquear premios.",
                        color=MARRON,
                        size=15,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text("🌸 🍓 🌸", size=25)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=13
            ),
            bgcolor=CREMA,
            padding=18,
            border_radius=25,
            border=ft.Border.all(2, "#F2B7CE"),
            width=280
        )

        # ZONA CENTRAL
        zona_principal = ft.Row(
            [
                jardin,
                panel_lateral
            ],
            spacing=15,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            wrap=True
        )

        # BOTONES DE ACCION
        acciones = ft.Row(
            [
                boton(
                    "🍓 Recolectar fresas",
                    recolectar,
                    ROSA,
                    205
                ),

                boton(
                    "🍽️ Alimentar a Capy",
                    alimentar,
                    "#F6C7D8",
                    205
                ),

                boton(
                    "👗 Vestuario",
                    mostrar_vestuario,
                    "#E8D9F5",
                    175
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
            wrap=True
        )

        # BOTONES INFERIORES
        opciones = ft.Row(
            [
                boton(
                    "🏆 Recompensas",
                    mostrar_recompensas,
                    CREMA,
                    190
                ),

                boton(
                    "🔄 Reiniciar juego",
                    reiniciar,
                    CREMA,
                    190
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            wrap=True
        )

        # ORGANIZAR TODA LA PANTALLA
        contenido = ft.Column(
            [
                encabezado,
                estadisticas,
                zona_principal,
                acciones,
                opciones
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

        page.add(contenido)
        page.update()

    # 7. PANTALLA DE VESTUARIO

    def mostrar_vestuario(e=None):

        page.clean()

        opciones = []

        for tipo in ["rosa", "fresa", "azul"]:

            nombre_ropa = ropas[tipo][0]

            contenido_boton = ft.Column(
                [
                    imagen_capy(tipo, 125),
                    titulo(nombre_ropa, 17),
                    ft.Text(
                        "Seleccionado 💗"
                        if ropa_actual == tipo
                        else "Elegir outfit",
                        color=MARRON,
                        size=13
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )

            opciones.append(
                ft.Button(
                    content=contenido_boton,
                    width=210,
                    height=220,
                    on_click=lambda e, t=tipo: seleccionar_ropa(t),
                    style=ft.ButtonStyle(
                        bgcolor=ROSA_CLARO,
                        color=MARRON,
                        padding=12,
                        shape=ft.RoundedRectangleBorder(radius=20),
                        side=ft.BorderSide(2, ROSA)
                    )
                )
            )

        contenido = ft.Column(
            [
                titulo("👗 VESTUARIO DE CAPY", 30),
                ft.Text(
                    "¡Elige una ropita para tu capibara!",
                    color=MARRON,
                    size=18
                ),
                imagen_capy(tamano=150),
                ft.Row(
                    opciones,
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                    spacing=15
                ),
                mensaje,
                boton("⬅ Volver al jardín", mostrar_inicio, ROSA)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=22,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

        page.add(contenido)
        actualizar()

    # 8. PANTALLA DE RECOMPENSAS

    def mostrar_recompensas(e=None):

        page.clean()

        if puntos >= 10:
            premio = ft.Column(
                [
                    titulo("¡FELICIDADES!", 32),
                    imagen_capy(tamano=190),
                    titulo("🏆 Capy Estilosa 🏆", 25),
                    ft.Text(
                        "¡Has conseguido 10 puntos!\n"
                        "Tu capibara es una estrella.",
                        color=MARRON,
                        size=18,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        else:
            premio = ft.Column(
                [
                    titulo("🎁 Próxima recompensa", 25),
                    imagen_capy(tamano=170),
                    titulo(f"{puntos} / 10 puntos", 22),
                    ft.Text(
                        "¡Consigue 10 puntos para desbloquear "
                        "a Capy Estilosa!",
                        color=MARRON,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.ProgressBar(
                        value=min(puntos / 10, 1),
                        width=300,
                        color=ROSA,
                        bgcolor=ROSA_CLARO
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )

        contenido = ft.Container(
            content=ft.Column(
                [
                    premio,
                    boton("¡Genial! 💗", mostrar_inicio)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25
            ),
            bgcolor=CREMA,
            padding=30,
            border_radius=28,
            border=ft.Border.all(3, ROSA)
        )

        page.add(
            ft.Column(
                [contenido],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        actualizar()

        # 9. INICIAR APLICACION
    mostrar_inicio()


# EJECUTAR CAPY COLLECTOR
ft.run(main, assets_dir="assets")


