import { Component, OnInit } from '@angular/core';
import { FormControl,FormGroup,Validators } from '@angular/forms';
import  viajees from 'src/assets/json/viajes.json';


interface VIAJES {
  fecha_salida: String;
  fecha_llegada: String;
  precio: String;
  ciudad_salida: String;
  ciudad_llegada: String;
}

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  destino: string = "destino";
  duracionIda: string = "duracionIda";
  duracionVuelta:string = "duracionVuelta";
  habitacion:string = "habitacion";
  hotelNombre:string = "hotelNombre";
  llegadaIda:string = "llegadaIda";
  llegadaVuelta:string = "llegadaVuelta";
  precioHotel:string = "precioHotel";
  precioIda:string = "precioIda";
  precioTotal:string = "precioTotal";
  precioVuelta:string = "precioVuelta";
  salidaIda:string = "salidaIda";
  salidaVuelta:string = "salidaVuelta";
  foto:string = "";
  resultados: any = viajees;
  valores: JSON = viajees;
  modalSwitch1: boolean = true;
  modalSwitch2: boolean = false;
  modalSwitch3: boolean = false;
  modalSwitch4: boolean = false;
  modalSwitch5: boolean = false;
  modalFiltro: boolean = true;
  numPasajeros: number = 1;

  miFormulario = new FormGroup({
    Presupuesto : new FormControl('',Validators.required)
  });

  constructor() {
  }

  ngOnInit(): void {
    /*this.resultados = (viajees);
    console.log(this.resultados);
    this.resultados = GetVueloByFechaPrecio(1500,'2022-03-01','2022-03-01');
    console.log(this.resultados);*/
  }
  

  async enviardatos() {
    let salida = '10/05/23 00:00:00';
    let llegada = '16/05/23 00:00:00';
    let Origen = 'MAD';
    try {
      const response = await fetch('http://88.17.114.199:9876/paq', {
        method: 'POST',
        body: JSON.stringify({
          origen: Origen,
          fechaIda: salida,
          fechaVuelta: llegada,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Error! status: ${response.status}');
      }

      const result = await response.json();

      console.log('result is: ', JSON.stringify(result, null, 4));

      const otro = JSON.stringify(result, null, 4);

      console.log(otro);

      this.resultados = result;
      this.modalSwitch1 = false;
      this.modalSwitch2 = true;
      this.modalSwitch3 = false;
      this.modalSwitch4 = false;
      this.modalSwitch5 = false;
      this.modalFiltro = true;
      return otro;

    } catch (error) {
      if (error instanceof Error) {
        console.log('Error message: ', error.message);
        return error.message;
      } else {
        console.log('Unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }

  }

  datosViaje(destino: string, duracionIda: string, duracionVuelta: string, habitacion: string, hotelNombre: string, llegadaIda: string,
    llegadaVuelta: string, precioHotel: string, precioIda: string, precioTotal: string, precioVuelta: string, salidaIda: string, salidaVuelta: string,foto: string) {
    this.destino = destino;
    this.duracionIda = duracionIda.substring(2);
    this.duracionVuelta = duracionVuelta.substring(2);
    this.habitacion = habitacion;
    this.hotelNombre = hotelNombre;
    this.llegadaIda = llegadaIda;
    this.llegadaVuelta = llegadaVuelta;
    this.precioHotel = precioHotel;
    this.precioIda = precioIda;
    this.precioTotal = precioTotal;
    this.precioVuelta = precioVuelta;
    this.salidaIda = salidaIda.substring(0,10) + " " + salidaIda.substring(11,16) + "h";
    this.salidaVuelta = salidaVuelta.substring(0,10) + " " + salidaVuelta.substring(11,16) + "h";
    this.foto = foto;

    this.modalSwitch1 = false;
    this.modalSwitch2 = false;
    this.modalSwitch3 = true;
    this.modalSwitch4 = false;
    this.modalSwitch5 = false;
    this.modalFiltro = false;
  }

  compraViaje() {
    this.modalSwitch1 = false;
    this.modalSwitch2 = false;
    this.modalSwitch3 = false;
    this.modalSwitch4 = true;
    this.modalSwitch5 = false;
    this.modalFiltro = false;
  }

  anyadirPasajero() {
    this.numPasajeros = this.numPasajeros + 1;

    var elementos = document.getElementsByTagName('input');

    for (let i = 0; i < elementos.length; i++) {
      elementos[i].value='';          
    }
  }

  enviarInfo() {
    const user = this.miFormulario.value;
    alert(user.Presupuesto);
  }

  realizarPago() {
    this.modalSwitch1 = false;
    this.modalSwitch2 = false;
    this.modalSwitch3 = false;
    this.modalSwitch4 = false;
    this.modalSwitch5 = true;
    this.modalFiltro = false;
  }
}


