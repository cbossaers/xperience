import { Component, OnInit } from '@angular/core';
import { SwitchService } from 'src/app/services/switch.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  modalSwitch: boolean = false;

  constructor(private modalSS:SwitchService) { }

  ngOnInit() {
    this.modalSS.$modal.subscribe((valor)=> {this.modalSwitch = valor})
  }

  openLogin() {
    this.modalSwitch = true;
  }

}
