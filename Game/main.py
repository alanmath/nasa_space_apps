import os, sys 

dirpath = os.getcwd()

sys.path.append(dirpath)
if getattr(sys, 'frozen', False) :
    os.chdir(sys._MEIPASS)






import pygame
from class_game import *
from  time import sleep
from constantes import *


def inicializa ():
    """INICIO DO JOGO! CARREGAMOS TODAS AS INFORMAÇÕES NECESSÁRIAS PARA O FUNCIONAMENTO"""
    pygame.init()
    pygame.mixer.init() 
    pygame.mixer.music.load("data/sound/music.mp3") 
    pygame.mixer.music.set_volume(0.3) 
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Code Scape")

    #Cricao da janela do jogo
    window = pygame.display.set_mode((1920, 1080))
    
    assets = {             #Carregamos todas as imagens necessárias para o jogo
        'player' : pygame.image.load('data/img/frente.png'),
        'costa' : [pygame.image.load('data/img/costa.png'), pygame.image.load('data/img/costa_anda_d.png'), pygame.image.load('data/img/costa_anda_e.png')],
        'frente' : [pygame.image.load('data/img/frente.png'), pygame.image.load('data/img/frente_anda_d.png'), pygame.image.load('data/img/frente_anda_e.png')],
        'ladod' : [pygame.image.load('data/img/lado_d.png'), pygame.image.load('data/img/lado_anda_d.png'), pygame.image.load('data/img/lado_anda_d2.png')],
        'ladoe' : [pygame.image.load('data/img/lado_e.png'), pygame.image.load('data/img/lado_anda_e.png'), pygame.image.load('data/img/lado_anda_e2.png')],
        'mapa' : [pygame.image.load('data/img/fase1.png'), pygame.image.load('data/img/menu.png'), pygame.image.load('data/img/fase2.png'), pygame.image.load('data/img/fase3.png')],
        'key' : [pygame.image.load('data/img/papeis.png')],
        "porta" : pygame.image.load('data/img/pc.png'),
        'menu_principal': pygame.image.load('data/img/inicio.jpeg'), 'vitoria': pygame.image.load('data/img/vitoria.jpeg') , 'derrota': pygame.image.load('data/img/derrota.png'),
        'papel' : [pygame.image.load('data/img/papel.png')],
        'cama': [pygame.image.load('data/img/cama.png')],
        'clock': [pygame.image.load('data/img/clock.png')],
        'mesa1': [pygame.image.load('data/img/mesa1.png')],
        'bolinha de papel' : [pygame.image.load('data/img/bola.png')],
        'computador' : [pygame.image.load('data/img/computador.png'), pygame.image.load('data/img/computador2.png')],
        'mesa2':[pygame.image.load('data/img/mesa2.png')],
        'disquete':[pygame.image.load('data/img/disquete.png')],
        'celular':[pygame.image.load('data/img/celular.png')],
        'tv':[pygame.image.load('data/img/tv.png'), pygame.image.load('data/img/tv2.png')],
        'estante': [pygame.image.load('data/img/estante.png')],
        'interacao' : pygame.mixer.Sound('data/sound/item.wav'),
        'door' : pygame.mixer.Sound('data/sound/door.flac'),
        'tutorial': pygame.image.load('data/img/tutorial.png'),
        'som1' : pygame.mixer.Sound('data/sound/Antena _de _alto_ganho.mp3'),
        'som2' : pygame.mixer.Sound('data/sound/Escudo_Termico.mp3'),
        'som3' : pygame.mixer.Sound('data/sound/Painel_Solar.mp3'),
        'som4' : pygame.mixer.Sound('data/sound/Sistema_de_refrigeração.mp3'),
        'nave0' : pygame.image.load('data/img/sonda/0.png'),
        'nave1' : pygame.image.load('data/img/sonda/1.png'),
        'nave2' : pygame.image.load('data/img/sonda/2.png'),
        'nave3' : pygame.image.load('data/img/sonda/3.png'),
        'nave4' : pygame.image.load('data/img/sonda/4.png'),
        
        'i1' : [pygame.image.load('data/img/sonda/i1.png')],
        'i2' : [pygame.image.load('data/img/sonda/i2.png')],
        'i3' : [pygame.image.load('data/img/sonda/i3.png')],
        'i4' : [pygame.image.load('data/img/sonda/i4.png')],
    } 
    state = {             #Aqui criamos a lista de itens para cada fase, passando eles dentro da classe Item, a qual passamos tudo que é necessário para cada ítem, que inclui sua imagem, dica e posição.
    'jogador' : Player(360, 240),
    'lista de itens1' :[], 
    'lista de itens2' :[Item(assets['papel'], (1073,700), pygame.image.load('data/img/dica_fase2.png')),Item(assets['disquete'], (237,633), pygame.image.load('data/img/disquete_dica.png'))], 
    'lista de itens3' :[Item(assets['celular'], (1064,527), pygame.image.load('data/img/celular_dica.png')), Item(assets['tv'], (684,62), pygame.image.load('data/img/tv_dica.png')), Item(assets['estante'], (237,23), pygame.image.load('data/img/estante_dica.png')), Item(assets['computador'], (843,35), pygame.image.load('data/img/computador2_dica.png')), Item(assets['mesa2'], (321,772), pygame.image.load('data/img/copo_dica.png'))],
    'primeiro_tempo'  :0,
    'last_enter': 0,
    'troca_status_move':0,      #Variáveis usadas em condições do jogo
    'numero_trocador':0,
    'tempo_geral': 0 ,
    'nave' : Nave([assets['nave0'],assets['nave1'],assets['nave2'],assets['nave3']])
    }
    
    portas = {  #Nesse dicionário portas passamos tudo necessário às portas do jogo, como imagem, posição, texto e senha.
        'PRIMEIRA FASE' : Porta(assets['porta'], (987, 21), "A SENHA é mais facil do que parece!","Digite e tecle ENTER", "senha"),  
        'SEGUNDA FASE' : Porta(assets['porta'], (987, 21), "Para controlar o PARKER","Digite a senha e tecle ENTER", "12/01/1986"),
        'TERCEIRA FASE' : Porta(assets['porta'], (987, 21), "Numeros nào servem pra nada...","Digite e tecle ENTER", "toshi"),
        'menu_principal': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'VITORIA': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'DERROTA':  Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no")
    }

    telas = {   #Criamos a tela de cada fase, passaremos ela na classe Tela onde desenhamos as alterações
        'menu_principal': Tela(assets['menu_principal'],[],[],portas['menu_principal']),
        'SEGUNDA FASE' : Tela(assets['mapa'][2], state['lista de itens2'],[],portas['SEGUNDA FASE']), 
        'PRIMEIRA FASE' : Tela(assets['mapa'][0], state['lista de itens1'],[Item_movel(assets['i1'], [1450,696],1,assets['som1']), Item_movel(assets['i2'], [400,600],2, assets['som4']),Item_movel(assets['i3'], [800,800],3,assets['som3']), Item_movel(assets['i4'], [890,200],4, assets['som2'])], portas['menu_principal']),
        'TERCEIRA FASE' : Tela(assets['mapa'][3], state['lista de itens3'], [],portas['TERCEIRA FASE']),
        'VITORIA': Tela(assets['vitoria'],[],[], portas['menu_principal']),
        'DERROTA':Tela(assets['derrota'],[], [],portas['menu_principal'])
    }
   

    
    state['tela atual'] = telas['menu_principal']


    return window, assets, state, telas, portas

