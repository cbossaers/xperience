import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule} from '@angular/forms';
import { FormsModule } from "@angular/forms"

import { AppComponent } from './app.component';
import { HeaderComponent } from './Componentes/header/header.component';
import { MainComponent } from './Componentes/main/main/main.component';
import { VistaViajeComponent } from './Componentes/vistaViaje/vista-viaje/vista-viaje.component';
import { LoginComponent } from './Componentes/login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { CuentaComponent } from './cuenta/cuenta.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MainComponent,
    VistaViajeComponent,
    LoginComponent,
    RegistroComponent,
    CuentaComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FormsModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
