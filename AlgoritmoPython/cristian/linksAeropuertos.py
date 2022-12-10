import json

a = {
    "ACE": {
        "nombre": "Lanzarote",
        "foto": "https://media.traveler.es/photos/6279555a5b37ba40f6561b1e/16:9/w_2580,c_limit/Jameos%20piscina%2008_LR_%C2%A9%20CACT%20Lanzarote.jpg",
    },
    "AMS": {
        "nombre": "Amsterdam",
        "foto": "https://media.traveler.es/photos/6231abc7d03e1c5549e648ca/16:9/w_2560%2Cc_limit/The%2520Best%2520Places%2520for%2520Female%2520Solo%2520Travelers_Amsterdam_GettyImages-923546342.jpg",
    },
    "ARN": {
        "nombre": "Estocolmo",
        "foto": "https://a.cdn-hotels.com/gdcs/production160/d1943/a0fe0b3e-1469-412a-a45e-276f65e77702.jpg?impolicy=fcrop&w=800&h=533&q=medium",
    },
    "BER": {
        "nombre": "Berlin",
        "foto": "https://cdn2.hometogo.net/assets/media/pics/1200_628/611a5609415e7.jpg",
    },
    "BIO": {
        "nombre": "Bilbao",
        "foto": "https://tourism.euskadi.eus/contenidos/d_destinos_turisticos/0000004981_d2_rec_turismo/en_4981/images/CT_cabecerabilbaoguggen.jpg",
    },
    "BRU": {
        "nombre": "Bruselas",
        "foto": "https://a.cdn-hotels.com/gdcs/production178/d1699/8f999c57-cf7b-47cf-9252-8e3513ef570d.jpg?impolicy=fcrop&w=800&h=533&q=medium",
    },
    "CDG": {
        "nombre": "Paris",
        "foto": "https://viajes.nationalgeographic.com.es/medio/2022/07/13/paris_37bc088a_1280x720.jpg",
    },
    "DUB": {
        "nombre": "Dublin",
        "foto": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dublin-1520287124.jpg",
    },
    "FCO": {
        "nombre": "Roma",
        "foto": "https://assets.buendiatours.com/s3fs-public/styles/highlight_large/public/2022-03/roma-coliseo-que-ver-en-roma_roma-guia-viaje_buendia-tours.jpg?VersionId=7tEtGNDNSgwq25cAYnwAwKPU9vFV22E_&itok=2qZldgwf",
    },
    "FRA": {
        "nombre": "Frankfurt",
        "foto": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Skyline_Frankfurt_am_Main_2015.jpg/800px-Skyline_Frankfurt_am_Main_2015.jpg",
    },
    "FUE": {
        "nombre": "Fuerteventura",
        "foto": "https://mejoreszonas.com/wp-content/uploads/2021/06/Las-mejores-zonas-donde-alojarse-en-Fuerteventura-Islas-Canarias-1600x1067.jpg",
    },
    "IBZ": {
        "nombre": "Ibiza",
        "foto": "https://destinoysabor.com/blog/wp-content/uploads/2021/05/Dalt-Vila-Imagen-de-Ibiza-Marathon-1050x483.jpg",
    },
    "LGW": {
        "nombre": "Londres-LGW",
        "foto": "https://www.visitbritain.com/sites/default/files/styles/consumer_campaigns_hero_mobile/public/consumer/paragraphs-bundles/image-banner/london_skyline_vb34141644.jpg?itok=eKyhb8l8",
    },
    "LHR": {
        "nombre": "Londres-LHR",
        "foto": "https://www.euroresidentes.com/viajes/viajar/wp-content/uploads/sites/3/2006/06/londres.jpg",
    },
    "LIS": {
        "nombre": "Lisboa",
        "foto": "https://vivecamino.com/img/loc/av/lisboa_247.jpg",
    },
    "LPA": {
        "nombre": "Gran Canaria",
        "foto": "https://a.cdn-hotels.com/gdcs/production166/d776/629944c6-ce02-45aa-bc0a-8ad628f6b82c.jpg?impolicy=fcrop&w=800&h=533&q=medium",
    },
    "MAH": {
        "nombre": "Menorca",
        "foto": "https://images.hola.com/imagenes/viajes/20190211137137/menorca-en-invierno-baleares/0-646-457/menorca-noche-mahon-t.jpg",
    },
    "MUC": {
        "nombre": "Múnich",
        "foto": "https://images.squarespace-cdn.com/content/v1/5ceac7567e6b0a0001be06df/1578858880348-DT3YMA8RYP5LXU1ZVVVA/MU12012020001-munich-alemania-que-ver.jpg?format=750w",
    },
    "MXP": {
        "nombre": "Milán",
        "foto": "https://www.viajarmilan.com/img/guia-milan.jpg",
    },
    "OPO": {
        "nombre": "Oporto",
        "foto": "https://upload.wikimedia.org/wikipedia/commons/5/55/O_Porto_%28visto_da_Ponte_Dom_Luis_I%29.jpg",
    },
    "OSL": {
        "nombre": "Oslo",
        "foto": "https://destinoysabor.com/blog/wp-content/uploads/2016/11/Oslo-una-ciudad-de-vikingos.jpg",
    },
    "OVD": {
        "nombre": "Astutrias",
        "foto": "https://img2.viajar.elperiodico.com/89/9b/c4/oviedo-asturias-650x436.jpg",
    },
    "PMI": {
        "nombre": "Palma de Mallorca",
        "foto": "https://www.spain.info/export/sites/segtur/.content/imagenes/cabeceras-grandes/baleares/catedral-santamaria-palma-s434080438.jpg_604889389.jpg",
    },
    "SCQ": {
        "nombre": "Santiago de Compostela",
        "foto": "https://images.squarespace-cdn.com/content/v1/5a86b05bcf81e0af04936cc7/1647202169084-N27PZELVGYBG4WX19KQK/que-ver-en-santiago-de-compostela.jpg?format=1500w",
    },
    "SDR": {
        "nombre": "Santander",
        "foto": "https://www.santander.es/sites/default/files/styles/cabecera/public/_dsc2734_0.jpg?itok=UJbwLB2R&c=3fd873c46227863b12ab5d8f988cedc6",
    },
    "TFN": {
        "nombre": "Tenerife Norte",
        "foto": "https://routeactivehotel.com/wp-content/uploads/2019/06/puerto_de_la_cruz-1024x627.jpg",
    },
    "VGO": {
        "nombre": "Vigo",
        "foto": "https://estaticos-cdn.prensaiberica.es/clip/ac331c49-07d4-4c83-aa29-5a7bf19916e1_21-9-aspect-ratio_default_0.jpg",
    },
    "ZRH": {
        "nombre": "Zúrich",
        "foto": "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2018/09/24/15377887462313.jpg",
    },
}

with open("./algoritmoPython/cristian/habitaciones.json", "w") as outfile:
        json.dump(a, outfile, indent=4, sort_keys=True)