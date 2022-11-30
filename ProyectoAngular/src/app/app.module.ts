import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HeaderComponent } from './Componentes/header/header.component';
import { MainComponent } from './Componentes/main/main/main.component';
import { VistaViajeComponent } from './Componentes/vistaViaje/vista-viaje/vista-viaje.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MainComponent,
    VistaViajeComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
