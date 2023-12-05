import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { SwitchService } from 'src/app/services/switch.service';
import  viajees from 'src/assets/json/viajes.json';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {

  loginSwitch: boolean = false;
  @Output() eventologin = new EventEmitter<boolean>();

  constructor(private modalSS:SwitchService) { }

  ngOnInit() {
    this.modalSS.$login.subscribe((valor)=> {this.loginSwitch = valor})
  }

  openLogin() {
    this.modalSS.$login.emit(true);
  }
  
}

