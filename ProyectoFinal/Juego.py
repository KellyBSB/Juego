import pygame
import random
import time
class Cursor(pygame.Rect):#Clase que los ayuda a reconocer el cursor en la pantalla para interactuar con el (menu)
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):#clase para cosntruir botones(Menu)
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
class Imagenes(pygame.sprite.Sprite):#clase que construye las imagenes usadas (cargar y da formato)
    def __init__(self, imagen):
        #llamar clase padre
        super().__init__() 
        #cargar imagen al grupo de sprits
        self.image = pygame.image.load(imagen).convert()
        #dar transparencia a la imagen 
        self.image.set_colorkey((0,0,0))
        #cargar el rectangulo a la imagen para poder analisar colisiones
        self.rect = self.image.get_rect()
def tiempo():#Inicia un reloj que controla el timepo del programa(tiempo global del programa) 
    #contador (tiempo)
    segundos = round(pygame.time.get_ticks()/1000)#medir tiempo
    segundos = "Tiempo: "+str(segundos)#variable que se va a pintar
    contador = fuente1.render(segundos,0,(250,250,250))#superficie que se va a pintar
    return contador
def pintar_alien():#Funcion para pintar la imagen con la cual se interactua al recogerla dentro dle juego
    bloquear = Imagenes("alien.png")
    bloquear.rect.x = random.randrange(ancho_Pantalla-50)
    bloquear.rect.y = random.randrange(alto_Pantalla-50)
    bloquear_list.add(bloquear)
    all_sprites_list.add(bloquear)
def iniciar_musica():#Funcion para cargar e iniciar la musica de fondo
    #Inicio de musica de fondo
    musica1=pygame.mixer.Sound("MusicaFondo.wav").play()
    return musica1
def Vertxt():#Funcion para ver los datos contedos dentro del archivo de texto plano
    pantalla.fill((255,255,255))
    archi=open('Puntaje.txt','r')
    puntaj=str(archi.readlines())
    pintPt= fuente1.render(puntaj,0,(0,0,0))
    pantalla.blit(pintPt,(50,50))
    pygame.display.flip()
    archi.close()
    time.sleep(3)
