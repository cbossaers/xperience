import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  modalSwitch:boolean = false;

  constructor() { }

  ngOnInit(): void {
    
  }
 
  openModal(){
    this.modalSwitch=true;
  }
}
