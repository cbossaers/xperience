import { Component } from '@angular/core';
import { SwitchService } from 'src/app/services/switch.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ProyectoAngular';

  constructor(private modalSS:SwitchService) { }

  public mainSwitch: boolean = true;

  ngOnInit() {
    this.modalSS.$login.subscribe((valor)=> {this.mainSwitch = !valor})
  }
}