def Jugadores():#INICIO JUEGO 2 jUADORES
    fondo = Imagenes("Fondo.jpg")
    all_sprites_list.add(fondo)
    pintar_alien()

    #carga de imagenes con llamado a la funcion init para que cargue la imagen 
    player = Imagenes("Platillo.png")
    #añadir la imagen al grupo de sprits
    all_sprites_list.add(player)
    #carga de imagenes con llamado a la funcion init para que cargue la imagen  del player2
    player2 = Imagenes("Nave.jpg")
    #añadir la imagen al grupo de sprits player 2
    all_sprites_list.add(player2)
    #condicion para ingreso al bucle
    asteroides = Imagenes("Asteroide.png")
    all_sprites_list.add(asteroides)
    asteroides_list.add(asteroides)
    asteroides1 = Imagenes("Asteroide.png")
    all_sprites_list.add(asteroides1)
    asteroides_list.add(asteroides1)
    fin_del_juego = False
    # variables de puntaje
    puntuacion = 0
    puntuacion2 = 0
    #variables de posicion de jugadores
    posx = 50
    posy = 50
    posx2 = 850
    posy2 = 500
    astx = 900
    asty = 0
    ast1x=750
    ast1y=0
    velocidad=15
    i=0
    j=0

    musica1=iniciar_musica()
    #inicio del reloj
    clock = pygame.time.Clock()
    # -------- Inicio del bucle principal del juego-----------
    while not fin_del_juego:
        for event in pygame.event.get():
            #condicion de salida por cierre de pantalla
            if event.type == pygame.QUIT:
                archi=open('Puntaje.txt','a')
                archi.write(punt+"\n")
                archi.write(punt2+"\n")
                archi.close() 
                fin_del_juego = True
            #condiciones por eventos de teclado (pulsar botones)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx-=velocidad
                if event.key == pygame.K_RIGHT:
                    posx+=velocidad
                if event.key == pygame.K_UP:
                    posy-=velocidad
                if event.key == pygame.K_DOWN:
                    posy+=velocidad
                if event.key == pygame.K_a:
                    posx2-=velocidad
                if event.key == pygame.K_d:
                    posx2+=velocidad
                if event.key == pygame.K_w:
                    posy2-=velocidad
                if event.key == pygame.K_s:
                    posy2+=velocidad

        i+=1
        if i==50:
            j+=1
            i=0

        astx-=1
        asty+=2
        ast1x-=2
        ast1y+=1
        pantalla.fill((0,0,0))
        #cambio de posiciones de los jugadores en x y y
        player.rect.x = posx
        player.rect.y = posy
        player2.rect.x = posx2
        player2.rect.y = posy2
        asteroides.rect.x = astx
        asteroides.rect.y = asty
        asteroides1.rect.x = ast1x
        asteroides1.rect.y = ast1y
        if astx==600 and asty<=600:
            astx=900
            asty=0
        if ast1x==200 and ast1y<=700:
            ast1x=750
            ast1y=0


        #deteccion de colisiones
        bloquears_hit_list = pygame.sprite.spritecollide(player, bloquear_list, True)
        bloquears_hit_list2 = pygame.sprite.spritecollide(player2,bloquear_list,True) 
        colisi = pygame.sprite.spritecollide(player,asteroides_list, True)
        colisi2 = pygame.sprite.spritecollide(player2,asteroides_list, True)
        #incremento de puntajes por colisiones
        for bloquear in bloquears_hit_list:
            puntuacion += 1
            pintar_alien()
            sonido1.play()

        for bloquear in bloquears_hit_list2:
            puntuacion2 +=1
            pintar_alien()
            sonido1.play()

        for bloquear in colisi:
            archi=open('Puntaje.txt','a')
            archi.write(punt+"\n")
            archi.write(punt2+"\n")
            archi.close()
            fin_del_juego=True
        for bloquear in colisi2:
            archi=open('Puntaje.txt','a')
            archi.write(punt+"\n")
            archi.write(punt2+"\n")
            archi.close()
            fin_del_juego=True

        #pintar todos los sprits
        all_sprites_list.draw(pantalla)
        reloj="Tiempo :"+str(j)
        contador=fuente1.render(reloj,0,(250,250,250))
        pantalla.blit(contador,(10,6))#pintar contador en pantalla
        #pintar en pantalla puntaje (jugador1)
        punt="Kelly  "+str(puntuacion*10)
        pintPunt= fuente1.render(punt,0,(250,250,250))
        pantalla.blit(pintPunt,(130,6))
        #pintar en pantalla puntaje (jugador2)
        punt2="Diana   "+str(puntuacion2*10)
        pintPunt2=fuente1.render(punt2,0,(250,250,250))
        pantalla.blit(pintPunt2,(300,6))
        #velocidad de los fotogramas por segundo
        clock.tick(60)
        #se muestra todo lo que hay actualizar
        pygame.display.flip()
    musica1.stop()
    Menu()
    pygame.quit()
