import { Component, OnInit } from '@angular/core';
import { SwitchService } from 'src/app/services/switch.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {



  constructor(private modalSS:SwitchService) {}
  

  login() {
    //console.log(this.email);
    //console.log(this.password);
  }

  closeLogin() {
    this.modalSS.$modal.emit(false);
  }
}