def entre_telas (state, fase) :
    """TEMPO DE ESPERA ENTRE AS FASES"""
    while state['tempo_geral']-state['last_enter']<3000 and state['jogador'].passou_menu:
        state['tempo_geral'] = pygame.time.get_ticks()
        window.fill((0,0,0))
        text_fase = BASE.render(fase, True, (255,225,255))
        window.blit(text_fase, (330,350))
        pygame.display.update()

def tutorial (state) :
    """TUTORIAL"""
    
    if state['tempo_geral']-state['last_enter']<8500 and state['jogador'].status == "PRIMEIRA FASE":
        state['tempo_geral'] = pygame.time.get_ticks()
        
        
        window.blit(assets['tutorial'], (326,232))
        pygame.display.update()

def desenha (window, assets, state, portas):
    """DESENHAMOS OS ÍTENS DO JOGO"""
    
    tempo = pygame.time.get_ticks()
    fase = state['jogador'].status # Fase recebe o nome da fase que o jogador está e isso ajuda na hora de controlar os itens e o cenário

    state['tela atual'] = telas[fase]

    state['tela atual'].img = pygame.transform.scale(state['tela atual'].img, (pygame.display.get_surface().get_size()))  # Parte de redmencionar a tela
    
    window.blit(state['tela atual'].img,(0,0)) 



    for item_movel in state['tela atual'].itens_moveis :

        if item_movel.status :
            item_movel.ponto[0] = state['jogador'].pos_x
            item_movel.ponto[1] = state['jogador'].pos_y
            item_movel.larg, item_movel.alt = item_movel.img[0].get_size()
            item_movel.rect = pygame.Rect(item_movel.ponto, (item_movel.larg, item_movel.alt))

        window.blit(item_movel.img[0], item_movel.ponto) #-------------------------------------------------------------------------------------------------------------------------------------------------------------

            
    if state['jogador'].status == 'PRIMEIRA FASE' :
        window.blit(state['nave'].img[state['nave'].status], state['nave'].ponto)


    for itens in state['tela atual'].itens:   # Estrutura de for que controla a animação dos itens caso eles tenham animação. 
        
        if itens.status:
            window.blit(itens.mensagem, (326,232))
        if len(itens.img) == 1:
            
            window.blit(itens.img[0], (itens.ponto[0],itens.ponto[1])) #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        elif tempo - state['troca_status_move'] > 1750:  #Fazer animação de alguns itens
            state['troca_status_move'] = tempo
            if state['numero_trocador'] == 0:
                state['numero_trocador'] = 1
            elif state['numero_trocador'] ==1:
                state['numero_trocador'] = 0
        if len(itens.img) == 2:    
            window.blit(itens.img[state['numero_trocador']], itens.ponto)
                 
    window.blit(portas[fase].img, portas[fase].ponto)
    tempo = pygame.time.get_ticks()

    if state['tela atual'] != telas['menu_principal'] and state['tela atual'] != telas['VITORIA'] and state['tela atual'] != telas['DERROTA']: # Controle de quais telas o jogador pode ser desenhado
        state['jogador'].desenha(window, assets)      # Desenha o jogador
        cronometro = BASE_MENOR.render(f"{(pygame.time.get_ticks()-state['primeiro_tempo'])/60000:.2f} Minutos", True, ROSA)
        window.blit(cronometro, (0,0))
        
        entre_telas(state, fase) # Caso o jogador tenha passado de fase é feito uma transição para outra a outra fase do jogo.
        if state['jogador'].status == 'PRIMEIRA FASE':
            tutorial(state)
        

    state['jogador'].passou_menu = False

    if portas[fase].esta:
    
        portas[fase].desenha(window, fase, portas)

    if fase == 'VITORIA':  # Verifica se o jogador venceu para assim desenhar a tela de vitória e o tempo em que resolveu os desafios
        state['jogador'].status = 'VITORIA'
        
    pygame.display.update()

def finaliza ():
    pygame.QUIT


def recebe (state, window):
    """Aqui r  recebe apenas o return da classe recebe que foi tranferida para a classe tela, já que para o game loop o recebe tem que returnar True"""
    r = state['tela atual'].recebe(state, window, assets)            
    return r


    

def gameloop (window, assets, state):
    """Loop do jogo"""
    while recebe(state, window) :
        desenha(window, assets, state, portas)


if __name__ == '__main__':
    """Inicialização do jogo"""
    window, assets, state, telas, portas = inicializa()
    gameloop(window, assets, state)
    finaliza()









