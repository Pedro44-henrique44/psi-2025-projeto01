from django.shortcuts import render

info =  [
    
    {
        "ppg": 105.1,
        "colocacao_ppg": "29ª",
        "rpg": 41.3,
        "colocacao_rpg": "29ª",
        "vit_der": "(V)26-56(D)",
        "posi": "12º lugar na conferência oeste.",
        "apg": 25.2,
         "colocacao_apg": "24ª",
    }
]

draft = [
    {
        "pick": 8,
        "nome": "Egor Demin",
        "pos": "G-F, Guard-Foward (armador/ala).",
        "Sch": "BYU",
        "Nacio": "Russia"
    },

    {
        "pick": 19,
        "nome": "Nolan Traoré",
        "pos": "G, Guard (armador).",
        "Sch": "Saint-Quentin BB (França)",
        "Nacio": "Francês"
    },

    {
        "pick": 26,
        "nome": "Ben Saraf",
        "pos": "G, Guard (armador).",
        "Sch": "Ratiopharm Ulm (Alemanha)",
        "Nacio": "Israel"
    },

    {
        "pick": 27,
        "nome": "Danny Wolf",
        "pos": "F-C, Foward-Center (ala/pivô).",
        "Sch": "Michigan",
        "Nacio": "Estados Unidos"
    },

    {
        "pick": 36,
        "nome": "Adou Thiero",
        "pos": "F, Foward (ala).",
        "Sch": "Arkansas",
        "Nacio": "Estados Unidos"
    }
]

lendas = [
    {
        "nome": "Paul Pierce",
        "posi": "F, Foward (ala)",
        "temp":  "2014"
    },

     {
        "nome": "Kevin Garnett",
        "posi": "F, Foward (ala)",
        "temp":  "2014-2015"
    },

     {
        "nome": "Maurice Cheeks",
        "posi": "G, Guard (armador)",
        "temp":  "1992-1993"
    },

     {
        "nome": "Jason Kidd",
        "posi": "G, Guard (armador)",
        "temp":  "2001-2008"
    },

     {
        "nome": "Dikembe Mutombo",
        "posi": "C, Center (pivô)",
        "temp":  "2003"
    },
]
elenco = [
    {
        "nome": "Dariq WhiteHead",
        "num": 0,
        "posi": "G-F, Guard-Foward (armador-ala)",
        "altura": "6-6ft",
        "peso": "220lbs",
        "nasc": "01 de agosto de 2004",
        "ano": 2,
        "sch": "Duke",
        "MTD": "22ª escolha do draft de 2023",
        "imagem": "MeuSite/img/Dariq.png"
    },

    {
        "nome": "Drake Powell",
        "num": 4,
        "posi": "F, Foward (ala)",
        "altura": "6-3ft",
        "peso": "195lbs",
        "nasc": "08 de setembro de 2005",
        "ano": "Novato",
        "sch": "North Carolina (Carolina do Norte)",
        "MTD": "Trocado no Draft pelo Atlanta",
        "imagem": "MeuSite/img/Drake.png"
    },

    {
        "nome": "Michael Porter Jr.",
        "num": 7,
        "posi": "F, Foward (ala)",
        "altura": "6-10ft",
        "peso": "218lbs",
        "nasc": "29 de junho de 1998",
        "ano": 6,
        "sch": "Missouri",
        "MTD": "Chegou de Denver no dia: 07/08/25 ",
        "imagem": "MeuSite/img/Micha.png"
    },

    {
        "nome": "Tyson Etienne.",
        "num": 10,
        "posi": "G, Guard (Armador)",
        "altura": "6-2ft",
        "peso": "200lbs",
        "nasc": "17 de setembro de 1999",
        "ano": 1,
        "sch": "Wichita State",
        "MTD": "Contratado em 09/10/24",
        "imagem": "MeuSite/img/Tyson.png"
    },

    {
        "nome": "Tosan Evbuomwan",
        "num": 12,
        "posi": "F, Foward (ala)",
        "altura": "6-7ft",
        "peso": "217 lbs",
        "nasc": "16 de fevereiro de 2001",
        "ano": 2,
        "sch": "Princeton",
        "MTD": "Contratado em 01/01/25 ",
        "imagem": "MeuSite/img/Tosan.png"
    },

    {
        "nome": "Terance Mann",
        "num": 14,
        "posi": "G-F, Guard-Foward (armador-ala)",
        "altura": "6-5ft",
        "peso": "215lbs",
        "nasc": "18 de outubro de 1996",
        "ano": 6,
        "sch": "Florida State",
        "MTD": "trocado do Atlanta em 07/07/25",
        "imagem": "MeuSite/img/terr.png"
    },

    {
        "nome": "Tyrese Martin",
        "num": 13,
        "posi": "F, Foward (ala)",
        "altura": "6-6ft",
        "peso": "215lbs",
        "nasc": "07 de março de 1999",
        "ano": 2,
        "sch": "Connecticut",
        "MTD": "Contratado em 09/20/24",
        "imagem": "MeuSite/img/tyre.png"
    },

    {
        "nome": "Cam Thomas",
        "num": 24,
        "posi": "G, Guard (armador)",
        "altura": "6-3ft",
        "peso": "210lbs",
        "nasc": "13 de outubro de 2001",
        "ano": 4,
        "sch": "Louisiana State",
        "MTD": "23ª escolha do draft de 2021",
        "imagem": "MeuSite/img/Cam.png"
    },

    {
        "nome": "Nic Claxton",
        "num": 33,
        "posi": "C, Center (pivô)",
        "altura": "6-11ft",
        "peso": "215lbs",
        "nasc": "17 de abril de 1999",
        "ano": 6,
        "sch": "Gergia",
        "MTD": "31ª escolha so draft de 2019",
        "imagem": "MeuSite/img/clax.png"
    },

    {
        "nome": "Jalen Wilson",
        "num": 22,
        "posi": "F, Foward (ala)",
        "altura": "6-6ft",
        "peso": "220lbs",
        "nasc": "04 de novembro de 2000",
        "ano": 2,
        "sch": "Kansas",
        "MTD": "51ª escolha do draft de 2023",
        "imagem": "MeuSite/img/Jalen.png"
    },

    {
        "nome": "Keon Johnson ",
        "num": 45,
        "posi": "G, Guard (armador)",
        "altura": "6-5ft",
        "peso": "185lbs",
        "nasc": "10 de março de 2002",
        "ano": 4,
        "sch": "Tennessee",
        "MTD": "Contratado em 11/01/23",
        "imagem": "MeuSite/img/Keon.png"
    },
]
def index(request):
    
    context = {
        "info": info,
        "draft": draft,
        "lendas": lendas,
    }
    return render(request, "MeuSite/index.html", context)

def elenco_view(request):

    context = {
        "elenco": elenco,
    }
    return render(request, "MeuSite/elenco.html", context)

def sobre(request):
    info_sobre = [
        {
            "autor": "Pedro Henrique Figueredo Ferreira, estudante do Campus IFRN SPP.",
            "Sbase": "este site se inspirou fortemente nos seguintes sites: NBA, ESPN",
            "Obj": "Este site foi criado no intuito de concluir um projeto acadêmico da matéria de PSI, lecionada pelo professor Diego Cirilo"
        }
    ]
    context = {
        "info_sobre": info_sobre
    }
    return render(request, "MeuSite/sobre.html", context)
# Create your views here.