def Jugador():#INICIO JUEGO 1 JUGADOR
    fondo = Imagenes("Fondo.jpg")
    all_sprites_list.add(fondo)

    pintar_alien()
    #carga de imagenes con llamado a la funcion init para que cargue la imagen 
    player = Imagenes("Platillo.png")
    all_sprites_list.add(player)

    asteroides = Imagenes("Asteroide.png")
    all_sprites_list.add(asteroides)
    asteroides_list.add(asteroides)
    asteroides1 = Imagenes("Asteroide.png")
    all_sprites_list.add(asteroides1)
    asteroides_list.add(asteroides1)
    asteroides2 = Imagenes("Asteroide.png")
    all_sprites_list.add(asteroides2)
    asteroides_list.add(asteroides2)


    #añadir la imagen al grupo de sprits

    fin_del_juego = False
    # variables de puntaje
    puntuacion = 0
    #variables de posicion de jugadores
    posx = 50
    posy = 50
    astx = 900
    asty = 0
    ast1x=800
    ast1y=0
    ast2x=600
    ast2y=0
    velocidad=15
    i=0
    j=0
    musica1=iniciar_musica()
    #inicio del reloj
    clock = pygame.time.Clock()
    while not fin_del_juego:
        for event in pygame.event.get():
            #condicion de salida por cierre de pantalla
            if event.type == pygame.QUIT:
                archi=open('Puntaje.txt','a')
                archi.write(punt+"\n")
                archi.close() 
                fin_del_juego = True
        pantalla.fill((255,255,255))
        i+=1
        if i==50:
            j+=1
            i=0

        astx-=1
        asty+=1
        ast1x-=2
        ast1y+=1
        ast2x-=1
        ast2y+=2
        #cambio de posiciones de los jugadores en x y y
        pos = pygame.mouse.get_pos()
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        asteroides.rect.x = astx
        asteroides.rect.y = asty
        asteroides1.rect.x = ast1x
        asteroides1.rect.y = ast1y
        asteroides2.rect.x = ast2x
        asteroides2.rect.y = ast2y

        if astx==300 and asty<=600:
            astx=900
            asty=0
        if ast1x==150 and ast1y<=1000:
            ast1x=750
            ast1y=0
        if ast2x==250 and ast2y<=1000:
            ast2x=650
            ast2y=0

        #deteccion de colisiones
        bloquears_hit_list = pygame.sprite.spritecollide(player, bloquear_list, True)
        colisi = pygame.sprite.spritecollide(player,asteroides_list, True)
        #incremento de puntajes por colisiones
        for bloquear in bloquears_hit_list:
            puntuacion += 1
            pintar_alien()
            sonido1.play()
        for bloquear in colisi:
            archi=open('Puntaje.txt','a')
            archi.write(punt+"\n")
            archi.write(punt2+"\n")
            archi.close()
            fin_del_juego=True
            
        #pintar todos los sprits
        all_sprites_list.draw(pantalla)
        #funcion para calcular tiempo
        reloj="Tiempo: "+str(j)
        contador=fuente1.render(reloj,0,(250,250,250))
        pantalla.blit(contador,(10,6))#pintar contador en pantalla
        #pintar en pantalla puntaje (jugador1)
        punt="José  "+str(puntuacion*10)
        pintPunt= fuente1.render(punt,0,(250,250,230))
        pantalla.blit(pintPunt,(130,6))
        #velocidad de los fotogramas por segundo
        clock.tick(60)
        #se muestra todo lo que hay actualizar
        pygame.display.flip()
    musica1.stop()
    Menu()
    pygame.quit()
def Menu():#Fcunion encargada de controlar el menu de inicio
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()

    fuente = pygame.font.SysFont("Times new roman",40,True,False)

    Titulo="--TRIGON FUCIONADO--"
    tit= fuente.render(Titulo,0,(0,0,200))
    
    imagen1_1_Jugador=pygame.image.load("Boton1Jugador2.png")
    imagen2_1_Jugador=pygame.image.load("Boton1jugador.png")
    imagen1_2_Jugador=pygame.image.load("Boton2Jugador2.png")
    imagen2_2_Jugador=pygame.image.load("Boton2jugador.png")    
    imagen1_Puntuacion=pygame.image.load("Boton1Puntuacion2.png")
    imagen2_Puntuacion=pygame.image.load("BotonPuntuacion.png")    

    boton1=Boton(imagen1_1_Jugador,imagen2_1_Jugador,400,150)
    boton2=Boton(imagen1_2_Jugador,imagen2_2_Jugador,400,220)
    boton3=Boton(imagen1_Puntuacion,imagen2_Puntuacion,400,290)
    cursor1=Cursor()
    
    blanco=(255,255,255) # color blanco en RGB
    rojo=(200,0,0)
    azul=(0,0,200)
    colordefondo=blanco
    
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    Jugador()
                if cursor1.colliderect(boton2.rect):
                    Jugadores()
                if cursor1.colliderect(boton3.rect):
                    Vertxt()
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(colordefondo) # pinto la superficie de blanco        
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla, cursor1)
        boton3.update(pantalla, cursor1)
        pantalla.blit(tit,(200,50))

        
        pygame.display.update() #actualizo el display
        
    pygame.quit() 
#---------- INICIO DEL JUEGO-------------
#Codigo para el inicio del programa y los modulos usados pygame
#-----iniciar modulos de pygame
pygame.init()
#-----tamaño de la ventana 
ancho_Pantalla = 1000
alto_Pantalla = 600
#----setear valores a la pantalla 
pantalla = pygame.display.set_mode([ancho_Pantalla, alto_Pantalla])
#----titulo de la pagina
pygame.display.set_caption("TRIGON FUCIONADO")
#grupo de lista para colisiones contabilizar coliciones
bloquear_list = pygame.sprite.Group()
bloquear_list2 = pygame.sprite.Group()
all_sprites_list=pygame.sprite.Group()
asteroides_list =pygame.sprite.Group()
#fuente de texto para ecribir en pantalla
fuente1 = pygame.font.SysFont("Arial",20,True,False)
sonido1=pygame.mixer.Sound("click.wav")
Menu()