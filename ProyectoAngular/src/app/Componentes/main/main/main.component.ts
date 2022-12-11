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
  s:string='2022-03-01';
  precioTotal:string="pt";
  ciudadLlegada:string="cll";
  ciudadSalida:string="cs";
  compa:string="compa";
  fechaS:string="salidaF";
  precioP:string="200";
  fechaLL:string="salidF";
  resultados:any = viajees;
  valores:JSON = viajees;
  modalSwitch1:boolean = true;
  modalSwitch2:boolean = false;
  modalSwitch3:boolean = false;
  modalSwitch4:boolean = false;

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
 
  async enviardatos(){
    let salida = '2022-03-01';
    let llegada = '2022-03-01';
    
    try {
      const response = await fetch('http://88.17.114.199:9879/vuelo', {
        method: 'POST',
        body: JSON.stringify({
          precio: 1500,
          fechaSalida: salida,
          fechaLlegada: llegada,
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
  
      this.resultados= result;
      this.modalSwitch1= false;
      this.modalSwitch2=true;
      this.modalSwitch3=false;
      this.modalSwitch4= false;
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



  datosViaje(precioTotal:string,ciudadSalida:string,ciudadLlegada:string,compa:string,fechaS:string,fechaLL:string){
    this.precioTotal=precioTotal;
    this.ciudadSalida=ciudadSalida;
    this.ciudadLlegada=ciudadLlegada;
    this.compa=compa;
    this.fechaS=fechaS;
    this.fechaLL=fechaLL;
    this.modalSwitch1= false;
    this.modalSwitch2= false;
    this.modalSwitch3= true;
    this.modalSwitch4= false;
  }
  compraViaje(){
    this.modalSwitch1= false;
    this.modalSwitch2= false;
    this.modalSwitch3=false;
    this.modalSwitch4=true;
  }
  enviarInfo(){
    const user = this.miFormulario.value;
    alert(user.Presupuesto);
  }
}

